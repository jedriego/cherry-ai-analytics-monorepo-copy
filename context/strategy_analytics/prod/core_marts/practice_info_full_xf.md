## Model: `practice_info_full_xf`

`practice_info_full_xf`

*   **Unique ID:** `model.cherry_data_model.practice_info_full_xf`
*   **FQN:** `prod.core_marts.practice_info_full_xf`
*   **Description:** **Comprehensive Practice Information and Analytics Dimension (Full Dataset)**
This model serves as Cherry's complete practice information and analytics dimension table, combining base practice data from stg_practices with extensive calculated metrics including  early performance indicators, lifetime value calculations, application success rates, health  assessments, market share data, and retention analytics. Unlike practice_info_xf, this model  includes ALL practice records, including those with null primary_merchant_id.
**Key Business Logic:** - **Complete Dataset**: Includes all practice records regardless of primary_merchant_id status - **Jinja-Generated Metrics**: Uses sophisticated jinja templating to dynamically generate metrics
  for multiple time periods (first 1, 4, 7, 14, 21, 30, 60 days for applications; first
  7, 14, 30, 60, 90, 120, 365 days for loans)
- **Multi-Platform Integration**: Handles both Cherry and Alle merchant relationships with
  sophisticated logic for primary merchant ID determination and platform-specific metrics
- **Historical User Context**: Provides 30-day post go-live user ownership context for opportunity
  owners and retention owners with historical role tracking

**Critical Data Sources:** - `stg_practices`: Core staging model with practice dimension data from Salesforce and merchants - Multiple calculated metric sources: loan totals, application totals, lifetime value, health scores - Historical user and territory assignments with temporal validity windows
**Primary Use Cases:** - Source model for practice_info_xf (production clean version) - Complete practice analytics including incomplete/test records - Data quality analysis and primary_merchant_id validation - Comprehensive practice research and administrative workflows

*   **Tags:** `['core', 'hourly', 'practice_hourly', 'core_hourly']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SF_ACCOUNT_ID` | 1 | `TEXT` | **Salesforce Account Identifier**
Primary unique identifier for the Salesforce account record. This serves as the primary key for practice-level analysis and links to all Salesforce-derived data including opportunity, user ownership, and territory information. Used extensively across analytics for practice identification and cross-system data joining.
 | **Salesforce Account Identifier**
Primary unique identifier for the Salesforce account record. This serves as the primary key for practice-level analysis and links to all Salesforce-derived data including opportunity, user ownership, and territory information. Used extensively across analytics for practice identification and cross-system data joining.
 | `[]` | `{}` |
    | `SF_OPPORTUNITY_ID` | 2 | `TEXT` | **Salesforce Opportunity Identifier**
Unique identifier for the primary Salesforce opportunity associated with this practice. Links to sales process data including opportunity ownership, stage progression, and sales attribution. Used for sales performance analysis and lead-to-customer conversion tracking.
 | **Salesforce Opportunity Identifier**
Unique identifier for the primary Salesforce opportunity associated with this practice. Links to sales process data including opportunity ownership, stage progression, and sales attribution. Used for sales performance analysis and lead-to-customer conversion tracking.
 | `[]` | `{}` |
    | `SF_ACCOUNT_NAME` | 3 | `TEXT` | **Salesforce Account Name**
Display name of the practice as recorded in Salesforce. Used for reporting, dashboards, and user-facing applications where practice identification is needed. May differ from organization name in cases of multi-location practices.
 | **Salesforce Account Name**
Display name of the practice as recorded in Salesforce. Used for reporting, dashboards, and user-facing applications where practice identification is needed. May differ from organization name in cases of multi-location practices.
 | `[]` | `{}` |
    | `SF_OPPORTUNITY_NAME` | 4 | `TEXT` | **Salesforce Opportunity Name**
Display name of the primary sales opportunity associated with this practice. Used for sales process tracking and opportunity-level analysis.
 | **Salesforce Opportunity Name**
Display name of the primary sales opportunity associated with this practice. Used for sales process tracking and opportunity-level analysis.
 | `[]` | `{}` |
    | `PRIMARY_MERCHANT_ID` | 5 | `FLOAT` | **Primary Merchant Identifier**
Primary key for this table representing the unique practice identifier. Similar to  cherry_merchant_id but with special handling for Alle locations which may have 2 distinct  merchant_id's - the practice will be based on the non-Alle merchant_id which is then  absorbed as the primary_merchant_id. Primary merchant ID's maintain a 1-to-1 relationship  with Salesforce accounts, which serve as the source of much of the sales and retention  related information in this model. May be null in this full dataset for incomplete records.
 | **Primary Merchant Identifier**
Primary key for this table representing the unique practice identifier. Similar to  cherry_merchant_id but with special handling for Alle locations which may have 2 distinct  merchant_id's - the practice will be based on the non-Alle merchant_id which is then  absorbed as the primary_merchant_id. Primary merchant ID's maintain a 1-to-1 relationship  with Salesforce accounts, which serve as the source of much of the sales and retention  related information in this model. May be null in this full dataset for incomplete records.
 | `[]` | `{}` |
    | `CHERRY_MERCHANT_ID` | 6 | `FLOAT` | **Cherry Merchant Identifier**
Cherry's internal merchant identifier for the primary Cherry platform integration. Used for linking to Cherry-specific transaction data, portal usage, and platform analytics. May be null for Alle-only practices.
 | **Cherry Merchant Identifier**
Cherry's internal merchant identifier for the primary Cherry platform integration. Used for linking to Cherry-specific transaction data, portal usage, and platform analytics. May be null for Alle-only practices.
 | `[]` | `{}` |
    | `ALLE_MERCHANT_ID` | 7 | `NUMBER` | **Alle Merchant Identifier**
Alle platform merchant identifier for practices with Alle integration. Used for linking to Alle-specific transaction data and platform analytics. May be null for Cherry-only practices.
 | **Alle Merchant Identifier**
Alle platform merchant identifier for practices with Alle integration. Used for linking to Alle-specific transaction data and platform analytics. May be null for Cherry-only practices.
 | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_ID` | 8 | `NUMBER` | **Primary Organization Identifier**
Unique identifier for the organization associated with this practice's primary merchant. Used for multi-practice organization analysis and grouping related practices under the same organizational entity.
 | **Primary Organization Identifier**
Unique identifier for the organization associated with this practice's primary merchant. Used for multi-practice organization analysis and grouping related practices under the same organizational entity.
 | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_NAME` | 9 | `TEXT` | **Primary Organization Name**
Display name of the organization associated with this practice. Used for organizational reporting and multi-practice relationship analysis.
 | **Primary Organization Name**
Display name of the organization associated with this practice. Used for organizational reporting and multi-practice relationship analysis.
 | `[]` | `{}` |
    | `ALLE_BUSINESS_ID` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `ALLE_LOCATION_ID` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `APPLICATION_LEAD_ID` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `COMMISSION_START_DATE` | 13 | `DATE` |  |  | `[]` | `{}` |
    | `INITIAL_TRANSACTIONS_DATE` | 14 | `DATE` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_APPLICATION_TIMESTAMP` | 15 | `TIMESTAMP_NTZ` | **First Application Timestamp**
Timestamp of the first loan application submitted by this practice. Used for onboarding timeline analysis and measuring time-to-first-activity metrics.
 | **First Application Timestamp**
Timestamp of the first loan application submitted by this practice. Used for onboarding timeline analysis and measuring time-to-first-activity metrics.
 | `[]` | `{}` |
    | `PRACTICE_FIRST_APPROVED_APPLICATION_TIMESTAMP` | 16 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_CONTRACT_TIMESTAMP` | 17 | `TIMESTAMP_NTZ` | **First Contract Timestamp**
Timestamp of the first funded loan contract for this practice. Represents the first successful loan transaction and key onboarding milestone.
 | **First Contract Timestamp**
Timestamp of the first funded loan contract for this practice. Represents the first successful loan transaction and key onboarding milestone.
 | `[]` | `{}` |
    | `PRACTICE_GO_LIVE_DATE` | 18 | `DATE` | **Practice Go-Live Date**
Official date when the practice became active with Cherry services. Derived from initial_transactions_date when available, otherwise calculated from first application or contract dates. Critical for all performance timing calculations and cohort analysis.
 | **Practice Go-Live Date**
Official date when the practice became active with Cherry services. Derived from initial_transactions_date when available, otherwise calculated from first application or contract dates. Critical for all performance timing calculations and cohort analysis.
 | `[]` | `{}` |
    | `PRACTICE_GO_LIVE_DATE_EVALUATION` | 19 | `TEXT` |  |  | `[]` | `{}` |
    | `DAYS_SINCE_PRACTICE_GO_LIVE` | 20 | `NUMBER` | **Days Since Go-Live**
Number of days between practice go-live date and current date. Used for practice lifecycle analysis, cohort segmentation, and time-based performance calculations.
 | **Days Since Go-Live**
Number of days between practice go-live date and current date. Used for practice lifecycle analysis, cohort segmentation, and time-based performance calculations.
 | `[]` | `{}` |
    | `MONTHS_SINCE_PRACTICE_GO_LIVE` | 21 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_ORGANIZATION_GO_LIVE_DATE` | 22 | `DATE` |  |  | `[]` | `{}` |
    | `PRACTICE_ORGANIZATION_SECOND_YEAR_START_DATE` | 23 | `DATE` |  |  | `[]` | `{}` |
    | `DEPARTMENT_OWNERSHIP` | 24 | `TEXT` |  |  | `[]` | `{}` |
    | `TERMINATION_DATE` | 25 | `DATE` |  |  | `[]` | `{}` |
    | `ONBOARDING_DATE` | 26 | `DATE` |  |  | `[]` | `{}` |
    | `ONBOARDING_SCHEDULED_TIMESTAMP` | 27 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `ONBOARDING_TYPE` | 28 | `TEXT` |  |  | `[]` | `{}` |
    | `WEBSITE_IMPLEMENTATION_DATE` | 29 | `DATE` |  |  | `[]` | `{}` |
    | `GOOGLE_BUSINESS_PROFILE_IMPLEMENTATION_DATE` | 30 | `DATE` |  |  | `[]` | `{}` |
    | `FACEBOOK_IMPLEMENTATION_DATE` | 31 | `DATE` |  |  | `[]` | `{}` |
    | `INSTAGRAM_IMPLEMENTATION_DATE` | 32 | `DATE` |  |  | `[]` | `{}` |
    | `TIKTOK_IMPLEMENTATION_DATE` | 33 | `DATE` |  |  | `[]` | `{}` |
    | `YELP_IMPLEMENTATION_DATE` | 34 | `DATE` |  |  | `[]` | `{}` |
    | `APPOINTMENT_REMINDER_IMPLEMENTATION_DATE` | 35 | `DATE` |  |  | `[]` | `{}` |
    | `INTAKE_FORM_IMPLEMENTATION_DATE` | 36 | `DATE` |  |  | `[]` | `{}` |
    | `BILLING_NOTIFICATIONS_IMPLEMENTATION_DATE` | 37 | `DATE` |  |  | `[]` | `{}` |
    | `ESHOP_IMPLEMENTATION_DATE` | 38 | `DATE` |  |  | `[]` | `{}` |
    | `MEMBERSHIP_IMPLEMENTATION_DATE` | 39 | `DATE` |  |  | `[]` | `{}` |
    | `INTEGRATION_COMPLETION_DATE` | 40 | `DATE` |  |  | `[]` | `{}` |
    | `CUSTOM_PRICING_SHEET_IMPLEMENTATION_DATE` | 41 | `DATE` |  |  | `[]` | `{}` |
    | `CUSTOM_MARKETING_IMPLEMENTATION_DATE` | 42 | `DATE` |  |  | `[]` | `{}` |
    | `CHERRY_ANNOUNCEMENT_DATE` | 43 | `DATE` |  |  | `[]` | `{}` |
    | `EMAIL_BLAST_DATE` | 44 | `DATE` |  |  | `[]` | `{}` |
    | `CREATED_DATE_PT` | 45 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `PARENT_ID` | 46 | `TEXT` |  |  | `[]` | `{}` |
    | `TOP_PARENT_SF_ID` | 47 | `TEXT` |  |  | `[]` | `{}` |
    | `ADDRESS_LINE_ONE` | 48 | `TEXT` | **Primary Address Line**
Street address of the practice location. Used for geographic analysis, territory assignment, and location-based reporting.
 | **Primary Address Line**
Street address of the practice location. Used for geographic analysis, territory assignment, and location-based reporting.
 | `[]` | `{}` |
    | `CITY_NAME` | 49 | `TEXT` | **Practice City**
City where the practice is located. Used for geographic segmentation and market analysis.
 | **Practice City**
City where the practice is located. Used for geographic segmentation and market analysis.
 | `[]` | `{}` |
    | `STATE_ABBREVIATION` | 50 | `TEXT` | **Practice State**
Two-letter state abbreviation for the practice location. Used for state-level analysis and regulatory reporting.
 | **Practice State**
Two-letter state abbreviation for the practice location. Used for state-level analysis and regulatory reporting.
 | `[]` | `{}` |
    | `ZIPCODE` | 51 | `TEXT` | **Practice ZIP Code**
ZIP code of the practice location. Used for granular geographic analysis and market segmentation.
 | **Practice ZIP Code**
ZIP code of the practice location. Used for granular geographic analysis and market segmentation.
 | `[]` | `{}` |
    | `SF_ACCOUNT_ZIPCODE` | 52 | `TEXT` |  |  | `[]` | `{}` |
    | `SF_ACCOUNT_LATITUDE` | 53 | `FLOAT` |  |  | `[]` | `{}` |
    | `SF_ACCOUNT_LONGITUDE` | 54 | `FLOAT` |  |  | `[]` | `{}` |
    | `PHONE` | 55 | `TEXT` |  |  | `[]` | `{}` |
    | `MAIN_CONTACT_EMAIL` | 56 | `TEXT` |  |  | `[]` | `{}` |
    | `SALESFORCE_URL` | 57 | `TEXT` |  |  | `[]` | `{}` |
    | `PRIMARY_MERCHANT_DASHBOARD_URL` | 58 | `TEXT` |  |  | `[]` | `{}` |
    | `PRIMARY_MERCHANT_HEADS_UP_URL` | 59 | `TEXT` |  |  | `[]` | `{}` |
    | `SF_INDUSTRY` | 60 | `TEXT` |  |  | `[]` | `{}` |
    | `UNDERWRITING_MERCHANT_POTENTIAL` | 61 | `TEXT` |  |  | `[]` | `{}` |
    | `FULL_TIME_VS_PART_TIME` | 62 | `TEXT` |  |  | `[]` | `{}` |
    | `MARKET_SIZE` | 63 | `TEXT` |  |  | `[]` | `{}` |
    | `SF_NUMBER_OF_EMPLOYEES` | 64 | `NUMBER` |  |  | `[]` | `{}` |
    | `ESTIMATED_MONTHLY_FINANCING` | 65 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_POTENTIAL_RESET_DATE` | 66 | `DATE` |  |  | `[]` | `{}` |
    | `PRACTICE_SIZE` | 67 | `TEXT` |  |  | `[]` | `{}` |
    | `PATIENTS_PER_WEEK_RANGE` | 68 | `TEXT` |  |  | `[]` | `{}` |
    | `PATIENTS_PER_WEEK` | 69 | `TEXT` |  |  | `[]` | `{}` |
    | `PRACTICE_POTENTIAL_VOLUME_USED_FOR_ASSIGNMENT` | 70 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_WEBSITE` | 71 | `TEXT` |  |  | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_SLUG` | 72 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_PRIMARY_ORGANIZATION_DEMO` | 73 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_APPLICATION_LEAD` | 74 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_INDUSTRY` | 75 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_PRIMARY_ORGANIZATION_ACTIVE` | 76 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_PRACTICE_ACTIVE` | 77 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `APPLICATION_INDUSTRY` | 78 | `TEXT` |  |  | `[]` | `{}` |
    | `INDUSTRY` | 79 | `TEXT` | **Final Industry Classification**
Final industry classification using coalesce logic: primary_organization_industry, application_industry, then sf_industry. Used as the primary industry field for all industry-based analysis and segmentation.
 | **Final Industry Classification**
Final industry classification using coalesce logic: primary_organization_industry, application_industry, then sf_industry. Used as the primary industry field for all industry-based analysis and segmentation.
 | `[]` | `{}` |
    | `ACCOUNT_INDUSTRY_SEGMENT` | 80 | `TEXT` | **Account Industry Segment**
Standardized industry segment classification (Dental, Veterinary, Plastic and Cosmetic Surgery, MedSpa, Other, Missing industry). Includes special logic for MedSpa potential thresholds. Used for strategic segmentation and industry-specific analysis.
 | **Account Industry Segment**
Standardized industry segment classification (Dental, Veterinary, Plastic and Cosmetic Surgery, MedSpa, Other, Missing industry). Includes special logic for MedSpa potential thresholds. Used for strategic segmentation and industry-specific analysis.
 | `[]` | `{}` |
    | `ACCOUNT_INDUSTRY_SEGMENT_EVALUATION` | 81 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_STAGE` | 82 | `TEXT` |  |  | `[]` | `{}` |
    | `HAS_ALLE_INTEGRATION` | 83 | `BOOLEAN` | **Has Alle Integration**
Boolean flag indicating if the practice has Alle platform integration. Used for platform adoption analysis and dual-platform practice identification.
 | **Has Alle Integration**
Boolean flag indicating if the practice has Alle platform integration. Used for platform adoption analysis and dual-platform practice identification.
 | `[]` | `{}` |
    | `ALLE_PRACTICE_TYPE` | 84 | `TEXT` | **Alle Practice Type**
Classification of Alle relationship type (New Practice, Existing Cherry Practice, No Alle Integration). Based on merchant creation dates and integration status. Used for Alle partnership analysis and integration effectiveness measurement.
 | **Alle Practice Type**
Classification of Alle relationship type (New Practice, Existing Cherry Practice, No Alle Integration). Based on merchant creation dates and integration status. Used for Alle partnership analysis and integration effectiveness measurement.
 | `[]` | `{}` |
    | `CHERRY_MERCHANT_CREATION_DATE` | 85 | `DATE` |  |  | `[]` | `{}` |
    | `ALLE_MERCHANT_CREATION_DATE` | 86 | `DATE` |  |  | `[]` | `{}` |
    | `FIRST_MERCHANT_CREATION_DATE` | 87 | `DATE` |  |  | `[]` | `{}` |
    | `IS_TERMINATED` | 88 | `BOOLEAN` | **Is Practice Terminated**
Boolean flag indicating if the practice relationship has been terminated. Includes special handling for pre-2024-05-01 terminations with subsequent activity. Used for churn analysis and active practice filtering.
 | **Is Practice Terminated**
Boolean flag indicating if the practice relationship has been terminated. Includes special handling for pre-2024-05-01 terminations with subsequent activity. Used for churn analysis and active practice filtering.
 | `[]` | `{}` |
    | `IS_RISK_TERMINATION` | 89 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TERMINATION_TYPE` | 90 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_PRIMARY_SF_ACCOUNT` | 91 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `SF_ACCOUNT_WEBSITE` | 92 | `TEXT` |  |  | `[]` | `{}` |
    | `HAS_NO_WEBSITE` | 93 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `HAS_NO_SOCIAL_MEDIA` | 94 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `HAS_NO_CUSTOMIZABLE_APPT_REMINDERS` | 95 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `PRACTICE_RISK_FLAG` | 96 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_TERRITORY` | 97 | `TEXT` |  |  | `[]` | `{}` |
    | `PRACTICE_DEVELOPMENT_ZONE` | 98 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_TEST_GROUP_OVER_ONE_YEAR` | 99 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_FIRST_YEAR_RETENTION_TEST_GROUP_COMPARABLE` | 100 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `GOOGLE_WEEKLY_HOURS_OPEN` | 101 | `FLOAT` |  |  | `[]` | `{}` |
    | `NUMBER_OF_GOOGLE_REVIEWS` | 102 | `FLOAT` |  |  | `[]` | `{}` |
    | `GOOGLE_MATCH_STATUS` | 103 | `TEXT` |  |  | `[]` | `{}` |
    | `NUMBER_OF_INSTAGRAM_FOLLOWERS` | 104 | `FLOAT` |  |  | `[]` | `{}` |
    | `DISQUALIFICATION_REASON` | 105 | `TEXT` |  |  | `[]` | `{}` |
    | `OVERRIDE_PDM_TERRITORY` | 106 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NEXT_QUARTER_RETENTION_OWNER_ID` | 107 | `TEXT` |  |  | `[]` | `{}` |
    | `NEXT_QUARTER_RETENTION_OWNER` | 108 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_LEAD_ID` | 109 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_LEAD` | 110 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_ID` | 111 | `TEXT` | **Account Executive User ID**
Salesforce user ID of the account executive responsible for this practice. Used for sales team performance analysis and account ownership tracking.
 | **Account Executive User ID**
Salesforce user ID of the account executive responsible for this practice. Used for sales team performance analysis and account ownership tracking.
 | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE` | 112 | `TEXT` | **Account Executive Name**
Full name of the account executive. Used for sales performance reporting and team member identification in analytics.
 | **Account Executive Name**
Full name of the account executive. Used for sales performance reporting and team member identification in analytics.
 | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_SUBTEAM` | 113 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_TEAM` | 114 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_DEPARTMENT` | 115 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_TITLE` | 116 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_IS_ACTIVE` | 117 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST_ID` | 118 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST` | 119 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST_SUBTEAM` | 120 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST_TEAM` | 121 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST_DEPARTMENT` | 122 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST_TITLE` | 123 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_SPECIALIST_IS_ACTIVE` | 124 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ONBOARDING_OWNER_ID` | 125 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_OWNER_DEPARTMENT` | 126 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_OWNER_TEAM` | 127 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_OWNER_SUBTEAM` | 128 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_OWNER_NAME` | 129 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_OWNER_TITLE` | 130 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_OWNER_IS_ACTIVE` | 131 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_ID` | 132 | `TEXT` | **Retention Owner User ID**
Salesforce user ID of the current retention owner. Used for retention team performance analysis and account ownership tracking.
 | **Retention Owner User ID**
Salesforce user ID of the current retention owner. Used for retention team performance analysis and account ownership tracking.
 | `[]` | `{}` |
    | `RETENTION_OWNER` | 133 | `TEXT` | **Retention Owner Name**
Full name of the current retention owner. Used for retention performance reporting and account manager identification.
 | **Retention Owner Name**
Full name of the current retention owner. Used for retention performance reporting and account manager identification.
 | `[]` | `{}` |
    | `RETENTION_OWNER_TEAM` | 134 | `TEXT` | **Retention Owner Team**
Team assignment of the retention owner. Used for retention team performance analysis and workload distribution.
 | **Retention Owner Team**
Team assignment of the retention owner. Used for retention team performance analysis and workload distribution.
 | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT` | 135 | `TEXT` | **Retention Owner Department**
Department assignment of the retention owner. Used for retention department performance analysis and organizational reporting.
 | **Retention Owner Department**
Department assignment of the retention owner. Used for retention department performance analysis and organizational reporting.
 | `[]` | `{}` |
    | `RETENTION_OWNER_TITLE` | 136 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_IS_ACTIVE` | 137 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `PRIOR_QUARTER_RETENTION_OWNER` | 138 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_ROLE_IN_TERRITORY` | 139 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_TERRITORY_SPECIAL_HANDLING` | 140 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_ID_30_DAY` | 141 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_DEPARTMENT_30_DAY` | 142 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_TEAM_30_DAY` | 143 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_SUBTEAM_30_DAY` | 144 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_NAME_30_DAY` | 145 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_TITLE_30_DAY` | 146 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_30_DAY_IS_ACTIVE` | 147 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_ID_30_DAY` | 148 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_NAME_30_DAY` | 149 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_TEAM_30_DAY` | 150 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT_30_DAY` | 151 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_TITLE_30_DAY` | 152 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_30_DAY_IS_ACTIVE` | 153 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ACCOUNT_TERRITORY_30_DAY` | 154 | `TEXT` |  |  | `[]` | `{}` |
    | `ORGANIZATION_NUMBER_OF_PRACTICES` | 155 | `NUMBER` |  |  | `[]` | `{}` |
    | `IS_PART_OF_MULTI_PRACTICE_ORG` | 156 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `PRACTICE_NUMBER_OF_MERCHANTS` | 157 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_GROUP_ID` | 158 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_GROUP_NAME` | 159 | `TEXT` |  |  | `[]` | `{}` |
    | `PARENT_ORGANIZATION_GROUP_ID` | 160 | `NUMBER` |  |  | `[]` | `{}` |
    | `TOP_ORGANIZATION_GROUP_ID` | 161 | `NUMBER` |  |  | `[]` | `{}` |
    | `LATEST_HEALTH_ASSESSMENT` | 162 | `TEXT` | **Latest Health Assessment**
Current health assessment classification for high-priority segments (High-Potential MedSpa, Dental, Plastic Surgery, Veterinary). Used for practice health monitoring and retention strategy decisions.
 | **Latest Health Assessment**
Current health assessment classification for high-priority segments (High-Potential MedSpa, Dental, Plastic Surgery, Veterinary). Used for practice health monitoring and retention strategy decisions.
 | `[]` | `{}` |
    | `LATEST_HEALTH_ASSESSMENT_NEW_VET_MODEL` | 163 | `TEXT` |  |  | `[]` | `{}` |
    | `CURRENT_FIRST_LOOK_SCORE` | 164 | `FLOAT` |  |  | `[]` | `{}` |
    | `CURRENT_PARTNERSHIP_HEALTH_SCORE` | 165 | `FLOAT` | **Current Partnership Health Score**
Current partnership health score with logic for first 60 days vs standard scoring. Used for ongoing practice health monitoring and retention prioritization.
 | **Current Partnership Health Score**
Current partnership health score with logic for first 60 days vs standard scoring. Used for ongoing practice health monitoring and retention prioritization.
 | `[]` | `{}` |
    | `DAYS_IN_HEALTH_ASSESSMENT` | 166 | `NUMBER` |  |  | `[]` | `{}` |
    | `HEALTH_ASSESSMENT_DASHBOARD_URL` | 167 | `TEXT` |  |  | `[]` | `{}` |
    | `LATEST_WEB_REVIEW_SCORE` | 168 | `NUMBER` |  |  | `[]` | `{}` |
    | `FINANCING_OPTIONS_ON_WEBSITE` | 169 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_RETENTION_FOCUS_ACCOUNT` | 170 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_RESERVES_ACCOUNT` | 171 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ORGANIZATION_EXPECTED_PROFIT_TO_CHERRY` | 172 | `FLOAT` |  |  | `[]` | `{}` |
    | `GOOGLE_PLACE_ID` | 173 | `TEXT` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_1_APPLICATIONS_COUNT` | 174 | `NUMBER` | **Practice First 1 Day Applications Count**
Count of applications created in the first 1 day after practice go-live. Part of the early performance indicator series generated using jinja templating for n_application_days = [1,4,7,14,21,30,60]. Used for identifying practices with immediate adoption and early engagement success.
 | **Practice First 1 Day Applications Count**
Count of applications created in the first 1 day after practice go-live. Part of the early performance indicator series generated using jinja templating for n_application_days = [1,4,7,14,21,30,60]. Used for identifying practices with immediate adoption and early engagement success.
 | `[]` | `{}` |
    | `PRACTICE_LAST_1_APPLICATIONS_COUNT` | 175 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_1_APPLICATIONS_COMPLETED_COUNT` | 176 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_4_APPLICATIONS_COUNT` | 177 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_LAST_4_APPLICATIONS_COUNT` | 178 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_4_APPLICATIONS_COMPLETED_COUNT` | 179 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_7_APPLICATIONS_COUNT` | 180 | `NUMBER` | **Practice First 7 Days Applications Count**
Count of applications created in the first 7 days after practice go-live. Early performance indicator for measuring initial practice adoption and onboarding success within the first week of operation.
 | **Practice First 7 Days Applications Count**
Count of applications created in the first 7 days after practice go-live. Early performance indicator for measuring initial practice adoption and onboarding success within the first week of operation.
 | `[]` | `{}` |
    | `PRACTICE_LAST_7_APPLICATIONS_COUNT` | 181 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_7_APPLICATIONS_COMPLETED_COUNT` | 182 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_14_APPLICATIONS_COUNT` | 183 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_LAST_14_APPLICATIONS_COUNT` | 184 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_14_APPLICATIONS_COMPLETED_COUNT` | 185 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_21_APPLICATIONS_COUNT` | 186 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_LAST_21_APPLICATIONS_COUNT` | 187 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_21_APPLICATIONS_COMPLETED_COUNT` | 188 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_30_APPLICATIONS_COUNT` | 189 | `NUMBER` | **Practice First 30 Days Applications Count**
Count of applications created in the first 30 days after practice go-live. Key early performance metric for measuring first-month onboarding success and practice engagement levels.
 | **Practice First 30 Days Applications Count**
Count of applications created in the first 30 days after practice go-live. Key early performance metric for measuring first-month onboarding success and practice engagement levels.
 | `[]` | `{}` |
    | `PRACTICE_LAST_30_APPLICATIONS_COUNT` | 190 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_30_APPLICATIONS_COMPLETED_COUNT` | 191 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_60_APPLICATIONS_COUNT` | 192 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_LAST_60_APPLICATIONS_COUNT` | 193 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_60_APPLICATIONS_COMPLETED_COUNT` | 194 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_7_GROSS_AMOUNT` | 195 | `FLOAT` |  |  | `[]` | `{}` |
    | `PRACTICE_LAST_7_GROSS_AMOUNT` | 196 | `FLOAT` |  |  | `[]` | `{}` |
    | `ALLE_FIRST_7_GROSS_AMOUNT` | 197 | `FLOAT` |  |  | `[]` | `{}` |
    | `ALLE_LAST_7_GROSS_AMOUNT` | 198 | `FLOAT` |  |  | `[]` | `{}` |
    | `CHERRY_FIRST_7_GROSS_AMOUNT` | 199 | `FLOAT` |  |  | `[]` | `{}` |
    | `CHERRY_LAST_7_GROSS_AMOUNT` | 200 | `FLOAT` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_14_GROSS_AMOUNT` | 201 | `FLOAT` |  |  | `[]` | `{}` |
    | `PRACTICE_LAST_14_GROSS_AMOUNT` | 202 | `FLOAT` |  |  | `[]` | `{}` |
    | `ALLE_FIRST_14_GROSS_AMOUNT` | 203 | `FLOAT` |  |  | `[]` | `{}` |
    | `ALLE_LAST_14_GROSS_AMOUNT` | 204 | `FLOAT` |  |  | `[]` | `{}` |
    | `CHERRY_FIRST_14_GROSS_AMOUNT` | 205 | `FLOAT` |  |  | `[]` | `{}` |
    | `CHERRY_LAST_14_GROSS_AMOUNT` | 206 | `FLOAT` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_30_GROSS_AMOUNT` | 207 | `FLOAT` | **Practice First 30 Days Gross Amount**
Total gross loan amount generated in the first 30 days after practice go-live. Key metric for measuring first-month financial performance and onboarding success, often used as a predictor of long-term practice success. In USD.
 | **Practice First 30 Days Gross Amount**
Total gross loan amount generated in the first 30 days after practice go-live. Key metric for measuring first-month financial performance and onboarding success, often used as a predictor of long-term practice success. In USD.
 | `[]` | `{}` |
    | `PRACTICE_LAST_30_GROSS_AMOUNT` | 208 | `FLOAT` |  |  | `[]` | `{}` |
    | `ALLE_FIRST_30_GROSS_AMOUNT` | 209 | `FLOAT` | **Alle First 30 Days Gross Amount**
Total gross loan amount generated through the Alle platform in the first 30 days after practice go-live. Used for measuring platform-specific early performance and adoption patterns. In USD.
 | **Alle First 30 Days Gross Amount**
Total gross loan amount generated through the Alle platform in the first 30 days after practice go-live. Used for measuring platform-specific early performance and adoption patterns. In USD.
 | `[]` | `{}` |
    | `ALLE_LAST_30_GROSS_AMOUNT` | 210 | `FLOAT` |  |  | `[]` | `{}` |
    | `CHERRY_FIRST_30_GROSS_AMOUNT` | 211 | `FLOAT` | **Cherry First 30 Days Gross Amount**
Total gross loan amount generated through the Cherry platform in the first 30 days after practice go-live. Used for measuring platform-specific early performance and adoption patterns. In USD.
 | **Cherry First 30 Days Gross Amount**
Total gross loan amount generated through the Cherry platform in the first 30 days after practice go-live. Used for measuring platform-specific early performance and adoption patterns. In USD.
 | `[]` | `{}` |
    | `CHERRY_LAST_30_GROSS_AMOUNT` | 212 | `FLOAT` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_60_GROSS_AMOUNT` | 213 | `FLOAT` | **Practice First 60 Days Gross Amount**
Total gross loan amount generated in the first 60 days after practice go-live. Important early performance indicator for practices that may need more time to ramp up their lending activity. In USD.
 | **Practice First 60 Days Gross Amount**
Total gross loan amount generated in the first 60 days after practice go-live. Important early performance indicator for practices that may need more time to ramp up their lending activity. In USD.
 | `[]` | `{}` |
    | `PRACTICE_LAST_60_GROSS_AMOUNT` | 214 | `FLOAT` |  |  | `[]` | `{}` |
    | `ALLE_FIRST_60_GROSS_AMOUNT` | 215 | `FLOAT` |  |  | `[]` | `{}` |
    | `ALLE_LAST_60_GROSS_AMOUNT` | 216 | `FLOAT` |  |  | `[]` | `{}` |
    | `CHERRY_FIRST_60_GROSS_AMOUNT` | 217 | `FLOAT` |  |  | `[]` | `{}` |
    | `CHERRY_LAST_60_GROSS_AMOUNT` | 218 | `FLOAT` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_90_GROSS_AMOUNT` | 219 | `FLOAT` |  |  | `[]` | `{}` |
    | `PRACTICE_LAST_90_GROSS_AMOUNT` | 220 | `FLOAT` | **Practice Last 90 Days Gross Amount**
Total gross loan amount generated in the last 90 days. Part of the recent performance series, used for measuring current practice activity and engagement levels. In USD.
 | **Practice Last 90 Days Gross Amount**
Total gross loan amount generated in the last 90 days. Part of the recent performance series, used for measuring current practice activity and engagement levels. In USD.
 | `[]` | `{}` |
    | `ALLE_FIRST_90_GROSS_AMOUNT` | 221 | `FLOAT` |  |  | `[]` | `{}` |
    | `ALLE_LAST_90_GROSS_AMOUNT` | 222 | `FLOAT` |  |  | `[]` | `{}` |
    | `CHERRY_FIRST_90_GROSS_AMOUNT` | 223 | `FLOAT` |  |  | `[]` | `{}` |
    | `CHERRY_LAST_90_GROSS_AMOUNT` | 224 | `FLOAT` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_120_GROSS_AMOUNT` | 225 | `FLOAT` |  |  | `[]` | `{}` |
    | `PRACTICE_LAST_120_GROSS_AMOUNT` | 226 | `FLOAT` |  |  | `[]` | `{}` |
    | `ALLE_FIRST_120_GROSS_AMOUNT` | 227 | `FLOAT` |  |  | `[]` | `{}` |
    | `ALLE_LAST_120_GROSS_AMOUNT` | 228 | `FLOAT` |  |  | `[]` | `{}` |
    | `CHERRY_FIRST_120_GROSS_AMOUNT` | 229 | `FLOAT` |  |  | `[]` | `{}` |
    | `CHERRY_LAST_120_GROSS_AMOUNT` | 230 | `FLOAT` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_365_GROSS_AMOUNT` | 231 | `FLOAT` |  |  | `[]` | `{}` |
    | `PRACTICE_LAST_365_GROSS_AMOUNT` | 232 | `FLOAT` |  |  | `[]` | `{}` |
    | `ALLE_FIRST_365_GROSS_AMOUNT` | 233 | `FLOAT` |  |  | `[]` | `{}` |
    | `ALLE_LAST_365_GROSS_AMOUNT` | 234 | `FLOAT` |  |  | `[]` | `{}` |
    | `CHERRY_FIRST_365_GROSS_AMOUNT` | 235 | `FLOAT` |  |  | `[]` | `{}` |
    | `CHERRY_LAST_365_GROSS_AMOUNT` | 236 | `FLOAT` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_FUNDED_CONTRACT_DATE` | 237 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `ALLE_FIRST_FUNDED_CONTRACT_DATE` | 238 | `TIMESTAMP_NTZ` | **Alle First Funded Contract Date**
Date of the first funded contract through the Alle platform. Used for tracking platform-specific onboarding milestones and timeline analysis.
 | **Alle First Funded Contract Date**
Date of the first funded contract through the Alle platform. Used for tracking platform-specific onboarding milestones and timeline analysis.
 | `[]` | `{}` |
    | `CHERRY_FIRST_FUNDED_CONTRACT_DATE` | 239 | `TIMESTAMP_NTZ` | **Cherry First Funded Contract Date**
Date of the first funded contract through the Cherry platform. Used for tracking platform-specific onboarding milestones and timeline analysis.
 | **Cherry First Funded Contract Date**
Date of the first funded contract through the Cherry platform. Used for tracking platform-specific onboarding milestones and timeline analysis.
 | `[]` | `{}` |
    | `ALLE_LAST_FUNDED_CONTRACT_DATE` | 240 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `CHERRY_LAST_FUNDED_CONTRACT_DATE` | 241 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `PRACTICE_FUNDED_CONTRACTS_COUNT` | 242 | `NUMBER` | **Practice Total Funded Contracts Count**
Total count of funded contracts for the practice across all time periods. Represents the total number of successful loan transactions completed.
 | **Practice Total Funded Contracts Count**
Total count of funded contracts for the practice across all time periods. Represents the total number of successful loan transactions completed.
 | `[]` | `{}` |
    | `PRACTICE_FIRST_30_FUNDED_CONTRACTS_COUNT` | 243 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_FIRST_60_FUNDED_CONTRACTS_COUNT` | 244 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_TOTAL_GROSS_AMOUNT` | 245 | `FLOAT` | **Practice Total Gross Amount (All Time)**
Total gross loan amount generated by the practice across all time periods and platforms. Used for lifetime value analysis and total relationship assessment. In USD.
 | **Practice Total Gross Amount (All Time)**
Total gross loan amount generated by the practice across all time periods and platforms. Used for lifetime value analysis and total relationship assessment. In USD.
 | `[]` | `{}` |
    | `ALLE_TOTAL_GROSS_AMOUNT` | 246 | `FLOAT` | **Alle Total Gross Amount (All Time)**
Total gross loan amount generated through the Alle platform across the entire practice relationship. Used for platform-specific lifetime value and performance analysis. In USD.
 | **Alle Total Gross Amount (All Time)**
Total gross loan amount generated through the Alle platform across the entire practice relationship. Used for platform-specific lifetime value and performance analysis. In USD.
 | `[]` | `{}` |
    | `CHERRY_TOTAL_GROSS_AMOUNT` | 247 | `FLOAT` | **Cherry Total Gross Amount (All Time)**
Total gross loan amount generated through the Cherry platform across the entire practice relationship. Used for platform-specific lifetime value and performance analysis. In USD.
 | **Cherry Total Gross Amount (All Time)**
Total gross loan amount generated through the Cherry platform across the entire practice relationship. Used for platform-specific lifetime value and performance analysis. In USD.
 | `[]` | `{}` |
    | `LIFETIME_VALUE` | 248 | `FLOAT` | **Practice Lifetime Value**
Calculated lifetime value of the practice relationship. Currently calculated at the merchant level for Cherry merchants only. Represents expected net present value of revenue over the projected practice lifespan. In USD.
 | **Practice Lifetime Value**
Calculated lifetime value of the practice relationship. Currently calculated at the merchant level for Cherry merchants only. Represents expected net present value of revenue over the projected practice lifespan. In USD.
 | `[]` | `{}` |
    | `TOTAL_ACQUISITION_COST` | 249 | `FLOAT` | **Total Acquisition Cost**
Total cost incurred to acquire the practice, including sales, marketing, onboarding, and setup costs. Used for calculating customer acquisition cost (CAC) and ROI analysis. In USD.
 | **Total Acquisition Cost**
Total cost incurred to acquire the practice, including sales, marketing, onboarding, and setup costs. Used for calculating customer acquisition cost (CAC) and ROI analysis. In USD.
 | `[]` | `{}` |
    | `GROSS_AMOUNT_TOTAL` | 250 | `FLOAT` |  |  | `[]` | `{}` |
    | `EVALUATION_MONTHS` | 251 | `NUMBER` |  |  | `[]` | `{}` |
    | `TOTAL_CONTRIBUTION_MARGIN_EXPECTED` | 252 | `FLOAT` |  |  | `[]` | `{}` |
    | `MONTHLY_RETENTION_COST` | 253 | `NUMBER` | **Monthly Retention Cost**
Monthly cost allocated for retaining this practice, including account management and customer success activities. Used for retention ROI analysis. In USD.
 | **Monthly Retention Cost**
Monthly cost allocated for retaining this practice, including account management and customer success activities. Used for retention ROI analysis. In USD.
 | `[]` | `{}` |
    | `SALES_DEVELOPMENT_COST` | 254 | `NUMBER` | **Sales Development Cost**
Cost attributed to sales development activities for acquiring this practice. Part of the detailed cost breakdown for acquisition analysis. In USD.
 | **Sales Development Cost**
Cost attributed to sales development activities for acquiring this practice. Part of the detailed cost breakdown for acquisition analysis. In USD.
 | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_COST` | 255 | `NUMBER` |  |  | `[]` | `{}` |
    | `ONBOARDING_COST` | 256 | `NUMBER` | **Onboarding Cost**
Cost incurred for onboarding this practice, including setup, training, and initial support. Used for understanding total acquisition investment. In USD.
 | **Onboarding Cost**
Cost incurred for onboarding this practice, including setup, training, and initial support. Used for understanding total acquisition investment. In USD.
 | `[]` | `{}` |
    | `MARKETING_COST` | 257 | `FLOAT` | **Marketing Cost**
Marketing costs attributed to acquiring this practice. Part of the comprehensive cost analysis for ROI calculations. In USD.
 | **Marketing Cost**
Marketing costs attributed to acquiring this practice. Part of the comprehensive cost analysis for ROI calculations. In USD.
 | `[]` | `{}` |
    | `MARKETING_BOX_COST` | 258 | `FLOAT` |  |  | `[]` | `{}` |
    | `WEBSITE_IMPLEMENTATION_COST` | 259 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_DEMO_DATE` | 260 | `DATE` |  |  | `[]` | `{}` |
    | `PRACTICE_SEGMENT` | 261 | `TEXT` | **Practice Segment Classification**
Calculated practice segment classification. Uses special logic for Alle 'New Practice' types with go-live dates before 2025-06-04 (classified as 'Alle'), otherwise uses the account_industry_segment. Used for strategic segmentation and targeted practice management.
 | **Practice Segment Classification**
Calculated practice segment classification. Uses special logic for Alle 'New Practice' types with go-live dates before 2025-06-04 (classified as 'Alle'), otherwise uses the account_industry_segment. Used for strategic segmentation and targeted practice management.
 | `[]` | `{}` |
    | `PRACTICE_SEGMENT_START_DATE` | 262 | `DATE` |  |  | `[]` | `{}` |
    | `SALES_OWNER_ID` | 263 | `TEXT` |  |  | `[]` | `{}` |
    | `SALES_OWNER_DEPARTMENT` | 264 | `TEXT` |  |  | `[]` | `{}` |
    | `SALES_OWNER_TEAM` | 265 | `TEXT` |  |  | `[]` | `{}` |
    | `SALES_OWNER_SUBTEAM` | 266 | `TEXT` |  |  | `[]` | `{}` |
    | `SALES_OWNER_NAME` | 267 | `TEXT` |  |  | `[]` | `{}` |
    | `SALES_OWNER_TITLE` | 268 | `TEXT` |  |  | `[]` | `{}` |
    | `SALES_OWNER_IS_ACTIVE` | 269 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `REGISTRATION_BUSINESS_NAME` | 270 | `TEXT` |  |  | `[]` | `{}` |
    | `REGISTRATION_DBA` | 271 | `TEXT` |  |  | `[]` | `{}` |
    | `REGISTRATION_STATUS` | 272 | `TEXT` |  |  | `[]` | `{}` |
    | `REGISTRATION_DATE` | 273 | `DATE` |  |  | `[]` | `{}` |
    | `REGISTRATION_OWNER_ID` | 274 | `TEXT` |  |  | `[]` | `{}` |
    | `REGISTRATION_OWNER_DEPARTMENT` | 275 | `TEXT` |  |  | `[]` | `{}` |
    | `REGISTRATION_OWNER_TEAM` | 276 | `TEXT` |  |  | `[]` | `{}` |
    | `REGISTRATION_OWNER_SUBTEAM` | 277 | `TEXT` |  |  | `[]` | `{}` |
    | `REGISTRATION_OWNER_NAME` | 278 | `TEXT` |  |  | `[]` | `{}` |
    | `REGISTRATION_OWNER_TITLE` | 279 | `TEXT` |  |  | `[]` | `{}` |
    | `INITIAL_HEALTH_ASSESSMENT` | 280 | `TEXT` | **Initial Health Assessment (60-Day)**
Health assessment classification at the 60-day mark after practice go-live. Only populated for high-priority segments (MedSpa, Dental, Plastic Surgery, Veterinary). Used for early practice health evaluation.
 | **Initial Health Assessment (60-Day)**
Health assessment classification at the 60-day mark after practice go-live. Only populated for high-priority segments (MedSpa, Dental, Plastic Surgery, Veterinary). Used for early practice health evaluation.
 | `[]` | `{}` |
    | `INITIAL_HEALTH_ASSESSMENT_NEW_VET_MODEL` | 281 | `TEXT` |  |  | `[]` | `{}` |
    | `ONBOARDING_INITIAL_HEALTH_ASSESSMENT` | 282 | `TEXT` | **Onboarding Health Assessment**
Health assessment during the onboarding period, calculated at the lesser of 60 days post go-live or end of quarter. Used for comprehensive onboarding success evaluation.
 | **Onboarding Health Assessment**
Health assessment during the onboarding period, calculated at the lesser of 60 days post go-live or end of quarter. Used for comprehensive onboarding success evaluation.
 | `[]` | `{}` |
    | `PAST_30D_PRACTICE_CHERRY_VOLUME` | 283 | `FLOAT` | **Past 30 Days Cherry Volume**
Total Cherry platform volume for the practice in the past 30 days. Derived from cherry share analysis, used for recent performance tracking. In USD.
 | **Past 30 Days Cherry Volume**
Total Cherry platform volume for the practice in the past 30 days. Derived from cherry share analysis, used for recent performance tracking. In USD.
 | `[]` | `{}` |
    | `PAST_30D_PRACTICE_CHERRY_SHARE_PCT` | 284 | `FLOAT` | **Past 30 Days Cherry Market Share Percentage**
Percentage of practice's total financing volume through Cherry in the past 30 days. Key metric for measuring market share and platform adoption within the practice's total financing activity.
 | **Past 30 Days Cherry Market Share Percentage**
Percentage of practice's total financing volume through Cherry in the past 30 days. Key metric for measuring market share and platform adoption within the practice's total financing activity.
 | `[]` | `{}` |
    | `LAST_PRACTICE_MYSTERY_SHOPPING_DATE` | 285 | `DATE` | **Last Mystery Shopping Date**
Date of the most recent mystery shopping evaluation for this practice. Used for tracking customer experience assessment frequency and recency.
 | **Last Mystery Shopping Date**
Date of the most recent mystery shopping evaluation for this practice. Used for tracking customer experience assessment frequency and recency.
 | `[]` | `{}` |
    | `LAST_PRACTICE_MYSTERY_SHOPPING_LOOK_RESPONSE` | 286 | `TEXT` | **Last Mystery Shopping Assessment Result**
Results from the most recent mystery shopping evaluation. Provides qualitative assessment of customer experience and operational quality.
 | **Last Mystery Shopping Assessment Result**
Results from the most recent mystery shopping evaluation. Provides qualitative assessment of customer experience and operational quality.
 | `[]` | `{}` |
    | `DAYS_SINCE_LAST_TRANSACTION` | 287 | `NUMBER` | **Days Since Last Transaction**
Number of days since the practice's last transaction. Calculated as DATEDIFF between the latest transaction date and current date. Used for identifying dormant or inactive practices.
 | **Days Since Last Transaction**
Number of days since the practice's last transaction. Calculated as DATEDIFF between the latest transaction date and current date. Used for identifying dormant or inactive practices.
 | `[]` | `{}` |
    | `LAST_30_APPROVAL_RATE` | 288 | `NUMBER` | **Last 30 Days Approval Rate**
Approval rate for applications in the last 30 days. Calculated as approved applications divided by total applications. Key metric for measuring practice application quality and success rates.
 | **Last 30 Days Approval Rate**
Approval rate for applications in the last 30 days. Calculated as approved applications divided by total applications. Key metric for measuring practice application quality and success rates.
 | `[]` | `{}` |
    | `LAST_30_ACTIVE_APPROVAL_RATE` | 289 | `NUMBER` | **Last 30 Days Active Source Approval Rate**
Approval rate for 'active' source applications in the last 30 days. Filtered to source_type = 'active' to measure approval rates for practice-generated applications specifically.
 | **Last 30 Days Active Source Approval Rate**
Approval rate for 'active' source applications in the last 30 days. Filtered to source_type = 'active' to measure approval rates for practice-generated applications specifically.
 | `[]` | `{}` |
    | `LAST_30_AVERAGE_APPROVAL_AMOUNT` | 290 | `FLOAT` | **Last 30 Days Average Approval Amount**
Average approval amount for approved applications in the last 30 days. Used for measuring practice application quality and customer profile. In USD.
 | **Last 30 Days Average Approval Amount**
Average approval amount for approved applications in the last 30 days. Used for measuring practice application quality and customer profile. In USD.
 | `[]` | `{}` |
    | `OUTSTANDING_APPROVALS` | 291 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_30_FUNDING_RATE` | 292 | `NUMBER` | **Last 30 Days Funding Rate**
Rate of approved applications that convert to funded loans in the last 30 days. Measures conversion efficiency from approval to funding.
 | **Last 30 Days Funding Rate**
Rate of approved applications that convert to funded loans in the last 30 days. Measures conversion efficiency from approval to funding.
 | `[]` | `{}` |
    | `APPROVED_APPLICATIONS` | 293 | `NUMBER` |  |  | `[]` | `{}` |
    | `FUNDED_APPLICATIONS` | 294 | `NUMBER` |  |  | `[]` | `{}` |
    | `TRAILING_30_PAYMENT_ESTIMATOR_COUNT` | 295 | `NUMBER` | **Trailing 30 Days Payment Estimator Usage Count**
Count of payment estimator tool usage in the last 30 days. Indicates practice engagement with digital tools and customer interaction levels.
 | **Trailing 30 Days Payment Estimator Usage Count**
Count of payment estimator tool usage in the last 30 days. Indicates practice engagement with digital tools and customer interaction levels.
 | `[]` | `{}` |
    | `INTERNAL_REFERRER_NAME` | 296 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERNAL_REFERRER_ID` | 297 | `TEXT` |  |  | `[]` | `{}` |
    | `LATEST_TRUE_RETENTION_OWNER` | 298 | `TEXT` | **Latest True Retention Owner**
Most recent retention owner for the practice, excluding 'Internal Performance Decision' team assignments. Represents the current account manager responsible for practice retention.
 | **Latest True Retention Owner**
Most recent retention owner for the practice, excluding 'Internal Performance Decision' team assignments. Represents the current account manager responsible for practice retention.
 | `[]` | `{}` |
    | `LATEST_TRUE_RETENTION_OWNER_TEAM` | 299 | `TEXT` | **Latest True Retention Owner Team**
Team of the most recent retention owner. Used for retention team performance analysis and workload distribution.
 | **Latest True Retention Owner Team**
Team of the most recent retention owner. Used for retention team performance analysis and workload distribution.
 | `[]` | `{}` |
    | `LATEST_TRUE_RETENTION_OWNER_DEPARTMENT` | 300 | `TEXT` | **Latest True Retention Owner Department**
Department of the most recent retention owner. Used for organizational analysis and retention strategy management.
 | **Latest True Retention Owner Department**
Department of the most recent retention owner. Used for organizational analysis and retention strategy management.
 | `[]` | `{}` |
    | `LATEST_TRUE_RETENTION_OWNER_TERRITORY` | 301 | `TEXT` |  |  | `[]` | `{}` |
    | `CHURN_RISK` | 302 | `TEXT` | **Churn Risk Classification**
Churn risk classification ('At Risk of Churn' or 'Not At Risk of Churn'). Based on churn triggers logic, used for proactive retention efforts and risk management.
 | **Churn Risk Classification**
Churn risk classification ('At Risk of Churn' or 'Not At Risk of Churn'). Based on churn triggers logic, used for proactive retention efforts and risk management.
 | `[]` | `{}` |
    | `PRACTICE_POTENTIAL_EXTERNAL_DATA` | 303 | `FLOAT` | **Practice Potential (External Data)**
Raw expected monthly Cherry volume based on external data analysis. Includes parent organization potential aggregation for organizational hierarchies. Represents practice potential derived from market research and external data sources. In USD.
 | **Practice Potential (External Data)**
Raw expected monthly Cherry volume based on external data analysis. Includes parent organization potential aggregation for organizational hierarchies. Represents practice potential derived from market research and external data sources. In USD.
 | `[]` | `{}` |
    | `PRACTICE_POTENTIAL_PERFORMANCE_ADJUSTED` | 304 | `FLOAT` | **Practice Potential (Performance Adjusted)**
Seasonally adjusted expected monthly Cherry volume that incorporates performance data and parent organization aggregation. Enhanced version of practice potential that considers actual performance patterns. In USD.
 | **Practice Potential (Performance Adjusted)**
Seasonally adjusted expected monthly Cherry volume that incorporates performance data and parent organization aggregation. Enhanced version of practice potential that considers actual performance patterns. In USD.
 | `[]` | `{}` |
    | `DATE_OF_LATEST_ONSITE_OR_MEANINGFUL_INTERACTION` | 305 | `DATE` | **Date of Latest On-Site or Meaningful Interaction**
Date of the most recent on-site visit or meaningful interaction with the practice. Used for measuring relationship depth and engagement quality.
 | **Date of Latest On-Site or Meaningful Interaction**
Date of the most recent on-site visit or meaningful interaction with the practice. Used for measuring relationship depth and engagement quality.
 | `[]` | `{}` |
    | `TRAILING_90_ON_SITES` | 306 | `NUMBER` | **Trailing 90 Days On-Site Visits**
Count of on-site visits in the last 90 days. Measures face-to-face relationship investment and engagement intensity.
 | **Trailing 90 Days On-Site Visits**
Count of on-site visits in the last 90 days. Measures face-to-face relationship investment and engagement intensity.
 | `[]` | `{}` |
    | `TRAILING_90_MEANINGFUL_INTERACTIONS` | 307 | `NUMBER` | **Trailing 90 Days Meaningful Interactions**
Count of meaningful interactions (non-on-site) in the last 90 days. Measures overall relationship engagement and touch point frequency.
 | **Trailing 90 Days Meaningful Interactions**
Count of meaningful interactions (non-on-site) in the last 90 days. Measures overall relationship engagement and touch point frequency.
 | `[]` | `{}` |
    | `STANDARD_MENU_REENGAGEMENT` | 308 | `TEXT` | **Standard Menu Reengagement Classification**
Strategic classification flag for practices positioned for menu promotion. Identifies practices with standard menu stage, health score >= 66, health assessment >= 14 days, min score > 50 in last 28 days, practice potential > 5000, and recent activity (last 90 days).
 | **Standard Menu Reengagement Classification**
Strategic classification flag for practices positioned for menu promotion. Identifies practices with standard menu stage, health score >= 66, health assessment >= 14 days, min score > 50 in last 28 days, practice potential > 5000, and recent activity (last 90 days).
 | `[]` | `{}` |
    | `QUALIFIED_OPPORTUNITY_SOURCE` | 309 | `TEXT` | **Qualified Opportunity Source Attribution**
Source attribution for how the practice opportunity was qualified. Used for understanding lead generation effectiveness and channel attribution.
 | **Qualified Opportunity Source Attribution**
Source attribution for how the practice opportunity was qualified. Used for understanding lead generation effectiveness and channel attribution.
 | `[]` | `{}` |
    | `IS_PLASTICS_TOP_2_PERCENT_Q2_2025` | 310 | `BOOLEAN` | **Is Plastic Surgery Top 2% (Q2 2025)**
Boolean flag identifying Plastic Surgery practices in the top 2% by volume for Q2 2025. Based on trailing 30-day volume >= [$]115,795 as of May 1, 2025, or first 30 days >= [$]115,795 for practices going live after May 1, 2025. Used for high-value practice identification.
 | **Is Plastic Surgery Top 2% (Q2 2025)**
Boolean flag identifying Plastic Surgery practices in the top 2% by volume for Q2 2025. Based on trailing 30-day volume >= $115,795 as of May 1, 2025, or first 30 days >= $115,795 for practices going live after May 1, 2025. Used for high-value practice identification.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.account_daily_ownership`
    *   `model.cherry_data_model.application_attribution`
    *   `model.cherry_data_model.attribution_demos`
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.churn_triggers`
    *   `model.cherry_data_model.daily_health_scores`
    *   `model.cherry_data_model.enhanced_practice_potential_v4`
    *   `model.cherry_data_model.internal_referral_go_lives_detailed`
    *   `model.cherry_data_model.internal_referral_leads_detailed`
    *   `model.cherry_data_model.loan_info_xf`
    *   `model.cherry_data_model.look_assessment_history`
    *   `model.cherry_data_model.look_assessment_history_new_vet_model`
    *   `model.cherry_data_model.meaningful_interactions_and_on_site_visits_xf`
    *   `model.cherry_data_model.merchant_lifetime_value`
    *   `model.cherry_data_model.merchant_loan_totals`
    *   `model.cherry_data_model.practice_application_totals`
    *   `model.cherry_data_model.prospect_attribution_summary`
    *   `model.cherry_data_model.retention_daily_ownership`
    *   `model.cherry_data_model.src_cherry_applications`
    *   `model.cherry_data_model.stg_account_level_product_use_salesforce`
    *   `model.cherry_data_model.stg_cherry_share_longitudinal`
    *   `model.cherry_data_model.stg_merchants`
    *   `model.cherry_data_model.stg_mystery_shopping`
    *   `model.cherry_data_model.stg_organization_product_use`
    *   `model.cherry_data_model.stg_practices`
    *   `model.cherry_data_model.stg_registrations_new`
    *   `model.cherry_data_model.stg_sf_users`

---
