## Model: `nice_daily_contact_rate_xf_archive`

`nice_daily_contact_rate_xf_archive`

*   **Unique ID:** `model.cherry_data_model.nice_daily_contact_rate_xf_archive`
*   **FQN:** `prod.archive.nice_daily_contact_rate_xf_archive`
*   **Description:** (No description provided)
*   **Tags:** `['archive']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `REFERENCE_DATE` | 1 | `DATE` |  |  | `[]` | `{}` |
    | `EVAL_WEEK` | 2 | `DATE` |  |  | `[]` | `{}` |
    | `EVAL_MONTH` | 3 | `DATE` |  |  | `[]` | `{}` |
    | `IS_WEEKEND` | 4 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `CUMULATIVE_LIVE_MERCHANTS` | 5 | `NUMBER` |  |  | `[]` | `{}` |
    | `NUMBER_SERVICING_ELIGIBLE_BORROWERS` | 6 | `NUMBER` |  |  | `[]` | `{}` |
    | `DENIED_APPLICANTS` | 7 | `NUMBER` |  |  | `[]` | `{}` |
    | `REVIEW_APPLICANTS` | 8 | `NUMBER` |  |  | `[]` | `{}` |
    | `INITIALIZED_APPLICANTS` | 9 | `NUMBER` |  |  | `[]` | `{}` |
    | `APPROVED_APPLICANTS` | 10 | `NUMBER` |  |  | `[]` | `{}` |
    | `APPROVED_NOT_FUNDED_APPLICANTS` | 11 | `NUMBER` |  |  | `[]` | `{}` |
    | `TOTAL_APPLICANTS` | 12 | `NUMBER` |  |  | `[]` | `{}` |
    | `DISPOSITION_NAME` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `NUM_PATIENT_CONTACTS` | 14 | `NUMBER` |  |  | `[]` | `{}` |
    | `NUM_PRACTICE_CONTACTS` | 15 | `NUMBER` |  |  | `[]` | `{}` |
    | `NUM_COLLECTIONS_CONTACTS` | 16 | `NUMBER` |  |  | `[]` | `{}` |
    | `NUM_MISSING_SKILL_NAME_CONTACTS` | 17 | `NUMBER` |  |  | `[]` | `{}` |
    | `NUM_OTHER_CONTACTS` | 18 | `NUMBER` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.nice_inbounds_xf_archive`
    *   `model.cherry_data_model.stg_daily_contact_rate_eligible`

---
