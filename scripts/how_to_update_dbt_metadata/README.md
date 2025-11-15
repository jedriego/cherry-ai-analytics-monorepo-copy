# Scripts - dbt Metadata Automation

Scripts for keeping the context library synchronized with dbt Cloud.

## 📋 Scripts

### `update_dbt_metadata.py`
Fetches fresh metadata from dbt Cloud Discovery API.

**What it does:**
- Connects to dbt Cloud Discovery API
- Fetches all model metadata (names, schemas, columns, tags, dependencies)
- Caches raw data to `data/dbt_api_cache.pkl`
- Generates formatted markdown to `data/dbt_cloud_metadata_output.md`

**Usage:**
```bash
python scripts/update_dbt_metadata.py
```

**Prerequisites:**
- `.env` file with dbt Cloud credentials (see `.env.example`)

---

### `generate_context_folders.py`
Parses dbt metadata and generates GitHub folder structure.

**What it does:**
- Reads `data/dbt_cloud_metadata_output.md`
- Creates hierarchical folder structure (database → schema → models)
- Generates navigation READMEs at each level
- Creates individual model.md files with full documentation
- **Currently filtered to `prod` database only** (224 models)

**Usage:**
```bash
python scripts/generate_context_folders.py
```

**Output:**
- `context/strategy_analytics/` - Complete folder structure with READMEs

---

## 🔄 Weekly Update Workflow

**Manual:**
```bash
# 1. Fetch fresh dbt metadata
python scripts/update_dbt_metadata.py

# 2. Regenerate folder structure
python scripts/generate_context_folders.py

# 3. Commit and push
git add context/
git commit -m "Update dbt metadata - $(date +%Y-%m-%d)"
git push origin main

# 4. Create PR (or auto-merge if you have permissions)
```

**Future: Automated via GitHub Actions** (Phase 2)
- Runs every Monday at 9 AM
- Auto-creates PR with updated metadata
- Team reviews and merges

---

## 🛠️ Setup

1. **Install dependencies:**
```bash
pip install -r requirements.txt
```

2. **Configure environment variables:**
```bash
cp .env.example .env
# Edit .env with your dbt Cloud credentials
```

3. **Test the pipeline:**
```bash
python scripts/update_dbt_metadata.py
python scripts/generate_context_folders.py
```

---

## 📝 Configuration

### Environment Variables (`.env`)

Required:
- `DBT_CLOUD_API_KEY` - Your dbt Cloud API token
- `DBT_CLOUD_ACCOUNT_ID` - Your dbt Cloud account ID
- `DBT_CLOUD_JOB_ID` - Production job ID to fetch metadata from

### Script Configuration

To include different databases (default is `prod` only):

Edit `generate_context_folders.py` line 275:
```python
# Include prep and prod
create_folder_structure(models, OUTPUT_DIR, databases_to_include=['prep', 'prod'])

# Include all databases
create_folder_structure(models, OUTPUT_DIR, databases_to_include=None)
```

---

## 🐛 Troubleshooting

**"DBT Cloud API Key not set"**
- Make sure `.env` file exists with `DBT_CLOUD_API_KEY`

**"Input file not found"**
- Run `update_dbt_metadata.py` first to fetch metadata

**"No models found"**
- Check that your `DBT_CLOUD_JOB_ID` is correct
- Verify job has run successfully in dbt Cloud

---

*For questions, contact #ai-analytics in Slack*
