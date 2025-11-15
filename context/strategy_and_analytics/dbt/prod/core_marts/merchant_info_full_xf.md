## Model: `merchant_info_full_xf`

`merchant_info_full_xf`

*   **Unique ID:** `model.cherry_data_model.merchant_info_full_xf`
*   **FQN:** `prod.core_marts.merchant_info_full_xf`
*   **Description:** Comprehensive merchant information table that combines core merchant data with enriched metrics including loan volume performance, lifetime value calculations, acquisition costs, and practice-level analytics. This model serves as the primary merchant dimension table by joining merchant details with loan totals, customer lifetime value analysis, and practice performance metrics. It provides a complete 360-degree view of merchant relationships including early performance indicators (first 7, 14, 30, 60 days volume), financial projections, cost analysis, and operational assessments. The model enables comprehensive merchant analysis for retention strategies, performance monitoring, profitability assessment, and strategic decision-making. All base merchant fields from stg_merchants are inherited, with additional calculated metrics and analytics layered on top.

*   **Tags:** `['core', 'hourly', 'practice_hourly', 'core_hourly']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `MERCHANT_ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
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
    | `IS_DEMO` | 67 | `BOOLEAN` |  |  | `[]` | `{}` |
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
    | `FIRST_7_GROSS_AMOUNT` | 119 | `FLOAT` | Total gross loan amount generated by the merchant in their first 7 days of operation. This early performance indicator helps identify merchants with strong initial adoption and can be predictive of long-term success. Generated using jinja templating for dynamic metric creation.
 | Total gross loan amount generated by the merchant in their first 7 days of operation. This early performance indicator helps identify merchants with strong initial adoption and can be predictive of long-term success. Generated using jinja templating for dynamic metric creation.
 | `[]` | `{}` |
    | `FIRST_14_GROSS_AMOUNT` | 120 | `FLOAT` | Total gross loan amount generated by the merchant in their first 14 days of operation. Provides a slightly longer view of early performance trends and helps validate initial success indicators from the first 7 days.
 | Total gross loan amount generated by the merchant in their first 14 days of operation. Provides a slightly longer view of early performance trends and helps validate initial success indicators from the first 7 days.
 | `[]` | `{}` |
    | `FIRST_30_GROSS_AMOUNT` | 121 | `FLOAT` | Total gross loan amount generated by the merchant in their first 30 days of operation. This metric represents the first month performance and is often used as a key indicator of merchant onboarding success and early engagement.
 | Total gross loan amount generated by the merchant in their first 30 days of operation. This metric represents the first month performance and is often used as a key indicator of merchant onboarding success and early engagement.
 | `[]` | `{}` |
    | `FIRST_60_GROSS_AMOUNT` | 122 | `FLOAT` | Total gross loan amount generated by the merchant in their first 60 days of operation. Represents the first two months of performance and helps identify merchants who may have slower initial adoption but build momentum over time.
 | Total gross loan amount generated by the merchant in their first 60 days of operation. Represents the first two months of performance and helps identify merchants who may have slower initial adoption but build momentum over time.
 | `[]` | `{}` |
    | `TOTAL_GROSS_AMOUNT` | 123 | `FLOAT` | Total gross loan amount generated by the merchant across their entire relationship history. This lifetime volume metric is crucial for understanding overall merchant value and contribution to the business.
 | Total gross loan amount generated by the merchant across their entire relationship history. This lifetime volume metric is crucial for understanding overall merchant value and contribution to the business.
 | `[]` | `{}` |
    | `LIFETIME_VALUE` | 124 | `FLOAT` | Calculated lifetime value of the merchant relationship, representing the total expected net present value of revenue over the projected merchant lifespan. Used for strategic decision-making, retention investment prioritization, and ROI analysis.
 | Calculated lifetime value of the merchant relationship, representing the total expected net present value of revenue over the projected merchant lifespan. Used for strategic decision-making, retention investment prioritization, and ROI analysis.
 | `[]` | `{}` |
    | `TOTAL_ACQUISITION_COST` | 125 | `FLOAT` | Total cost incurred to acquire this merchant, including all sales, marketing, onboarding, and setup costs. Used for calculating customer acquisition cost (CAC) and return on investment metrics.
 | Total cost incurred to acquire this merchant, including all sales, marketing, onboarding, and setup costs. Used for calculating customer acquisition cost (CAC) and return on investment metrics.
 | `[]` | `{}` |
    | `GROSS_AMOUNT_TOTAL` | 126 | `FLOAT` | Total gross amount used in lifetime value calculations, may differ from total_gross_amount due to different calculation periods or methodologies used in the lifetime value model.
 | Total gross amount used in lifetime value calculations, may differ from total_gross_amount due to different calculation periods or methodologies used in the lifetime value model.
 | `[]` | `{}` |
    | `EVALUATION_MONTHS` | 127 | `NUMBER` | Number of months used in the lifetime value evaluation period. Indicates the time horizon over which the lifetime value projection is calculated.
 | Number of months used in the lifetime value evaluation period. Indicates the time horizon over which the lifetime value projection is calculated.
 | `[]` | `{}` |
    | `TOTAL_CONTRIBUTION_MARGIN_EXPECTED` | 128 | `FLOAT` | Expected total contribution margin from this merchant over the evaluation period. Represents the projected profit contribution after variable costs, used for profitability analysis and strategic planning.
 | Expected total contribution margin from this merchant over the evaluation period. Represents the projected profit contribution after variable costs, used for profitability analysis and strategic planning.
 | `[]` | `{}` |
    | `MONTHLY_RETENTION_COST` | 129 | `NUMBER` | Monthly cost allocated for retaining this merchant, including account management, customer success, and ongoing support activities. Used for calculating retention ROI and optimizing retention strategies.
 | Monthly cost allocated for retaining this merchant, including account management, customer success, and ongoing support activities. Used for calculating retention ROI and optimizing retention strategies.
 | `[]` | `{}` |
    | `SALES_DEVELOPMENT_COST` | 130 | `NUMBER` | Cost attributed to sales development activities for acquiring this merchant, including lead generation, qualification, and early-stage sales efforts.
 | Cost attributed to sales development activities for acquiring this merchant, including lead generation, qualification, and early-stage sales efforts.
 | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_COST` | 131 | `NUMBER` | Cost attributed to account executive activities for acquiring this merchant, including sales meetings, proposal development, and closing activities.
 | Cost attributed to account executive activities for acquiring this merchant, including sales meetings, proposal development, and closing activities.
 | `[]` | `{}` |
    | `ONBOARDING_COST` | 132 | `NUMBER` | Cost incurred for onboarding this merchant, including setup, training, integration, and initial support activities required to get the merchant operational.
 | Cost incurred for onboarding this merchant, including setup, training, integration, and initial support activities required to get the merchant operational.
 | `[]` | `{}` |
    | `MARKETING_COST` | 133 | `FLOAT` | Marketing costs attributed to acquiring this merchant, including advertising, content creation, and promotional activities that contributed to the acquisition.
 | Marketing costs attributed to acquiring this merchant, including advertising, content creation, and promotional activities that contributed to the acquisition.
 | `[]` | `{}` |
    | `MARKETING_BOX_COST` | 134 | `FLOAT` | Cost of marketing materials, welcome packages, or promotional items provided to the merchant as part of the acquisition or onboarding process.
 | Cost of marketing materials, welcome packages, or promotional items provided to the merchant as part of the acquisition or onboarding process.
 | `[]` | `{}` |
    | `WEBSITE_IMPLEMENTATION_COST` | 135 | `FLOAT` | Cost for implementing website integration, payment flows, or other technical implementations required for the merchant to begin using the platform.
 | Cost for implementing website integration, payment flows, or other technical implementations required for the merchant to begin using the platform.
 | `[]` | `{}` |
    | `INITIAL_LOOK_ASSESSMENT` | 136 | `TEXT` | Initial assessment or evaluation score assigned to the merchant during the onboarding or early relationship phase. Used for tracking initial impressions and comparing with later performance.
 | Initial assessment or evaluation score assigned to the merchant during the onboarding or early relationship phase. Used for tracking initial impressions and comparing with later performance.
 | `[]` | `{}` |
    | `LATEST_LOOK_ASSESSMENT` | 137 | `TEXT` | Most recent assessment or evaluation score for the merchant. Used for tracking merchant performance evolution and identifying changes in merchant quality or engagement over time.
 | Most recent assessment or evaluation score for the merchant. Used for tracking merchant performance evolution and identifying changes in merchant quality or engagement over time.
 | `[]` | `{}` |
    | `PAST_30D_PRACTICE_CHERRY_VOLUME` | 138 | `FLOAT` | Total Cherry platform volume for the entire practice (all merchant locations) in the past 30 days. Provides practice-level performance context beyond individual merchant performance.
 | Total Cherry platform volume for the entire practice (all merchant locations) in the past 30 days. Provides practice-level performance context beyond individual merchant performance.
 | `[]` | `{}` |
    | `PAST_30D_PRACTICE_CHERRY_SHARE_PCT` | 139 | `FLOAT` | Percentage of the practice's total financing volume that goes through the Cherry platform in the past 30 days. Indicates market share and platform adoption within the practice.
 | Percentage of the practice's total financing volume that goes through the Cherry platform in the past 30 days. Indicates market share and platform adoption within the practice.
 | `[]` | `{}` |
    | `LAST_PRACTICE_MYSTERY_SHOPPING_DATE` | 140 | `DATE` | Date of the most recent mystery shopping evaluation conducted for this practice. Mystery shopping provides insights into customer experience and operational quality from a customer perspective.
 | Date of the most recent mystery shopping evaluation conducted for this practice. Mystery shopping provides insights into customer experience and operational quality from a customer perspective.
 | `[]` | `{}` |
    | `LAST_PRACTICE_MYSTERY_SHOPPING_LOOK_RESPONSE` | 141 | `TEXT` | Results or response from the most recent mystery shopping evaluation. Provides qualitative insights into customer experience, staff knowledge, and operational effectiveness at the practice level. | Results or response from the most recent mystery shopping evaluation. Provides qualitative insights into customer experience, staff knowledge, and operational effectiveness at the practice level. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.merchant_lifetime_value`
    *   `model.cherry_data_model.merchant_loan_totals`
    *   `model.cherry_data_model.practice_info_xf`
    *   `model.cherry_data_model.stg_merchants`

---
