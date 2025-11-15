## Model: `merchant_info_xf`

`merchant_info_xf`

*   **Unique ID:** `model.cherry_data_model.merchant_info_xf`
*   **FQN:** `prod.core_marts.merchant_info_xf`
*   **Description:** Filtered merchant information table that provides a production-ready view of merchant data by excluding demo merchants from the comprehensive merchant_info_full_xf model. This model serves as the primary merchant dimension table for production analytics and reporting by filtering out test, demo, and development merchants that should not be included in business metrics and performance analysis. The model inherits all columns and enriched metrics from merchant_info_full_xf including loan volume performance, lifetime value calculations, acquisition costs, and practice-level analytics, but ensures only real operational merchants are included. This filtered view is essential for accurate business intelligence, financial reporting, and strategic analysis where demo data could skew results or provide misleading insights about actual merchant performance and business health.

*   **Tags:** `['core']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `MERCHANT_ID` | 1 | `NUMBER` | Unique identifier for the merchant. Inherited from merchant_info_full_xf. Only includes production merchants, excluding demo accounts.
 | Unique identifier for the merchant. Inherited from merchant_info_full_xf. Only includes production merchants, excluding demo accounts.
 | `[]` | `{}` |
    | `PRIMARY_MERCHANT_ID` | 2 | `FLOAT` |  |  | `[]` | `{}` |
    | `ORGANIZATION_ID` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `MERCHANT_NAME` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `ORGANIZATION_NAME` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `ORGANIZATION_GROUP_ID` | 7 | `NUMBER` |  |  | `[]` | `{}` |
    | `ORGANIZATION_GROUP_NAME` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `SF_ACCOUNT_ID` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `SF_ACCOUNT_NAME` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `SF_OPPORTUNITY_ID` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `SF_OPPORTUNITY_NAME` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERNAL_REFERRER_ID` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERNAL_REFERRER` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `FIRST_APPLICATION_DATE` | 15 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `FIRST_CONTRACT_TIMESTAMP` | 16 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_APPLICATION_TIMESTAMP` | 17 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_APPROVED_APPLICATION_TIMESTAMP` | 18 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_CONTRACT_TIMESTAMP` | 19 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `COMMISSION_START_DATE` | 20 | `DATE` |  |  | `[]` | `{}` |
    | `MERCHANT_CREATED_AT_PT` | 21 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `MERCHANT_CREATION_DATE` | 22 | `DATE` |  |  | `[]` | `{}` |
    | `MERCHANT_UPDATED_AT_PT` | 23 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `GO_LIVE_DATE` | 24 | `DATE` |  |  | `[]` | `{}` |
    | `GO_LIVE_DATE_EVALUATION` | 25 | `TEXT` |  |  | `[]` | `{}` |
    | `DAYS_SINCE_GO_LIVE` | 26 | `NUMBER` |  |  | `[]` | `{}` |
    | `MONTHS_SINCE_GO_LIVE` | 27 | `NUMBER` |  |  | `[]` | `{}` |
    | `ORGANIZATION_GO_LIVE_DATE` | 28 | `DATE` |  |  | `[]` | `{}` |
    | `TERMINATION_DATE` | 29 | `DATE` |  |  | `[]` | `{}` |
    | `WEBSITE_IMPLEMENTATION_DATE` | 30 | `DATE` |  |  | `[]` | `{}` |
    | `GOOGLE_BUSINESS_PROFILE_IMPLEMENTATION_DATE` | 31 | `DATE` |  |  | `[]` | `{}` |
    | `FACEBOOK_IMPLEMENTATION_DATE` | 32 | `DATE` |  |  | `[]` | `{}` |
    | `INSTAGRAM_IMPLEMENTATION_DATE` | 33 | `DATE` |  |  | `[]` | `{}` |
    | `TIKTOK_IMPLEMENTATION_DATE` | 34 | `DATE` |  |  | `[]` | `{}` |
    | `YELP_IMPLEMENTATION_DATE` | 35 | `DATE` |  |  | `[]` | `{}` |
    | `APPOINTMENT_REMINDER_IMPLEMENTATION_DATE` | 36 | `DATE` |  |  | `[]` | `{}` |
    | `INTAKE_FORM_IMPLEMENTATION_DATE` | 37 | `DATE` |  |  | `[]` | `{}` |
    | `ESHOP_IMPLEMENTATION_DATE` | 38 | `DATE` |  |  | `[]` | `{}` |
    | `MEMBERSHIP_IMPLEMENTATION_DATE` | 39 | `DATE` |  |  | `[]` | `{}` |
    | `INTEGRATION_COMPLETION_DATE` | 40 | `DATE` |  |  | `[]` | `{}` |
    | `CUSTOM_PRICING_SHEET_IMPLEMENTATION_DATE` | 41 | `DATE` |  |  | `[]` | `{}` |
    | `CHERRY_ANNOUNCEMENT_DATE` | 42 | `DATE` |  |  | `[]` | `{}` |
    | `MERCHANT_TYPE` | 43 | `TEXT` |  |  | `[]` | `{}` |
    | `SALESFORCE_URL` | 44 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_DASHBOARD_URL` | 45 | `TEXT` |  |  | `[]` | `{}` |
    | `HEADS_UP_URL` | 46 | `TEXT` |  |  | `[]` | `{}` |
    | `POC_USER_ID` | 47 | `NUMBER` |  |  | `[]` | `{}` |
    | `POC_FULL_NAME` | 48 | `TEXT` |  |  | `[]` | `{}` |
    | `POC_EMAIL` | 49 | `TEXT` |  |  | `[]` | `{}` |
    | `POC_PHONE` | 50 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_LEAD_ID` | 51 | `NUMBER` |  |  | `[]` | `{}` |
    | `IS_ACTIVE` | 52 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `SUPER_ORG_NAME` | 53 | `TEXT` |  |  | `[]` | `{}` |
    | `ADDRESS_LINE_ONE` | 54 | `TEXT` |  |  | `[]` | `{}` |
    | `CITY_NAME` | 55 | `TEXT` |  |  | `[]` | `{}` |
    | `STATE_ABBREVIATION` | 56 | `TEXT` |  |  | `[]` | `{}` |
    | `ZIPCODE` | 57 | `TEXT` |  |  | `[]` | `{}` |
    | `PHONE` | 58 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_INDUSTRY_SEGMENT` | 59 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_INDUSTRY_SEGMENT_EVALUATION` | 60 | `TEXT` |  |  | `[]` | `{}` |
    | `ORGANIZATION_WEBSITE` | 61 | `TEXT` |  |  | `[]` | `{}` |
    | `SLUG` | 62 | `TEXT` |  |  | `[]` | `{}` |
    | `PRICING_TIER` | 63 | `TEXT` |  |  | `[]` | `{}` |
    | `PRICING_MENU_NAME` | 64 | `TEXT` |  |  | `[]` | `{}` |
    | `MAX_INTEREST_BEARING_TERM_ENABLED` | 65 | `TEXT` |  |  | `[]` | `{}` |
    | `PAY_IN_4_ENABLED` | 66 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_DEMO` | 67 | `BOOLEAN` | Boolean flag indicating whether this merchant is a demo or test merchant. In this filtered model, this field will always be false or null, as demo merchants (where is_demo = true) are explicitly excluded from the results. This filtering ensures that only production merchants are included in business analysis and reporting.
 | Boolean flag indicating whether this merchant is a demo or test merchant. In this filtered model, this field will always be false or null, as demo merchants (where is_demo = true) are explicitly excluded from the results. This filtering ensures that only production merchants are included in business analysis and reporting.
 | `[]` | `{}` |
    | `APPLICATION_LEAD_ID` | 68 | `NUMBER` |  |  | `[]` | `{}` |
    | `CHERRY_DB_INDUSTRY` | 69 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_ACTIVE_ORGANIZATION` | 70 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_ACTIVE_PRACTICE` | 71 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `SF_INDUSTRY` | 72 | `TEXT` |  |  | `[]` | `{}` |
    | `UNDERWRITING_MERCHANT_POTENTIAL` | 73 | `TEXT` |  |  | `[]` | `{}` |
    | `FULL_TIME_VS_PART_TIME` | 74 | `TEXT` |  |  | `[]` | `{}` |
    | `MARKET_SIZE` | 75 | `TEXT` |  |  | `[]` | `{}` |
    | `SF_NUMBER_OF_EMPLOYEES` | 76 | `NUMBER` |  |  | `[]` | `{}` |
    | `ESTIMATED_MONTHLY_FINANCING` | 77 | `NUMBER` |  |  | `[]` | `{}` |
    | `MERCHANT_SIZE` | 78 | `TEXT` |  |  | `[]` | `{}` |
    | `PATIENTS_PER_WEEK_RANGE` | 79 | `TEXT` |  |  | `[]` | `{}` |
    | `PATIENTS_PER_WEEK` | 80 | `TEXT` |  |  | `[]` | `{}` |
    | `LOOK_ASSESSMENT_DASHBOARD_URL` | 81 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_ID` | 82 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE` | 83 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_SUBTEAM` | 84 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_TEAM` | 85 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_DEPARTMENT` | 86 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_IS_ACTIVE` | 87 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST_ID` | 88 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST` | 89 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST_TEAM` | 90 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST_DEPARTMENT` | 91 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_ID` | 92 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER` | 93 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_TEAM` | 94 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT` | 95 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_TERRITORY` | 96 | `TEXT` |  |  | `[]` | `{}` |
    | `DEPARTMENT_OWNERSHIP` | 97 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_STAGE` | 98 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_TERMINATED` | 99 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `MERCHANT_TERMINATED_BY_RISK` | 100 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_PRIMARY_ACCOUNT` | 101 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NO_WEBSITE` | 102 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NO_SOCIAL_MEDIA` | 103 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NO_CUSTOMIZABLE_APPOINTMENT_REMINDERS` | 104 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_ID_30_DAY` | 105 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_NAME_30_DAY` | 106 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_SUBTEAM_30_DAY` | 107 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_TEAM_30_DAY` | 108 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_DEPARTMENT_30_DAY` | 109 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_TITLE_30_DAY` | 110 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_ID_30_DAY` | 111 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_NAME_30_DAY` | 112 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_TEAM_30_DAY` | 113 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT_30_DAY` | 114 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_TERRITORY_30_DAY` | 115 | `TEXT` |  |  | `[]` | `{}` |
    | `ORGANIZATION_NUMBER_OF_PRACTICES` | 116 | `NUMBER` |  |  | `[]` | `{}` |
    | `IS_PART_OF_MULTI_PRACTICE_ORG` | 117 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `PRACTICE_NUMBER_OF_MERCHANTS` | 118 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_7_GROSS_AMOUNT` | 119 | `FLOAT` | Total gross loan amount generated by the merchant in their first 7 days of operation. Inherited from merchant_info_full_xf. Only includes data from production merchants, ensuring accurate early performance analysis without demo data contamination.
 | Total gross loan amount generated by the merchant in their first 7 days of operation. Inherited from merchant_info_full_xf. Only includes data from production merchants, ensuring accurate early performance analysis without demo data contamination.
 | `[]` | `{}` |
    | `FIRST_14_GROSS_AMOUNT` | 120 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_30_GROSS_AMOUNT` | 121 | `FLOAT` | Total gross loan amount generated by the merchant in their first 30 days of operation. Inherited from merchant_info_full_xf. Filtered to exclude demo merchants for accurate onboarding success analysis.
 | Total gross loan amount generated by the merchant in their first 30 days of operation. Inherited from merchant_info_full_xf. Filtered to exclude demo merchants for accurate onboarding success analysis.
 | `[]` | `{}` |
    | `FIRST_60_GROSS_AMOUNT` | 122 | `FLOAT` |  |  | `[]` | `{}` |
    | `TOTAL_GROSS_AMOUNT` | 123 | `FLOAT` | Total gross loan amount generated by the merchant across their entire relationship. Inherited from merchant_info_full_xf. Excludes demo merchants to ensure accurate lifetime volume reporting and merchant value assessment. | Total gross loan amount generated by the merchant across their entire relationship. Inherited from merchant_info_full_xf. Excludes demo merchants to ensure accurate lifetime volume reporting and merchant value assessment. | `[]` | `{}` |
    | `LIFETIME_VALUE` | 124 | `FLOAT` | Calculated lifetime value of the merchant relationship. Inherited from merchant_info_full_xf. Only includes production merchants, ensuring accurate LTV calculations for strategic decision-making and ROI analysis.
 | Calculated lifetime value of the merchant relationship. Inherited from merchant_info_full_xf. Only includes production merchants, ensuring accurate LTV calculations for strategic decision-making and ROI analysis.
 | `[]` | `{}` |
    | `TOTAL_ACQUISITION_COST` | 125 | `FLOAT` | Total cost incurred to acquire this merchant. Inherited from merchant_info_full_xf. Filtered to exclude demo merchants for accurate CAC calculations and return on investment analysis.
 | Total cost incurred to acquire this merchant. Inherited from merchant_info_full_xf. Filtered to exclude demo merchants for accurate CAC calculations and return on investment analysis.
 | `[]` | `{}` |
    | `GROSS_AMOUNT_TOTAL` | 126 | `FLOAT` |  |  | `[]` | `{}` |
    | `EVALUATION_MONTHS` | 127 | `NUMBER` |  |  | `[]` | `{}` |
    | `TOTAL_CONTRIBUTION_MARGIN_EXPECTED` | 128 | `FLOAT` |  |  | `[]` | `{}` |
    | `MONTHLY_RETENTION_COST` | 129 | `NUMBER` |  |  | `[]` | `{}` |
    | `SALES_DEVELOPMENT_COST` | 130 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_COST` | 131 | `NUMBER` |  |  | `[]` | `{}` |
    | `ONBOARDING_COST` | 132 | `NUMBER` |  |  | `[]` | `{}` |
    | `MARKETING_COST` | 133 | `FLOAT` |  |  | `[]` | `{}` |
    | `MARKETING_BOX_COST` | 134 | `FLOAT` |  |  | `[]` | `{}` |
    | `WEBSITE_IMPLEMENTATION_COST` | 135 | `FLOAT` |  |  | `[]` | `{}` |
    | `INITIAL_LOOK_ASSESSMENT` | 136 | `TEXT` |  |  | `[]` | `{}` |
    | `LATEST_LOOK_ASSESSMENT` | 137 | `TEXT` |  |  | `[]` | `{}` |
    | `PAST_30D_PRACTICE_CHERRY_VOLUME` | 138 | `FLOAT` |  |  | `[]` | `{}` |
    | `PAST_30D_PRACTICE_CHERRY_SHARE_PCT` | 139 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_PRACTICE_MYSTERY_SHOPPING_DATE` | 140 | `DATE` |  |  | `[]` | `{}` |
    | `LAST_PRACTICE_MYSTERY_SHOPPING_LOOK_RESPONSE` | 141 | `TEXT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.merchant_info_full_xf`

---
