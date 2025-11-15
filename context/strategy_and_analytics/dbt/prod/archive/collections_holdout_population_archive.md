## Model: `collections_holdout_population_archive`

`collections_holdout_population_archive`

*   **Unique ID:** `model.cherry_data_model.collections_holdout_population_archive`
*   **FQN:** `prod.archive.collections_holdout_population_archive`
*   **Description:** (No description provided)
*   **Tags:** `['archive']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `LOAN_ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `CONTRACT_ID` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `BORROWER_ID` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `APPLICATION_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRODUCT_ID` | 5 | `NUMBER` |  |  | `[]` | `{}` |
    | `CHANNEL` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `API_PARTNER` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `PROMO_USED` | 8 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `LOAN_TERM` | 9 | `NUMBER` |  |  | `[]` | `{}` |
    | `CURRENT_APR` | 10 | `FLOAT` |  |  | `[]` | `{}` |
    | `ORIGINAL_APR` | 11 | `FLOAT` |  |  | `[]` | `{}` |
    | `ORIGINAL_LOAN_TERM` | 12 | `NUMBER` |  |  | `[]` | `{}` |
    | `MENU_NAME` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_PAY_IN_FOUR` | 14 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `PURCHASE_AMOUNT` | 15 | `FLOAT` |  |  | `[]` | `{}` |
    | `MERCHANT_FEE` | 16 | `FLOAT` |  |  | `[]` | `{}` |
    | `MERCHANT_FUND` | 17 | `FLOAT` |  |  | `[]` | `{}` |
    | `GROSS_AMOUNT` | 18 | `FLOAT` |  |  | `[]` | `{}` |
    | `DOWN_PAYMENT_AMOUNT` | 19 | `FLOAT` |  |  | `[]` | `{}` |
    | `NET_LOAN_AMOUNT` | 20 | `FLOAT` |  |  | `[]` | `{}` |
    | `FINANCE_CHARGE` | 21 | `FLOAT` |  |  | `[]` | `{}` |
    | `TOTAL_AMOUNT` | 22 | `FLOAT` |  |  | `[]` | `{}` |
    | `INSTALLMENT_AMOUNT` | 23 | `FLOAT` |  |  | `[]` | `{}` |
    | `LOAN_PLAN_STATUS` | 24 | `TEXT` |  |  | `[]` | `{}` |
    | `LOAN_PLAN_SUBSTATUS` | 25 | `TEXT` |  |  | `[]` | `{}` |
    | `OUTSTANDING_BALANCE` | 26 | `FLOAT` |  |  | `[]` | `{}` |
    | `IS_AUTOPAY` | 27 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_FRAUD` | 28 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_DO_NOT_REPORT` | 29 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_DO_NOT_CALL` | 30 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_OUTSOURCED` | 31 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_ACTIVATION` | 32 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `LOAN_STATUS` | 33 | `TEXT` |  |  | `[]` | `{}` |
    | `REFUND_AMOUNT` | 34 | `FLOAT` |  |  | `[]` | `{}` |
    | `FUNDED_AT_PT` | 35 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `FUNDED_QUARTER` | 36 | `TEXT` |  |  | `[]` | `{}` |
    | `LOANPRO_LOAN_ID` | 37 | `NUMBER` |  |  | `[]` | `{}` |
    | `CREATED_AT_PT` | 38 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `CREATED_BY_NAME` | 39 | `TEXT` |  |  | `[]` | `{}` |
    | `CREATED_BY_EMAIL` | 40 | `TEXT` |  |  | `[]` | `{}` |
    | `UPDATED_AT_PT` | 41 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `UPDATED_BY_NAME` | 42 | `TEXT` |  |  | `[]` | `{}` |
    | `UPDATED_BY_EMAIL` | 43 | `TEXT` |  |  | `[]` | `{}` |
    | `RISK_SCORE` | 44 | `NUMBER` |  |  | `[]` | `{}` |
    | `VINTAGE` | 45 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_FEE_RATE` | 46 | `FLOAT` |  |  | `[]` | `{}` |
    | `FORECASTED_INTEREST` | 47 | `FLOAT` |  |  | `[]` | `{}` |
    | `FORECASTED_FEES` | 48 | `FLOAT` |  |  | `[]` | `{}` |
    | `FORECASTED_SERVICING_FEE` | 49 | `FLOAT` |  |  | `[]` | `{}` |
    | `REVENUE` | 50 | `FLOAT` |  |  | `[]` | `{}` |
    | `CONTRIBUTION_MARGIN` | 51 | `FLOAT` |  |  | `[]` | `{}` |
    | `MERCHANT_ID` | 52 | `NUMBER` |  |  | `[]` | `{}` |
    | `MERCHANT_NAME` | 53 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_TYPE` | 54 | `TEXT` |  |  | `[]` | `{}` |
    | `SF_ACCOUNT_ID` | 55 | `TEXT` |  |  | `[]` | `{}` |
    | `SF_ACCOUNT_NAME` | 56 | `TEXT` |  |  | `[]` | `{}` |
    | `PRIMARY_MERCHANT_ID` | 57 | `FLOAT` |  |  | `[]` | `{}` |
    | `INDUSTRY` | 58 | `TEXT` |  |  | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 59 | `TEXT` |  |  | `[]` | `{}` |
    | `PRACTICE_SEGMENT` | 60 | `TEXT` |  |  | `[]` | `{}` |
    | `MARKET_SIZE` | 61 | `TEXT` |  |  | `[]` | `{}` |
    | `PRICING_TIER` | 62 | `TEXT` |  |  | `[]` | `{}` |
    | `GO_LIVE_DATE` | 63 | `DATE` |  |  | `[]` | `{}` |
    | `ORGANIZATION_GO_LIVE_DATE` | 64 | `DATE` |  |  | `[]` | `{}` |
    | `PRACTICE_SEGMENT_START_DATE` | 65 | `DATE` |  |  | `[]` | `{}` |
    | `MERCHANT_TERMINATED_BY_RISK` | 66 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ORGANIZATION_ID` | 67 | `NUMBER` |  |  | `[]` | `{}` |
    | `ORGANIZATION_NAME` | 68 | `TEXT` |  |  | `[]` | `{}` |
    | `ORGANIZATION_GROUP_ID` | 69 | `NUMBER` |  |  | `[]` | `{}` |
    | `ORGANIZATION_GROUP_NAME` | 70 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT_CURRENT` | 71 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_TEAM_CURRENT` | 72 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_CURRENT` | 73 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_TERRITORY_CURRENT` | 74 | `TEXT` |  |  | `[]` | `{}` |
    | `CURRENT_PARTNERSHIP_HEALTH_SCORE` | 75 | `FLOAT` |  |  | `[]` | `{}` |
    | `ALLE_PRACTICE_TYPE` | 76 | `TEXT` |  |  | `[]` | `{}` |
    | `FIRST_ALLE_DEMO_DATE` | 77 | `DATE` |  |  | `[]` | `{}` |
    | `ONBOARDING_OWNER_ID` | 78 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_OWNER_NAME` | 79 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_OWNER_DEPARTMENT` | 80 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_OWNER_TEAM` | 81 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_OWNER_SUBTEAM` | 82 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_OWNER_TITLE` | 83 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_ID` | 84 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_NAME` | 85 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_DEPARTMENT` | 86 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_TEAM` | 87 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_SUBTEAM` | 88 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_TITLE` | 89 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_CREDIT_PERCENT` | 90 | `FLOAT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_GROSS_AMOUNT` | 91 | `FLOAT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_ASSISTOR_ID` | 92 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_ASSISTOR_NAME` | 93 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_ASSISTOR_DEPARTMENT` | 94 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_ASSISTOR_TEAM` | 95 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_ASSISTOR_SUBTEAM` | 96 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_ASSISTOR_TITLE` | 97 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_ASSISTOR_CREDIT_PERCENT` | 98 | `FLOAT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_ASSISTOR_GROSS_AMOUNT` | 99 | `FLOAT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_ID` | 100 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_NAME` | 101 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT` | 102 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_TEAM` | 103 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_TITLE` | 104 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_TERRITORY` | 105 | `TEXT` |  |  | `[]` | `{}` |
    | `DEPARTMENT_OWNERSHIP` | 106 | `TEXT` |  |  | `[]` | `{}` |
    | `ORGANIZATION_AGE` | 107 | `TEXT` |  |  | `[]` | `{}` |
    | `DEMO_BOOKED_BY_NAME` | 108 | `TEXT` |  |  | `[]` | `{}` |
    | `DEMO_BOOKED_BY_TEAM` | 109 | `TEXT` |  |  | `[]` | `{}` |
    | `DEMO_BOOKED_BY_CATEGORY` | 110 | `TEXT` |  |  | `[]` | `{}` |
    | `INITIAL_LOOK_ASSESSMENT` | 111 | `TEXT` |  |  | `[]` | `{}` |
    | `LATEST_LOOK_ASSESSMENT` | 112 | `TEXT` |  |  | `[]` | `{}` |
    | `STATE_ABBREVIATION` | 113 | `TEXT` |  |  | `[]` | `{}` |
    | `HOLDOUT_FLAG` | 114 | `BOOLEAN` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.loan_info_xf`

---
