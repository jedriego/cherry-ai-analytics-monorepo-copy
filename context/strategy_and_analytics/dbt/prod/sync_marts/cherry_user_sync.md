## Model: `cherry_user_sync`

`cherry_user_sync`

*   **Unique ID:** `model.cherry_data_model.cherry_user_sync`
*   **FQN:** `prod.sync_marts.cherry_user_sync`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `USER_ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `EMPLOYEE_ID` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `FIRST_NAME` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `LAST_NAME` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `STATUS` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `CREATED_TIMESTAMP` | 6 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `UPDATED_TIMESTAMP` | 7 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `LAST_CONFIRMED_TIMESTAMP` | 8 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `CREATED_BY` | 9 | `NUMBER` |  |  | `[]` | `{}` |
    | `UPDATED_BY` | 10 | `NUMBER` |  |  | `[]` | `{}` |
    | `EMAIL` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `PHONE` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_FIVETRAN_DELETED` | 13 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `FIVETRAN_SYNC_TIMESTAMP` | 14 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `source.cherry_data_model.cherry_data.cherry_users`

---
