#!/usr/bin/env python3
"""
Generate GitHub folder structure from dbt metadata.

Parses dbt_cloud_metadata_output.md and creates hierarchical folder structure:
- Uses database.schema as folder hierarchy
- Creates individual model.md files with full documentation
- Generates README.md files for navigation
"""

import os
import re
from pathlib import Path
from collections import defaultdict
from typing import Dict, List, Any


# Configuration
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
DATA_DIR = PROJECT_ROOT / "data"
MARKDOWN_INPUT_PATH = DATA_DIR / "dbt_cloud_metadata_output.md"
OUTPUT_DIR = PROJECT_ROOT / "context" / "strategy_analytics"


def parse_dbt_markdown(file_path: Path) -> List[Dict[str, Any]]:
    """
    Parse the dbt_cloud_metadata_output.md file and extract model metadata.

    Returns a list of model dictionaries with:
    - name: Model name
    - fqn: Fully qualified name (database.schema.name)
    - database: Database name
    - schema: Schema name
    - description: Model description
    - tags: List of tags
    - content: Full markdown content for this model
    """
    print(f"Parsing dbt metadata from: {file_path}")

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by model sections (starts with ## Model:)
    model_sections = re.split(r'\n## Model: ', content)

    models = []

    # Skip first section (header)
    for section in model_sections[1:]:
        model = {}

        # Extract model name (first line after ## Model:)
        name_match = re.search(r'^`([^`]+)`', section)
        if name_match:
            model['name'] = name_match.group(1)

        # Extract FQN
        fqn_match = re.search(r'\*\s+\*\*FQN:\*\*\s+`([^`]+)`', section)
        if fqn_match:
            fqn = fqn_match.group(1)
            model['fqn'] = fqn

            # Split FQN into components
            parts = fqn.split('.')
            if len(parts) >= 2:
                model['database'] = parts[0]
                model['schema'] = parts[1]
            else:
                # Fallback if FQN format is unexpected
                model['database'] = 'unknown'
                model['schema'] = 'unknown'

        # Extract description
        desc_match = re.search(r'\*\s+\*\*Description:\*\*\s+(.+?)(?=\n\*|\n---)', section, re.DOTALL)
        if desc_match:
            model['description'] = desc_match.group(1).strip()
        else:
            model['description'] = '(No description provided)'

        # Extract tags
        tags_match = re.search(r'\*\s+\*\*Tags:\*\*\s+`(\[.*?\])`', section)
        if tags_match:
            tags_str = tags_match.group(1)
            # Parse the list string
            model['tags'] = eval(tags_str)  # Safe here as it's our own generated data
        else:
            model['tags'] = []

        # Store full content for this model
        model['content'] = f"## Model: `{model.get('name', 'Unknown')}`\n\n{section}"

        models.append(model)

    print(f"Parsed {len(models)} models")
    return models


def create_folder_structure(models: List[Dict[str, Any]], output_dir: Path, databases_to_include: List[str] = None):
    """
    Create folder structure based on database.schema hierarchy.

    Creates:
    - Folders for each database/schema combination
    - Individual model.md files
    - README.md files for navigation

    Args:
        databases_to_include: List of database names to include (e.g., ['prod']). If None, includes all.
    """
    print(f"\nCreating folder structure in: {output_dir}")

    # Group models by database and schema
    hierarchy = defaultdict(lambda: defaultdict(list))

    for model in models:
        database = model.get('database', 'unknown')

        # Filter by database if specified
        if databases_to_include and database not in databases_to_include:
            continue

        schema = model.get('schema', 'unknown')
        hierarchy[database][schema].append(model)

    # Create root README
    create_root_readme(output_dir, hierarchy)

    # Create folders and files
    for database, schemas in hierarchy.items():
        db_path = output_dir / database
        db_path.mkdir(parents=True, exist_ok=True)

        # Create database-level README
        create_database_readme(db_path, database, schemas)

        for schema, schema_models in schemas.items():
            schema_path = db_path / schema
            schema_path.mkdir(parents=True, exist_ok=True)

            # Create schema-level README
            create_schema_readme(schema_path, database, schema, schema_models)

            # Create individual model files
            for model in schema_models:
                model_file = schema_path / f"{model['name']}.md"
                model_file.write_text(model['content'], encoding='utf-8')

    print(f"✓ Created folder structure with {len(models)} model files")


def create_root_readme(output_dir: Path, hierarchy: Dict):
    """Create the root README.md with navigation to all databases."""

    content = """# Strategy Analytics dbt Models

Auto-generated from dbt Cloud Discovery API metadata.

## Browse by Database

"""

    for database in sorted(hierarchy.keys()):
        schema_count = len(hierarchy[database])
        model_count = sum(len(models) for models in hierarchy[database].values())
        content += f"### [{database}/]({database}/)\n"
        content += f"- {schema_count} schemas\n"
        content += f"- {model_count} models\n\n"

    content += """
## How to Use

1. **Browse hierarchically**: Navigate to your database → schema → model
2. **Search by tag**: Use GitHub search with tag names (e.g., `marketing_analytics`)
3. **Add context**: Create `gotchas.md` or `patterns.md` files alongside models

## Contributing

To add business logic or gotchas:
1. Navigate to the relevant schema folder
2. Create a new `.md` file (e.g., `gotchas.md`, `common_queries.md`)
3. Open a PR with your documentation
4. Once merged, AI agents have permanent context

---

*Last updated: Auto-generated from dbt Cloud*
"""

    readme_path = output_dir / "README.md"
    readme_path.write_text(content, encoding='utf-8')
    print(f"✓ Created root README: {readme_path}")


def create_database_readme(db_path: Path, database: str, schemas: Dict):
    """Create database-level README with navigation to schemas."""

    content = f"# {database}\n\n"
    content += f"Database: `{database}`\n\n"
    content += "## Schemas\n\n"

    for schema in sorted(schemas.keys()):
        model_count = len(schemas[schema])
        content += f"### [{schema}/]({schema}/)\n"
        content += f"- {model_count} models\n\n"

    readme_path = db_path / "README.md"
    readme_path.write_text(content, encoding='utf-8')
    print(f"✓ Created database README: {readme_path}")


def create_schema_readme(schema_path: Path, database: str, schema: str, models: List[Dict]):
    """Create schema-level README with all models listed and grouped by tags."""

    content = f"# {database}.{schema}\n\n"
    content += f"Schema: `{database}.{schema}`\n"
    content += f"Total models: {len(models)}\n\n"

    # Group by tags
    tags_dict = defaultdict(list)
    for model in models:
        if model.get('tags'):
            for tag in model['tags']:
                tags_dict[tag].append(model)
        else:
            tags_dict['untagged'].append(model)

    # List models by tag
    if tags_dict:
        content += "## Models by Tag\n\n"
        for tag in sorted(tags_dict.keys()):
            content += f"### {tag}\n\n"
            for model in sorted(tags_dict[tag], key=lambda m: m['name']):
                desc = model.get('description', '(No description)')
                # Truncate long descriptions
                if len(desc) > 100:
                    desc = desc[:97] + "..."
                content += f"- [{model['name']}]({model['name']}.md) - {desc}\n"
            content += "\n"

    # Alphabetical list of all models
    content += "## All Models (A-Z)\n\n"
    for model in sorted(models, key=lambda m: m['name']):
        content += f"- [{model['name']}]({model['name']}.md)\n"

    readme_path = schema_path / "README.md"
    readme_path.write_text(content, encoding='utf-8')
    print(f"✓ Created schema README: {readme_path}")


def main():
    """Main execution function."""
    print("=" * 60)
    print("dbt Context Folder Generator")
    print("=" * 60)

    # Check if input file exists
    if not MARKDOWN_INPUT_PATH.exists():
        print(f"ERROR: Input file not found: {MARKDOWN_INPUT_PATH}")
        print("Run update_dbt_metadata.py first to generate the markdown file.")
        return

    # Parse markdown
    models = parse_dbt_markdown(MARKDOWN_INPUT_PATH)

    if not models:
        print("No models found in markdown file. Exiting.")
        return

    # Create output directory
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    # Generate folder structure - PROD ONLY for MVP
    print("\nℹ️  Filtering to production models only (database='prod')")
    create_folder_structure(models, OUTPUT_DIR, databases_to_include=['prod'])

    print("\n" + "=" * 60)
    print("✓ Context folder generation complete!")
    print(f"✓ Output location: {OUTPUT_DIR}")
    print("=" * 60)


if __name__ == "__main__":
    main()
