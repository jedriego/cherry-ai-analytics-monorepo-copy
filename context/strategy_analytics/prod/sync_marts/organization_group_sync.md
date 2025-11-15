## Model: `organization_group_sync`

`organization_group_sync`

*   **Unique ID:** `model.cherry_data_model.organization_group_sync`
*   **FQN:** `prod.sync_marts.organization_group_sync`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `RECORD_TYPE_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `ORGANIZATION_GROUP_ID` | 2 | `NUMBER` |  |  | `[]` | `{}` |
    | `ORGANIZATION_GROUP_NAME` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `ORGANIZATION_GROUP_PARENT_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `TIER_ID` | 5 | `NUMBER` |  |  | `[]` | `{}` |
    | `SLUG` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `CREATED_TIMESTAMP` | 7 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `UPDATED_TIMESTAMP` | 8 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `IS_FIVETRAN_DELETED` | 9 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `FIVETRAN_SYNC_TIMESTAMP` | 10 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `MAX_TIMESTAMP` | 11 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `source.cherry_data_model.cherry_data.organization_group`

---
