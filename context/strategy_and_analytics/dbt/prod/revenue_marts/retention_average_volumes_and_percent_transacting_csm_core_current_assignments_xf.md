## Model: `retention_average_volumes_and_percent_transacting_csm_core_current_assignments_xf`

`retention_average_volumes_and_percent_transacting_csm_core_current_assignments_xf`

*   **Unique ID:** `model.cherry_data_model.retention_average_volumes_and_percent_transacting_csm_core_current_assignments_xf`
*   **FQN:** `prod.revenue_marts.retention_average_volumes_and_percent_transacting_csm_core_current_assignments_xf`
*   **Description:** (No description provided)
*   **Tags:** `['revenue_analytics', 'revenue_hourly']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `FULL_DATE` | 1 | `DATE` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_TEAM` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `PRACTICE_COUNT` | 6 | `NUMBER` |  |  | `[]` | `{}` |
    | `TEST_GROUP_PRACTICE_COUNT` | 7 | `NUMBER` |  |  | `[]` | `{}` |
    | `PERCENT_HEALTHY_TRANSACTING_IN_LAST_30_DAYS` | 8 | `NUMBER` |  |  | `[]` | `{}` |
    | `AVERAGE_LAST_30_HEALTHY_VOLUME` | 9 | `FLOAT` |  |  | `[]` | `{}` |
    | `PRIOR_DAY_HEALTHY_VOLUME_RUN_RATE` | 10 | `FLOAT` |  |  | `[]` | `{}` |
    | `TOTAL_PRIOR_DAY_HEALTHY_VOLUME` | 11 | `FLOAT` |  |  | `[]` | `{}` |
    | `TEST_GROUP_PRIOR_DAY_HEALTHY_VOLUME_RUN_RATE` | 12 | `FLOAT` |  |  | `[]` | `{}` |
    | `TRAILING_7_DAY_AVERAGE_PERCENT_HEALTHY_TRANSACTING_IN_LAST_30` | 13 | `NUMBER` |  |  | `[]` | `{}` |
    | `TEST_GROUP_TRAILING_7_DAY_AVERAGE_PERCENT_HEALTHY_TRANSACTING_IN_LAST_30` | 14 | `NUMBER` |  |  | `[]` | `{}` |
    | `TEST_GROUP_TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME` | 15 | `FLOAT` |  |  | `[]` | `{}` |
    | `TRAILING_7_DAY_PERCENT_HEALTHY_TRANSACTING_IN_LAST_30_TARGET` | 16 | `FLOAT` |  |  | `[]` | `{}` |
    | `TRAILING_7_DAY_PERCENT_HEALTHY_TRANSACTING_IN_LAST_30_TARGET_QUARTERLY` | 17 | `FLOAT` |  |  | `[]` | `{}` |
    | `TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME_TARGET` | 18 | `FLOAT` |  |  | `[]` | `{}` |
    | `TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME_TARGET_QUARTERLY` | 19 | `FLOAT` |  |  | `[]` | `{}` |
    | `TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME` | 20 | `FLOAT` |  |  | `[]` | `{}` |
    | `VOLUME_PHASE_IN` | 21 | `FLOAT` |  |  | `[]` | `{}` |
    | `TRANSACTING_PHASE_IN` | 22 | `FLOAT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.loan_info_xf`
    *   `model.cherry_data_model.practice_info_full_xf`
    *   `model.cherry_data_model.src_gsheets_retention_phase_ins`
    *   `model.cherry_data_model.src_gsheets_retention_targets`

---
