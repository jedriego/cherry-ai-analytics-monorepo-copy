## Model: `sales_merchant_totals`

`sales_merchant_totals`

*   **Unique ID:** `model.cherry_data_model.sales_merchant_totals`
*   **FQN:** `prod.revenue_marts.sales_merchant_totals`
*   **Description:** This model provides a consolidated view of merchant details, including  loan totals, demo details, and outstanding approvals. The data is sourced  from the merchant loan totals, stage merchants, demo details, and stage  applications datasets.

*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `MERCHANT_ID` | 1 | `NUMBER` | The unique identifier for the merchant. | The unique identifier for the merchant. | `[]` | `{}` |
    | `SF_ACCOUNT_ID` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `SF_OPPORTUNITY_ID` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `TOTAL_GROSS_AMOUNT` | 4 | `FLOAT` |  |  | `[]` | `{}` |
    | `TOTAL_REVENUE` | 5 | `FLOAT` |  |  | `[]` | `{}` |
    | `TOTAL_CONTRIBUTION_MARGIN` | 6 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_1_GROSS_AMOUNT` | 7 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_7_GROSS_AMOUNT` | 8 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_14_GROSS_AMOUNT` | 9 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_21_GROSS_AMOUNT` | 10 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_30_GROSS_AMOUNT` | 11 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_60_GROSS_AMOUNT` | 12 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_90_GROSS_AMOUNT` | 13 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_120_GROSS_AMOUNT` | 14 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_365_GROSS_AMOUNT` | 15 | `FLOAT` |  |  | `[]` | `{}` |
    | `CURRENT_QUARTER_GROSS_AMOUNT` | 16 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_14_REVENUE` | 17 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_30_REVENUE` | 18 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_60_REVENUE` | 19 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_365_REVENUE` | 20 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_14_CONTRIBUTION_MARGIN` | 21 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_30_CONTRIBUTION_MARGIN` | 22 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_60_CONTRIBUTION_MARGIN` | 23 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_30_GROSS_AMOUNT` | 24 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_60_GROSS_AMOUNT` | 25 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_90_GROSS_AMOUNT` | 26 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_365_GROSS_AMOUNT` | 27 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_30_REVENUE` | 28 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_60_REVENUE` | 29 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_90_REVENUE` | 30 | `FLOAT` |  |  | `[]` | `{}` |
    | `MONTHS_SINCE_GO_LIVE` | 31 | `NUMBER` |  |  | `[]` | `{}` |
    | `WEEKS_SINCE_GO_LIVE` | 32 | `NUMBER` |  |  | `[]` | `{}` |
    | `MONTHLY_GROSS_AMOUNT_AVERAGE` | 33 | `FLOAT` |  |  | `[]` | `{}` |
    | `WEEKLY_GROSS_AMOUNT_AVERAGE` | 34 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_1_FUNDED_CONTRACTS_COUNT` | 35 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_7_FUNDED_CONTRACTS_COUNT` | 36 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_14_FUNDED_CONTRACTS_COUNT` | 37 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_21_FUNDED_CONTRACTS_COUNT` | 38 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_30_FUNDED_CONTRACTS_COUNT` | 39 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_60_FUNDED_CONTRACTS_COUNT` | 40 | `NUMBER` |  |  | `[]` | `{}` |
    | `FUNDED_CONTRACTS_COUNT` | 41 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_FUNDED_CONTRACT_DATE` | 42 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `LAST_FUNDED_CONTRACT_DATE` | 43 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `AVERAGE_TRANSACTION_AMOUNT` | 44 | `FLOAT` |  |  | `[]` | `{}` |
    | `APPLICATIONS_COUNT` | 45 | `NUMBER` |  |  | `[]` | `{}` |
    | `DENIED_APPLICATIONS_COUNT` | 46 | `NUMBER` |  |  | `[]` | `{}` |
    | `APPROVED_VOLUME_OUTSTANDING` | 47 | `FLOAT` |  |  | `[]` | `{}` |
    | `APPROVED_VOLUME_FIRST_60_DAYS` | 48 | `FLOAT` |  |  | `[]` | `{}` |
    | `APPROVED_VOLUME_LAST_7_DAYS` | 49 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_30_APPLICATIONS_COUNT` | 50 | `NUMBER` |  |  | `[]` | `{}` |
    | `COMPLETED_APPLICATIONS_LAST_30_DAYS` | 51 | `NUMBER` |  |  | `[]` | `{}` |
    | `COMPLETED_APPLICATIONS` | 52 | `NUMBER` |  |  | `[]` | `{}` |
    | `APPROVED_APPLICATIONS_LAST_30_DAYS` | 53 | `NUMBER` |  |  | `[]` | `{}` |
    | `APPROVED_APPLICATIONS` | 54 | `NUMBER` |  |  | `[]` | `{}` |
    | `DENIED_APPLICATIONS_LAST_30_DAYS` | 55 | `NUMBER` |  |  | `[]` | `{}` |
    | `INCOMPLETE_APPLICATIONS_LAST_30_DAYS` | 56 | `NUMBER` |  |  | `[]` | `{}` |
    | `FUNDED_APPLICATIONS_LAST_30_DAYS` | 57 | `NUMBER` |  |  | `[]` | `{}` |
    | `FUNDED_APPLICATIONS` | 58 | `NUMBER` |  |  | `[]` | `{}` |
    | `APPROVAL_RATE_LAST_30_DAYS` | 59 | `NUMBER` |  |  | `[]` | `{}` |
    | `FUNDED_RATE_LAST_30_DAYS` | 60 | `NUMBER` |  |  | `[]` | `{}` |
    | `APPLICATION_COMPLETION_RATE_LAST_30_DAYS` | 61 | `NUMBER` |  |  | `[]` | `{}` |
    | `APPROVAL_RATE` | 62 | `NUMBER` |  |  | `[]` | `{}` |
    | `FUNDED_RATE` | 63 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_1_APPLICATIONS_COUNT` | 64 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_4_APPLICATIONS_COUNT` | 65 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_7_APPLICATIONS_COUNT` | 66 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_14_APPLICATIONS_COUNT` | 67 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_21_APPLICATIONS_COUNT` | 68 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_30_APPLICATIONS_COUNT` | 69 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_60_APPLICATIONS_COUNT` | 70 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_1_APPLICATIONS_COMPLETED_COUNT` | 71 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_4_APPLICATIONS_COMPLETED_COUNT` | 72 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_7_APPLICATIONS_COMPLETED_COUNT` | 73 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_14_APPLICATIONS_COMPLETED_COUNT` | 74 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_21_APPLICATIONS_COMPLETED_COUNT` | 75 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_30_APPLICATIONS_COMPLETED_COUNT` | 76 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_60_APPLICATIONS_COMPLETED_COUNT` | 77 | `NUMBER` |  |  | `[]` | `{}` |
    | `MERCHANT_NAME` | 78 | `TEXT` |  |  | `[]` | `{}` |
    | `SF_ACCOUNT_NAME` | 79 | `TEXT` |  |  | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 80 | `TEXT` |  |  | `[]` | `{}` |
    | `INDUSTRY` | 81 | `TEXT` |  |  | `[]` | `{}` |
    | `MARKET_SIZE` | 82 | `TEXT` |  |  | `[]` | `{}` |
    | `PRICING_MENU_NAME` | 83 | `TEXT` |  |  | `[]` | `{}` |
    | `GO_LIVE_DATE` | 84 | `DATE` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_ID_30_DAY` | 85 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_NAME_30_DAY` | 86 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_SUBTEAM_30_DAY` | 87 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_TEAM_30_DAY` | 88 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_DEPARTMENT_30_DAY` | 89 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_ID_30_DAY` | 90 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_NAME_30_DAY` | 91 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_TEAM_30_DAY` | 92 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT_30_DAY` | 93 | `TEXT` |  |  | `[]` | `{}` |
    | `INITIAL_LOOK_ASSESSMENT` | 94 | `TEXT` |  |  | `[]` | `{}` |
    | `INITIAL_PARTNERSHIP_HEALTH_SCORE` | 95 | `FLOAT` |  |  | `[]` | `{}` |
    | `MYSTERY_SHOPPING_SCORE` | 96 | `NUMBER` |  |  | `[]` | `{}` |
    | `LOOK_ASSESSMENT_SEGMENT` | 97 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST` | 98 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST_TEAM` | 99 | `TEXT` |  |  | `[]` | `{}` |
    | `DEMO_OWNER_NAME` | 100 | `TEXT` |  |  | `[]` | `{}` |
    | `DEMO_OWNER_SUBTEAM` | 101 | `TEXT` |  |  | `[]` | `{}` |
    | `DEMO_OWNER_TEAM` | 102 | `TEXT` |  |  | `[]` | `{}` |
    | `DEMO_OWNER_DEPARTMENT` | 103 | `TEXT` |  |  | `[]` | `{}` |
    | `BOOKED_BY_NAME` | 104 | `TEXT` |  |  | `[]` | `{}` |
    | `BOOKED_BY_SUBTEAM` | 105 | `TEXT` |  |  | `[]` | `{}` |
    | `BOOKED_BY_TEAM` | 106 | `TEXT` |  |  | `[]` | `{}` |
    | `BOOKED_BY_DEPARTMENT` | 107 | `TEXT` |  |  | `[]` | `{}` |
    | `BOOKED_BY_CATEGORY` | 108 | `TEXT` |  |  | `[]` | `{}` |
    | `MAX_TIMESTAMP` | 109 | `DATE` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.demo_details_xf`
    *   `model.cherry_data_model.look_assessment_scores`
    *   `model.cherry_data_model.merchant_health_score_daily`
    *   `model.cherry_data_model.merchant_loan_totals`
    *   `model.cherry_data_model.practice_application_totals`
    *   `model.cherry_data_model.src_sf_accounts`
    *   `model.cherry_data_model.stg_merchants`

---
