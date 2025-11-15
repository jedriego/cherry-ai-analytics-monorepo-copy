## Model: `safeselect_cured_accounts_yesterday_xf_archive`

`safeselect_cured_accounts_yesterday_xf_archive`

*   **Unique ID:** `model.cherry_data_model.safeselect_cured_accounts_yesterday_xf_archive`
*   **FQN:** `prod.archive.safeselect_cured_accounts_yesterday_xf_archive`
*   **Description:** (No description provided)
*   **Tags:** `['archive']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `BORROWER_ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `CONTRACT_ID` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `FIRST_NAME` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `LAST_NAME` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `VANTAGE_SCORE` | 5 | `FLOAT` |  |  | `[]` | `{}` |
    | `MERCHANT_NAME` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `ORIGINAL_MATURITY_DATE` | 7 | `DATE` |  |  | `[]` | `{}` |
    | `PAYOFF` | 8 | `NUMBER` |  |  | `[]` | `{}` |
    | `AMOUNT_DUE` | 9 | `NUMBER` |  |  | `[]` | `{}` |
    | `DAYS_PAST_DUE` | 10 | `NUMBER` |  |  | `[]` | `{}` |
    | `PHONE_NUMBER` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `EMAIL` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `LAST_INSTALLMENT_NUMBER` | 13 | `NUMBER` |  |  | `[]` | `{}` |
    | `DQ_STATUS` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `CITY_NAME` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `STATE_ABBREVIATION` | 16 | `TEXT` |  |  | `[]` | `{}` |
    | `ZIPCODE` | 17 | `TEXT` |  |  | `[]` | `{}` |
    | `TIMEZONE` | 18 | `TEXT` |  |  | `[]` | `{}` |
    | `CALLING_ORDER` | 19 | `NUMBER` |  |  | `[]` | `{}` |
    | `SERVICING_URL` | 20 | `TEXT` |  |  | `[]` | `{}` |
    | `EXCLUSION_REASON` | 21 | `TEXT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.cherry_data_model.convert_to_pt`
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.open_contract_info_today_xf_archive`
    *   `model.cherry_data_model.stg_active_loan_setups`

---
