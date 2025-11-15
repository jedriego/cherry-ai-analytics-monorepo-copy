## Model: `merchant_sync`

`merchant_sync`

*   **Unique ID:** `model.cherry_data_model.merchant_sync`
*   **FQN:** `prod.sync_marts.merchant_sync`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `RECORD_TYPE_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_ID` | 2 | `NUMBER` |  |  | `[]` | `{}` |
    | `MERCHANT_NAME` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_CODE` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `ORGANIZATION_ID` | 5 | `NUMBER` |  |  | `[]` | `{}` |
    | `BANK_NAME` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_TYPE` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_CLASSIFICATION` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_DESCRIPTION` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_STATUS` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `STATUS` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_DASHBOARD_STATUS` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `STARTED_TIMESTAMP` | 13 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `CREATED_TIMESTAMP` | 14 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `UPDATED_TIMESTAMP` | 15 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `CREATED_BY` | 16 | `NUMBER` |  |  | `[]` | `{}` |
    | `UPDATED_BY` | 17 | `NUMBER` |  |  | `[]` | `{}` |
    | `TOTAL_GROSS_AMOUNT` | 18 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_1_GROSS_AMOUNT` | 19 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_1_GROSS_AMOUNT` | 20 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_7_GROSS_AMOUNT` | 21 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_7_GROSS_AMOUNT` | 22 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_14_GROSS_AMOUNT` | 23 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_14_GROSS_AMOUNT` | 24 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_21_GROSS_AMOUNT` | 25 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_21_GROSS_AMOUNT` | 26 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_30_GROSS_AMOUNT` | 27 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_30_GROSS_AMOUNT` | 28 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_60_GROSS_AMOUNT` | 29 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_60_GROSS_AMOUNT` | 30 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_90_GROSS_AMOUNT` | 31 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_90_GROSS_AMOUNT` | 32 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_120_GROSS_AMOUNT` | 33 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_120_GROSS_AMOUNT` | 34 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_365_GROSS_AMOUNT` | 35 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_365_GROSS_AMOUNT` | 36 | `FLOAT` |  |  | `[]` | `{}` |
    | `ACCOUNT_NUMBER` | 37 | `TEXT` |  |  | `[]` | `{}` |
    | `ROUTING_NUMBER` | 38 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_NICKNAME` | 39 | `TEXT` |  |  | `[]` | `{}` |
    | `PHONE` | 40 | `TEXT` |  |  | `[]` | `{}` |
    | `STREET` | 41 | `TEXT` |  |  | `[]` | `{}` |
    | `CITY` | 42 | `TEXT` |  |  | `[]` | `{}` |
    | `STATE` | 43 | `TEXT` |  |  | `[]` | `{}` |
    | `ZIPCODE` | 44 | `TEXT` |  |  | `[]` | `{}` |
    | `TAX_ID` | 45 | `TEXT` |  |  | `[]` | `{}` |
    | `GROUP_ID` | 46 | `NUMBER` |  |  | `[]` | `{}` |
    | `POC_USER_ID` | 47 | `NUMBER` |  |  | `[]` | `{}` |
    | `MERCHANT_LEAD_ID` | 48 | `NUMBER` |  |  | `[]` | `{}` |
    | `COUNTERPARTY_ID` | 49 | `TEXT` |  |  | `[]` | `{}` |
    | `GIACT_LOG_ID` | 50 | `TEXT` |  |  | `[]` | `{}` |
    | `MONTHLY_FEE` | 51 | `FLOAT` |  |  | `[]` | `{}` |
    | `PROMO_PERIOD` | 52 | `NUMBER` |  |  | `[]` | `{}` |
    | `CHARGED_MONTHLY_FEE` | 53 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_FIVETRAN_DELETED` | 54 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `FIVETRAN_SYNC_TIMESTAMP` | 55 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `MAX_TIMESTAMP` | 56 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.merchant_account_mapping`
    *   `source.cherry_data_model.cherry_data.loans`
    *   `source.cherry_data_model.cherry_data.merchant_addresses`
    *   `source.cherry_data_model.cherry_data.merchants`
    *   `source.cherry_data_model.cherry_data.organization`
    *   `source.cherry_data_model.salesforce.accounts`

---
