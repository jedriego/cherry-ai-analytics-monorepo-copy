## Model: `account_sync_view`

`account_sync_view`

*   **Unique ID:** `model.cherry_data_model.account_sync_view`
*   **FQN:** `prod.sync_marts.account_sync_view`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `ACCOUNT_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `RECORD_TYPE_ID` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_ID` | 3 | `FLOAT` |  |  | `[]` | `{}` |
    | `ALLE_MERCHANT_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `INDUSTRY` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `SLUG` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_DASHBOARD_STATUS` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `TOTAL_TRANSACTION_VOLUME` | 8 | `FLOAT` |  |  | `[]` | `{}` |
    | `FUNDED_CONTRACTS_COUNT` | 9 | `NUMBER` |  |  | `[]` | `{}` |
    | `AVERAGE_TRANSACTION_AMOUNT` | 10 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_7_GROSS_AMOUNT` | 11 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_14_GROSS_AMOUNT` | 12 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_30_GROSS_AMOUNT` | 13 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_60_GROSS_AMOUNT` | 14 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_30_GROSS_AMOUNT` | 15 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_60_GROSS_AMOUNT` | 16 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_90_GROSS_AMOUNT` | 17 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_365_GROSS_AMOUNT` | 18 | `FLOAT` |  |  | `[]` | `{}` |
    | `APPLICATIONS_COUNT` | 19 | `NUMBER` |  |  | `[]` | `{}` |
    | `DENIED_APPLICATIONS_COUNT` | 20 | `NUMBER` |  |  | `[]` | `{}` |
    | `INCOMPLETE_APPLICATIONS_LAST_30_DAYS` | 21 | `NUMBER` |  |  | `[]` | `{}` |
    | `STREET` | 22 | `TEXT` |  |  | `[]` | `{}` |
    | `CITY` | 23 | `TEXT` |  |  | `[]` | `{}` |
    | `STATE` | 24 | `TEXT` |  |  | `[]` | `{}` |
    | `ZIPCODE` | 25 | `TEXT` |  |  | `[]` | `{}` |
    | `MAX_TIMESTAMP` | 26 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.cherry_data_model.convert_to_pt`
    *   `model.cherry_data_model.merchant_account_mapping`
    *   `model.cherry_data_model.src_alle_practice_metadata`
    *   `model.cherry_data_model.src_application_leads`
    *   `model.cherry_data_model.src_merchants`
    *   `model.cherry_data_model.src_organizations`
    *   `model.cherry_data_model.src_partner_practices`
    *   `model.cherry_data_model.src_sf_accounts`
    *   `source.cherry_data_model.cherry_data.applications`
    *   `source.cherry_data_model.cherry_data.loans`
    *   `source.cherry_data_model.cherry_data.merchant_addresses`

---
