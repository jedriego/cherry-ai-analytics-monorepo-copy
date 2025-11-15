## Model: `retention_average_volumes_and_percent_transacting_pdm_vet_xf`

`retention_average_volumes_and_percent_transacting_pdm_vet_xf`

*   **Unique ID:** `model.cherry_data_model.retention_average_volumes_and_percent_transacting_pdm_vet_xf`
*   **FQN:** `prod.revenue_marts.retention_average_volumes_and_percent_transacting_pdm_vet_xf`
*   **Description:** (No description provided)
*   **Tags:** `['revenue_analytics']`
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
    | `AVERAGE_LAST_30_HEALTHY_VOLUME_UNCAPPED` | 10 | `FLOAT` |  |  | `[]` | `{}` |
    | `PRIOR_DAY_HEALTHY_VOLUME_RUN_RATE` | 11 | `FLOAT` |  |  | `[]` | `{}` |
    | `TOTAL_PRIOR_DAY_HEALTHY_VOLUME` | 12 | `FLOAT` |  |  | `[]` | `{}` |
    | `TOTAL_LAST_30_HEALTHY_VOLUME` | 13 | `FLOAT` |  |  | `[]` | `{}` |
    | `TOTAL_PRACTICE_POTENTIAL_EXTERNAL_DATA` | 14 | `FLOAT` |  |  | `[]` | `{}` |
    | `TEST_GROUP_PRIOR_DAY_HEALTHY_VOLUME_RUN_RATE` | 15 | `FLOAT` |  |  | `[]` | `{}` |
    | `TRAILING_7_DAY_AVERAGE_PERCENT_HEALTHY_TRANSACTING_IN_LAST_30` | 16 | `NUMBER` |  |  | `[]` | `{}` |
    | `TEST_GROUP_TRAILING_7_DAY_AVERAGE_PERCENT_HEALTHY_TRANSACTING_IN_LAST_30` | 17 | `NUMBER` |  |  | `[]` | `{}` |
    | `TEST_GROUP_TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME` | 18 | `FLOAT` |  |  | `[]` | `{}` |
    | `TEST_GROUP_TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME_UNCAPPED` | 19 | `FLOAT` |  |  | `[]` | `{}` |
    | `TRAILING_7_DAY_PERCENT_HEALTHY_TRANSACTING_IN_LAST_30_TARGET` | 20 | `FLOAT` |  |  | `[]` | `{}` |
    | `TRAILING_7_DAY_PERCENT_HEALTHY_TRANSACTING_IN_LAST_30_TARGET_QUARTERLY` | 21 | `FLOAT` |  |  | `[]` | `{}` |
    | `TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME_TARGET` | 22 | `FLOAT` |  |  | `[]` | `{}` |
    | `TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME_TARGET_QUARTERLY` | 23 | `FLOAT` |  |  | `[]` | `{}` |
    | `TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME` | 24 | `FLOAT` |  |  | `[]` | `{}` |
    | `TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME_UNCAPPED` | 25 | `FLOAT` |  |  | `[]` | `{}` |
    | `VOLUME_PHASE_IN` | 26 | `FLOAT` |  |  | `[]` | `{}` |
    | `TRANSACTING_PHASE_IN` | 27 | `FLOAT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.loan_info_xf`
    *   `model.cherry_data_model.practice_info_full_xf`
    *   `model.cherry_data_model.src_gsheets_retention_phase_ins`
    *   `model.cherry_data_model.src_gsheets_retention_targets`
    *   `snapshot.cherry_data_model.enhanced_practice_potential_snapshot_v3`

---
