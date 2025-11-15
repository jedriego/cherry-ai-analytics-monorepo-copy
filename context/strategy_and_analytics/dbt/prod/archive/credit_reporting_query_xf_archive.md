## Model: `credit_reporting_query_xf_archive`

`credit_reporting_query_xf_archive`

*   **Unique ID:** `model.cherry_data_model.credit_reporting_query_xf_archive`
*   **FQN:** `prod.archive.credit_reporting_query_xf_archive`
*   **Description:** (No description provided)
*   **Tags:** `['archive']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `ASSOCIATION_CODE` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `FIRST_NAME` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `MIDDLE_NAME` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `LAST_NAME` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `ADDRESS_LINE_ONE` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `ADDRESS_LINE_TWO` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `CITY` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `STATE` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `ZIPCODE` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `SSN` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `PHONE_NUMBER` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `DATE_OF_BIRTH` | 12 | `DATE` |  |  | `[]` | `{}` |
    | `END_OF_MONTH_LOAN_STATUS` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `CONSUMER_INFORMATION_INDICATOR` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_NUMBER` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `PORTFOLIO_TYPE` | 16 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_TYPE` | 17 | `TEXT` |  |  | `[]` | `{}` |
    | `DATE_OPEN` | 18 | `DATE` |  |  | `[]` | `{}` |
    | `DATE_OF_LAST_PAYMENT` | 19 | `DATE` |  |  | `[]` | `{}` |
    | `DATE_CLOSED` | 20 | `DATE` |  |  | `[]` | `{}` |
    | `ACCOUNT_STATUS` | 21 | `TEXT` |  |  | `[]` | `{}` |
    | `PAYMENT_RATING` | 22 | `TEXT` |  |  | `[]` | `{}` |
    | `DATE_OF_FIRST_DELINQUENCY` | 23 | `DATE` |  |  | `[]` | `{}` |
    | `DAYS_PAST_DUE` | 24 | `NUMBER` |  |  | `[]` | `{}` |
    | `CREDIT_LIMIT` | 25 | `NUMBER` |  |  | `[]` | `{}` |
    | `HIGHEST_CREDIT` | 26 | `FLOAT` |  |  | `[]` | `{}` |
    | `CURRENT_BALANCE` | 27 | `NUMBER` |  |  | `[]` | `{}` |
    | `AMOUNT_PAST_DUE` | 28 | `NUMBER` |  |  | `[]` | `{}` |
    | `MONTHLY_PAYMENT` | 29 | `FLOAT` |  |  | `[]` | `{}` |
    | `ACTUAL_PAYMENT` | 30 | `NUMBER` |  |  | `[]` | `{}` |
    | `TERMS_FREQUENCY` | 31 | `TEXT` |  |  | `[]` | `{}` |
    | `TERMS` | 32 | `NUMBER` |  |  | `[]` | `{}` |
    | `ORIGINAL_CHARGE_OFF_AMOUNT` | 33 | `NUMBER` |  |  | `[]` | `{}` |
    | `ORIGINAL_CHARGE_OFF_DATE` | 34 | `DATE` |  |  | `[]` | `{}` |
    | `DATE_OF_ACCOUNT_INFORMATION` | 35 | `DATE` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.borrowers_merged_emails_xf`
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.src_borrower_addresses`
    *   `model.cherry_data_model.src_borrowers`
    *   `model.cherry_data_model.src_cherry_loans`
    *   `model.cherry_data_model.src_debt_sale_transactions`
    *   `model.cherry_data_model.src_loan_plans`
    *   `model.cherry_data_model.src_loanpro_chargeoff_transactions`
    *   `model.cherry_data_model.stg_active_loanpro_payments`
    *   `model.cherry_data_model.stg_borrower_addresses_with_tz`
    *   `model.cherry_data_model.stg_idicore_bankruptcies`
    *   `model.cherry_data_model.stg_loanpro_chargeoffs_aggregation`
    *   `source.cherry_data_model.cherry_data.loan_status_history`

---
