## Model: `organization_user_sync`

`organization_user_sync`

*   **Unique ID:** `model.cherry_data_model.organization_user_sync`
*   **FQN:** `prod.sync_marts.organization_user_sync`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `RECORD_TYPE_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `ORGANIZATION_USER_ID` | 2 | `NUMBER` |  |  | `[]` | `{}` |
    | `ORGANIZATION_ID` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `USER_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `USER_ROLE` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `CREATED_TIMESTAMP` | 6 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `UPDATED_TIMESTAMP` | 7 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `CREATED_BY` | 8 | `NUMBER` |  |  | `[]` | `{}` |
    | `UPDATED_BY` | 9 | `NUMBER` |  |  | `[]` | `{}` |
    | `IS_FIVETRAN_DELETED` | 10 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `FIVETRAN_SYNC_TIMESTAMP` | 11 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `source.cherry_data_model.cherry_data.cherry_users`
    *   `source.cherry_data_model.cherry_data.organization_users`

---
