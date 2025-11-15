## Model: `organization_sync`

`organization_sync`

*   **Unique ID:** `model.cherry_data_model.organization_sync`
*   **FQN:** `prod.sync_marts.organization_sync`
*   **Description:** (No description provided)
*   **Tags:** `[]`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `RECORD_TYPE_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `ORGANIZATION_ID` | 2 | `NUMBER` |  |  | `[]` | `{}` |
    | `ORGANIZATION_NAME` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `ORGANIZATION_GROUP_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `ORGANIZATION_CODE` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `APPLICATION_LEAD_ID` | 6 | `NUMBER` |  |  | `[]` | `{}` |
    | `SLUG` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `STATUS` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_DEMO` | 9 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_CONDITIONAL_APPROVED` | 10 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `UNDERWRITING_POLICY_ID` | 11 | `NUMBER` |  |  | `[]` | `{}` |
    | `UNDERWRITING_MENU_CODE` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `APPLICATION_VALIDITY_LENGTH` | 13 | `NUMBER` |  |  | `[]` | `{}` |
    | `DENIAL_REAPPLICATION_LENGTH` | 14 | `NUMBER` |  |  | `[]` | `{}` |
    | `CREDIT_LINE_POLICY_CODE` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `SIGNED_RETAIL_INSTALLMENT_AGREEMENT` | 16 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `INDUSTRY` | 17 | `TEXT` |  |  | `[]` | `{}` |
    | `PROMO_PERIOD` | 18 | `NUMBER` |  |  | `[]` | `{}` |
    | `ORGANIZATION_SOURCE` | 19 | `TEXT` |  |  | `[]` | `{}` |
    | `PHONE` | 20 | `TEXT` |  |  | `[]` | `{}` |
    | `WEBSITE` | 21 | `TEXT` |  |  | `[]` | `{}` |
    | `OWNER_USER_ID` | 22 | `NUMBER` |  |  | `[]` | `{}` |
    | `BANK_PARTNER` | 23 | `TEXT` |  |  | `[]` | `{}` |
    | `RISC_STATE` | 24 | `TEXT` |  |  | `[]` | `{}` |
    | `SOURCE_REF` | 25 | `TEXT` |  |  | `[]` | `{}` |
    | `SOURCE_ID` | 26 | `TEXT` |  |  | `[]` | `{}` |
    | `REFUND_FEE` | 27 | `FLOAT` |  |  | `[]` | `{}` |
    | `HAS_NO_REFUND_POLICY` | 28 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_FIRST_LOOK` | 29 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `FIRST_LOOK_DECLINE_EXPLANATION` | 30 | `TEXT` |  |  | `[]` | `{}` |
    | `TREATMENT_PLAN_START_COUNT` | 31 | `NUMBER` |  |  | `[]` | `{}` |
    | `PREAPPROVAL_COUNT` | 32 | `NUMBER` |  |  | `[]` | `{}` |
    | `APPLICATION_PAGE_LOAD_COUNT` | 33 | `NUMBER` |  |  | `[]` | `{}` |
    | `STATEMENT_PAGE_LOAD_COUNT` | 34 | `NUMBER` |  |  | `[]` | `{}` |
    | `TRANSACTION_PAGE_LOAD_COUNT` | 35 | `NUMBER` |  |  | `[]` | `{}` |
    | `DOC_REQUEST_PAGE_LOAD_COUNT` | 36 | `NUMBER` |  |  | `[]` | `{}` |
    | `REPORTING_PAGE_LOAD_COUNT` | 37 | `NUMBER` |  |  | `[]` | `{}` |
    | `TRAINING_PAGE_LOAD_COUNT` | 38 | `NUMBER` |  |  | `[]` | `{}` |
    | `HELP_PAGE_LOAD_COUNT` | 39 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACTIVATED_TIMESTAMP` | 40 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `CREATED_TIMESTAMP` | 41 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `ESTABLISHED_TIMESTAMP` | 42 | `DATE` |  |  | `[]` | `{}` |
    | `UPDATED_TIMESTAMP` | 43 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `CREATED_BY` | 44 | `NUMBER` |  |  | `[]` | `{}` |
    | `UPDATED_BY` | 45 | `NUMBER` |  |  | `[]` | `{}` |
    | `IS_FIVETRAN_DELETED` | 46 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `FIVETRAN_SYNC_TIMESTAMP` | 47 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `TERM_60_PROMO_IS_ENABLED` | 48 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERM_60_IS_ENABLED` | 49 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERM_60_PROMO_MINIMUM_AMOUNT` | 50 | `NUMBER` |  |  | `[]` | `{}` |
    | `TERM_48_PROMO_IS_ENABLED` | 51 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERM_48_IS_ENABLED` | 52 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERM_48_PROMO_MINIMUM_AMOUNT` | 53 | `NUMBER` |  |  | `[]` | `{}` |
    | `TERM_36_PROMO_IS_ENABLED` | 54 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERM_36_IS_ENABLED` | 55 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERM_36_PROMO_MINIMUM_AMOUNT` | 56 | `NUMBER` |  |  | `[]` | `{}` |
    | `TERM_24_PROMO_IS_ENABLED` | 57 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERM_24_IS_ENABLED` | 58 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERM_24_PROMO_MINIMUM_AMOUNT` | 59 | `NUMBER` |  |  | `[]` | `{}` |
    | `TERM_18_PROMO_IS_ENABLED` | 60 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERM_18_IS_ENABLED` | 61 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERM_18_PROMO_MINIMUM_AMOUNT` | 62 | `NUMBER` |  |  | `[]` | `{}` |
    | `TERM_12_PROMO_IS_ENABLED` | 63 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERM_12_IS_ENABLED` | 64 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERM_12_PROMO_MINIMUM_AMOUNT` | 65 | `NUMBER` |  |  | `[]` | `{}` |
    | `TERM_9_PROMO_IS_ENABLED` | 66 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERM_9_IS_ENABLED` | 67 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERM_9_PROMO_MINIMUM_AMOUNT` | 68 | `NUMBER` |  |  | `[]` | `{}` |
    | `TERM_6_PROMO_IS_ENABLED` | 69 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERM_6_IS_ENABLED` | 70 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERM_6_PROMO_MINIMUM_AMOUNT` | 71 | `NUMBER` |  |  | `[]` | `{}` |
    | `TERM_3_PROMO_IS_ENABLED` | 72 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERM_3_IS_ENABLED` | 73 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERM_3_PROMO_MINIMUM_AMOUNT` | 74 | `NUMBER` |  |  | `[]` | `{}` |
    | `MOST_RECENT_PRICING_SETTINGS_VIEW_DATE` | 75 | `DATE` |  |  | `[]` | `{}` |
    | `MOST_RECENT_PRICING_SETTINGS_VIEW_USER_ID` | 76 | `TEXT` |  |  | `[]` | `{}` |
    | `MOST_RECENT_PRICING_SETTINGS_VIEW_USER_EMAIL` | 77 | `TEXT` |  |  | `[]` | `{}` |
    | `TRAILING_90_GROWTH_APPROVAL_GAP` | 78 | `FLOAT` |  |  | `[]` | `{}` |
    | `MAX_TIMESTAMP` | 79 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.src_borrowers`
    *   `model.cherry_data_model.src_cherry_application_menu_setting_outcomes`
    *   `model.cherry_data_model.src_cherry_applications`
    *   `model.cherry_data_model.stg_organization_product_use`
    *   `model.cherry_data_model.stg_pricing_settings_page_views`
    *   `model.cherry_data_model.stg_promo_settings`
    *   `source.cherry_data_model.cherry_data.organization`

---
