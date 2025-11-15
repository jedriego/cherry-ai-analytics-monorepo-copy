# dbt Cloud Discovery API integration script

import os
import sys
import requests
import json
import pickle
from pathlib import Path
from dotenv import load_dotenv
from typing import Union, List, Dict, Any

# Load environment variables from .env file if it exists
load_dotenv()

# --- Configuration ---
DBT_CLOUD_API_KEY = os.getenv("DBT_CLOUD_API_KEY")
DBT_CLOUD_ACCOUNT_ID = os.getenv("DBT_CLOUD_ACCOUNT_ID")
DBT_CLOUD_JOB_ID = os.getenv("DBT_CLOUD_JOB_ID") # Job ID is needed for this query

# Discovery API base URL
DISCOVERY_API_URL = "https://rp528.metadata.us1.dbt.com"
# Define the specific GraphQL endpoint path
DISCOVERY_GRAPHQL_ENDPOINT = f"{DISCOVERY_API_URL}/graphql" # Standard path

# Check for required environment variables at the start
if not all([DBT_CLOUD_API_KEY, DBT_CLOUD_ACCOUNT_ID, DBT_CLOUD_JOB_ID]):
    print("ERROR: DBT Cloud API Key, Account ID, or Job ID not set in environment variables. Exiting.")
    sys.exit(1)

# --- Cache Configuration ---
# Determine script directory and project root
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent # Navigate up one level: src -> project root
DATA_DIR = PROJECT_ROOT / "data"
CACHE_FILE_PATH = DATA_DIR / "dbt_api_cache.pkl"
MARKDOWN_OUTPUT_PATH = DATA_DIR / "dbt_cloud_metadata_output.md" # Define MD output path

# --- Function: Format Models to Markdown ---
def format_metadata_to_markdown(models_metadata: List[Dict[str, Any]]) -> str:
    """Formats the fetched metadata into a Markdown string."""
    md_string = "# dbt Cloud Model Metadata\n\n"
    md_string += f"Fetched {len(models_metadata)} models.\n\n"

    for model in models_metadata:
        md_string += f"## Model: `{model.get('name', 'N/A')}`\n\n"
        md_string += f"*   **Unique ID:** `{model.get('uniqueId', 'N/A')}`\n"
        # Construct FQN using database, schema, and alias/name
        db = model.get('database', '?')
        schema = model.get('schema', '?')
        alias_or_name = model.get('alias') or model.get('name', '?')
        fqn = f"`{db}.{schema}.{alias_or_name}`" if db != '?' and schema != '?' and alias_or_name != '?' else '`N/A`'
        md_string += f"*   **FQN:** {fqn}\n"
        description = model.get('description', '') or '(No description provided)' # Handle None or empty string
        md_string += f"*   **Description:** {description}\n"
        md_string += f"*   **Tags:** `{model.get('tags', [])}`\n"
        md_string += f"*   **Meta:** `{model.get('meta', {})}`\n"

        # Format Columns
        columns = model.get('columns', []) # Use 'columns' key
        if columns:
            md_string += "*   **Columns:**\n"
            md_string += "    | Name | Index | Type | Comment | Description | Tags | Meta |\n"
            md_string += "    |------|-------|------|---------|-------------|------|------|\n"
            for col in columns:
                 # Use .get() for safety, provide default like 'N/A' or empty string
                 name = col.get('name', '?')
                 index = col.get('index', 'N/A')
                 col_type = col.get('type', '?')
                 comment = col.get('comment', '') or '' # Handle None from .get() and ensure string
                 description = col.get('description', '') or '' # Handle None from .get()
                 tags = col.get('tags', [])
                 meta = col.get('meta', {})
                 md_string += f"    | `{name}` | {index} | `{col_type}` | {comment} | {description} | `{tags}` | `{meta}` |\n"
        else:
             md_string += "*   **Columns:** (No column data returned by API)\n"

        # Format Parents (Lineage) using dependsOn
        parents = model.get('dependsOn', []) # Use 'dependsOn' key
        if parents:
             md_string += "*   **Depends On (Parents):**\n"
             for parent_id in parents:
                  # We only get the uniqueId list from dependsOn
                  md_string += f"    *   `{parent_id}`\n"
        else:
             md_string += "*   **Depends On (Parents):** (No parent data returned by API)\n"

        md_string += "\n---\n\n" # Separator

    return md_string

# --- Function: Write Markdown to File ---
def write_markdown_to_file(markdown_content: str, file_path: Path):
    """Writes the given Markdown content to the specified file path."""
    try:
        print(f"Writing formatted metadata to Markdown file: {file_path}")
        file_path.write_text(markdown_content, encoding='utf-8')
        print("Successfully wrote Markdown file.")
    except IOError as e:
        print(f"Error writing Markdown file {file_path}: {e}")
    except Exception as e:
        print(f"An unexpected error occurred while writing Markdown file: {e}")

# --- Function: Query Comprehensive Model Metadata from Job Run ---
def get_all_metadata_from_job_run(job_id: str) -> Union[List[Dict[str, Any]], None]:
    """Queries the Discovery API for comprehensive model metadata from the latest run of a specific job."""
    headers = {
        "Authorization": f"Token {DBT_CLOUD_API_KEY}",
        "Content-Type": "application/json"
    }

    # Comprehensive GraphQL query
    graphql_query = """
    query JobModelsComprehensive($jobId: BigInt!) {
      job(id: $jobId) {
        models {
          # Identity & Location
          uniqueId
          name
          alias
          database
          schema
          # Documentation & Metadata
          description
          tags
          meta
          # Columns (Using the correct 'columns' field)
          columns {
            name
            index
            type
            comment
            description
            tags
            meta
          }
          # Lineage (Using 'dependsOn')
          dependsOn # List of parent uniqueIds
        }
      }
    }
    """

    variables = {"jobId": int(job_id)}
    post_body = json.dumps({"query": graphql_query, "variables": variables})

    print(f"Attempting Comprehensive GraphQL query to Discovery API endpoint: {DISCOVERY_GRAPHQL_ENDPOINT}")

    try:
        # Increased timeout for potentially larger response
        response = requests.post(DISCOVERY_GRAPHQL_ENDPOINT, headers=headers, data=post_body, timeout=180)
        print(f"Discovery API GraphQL Status Code: {response.status_code}")
        response.raise_for_status()
        response_data = response.json()

        if "errors" in response_data:
            print(f"GraphQL Errors: {response_data['errors']}")
            return None

        models_list = response_data.get("data", {}).get("job", {}).get("models", None)

        if models_list is None:
             print("GraphQL query succeeded, but 'models' field was missing or null.")
             return None
        elif not isinstance(models_list, list):
             print(f"GraphQL query succeeded, but 'models' field was not a list. Type: {type(models_list)}")
             return None

        print(f"Successfully fetched metadata for {len(models_list)} model(s).")
        return models_list

    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        try: print(f"Error details: {e.response.json()}")
        except: print(f"Response Text: {e.response.text}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"Network Error: {e}")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return None

# --- Main Execution Logic ---
def run_discovery_model_query():
    """
    Attempts to query model metadata using the Discovery API, utilizing a cache.
    Raises AssertionError if the query fails and cache is empty.
    Returns the models metadata list.
    """
    print(f"\nRunning Discovery API model query for Job ID: {DBT_CLOUD_JOB_ID}...")

    # Ensure data directory exists
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # --- Cache Check ---
    models_metadata = None
    if CACHE_FILE_PATH.exists():
        print(f"Attempting to load metadata from cache: {CACHE_FILE_PATH}")
        try:
            with open(CACHE_FILE_PATH, "rb") as f:
                models_metadata = pickle.load(f)
            print("Successfully loaded metadata from cache.")
        except (pickle.UnpicklingError, EOFError, FileNotFoundError, Exception) as e:
            print(f"Failed to load from cache or cache invalid: {e}. Fetching fresh data.")
            models_metadata = None # Ensure we fetch fresh if cache load fails

    # --- Fetch from API if Cache Miss/Invalid ---
    if models_metadata is None:
        print("Cache empty or invalid, fetching fresh data from Discovery API...")
        models_metadata = get_all_metadata_from_job_run(DBT_CLOUD_JOB_ID)

        if models_metadata is None:
            # If API fetch also fails, raise error.
            raise AssertionError("Failed to fetch model metadata from Discovery API and cache is empty/invalid.")

        # --- Save to Cache ---
        try:
            print(f"Saving freshly fetched metadata to cache: {CACHE_FILE_PATH}")
            with open(CACHE_FILE_PATH, "wb") as f:
                pickle.dump(models_metadata, f)
            print("Successfully saved metadata to cache.")
        except (pickle.PicklingError, IOError, Exception) as e:
            print(f"Warning: Failed to save metadata to cache: {e}")
            # Continue execution even if caching fails, but warn the user.

    # --- Process and Print ---
    if not models_metadata:
        print("Warning: Query/Cache successful, but no models were found for this job.")
    else:
        # Limit printing for brevity if many models are returned
        print_limit = 5
        print(f"--- Found Model Metadata (Showing first {min(len(models_metadata), print_limit)}) ---")
        for i, model in enumerate(models_metadata):
            if i >= print_limit:
                print(f"... and {len(models_metadata) - print_limit} more models.")
                break
            print(json.dumps(model, indent=2)) # Pretty print the model data
        print("---------------------------------------")

    print("Discovery API model query process completed!")
    return models_metadata # Return the data


# --- Script Execution Entry Point ---
if __name__ == "__main__":
    returned_metadata = None
    try:
        returned_metadata = run_discovery_model_query()

        # --- Format and Write Markdown --- 
        if returned_metadata is not None:
            # Proceed with formatting and writing even if the list is empty
            print("\nFormatting metadata to Markdown...")
            markdown_output = format_metadata_to_markdown(returned_metadata)
            write_markdown_to_file(markdown_output, MARKDOWN_OUTPUT_PATH)
        else:
            print("\nSkipping Markdown generation as no metadata was loaded or fetched.")

    except AssertionError as e:
        print(f"\nAssertion Failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred during execution: {e}")
        sys.exit(1) 