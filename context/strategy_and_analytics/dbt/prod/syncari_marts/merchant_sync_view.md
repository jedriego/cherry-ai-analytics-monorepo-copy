## Model: `merchant_sync_view`

`merchant_sync_view`

*   **Unique ID:** `model.cherry_data_model.merchant_sync_view`
*   **FQN:** `prod.syncari_marts.merchant_sync_view`
*   **Description:** (No description provided)
*   **Tags:** `['syncari_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `ACCOUNT_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_ID` | 2 | `FLOAT` |  |  | `[]` | `{}` |
    | `ORGANIZATION_ID` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `MERCHANT_DASHBOARD_STATUS` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `MAX_TIMESTAMP` | 5 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `source.cherry_data_model.cherry_data.merchants`
    *   `source.cherry_data_model.cherry_data.organization`
    *   `source.cherry_data_model.salesforce.account_history`
    *   `source.cherry_data_model.salesforce.accounts`

---
