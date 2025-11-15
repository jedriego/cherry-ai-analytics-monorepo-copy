## Model: `retention_focus_groups_xf`

`retention_focus_groups_xf`

*   **Unique ID:** `model.cherry_data_model.retention_focus_groups_xf`
*   **FQN:** `prod.revenue_marts.retention_focus_groups_xf`
*   **Description:** (No description provided)
*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `BUCKET_QUARTER` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `SF_ACCOUNT_ID` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `HEALTHY_LAST_30_VOLUME` | 3 | `FLOAT` |  |  | `[]` | `{}` |
    | `CAPPED_HEALTHY_LAST_30_VOLUME` | 4 | `FLOAT` |  |  | `[]` | `{}` |
    | `DELTA_TO_POTENTIAL` | 5 | `FLOAT` |  |  | `[]` | `{}` |
    | `FOCUS_GROUP` | 6 | `TEXT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.first_look_upgrade_inputs`
    *   `model.cherry_data_model.loan_info_xf`
    *   `model.cherry_data_model.merchant_info_xf`
    *   `model.cherry_data_model.practice_info_full_xf`
    *   `model.cherry_data_model.src_sf_accounts`

---
