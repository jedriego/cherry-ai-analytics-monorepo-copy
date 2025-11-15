# Scripts - Repository Automation

This folder houses automations to update the repository with fresh data and documentation.

## 📂 Available Automations

### `how_to_update_dbt_metadata/`
Automatically syncs dbt Cloud model metadata into the repository.

**What it does:**
- Fetches latest dbt model metadata from dbt Cloud Discovery API
- Generates organized folder structure with model documentation
- Keeps AI context library up-to-date with your data warehouse

**Usage:**
```bash
python scripts/how_to_update_dbt_metadata/update_dbt_metadata.py
python scripts/how_to_update_dbt_metadata/generate_context_folders.py
```

See [how_to_update_dbt_metadata/README.md](how_to_update_dbt_metadata/README.md) for detailed documentation.

---

## 🔮 Future Automations

Other planned automation scripts:
- Metabase dashboard sync
- Business metrics documentation
- Team runbook updates
- KPI tracking snapshots

---

*Each automation has its own subfolder with dedicated documentation.*
