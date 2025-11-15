## Model: `merchant_user_sync`

`merchant_user_sync`

*   **Unique ID:** `model.cherry_data_model.merchant_user_sync`
*   **FQN:** `prod.sync_marts.merchant_user_sync`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `RECORD_TYPE_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_USER_ID` | 2 | `NUMBER` |  |  | `[]` | `{}` |
    | `MERCHANT_ID` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `USER_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `USER_ROLE` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_POC` | 6 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `LATEST_LOGIN_DATE` | 7 | `DATE` |  |  | `[]` | `{}` |
    | `CREATED_TIMESTAMP` | 8 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `UPDATED_TIMESTAMP` | 9 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `CREATED_BY` | 10 | `NUMBER` |  |  | `[]` | `{}` |
    | `UPDATED_BY` | 11 | `NUMBER` |  |  | `[]` | `{}` |
    | `IS_FIVETRAN_DELETED` | 12 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `FIVETRAN_SYNC_TIMESTAMP` | 13 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.user_product_use_xf`
    *   `source.cherry_data_model.cherry_data.cherry_users`
    *   `source.cherry_data_model.cherry_data.merchant_users`
    *   `source.cherry_data_model.cherry_data.merchants`

---
