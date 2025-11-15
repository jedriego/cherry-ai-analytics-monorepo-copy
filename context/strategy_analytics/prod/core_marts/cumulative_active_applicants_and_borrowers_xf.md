## Model: `cumulative_active_applicants_and_borrowers_xf`

`cumulative_active_applicants_and_borrowers_xf`

*   **Unique ID:** `model.cherry_data_model.cumulative_active_applicants_and_borrowers_xf`
*   **FQN:** `prod.core_marts.cumulative_active_applicants_and_borrowers_xf`
*   **Description:** Daily time series model that tracks the cumulative count of active applicants and borrowers in the system. This model provides a comprehensive view of the active user base by combining new applicants (those with unexpired applications but no loans) and existing borrowers  (those with active loans in LATE or OPEN status). The model creates a daily snapshot  starting from January 1, 2023, and is used for monitoring business growth, user acquisition, and portfolio health metrics. New applicants are defined as borrowers who have submitted applications that haven't expired but haven't yet received loans, while existing borrowers are those with currently active loan products.

*   **Tags:** `['core']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `DAY` | 1 | `DATE` | Date dimension representing each calendar day for which metrics are calculated. Serves as the primary key for this daily time series, covering dates from  January 1, 2023 through yesterday (current date minus 1 day).
 | Date dimension representing each calendar day for which metrics are calculated. Serves as the primary key for this daily time series, covering dates from  January 1, 2023 through yesterday (current date minus 1 day).
 | `[]` | `{}` |
    | `NEW_APPLICANT_CNT` | 2 | `NUMBER` | Count of distinct new applicants on the given day. New applicants are defined as borrowers who have submitted applications that are still valid (not expired) as of the measurement date, have applied on or before the measurement date, but do not have any loans (neither loan_id nor active_loan_id) and are not counted as existing borrowers with active loans. This metric uses ZEROIFNULL to ensure clean reporting when no new applicants are present on a given day.
 | Count of distinct new applicants on the given day. New applicants are defined as borrowers who have submitted applications that are still valid (not expired) as of the measurement date, have applied on or before the measurement date, but do not have any loans (neither loan_id nor active_loan_id) and are not counted as existing borrowers with active loans. This metric uses ZEROIFNULL to ensure clean reporting when no new applicants are present on a given day.
 | `[]` | `{}` |
    | `EXISTING_BORROWER_CNT` | 3 | `NUMBER` | Count of distinct existing borrowers on the given day. Existing borrowers are defined as those who have active loans with status of either 'LATE' or 'OPEN' as recorded in the daily loan snapshot. This represents borrowers who currently have outstanding loan obligations with the company. The metric uses ZEROIFNULL to ensure clean  reporting when no existing borrowers are present on a given day.
 | Count of distinct existing borrowers on the given day. Existing borrowers are defined as those who have active loans with status of either 'LATE' or 'OPEN' as recorded in the daily loan snapshot. This represents borrowers who currently have outstanding loan obligations with the company. The metric uses ZEROIFNULL to ensure clean  reporting when no existing borrowers are present on a given day.
 | `[]` | `{}` |
    | `TOTAL_BORROWER_CNT` | 4 | `NUMBER` | Total count of active users in the system, calculated as the sum of new_applicant_cnt and existing_borrower_cnt. This provides a comprehensive view of the total active user base, including both those in the application pipeline and those with active loans. The metric represents the complete picture of users who are either actively engaged in the lending process or have current loan obligations. | Total count of active users in the system, calculated as the sum of new_applicant_cnt and existing_borrower_cnt. This provides a comprehensive view of the total active user base, including both those in the application pipeline and those with active loans. The metric represents the complete picture of users who are either actively engaged in the lending process or have current loan obligations. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.applications_loans_xf`
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.daily_loan_xf`

---
