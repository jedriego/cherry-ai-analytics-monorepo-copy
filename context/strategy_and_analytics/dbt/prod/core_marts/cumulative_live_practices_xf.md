## Model: `cumulative_live_practices_xf`

`cumulative_live_practices_xf`

*   **Unique ID:** `model.cherry_data_model.cumulative_live_practices_xf`
*   **FQN:** `prod.core_marts.cumulative_live_practices_xf`
*   **Description:** This table shows the cumulative number of practices that have gone live with Cherry over time.

*   **Tags:** `['core', 'contact_rate', 'key-metrics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `REFERENCE_DATE` | 1 | `DATE` | The date in question. One row for each day since September 1, 2020 excluding today | The date in question. One row for each day since September 1, 2020 excluding today | `[]` | `{}` |
    | `INDUSTRY` | 2 | `TEXT` | The industry of the primary organization for a given primary_merchant_id.
 | The industry of the primary organization for a given primary_merchant_id.
 | `[]` | `{}` |
    | `CUMULATIVE_PRACTICES_ACTIVE` | 3 | `NUMBER` | The cumulative number of practices active in the industry.
 | The cumulative number of practices active in the industry.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.cherry_data_model.convert_to_pt`
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.stg_practices`

---
