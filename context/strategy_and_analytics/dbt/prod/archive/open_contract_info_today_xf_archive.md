## Model: `open_contract_info_today_xf_archive`

`open_contract_info_today_xf_archive`

*   **Unique ID:** `model.cherry_data_model.open_contract_info_today_xf_archive`
*   **FQN:** `prod.archive.open_contract_info_today_xf_archive`
*   **Description:** (No description provided)
*   **Tags:** `['archive', 'daily', 'hourly', 'loan-statuses']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `LOAN_ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `LOANPRO_LOAN_ID` | 2 | `NUMBER` |  |  | `[]` | `{}` |
    | `CONTRACT_ID` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `BORROWER_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_NAME` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `LAST_NAME` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `PHONE_NUMBER` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `EMAIL` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_DO_NOT_CALL` | 9 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_CEASE_AND_DESIST` | 10 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_FRAUD` | 11 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_DECEASED` | 12 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ADDRESS_LINE_ONE` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `CITY_NAME` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `STATE_ABBREVIATION` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `ZIPCODE` | 16 | `TEXT` |  |  | `[]` | `{}` |
    | `TIMEZONE` | 17 | `TEXT` |  |  | `[]` | `{}` |
    | `VANTAGE_SCORE` | 18 | `FLOAT` |  |  | `[]` | `{}` |
    | `MERCHANT_NAME` | 19 | `TEXT` |  |  | `[]` | `{}` |
    | `LAST_INSTALLMENT_NUMBER` | 20 | `NUMBER` |  |  | `[]` | `{}` |
    | `LAST_SCHEDULED_PMT_DATE` | 21 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `NEXT_SCHEDULED_PMT_DATE` | 22 | `DATE` |  |  | `[]` | `{}` |
    | `PRINCIPAL_BALANCE` | 23 | `NUMBER` |  |  | `[]` | `{}` |
    | `PERDIEM` | 24 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRINCIPAL_DUE` | 25 | `NUMBER` |  |  | `[]` | `{}` |
    | `FEES_DUE` | 26 | `NUMBER` |  |  | `[]` | `{}` |
    | `INTEREST_DUE` | 27 | `NUMBER` |  |  | `[]` | `{}` |
    | `AMOUNT_DUE` | 28 | `NUMBER` |  |  | `[]` | `{}` |
    | `TOTAL_AMOUNT_DUE` | 29 | `NUMBER` |  |  | `[]` | `{}` |
    | `DAYS_PAST_DUE` | 30 | `NUMBER` |  |  | `[]` | `{}` |
    | `DELINQUENCY_BUCKET` | 31 | `NUMBER` |  |  | `[]` | `{}` |
    | `PAYOFF` | 32 | `NUMBER` |  |  | `[]` | `{}` |
    | `CHARGE_OFF` | 33 | `NUMBER` |  |  | `[]` | `{}` |
    | `LOAN_STATUS` | 34 | `TEXT` |  |  | `[]` | `{}` |
    | `LOAN_SUBSTATUS` | 35 | `TEXT` |  |  | `[]` | `{}` |
    | `HAS_PENDING_PAYMENT` | 36 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `HAS_ACTIVE_COMMITMENT` | 37 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `HAS_ACTIVE_FORBEARANCE` | 38 | `BOOLEAN` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt_utils.group_by`
    *   `model.cherry_data_model.borrowers_merged_emails_xf`
    *   `model.cherry_data_model.int_active_commitments`
    *   `model.cherry_data_model.int_aggregated_vantage_scores`
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.int_max_loan_flag_values`
    *   `model.cherry_data_model.int_pending_cherry_payments`
    *   `model.cherry_data_model.loan_statuses_today_xf`
    *   `model.cherry_data_model.src_merchants`
    *   `model.cherry_data_model.stg_active_forbearances`
    *   `model.cherry_data_model.stg_borrower_addresses_with_tz`
    *   `model.cherry_data_model.stg_soonest_payments`

---
