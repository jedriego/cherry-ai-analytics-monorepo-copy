## Model: `merchant_applications_xf`

`merchant_applications_xf`

*   **Unique ID:** `model.cherry_data_model.merchant_applications_xf`
*   **FQN:** `prod.core_marts.merchant_applications_xf`
*   **Description:** (No description provided)
*   **Tags:** `['core']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `MERCHANT_APPLICATION_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_LEAD_ID` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `USER_ID` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `INDUSTRY` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `REGISTRATION_TYPE` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `APPLICATION_CREATED_AT_PT` | 7 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `FIRST_SUBMITTED_TIMESTAMP` | 8 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `FIRST_SUBMITTED_TIMESTAMP_PT` | 9 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `LAST_SUBMITTED_TIMESTAMP_PT` | 10 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `FIRST_IN_REVIEW_TIMESTAMP_PT` | 11 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `LAST_IN_REVIEW_TIMESTAMP_PT` | 12 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `FINAL_OUTCOME_TIMESTAMP_PT` | 13 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `FIRST_OUTCOME_AFTER_SUBMITTED` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `FIRST_OUTCOME_AFTER_REVIEW` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `FINAL_OUTCOME_STATUS` | 16 | `TEXT` |  |  | `[]` | `{}` |
    | `ADDITIONAL_INFO_OUTCOME` | 17 | `TEXT` |  |  | `[]` | `{}` |
    | `UNIQUE_MERCHANT_LEAD_STATUSES` | 18 | `TEXT` |  |  | `[]` | `{}` |
    | `MOST_RECENT_APPLICATION_STATUS` | 19 | `TEXT` |  |  | `[]` | `{}` |
    | `DECISION_STATUS` | 20 | `TEXT` |  |  | `[]` | `{}` |
    | `FIRST_DECISION_TIMESTAMP_PT` | 21 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `LAST_DECISION_TIMESTAMP_PT` | 22 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `FIRST_SUBMITTED_TO_FIRST_DECISION_SECONDS` | 23 | `NUMBER` |  |  | `[]` | `{}` |
    | `LAST_SUBMITTED_TO_LAST_DECISION_SECONDS` | 24 | `NUMBER` |  |  | `[]` | `{}` |
    | `ADDITIONAL_INFO_TO_OUTCOME_SECONDS` | 25 | `NUMBER` |  |  | `[]` | `{}` |
    | `IS_REVIEW` | 26 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_INSTANT_DECISION` | 27 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_ADDITIONAL_INFO_REQUIRED` | 28 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_APPLICATION_SUBMITTED` | 29 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `REGISTRATION_TIMESTAMP_PT` | 30 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `IS_REGISTRATION_COMPLETE` | 31 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_ALLE_MERCHANT_LEAD` | 32 | `BOOLEAN` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt_utils.generate_surrogate_key`
    *   `model.cherry_data_model.registration_to_industry_mapping`
    *   `model.cherry_data_model.stg_merchant_leads`
    *   `model.cherry_data_model.stg_merchant_leads_history`

---
