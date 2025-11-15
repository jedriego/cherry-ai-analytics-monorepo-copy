## Model: `referral_details_xf`

`referral_details_xf`

*   **Unique ID:** `model.cherry_data_model.referral_details_xf`
*   **FQN:** `prod.marketing_marts.referral_details_xf`
*   **Description:** **Comprehensive Referral Program Analytics and Attribution Table**
This model serves as Cherry's definitive source of truth for referral program analysis, combining  comprehensive referral tracking, qualification status, cost calculations, revenue attribution,  and payment processing across all iterations of Cherry's referral program. It integrates data  from both automated Referral Rock campaigns and manually-added Salesforce referrals to provide  complete visibility into referral program performance.
**Key Business Logic:** - **Referral Validation**: Applies sophisticated validation rules to determine valid referrals 
  vs. invalid submissions across multiple program versions
- **Qualification Tracking**: Complex deadline management for registration and transaction criteria 
  with time-based qualification windows (registration deadlines, loan qualification periods)
- **Cost Attribution**: Calculates referrer bonuses, referral bonuses, and total program costs 
  with payment reconciliation and historical program-specific bonus structures
- **Revenue Analysis**: Tracks loan performance across multiple time windows (14, 30, 60, 90, 180 days) 
  from go-live date to measure referral lifetime value
- **Multi-Platform Integration**: Harmonizes data from Referral Rock automation, manual Salesforce entries, 
  and various payment platforms (Modern Treasury, Referral Rock payments)

**Critical Data Sources:** - `all_referrals`: Core referral data combining lead and account information with validation logic - `referral_referrers`: Complex referrer attribution across Referral Rock, Salesforce contacts, and manual entries - `referral_qualification`: Qualification criteria, deadlines, and denial logic with program-specific rules - `referral_cost`: Cost calculations including bonuses, payments, and merchant fee rebates for legacy programs - `referral_revenue`: Time-based revenue tracking from loan originations linked to referral merchants - `referral_payments`: Payment aggregation from multiple platforms with status and amount tracking
**Program Evolution Coverage:** - Multiple program versions (1-4) with varying qualification criteria and bonus structures - Standard Referral Program (transaction/amount-based qualification) - Dental Partner Program (demo-based qualification) - Legacy merchant fee rebate programs (2022 and earlier) - Central Pacific Bank campaign tracking
**Primary Use Cases:** - Referral program ROI analysis and lifetime value calculations - Qualification tracking and payment processing workflows - Referrer performance analysis and attribution accuracy - Program iteration effectiveness measurement and optimization - Fraud detection and referral validation processes
### External Resources - [Guru Documentation](https://app.getguru.com/card/c6Aornxi/Referral-Details-Table) - [Current Program Terms](https://refer.withcherry.com/v2/1/terms) - [Program Registration](https://refer.withcherry.com/v2/1/register)

*   **Tags:** `['marketing_analytics', 'marketing', 'referrals', 'referrers', 'reward', 'bonus', 'referral_program']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `LEAD_ID` | 1 | `TEXT` | **Salesforce Lead Identifier** - Original Salesforce lead ID for referrals that entered as leads.  NULL for account-only referrals. Used for linking to lead-specific data and conversion tracking.  Sourced from all_referrals.
 | **Salesforce Lead Identifier** - Original Salesforce lead ID for referrals that entered as leads.  NULL for account-only referrals. Used for linking to lead-specific data and conversion tracking.  Sourced from all_referrals.
 | `[]` | `{}` |
    | `ACCOUNT_ID` | 2 | `TEXT` | **Salesforce Account Identifier** - Salesforce account ID for the referral. Present when leads  convert to accounts or for direct account referrals. Used for merchant-level analysis and  account relationship tracking. Sourced from all_referrals.
 | **Salesforce Account Identifier** - Salesforce account ID for the referral. Present when leads  convert to accounts or for direct account referrals. Used for merchant-level analysis and  account relationship tracking. Sourced from all_referrals.
 | `[]` | `{}` |
    | `PARENT_ACCOUNT_ID` | 3 | `TEXT` | **Parent Account Identifier** - Salesforce parent account ID for referrals belonging to  multi-location organizations. Used for enterprise-level referral tracking and parent account  qualification rules. NULL for single-location referrals. Sourced from all_referrals.
 | **Parent Account Identifier** - Salesforce parent account ID for referrals belonging to  multi-location organizations. Used for enterprise-level referral tracking and parent account  qualification rules. NULL for single-location referrals. Sourced from all_referrals.
 | `[]` | `{}` |
    | `REFERRAL_OBJECT_ID` | 4 | `TEXT` | **Primary Referral Identifier** - Unified identifier for each referral record, using Salesforce  lead_id when available, otherwise account_id. This composite key ensures every referral has a  unique identifier regardless of data source. Critical for all referral program analytics and  cross-referencing. Sourced from all_referrals.
 | **Primary Referral Identifier** - Unified identifier for each referral record, using Salesforce  lead_id when available, otherwise account_id. This composite key ensures every referral has a  unique identifier regardless of data source. Critical for all referral program analytics and  cross-referencing. Sourced from all_referrals.
 | `[]` | `{}` |
    | `FORM_SUBMISSION_ID` | 5 | `TEXT` | **Form Submission Identifier** - Unique identifier for the form submission that created the  referral lead. Used for form tracking and conversion analysis. NULL for non-form referrals.  Sourced from all_referrals.
 | **Form Submission Identifier** - Unique identifier for the form submission that created the  referral lead. Used for form tracking and conversion analysis. NULL for non-form referrals.  Sourced from all_referrals.
 | `[]` | `{}` |
    | `HAS_FORM_SUBMISSION` | 6 | `BOOLEAN` | **Form Submission Flag** - Boolean indicating whether the referral originated from a form  submission. Used for lead source analysis and form effectiveness tracking. Sourced from all_referrals.
 | **Form Submission Flag** - Boolean indicating whether the referral originated from a form  submission. Used for lead source analysis and form effectiveness tracking. Sourced from all_referrals.
 | `[]` | `{}` |
    | `REFERRAL_COMPANY_NAME` | 7 | `TEXT` | **Referral Company Name** - Business name of the referred organization. Prioritizes lead company  name over account name when both exist. Used for referral identification and duplicate detection.  Sourced from all_referrals (company name prioritization logic).
 | **Referral Company Name** - Business name of the referred organization. Prioritizes lead company  name over account name when both exist. Used for referral identification and duplicate detection.  Sourced from all_referrals (company name prioritization logic).
 | `[]` | `{}` |
    | `IS_VALID_REFERRAL` | 8 | `BOOLEAN` | **Referral Validity Status** - Boolean indicating whether the referral meets Cherry's definition  of a valid referral based on source validation, timing rules, and quality criteria. Primary  filter for referral program analysis. Sourced from all_referrals validation logic.
 | **Referral Validity Status** - Boolean indicating whether the referral meets Cherry's definition  of a valid referral based on source validation, timing rules, and quality criteria. Primary  filter for referral program analysis. Sourced from all_referrals validation logic.
 | `[]` | `{}` |
    | `IS_VALID_REFERRAL_EVALUATION` | 9 | `TEXT` | **Validity Evaluation Reason** - Text explanation of why is_valid_referral is TRUE or FALSE,  providing specific validation criteria that were evaluated. Used for referral quality analysis  and validation rule improvement. Sourced from all_referrals validation evaluation.
 | **Validity Evaluation Reason** - Text explanation of why is_valid_referral is TRUE or FALSE,  providing specific validation criteria that were evaluated. Used for referral quality analysis  and validation rule improvement. Sourced from all_referrals validation evaluation.
 | `[]` | `{}` |
    | `REFERRALROCK_REFERRAL_ID` | 10 | `TEXT` | **Referral Rock Identifier** - External identifier from Referral Rock platform for automated  referrals. NULL for manual Salesforce referrals. Used for Referral Rock integration and  cross-platform tracking. Sourced from all_referrals.
 | **Referral Rock Identifier** - External identifier from Referral Rock platform for automated  referrals. NULL for manual Salesforce referrals. Used for Referral Rock integration and  cross-platform tracking. Sourced from all_referrals.
 | `[]` | `{}` |
    | `REFERRING_ACCOUNT` | 11 | `TEXT` | **Referring Account Identifier** - Salesforce account ID of the merchant who made the referral  for manually-added referrals. Used for referrer identification and attribution in manual  referral processes. Sourced from all_referrals.
 | **Referring Account Identifier** - Salesforce account ID of the merchant who made the referral  for manually-added referrals. Used for referrer identification and attribution in manual  referral processes. Sourced from all_referrals.
 | `[]` | `{}` |
    | `REFERRAL_OBJECT_SOURCE` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_ID` | 13 | `FLOAT` | **Cherry Merchant Identifier** - Cherry's internal merchant ID assigned to the referral when  they become an active merchant. NULL for referrals that never activated. Critical for linking  to loan and transaction data. Sourced from all_referrals.
 | **Cherry Merchant Identifier** - Cherry's internal merchant ID assigned to the referral when  they become an active merchant. NULL for referrals that never activated. Critical for linking  to loan and transaction data. Sourced from all_referrals.
 | `[]` | `{}` |
    | `REFERRAL_OWNER_ID` | 14 | `TEXT` | **Referral Owner Identifier** - Salesforce user ID of the person who owns the referral record  (lead or account owner). Used for ownership tracking and responsibility attribution. Sourced  from all_referrals ownership logic.
 | **Referral Owner Identifier** - Salesforce user ID of the person who owns the referral record  (lead or account owner). Used for ownership tracking and responsibility attribution. Sourced  from all_referrals ownership logic.
 | `[]` | `{}` |
    | `REFERRAL_OWNER_NAME` | 15 | `TEXT` | **Referral Owner Name** - Full name of the Salesforce user who owns the referral record. Used  for ownership identification and performance attribution. Sourced from all_referrals user data integration.
 | **Referral Owner Name** - Full name of the Salesforce user who owns the referral record. Used  for ownership identification and performance attribution. Sourced from all_referrals user data integration.
 | `[]` | `{}` |
    | `REFERRAL_OWNER_TEAM` | 16 | `TEXT` | **Referral Owner Team** - Team assignment of the referral owner. Used for team-level performance  analysis and referral attribution. Sourced from all_referrals team data integration.
 | **Referral Owner Team** - Team assignment of the referral owner. Used for team-level performance  analysis and referral attribution. Sourced from all_referrals team data integration.
 | `[]` | `{}` |
    | `ACCOUNT_REFERRAL_ORDER` | 17 | `NUMBER` | **Account Referral Order** - Sequential order number of this referral within the same account  (1 = first referral for this account). Only the first referral per account is typically  eligible for rewards. Used for referral hierarchy analysis. Derived from all_referrals ordering logic.
 | **Account Referral Order** - Sequential order number of this referral within the same account  (1 = first referral for this account). Only the first referral per account is typically  eligible for rewards. Used for referral hierarchy analysis. Derived from all_referrals ordering logic.
 | `[]` | `{}` |
    | `PARENT_ACCOUNT_REFERRAL_ORDER` | 18 | `NUMBER` | **Parent Account Referral Order** - Sequential order number of this referral within the same  parent account for multi-location organizations. Used for enterprise-level referral hierarchy  and eligibility determination. Derived from all_referrals ordering logic.
 | **Parent Account Referral Order** - Sequential order number of this referral within the same  parent account for multi-location organizations. Used for enterprise-level referral hierarchy  and eligibility determination. Derived from all_referrals ordering logic.
 | `[]` | `{}` |
    | `REFERRER_REFERRAL_ORDER` | 19 | `NUMBER` | **Referrer's Referral Count Order** - Sequential number indicating which referral this is for  the referrer (1 = their first referral made). Used for referrer behavior analysis and repeat  referrer identification. Sourced from referral_referrers ordering logic.
 | **Referrer's Referral Count Order** - Sequential number indicating which referral this is for  the referrer (1 = their first referral made). Used for referrer behavior analysis and repeat  referrer identification. Sourced from referral_referrers ordering logic.
 | `[]` | `{}` |
    | `REFERRER_REFERRAL_RECENCY` | 20 | `NUMBER` | **Referrer's Referral Recency Rank** - Reverse ranking of referrals by the same referrer  (1 = most recent referral made). Used for referrer activity analysis and recent behavior tracking.  Sourced from referral_referrers recency ranking.
 | **Referrer's Referral Recency Rank** - Reverse ranking of referrals by the same referrer  (1 = most recent referral made). Used for referrer activity analysis and recent behavior tracking.  Sourced from referral_referrers recency ranking.
 | `[]` | `{}` |
    | `OPPORTUNITY_ID` | 21 | `TEXT` | **Salesforce Opportunity Identifier** - Salesforce opportunity ID linked to the referral  for sales pipeline tracking. Used for opportunity conversion analysis and sales attribution.  NULL when no opportunity exists. Sourced from all_referrals.
 | **Salesforce Opportunity Identifier** - Salesforce opportunity ID linked to the referral  for sales pipeline tracking. Used for opportunity conversion analysis and sales attribution.  NULL when no opportunity exists. Sourced from all_referrals.
 | `[]` | `{}` |
    | `REFERRAL_OBJECT_CREATED_DATETIME_PT` | 22 | `TIMESTAMP_NTZ` | **Referral Creation Time (Pacific)** - Pacific Time timestamp when the referral object was created  in Salesforce. Uses lead creation date when available, otherwise account creation date. Critical  for program version assignment and timeline analysis. Sourced from all_referrals.
 | **Referral Creation Time (Pacific)** - Pacific Time timestamp when the referral object was created  in Salesforce. Uses lead creation date when available, otherwise account creation date. Critical  for program version assignment and timeline analysis. Sourced from all_referrals.
 | `[]` | `{}` |
    | `IS_CREATED_DATE_OVERRIDE` | 23 | `BOOLEAN` | **Creation Date Override Flag** - Boolean indicating whether the referral creation date was  manually overridden from the original Salesforce timestamp. Used for data quality tracking  and timeline adjustments. Sourced from all_referrals.
 | **Creation Date Override Flag** - Boolean indicating whether the referral creation date was  manually overridden from the original Salesforce timestamp. Used for data quality tracking  and timeline adjustments. Sourced from all_referrals.
 | `[]` | `{}` |
    | `CREATED_DATE_OVERRIDE_NOTE` | 24 | `TEXT` | **Date Override Explanation** - Text note explaining why the creation date was overridden  and what the original date was. Used for audit trails and data quality validation. Sourced  from all_referrals.
 | **Date Override Explanation** - Text note explaining why the creation date was overridden  and what the original date was. Used for audit trails and data quality validation. Sourced  from all_referrals.
 | `[]` | `{}` |
    | `DEADLINE_TO_REGISTER` | 25 | `DATE` | **Registration Deadline** - Deadline by which referrals must start their underwriting application  to remain eligible. NULL for referrals outside valid program date ranges. Used for registration  criteria evaluation. Sourced from all_referrals.
 | **Registration Deadline** - Deadline by which referrals must start their underwriting application  to remain eligible. NULL for referrals outside valid program date ranges. Used for registration  criteria evaluation. Sourced from all_referrals.
 | `[]` | `{}` |
    | `DEMO_SCHEDULED_DATETIME_PT` | 26 | `TIMESTAMP_NTZ` | **Demo Scheduled Time (Pacific)** - Pacific Time when a demo was scheduled for the referral.  Used in Dental Partner Program for demo-based qualification criteria. NULL when no demo scheduled.  Sourced from referral_qualification demo tracking.
 | **Demo Scheduled Time (Pacific)** - Pacific Time when a demo was scheduled for the referral.  Used in Dental Partner Program for demo-based qualification criteria. NULL when no demo scheduled.  Sourced from referral_qualification demo tracking.
 | `[]` | `{}` |
    | `DEMO_ATTENDED_DATETIME_PT` | 27 | `TIMESTAMP_NTZ` | **Demo Attended Time (Pacific)** - Pacific Time when the referral attended their scheduled demo.  Used in Dental Partner Program for qualification determination. NULL when demo not attended.  Sourced from referral_qualification demo tracking.
 | **Demo Attended Time (Pacific)** - Pacific Time when the referral attended their scheduled demo.  Used in Dental Partner Program for qualification determination. NULL when demo not attended.  Sourced from referral_qualification demo tracking.
 | `[]` | `{}` |
    | `REGISTERED_DATE` | 28 | `TIMESTAMP_NTZ` | **Registration Date** - Date the referral submitted their underwriting application or earliest  date thereafter. Used for registration criteria evaluation and timeline tracking. Sourced from  referral_qualification registration tracking.
 | **Registration Date** - Date the referral submitted their underwriting application or earliest  date thereafter. Used for registration criteria evaluation and timeline tracking. Sourced from  referral_qualification registration tracking.
 | `[]` | `{}` |
    | `GO_LIVE_DATE` | 29 | `DATE` | **Merchant Go-Live Date** - Date when the referral became eligible to transact with Cherry and  the qualification clock started ticking. NULL for referrals that never activated. Critical for  deadline calculations and timeline analysis. Sourced from all_referrals.
 | **Merchant Go-Live Date** - Date when the referral became eligible to transact with Cherry and  the qualification clock started ticking. NULL for referrals that never activated. Critical for  deadline calculations and timeline analysis. Sourced from all_referrals.
 | `[]` | `{}` |
    | `DEADLINE_TO_QUALIFY` | 30 | `DATE` | **Qualification Deadline** - Calculated deadline (go_live_date + days_to_qualify) by which  referrals must meet qualification criteria. Used for qualification evaluation and timeline  tracking. Derived from all_referrals date calculations.
 | **Qualification Deadline** - Calculated deadline (go_live_date + days_to_qualify) by which  referrals must meet qualification criteria. Used for qualification evaluation and timeline  tracking. Derived from all_referrals date calculations.
 | `[]` | `{}` |
    | `REFERRER_CODE` | 31 | `TEXT` | **Referrer Unique Code** - Unique referral code assigned to the referrer in Referral Rock  system. Used for referrer identification and tracking. NULL for manually-added referrals.  Sourced from referral_referrers attribution logic.
 | **Referrer Unique Code** - Unique referral code assigned to the referrer in Referral Rock  system. Used for referrer identification and tracking. NULL for manually-added referrals.  Sourced from referral_referrers attribution logic.
 | `[]` | `{}` |
    | `REFERRAL_SOURCE` | 32 | `TEXT` | **Referral Source Type** - Indicates how the referral was captured: 'Referral Rock' for automated  campaigns, 'Manual' for Salesforce entries, or other system sources. Used for channel analysis  and processing workflow determination. Sourced from all_referrals.
 | **Referral Source Type** - Indicates how the referral was captured: 'Referral Rock' for automated  campaigns, 'Manual' for Salesforce entries, or other system sources. Used for channel analysis  and processing workflow determination. Sourced from all_referrals.
 | `[]` | `{}` |
    | `IS_IN_CENTRAL_PACIFIC_BANK_CAMPAIGN` | 33 | `BOOLEAN` | **Central Pacific Bank Campaign Flag** - Boolean indicating whether the referral is part of  the Central Pacific Bank special campaign. Used for campaign-specific analysis and reporting.  Sourced from all_referrals campaign tracking.
 | **Central Pacific Bank Campaign Flag** - Boolean indicating whether the referral is part of  the Central Pacific Bank special campaign. Used for campaign-specific analysis and reporting.  Sourced from all_referrals campaign tracking.
 | `[]` | `{}` |
    | `PROGRAM_NUMBER` | 34 | `NUMBER` | **Referral Program Version** - Version number (1-4) of Cherry's referral program that applies  to this referral based on creation date. NULL for referrals outside valid program date ranges.  Determines qualification criteria and bonus structures. Sourced from all_referrals.
 | **Referral Program Version** - Version number (1-4) of Cherry's referral program that applies  to this referral based on creation date. NULL for referrals outside valid program date ranges.  Determines qualification criteria and bonus structures. Sourced from all_referrals.
 | `[]` | `{}` |
    | `PROGRAM_NAME` | 35 | `TEXT` | **Referral Program Name** - Human-readable name of the program version (e.g., 'Standard Referral Program',  'Dental Partner Program'). Used for program-specific analysis and qualification rule application.  Sourced from all_referrals.
 | **Referral Program Name** - Human-readable name of the program version (e.g., 'Standard Referral Program',  'Dental Partner Program'). Used for program-specific analysis and qualification rule application.  Sourced from all_referrals.
 | `[]` | `{}` |
    | `PROGRAM_START_DATE` | 36 | `DATE` | **Program Start Date** - Date when the referral program version began. Used for program timeline  analysis and determining which referrals fall under each program iteration. Sourced from all_referrals.
 | **Program Start Date** - Date when the referral program version began. Used for program timeline  analysis and determining which referrals fall under each program iteration. Sourced from all_referrals.
 | `[]` | `{}` |
    | `PROGRAM_END_DATE` | 37 | `DATE` | **Program End Date** - Date when the referral program version ended. Used for program lifecycle  analysis and transition tracking between program versions. Sourced from all_referrals.
 | **Program End Date** - Date when the referral program version ended. Used for program lifecycle  analysis and transition tracking between program versions. Sourced from all_referrals.
 | `[]` | `{}` |
    | `DAYS_TO_REGISTER` | 38 | `NUMBER` | **Registration Period Days** - Number of days referrals have to register (submit underwriting  application) in their program version. Used to calculate registration deadlines. Sourced from  all_referrals program rules.
 | **Registration Period Days** - Number of days referrals have to register (submit underwriting  application) in their program version. Used to calculate registration deadlines. Sourced from  all_referrals program rules.
 | `[]` | `{}` |
    | `DAYS_TO_QUALIFY` | 39 | `NUMBER` | **Qualification Period Days** - Number of days from go_live_date that referrals have to meet  qualification criteria. Varies by program version. Used to calculate deadline_to_qualify.  Sourced from all_referrals program rules.
 | **Qualification Period Days** - Number of days from go_live_date that referrals have to meet  qualification criteria. Varies by program version. Used to calculate deadline_to_qualify.  Sourced from all_referrals program rules.
 | `[]` | `{}` |
    | `TRANSACTIONS_TO_QUALIFY` | 40 | `NUMBER` | **Required Transaction Count** - Number of transactions required for qualification when  qualification_method is 'Transactions'. NULL for amount-based programs. Used for qualification  evaluation. Sourced from all_referrals program rules.
 | **Required Transaction Count** - Number of transactions required for qualification when  qualification_method is 'Transactions'. NULL for amount-based programs. Used for qualification  evaluation. Sourced from all_referrals program rules.
 | `[]` | `{}` |
    | `GROSS_AMOUNT_TO_QUALIFY` | 41 | `NUMBER` | **Required Gross Amount** - Dollar amount of loan volume required for qualification when  qualification_method is 'Gross Amount'. NULL for transaction-based programs. Used for  qualification evaluation. Sourced from all_referrals program rules.
 | **Required Gross Amount** - Dollar amount of loan volume required for qualification when  qualification_method is 'Gross Amount'. NULL for transaction-based programs. Used for  qualification evaluation. Sourced from all_referrals program rules.
 | `[]` | `{}` |
    | `QUALIFICATION_METHOD` | 42 | `TEXT` | **Qualification Method** - Defines how referrals must qualify for rewards: 'Transactions' (count-based)  or 'Gross Amount' (volume-based). Determines which criteria are evaluated for qualification.  Sourced from all_referrals program configuration.
 | **Qualification Method** - Defines how referrals must qualify for rewards: 'Transactions' (count-based)  or 'Gross Amount' (volume-based). Determines which criteria are evaluated for qualification.  Sourced from all_referrals program configuration.
 | `[]` | `{}` |
    | `REFERRER_LEAD_ID` | 43 | `TEXT` | **Referrer Lead Identifier** - Salesforce lead ID of the person who made the referral when  they can be matched to a lead record. Used for referrer lead tracking and conversion analysis.  Sourced from referral_referrers complex matching logic.
 | **Referrer Lead Identifier** - Salesforce lead ID of the person who made the referral when  they can be matched to a lead record. Used for referrer lead tracking and conversion analysis.  Sourced from referral_referrers complex matching logic.
 | `[]` | `{}` |
    | `REFERRER_ACCOUNT_ID` | 44 | `TEXT` | **Referrer Account Identifier** - Salesforce account ID of the referrer when they can be  matched to an account. Used for referrer account relationship tracking and analysis. Sourced  from referral_referrers account matching logic.
 | **Referrer Account Identifier** - Salesforce account ID of the referrer when they can be  matched to an account. Used for referrer account relationship tracking and analysis. Sourced  from referral_referrers account matching logic.
 | `[]` | `{}` |
    | `REFERRER_EMAIL` | 45 | `TEXT` | **Referrer Email Address** - Email address of the person who made the referral, using complex  coalescing logic across multiple data sources (Referral Rock, Salesforce contacts, account data).  Used for referrer communication and identification. Sourced from referral_referrers email prioritization.
 | **Referrer Email Address** - Email address of the person who made the referral, using complex  coalescing logic across multiple data sources (Referral Rock, Salesforce contacts, account data).  Used for referrer communication and identification. Sourced from referral_referrers email prioritization.
 | `[]` | `{}` |
    | `REFERRER_EMAIL_SOURCE_FIELD` | 46 | `TEXT` | **Referrer Email Data Source** - Indicates which field/system provided the referrer email  (e.g., 'referrals.referrer_email', 'contacts.email'). Used for data quality tracking and  source attribution. Sourced from referral_referrers source field tracking.
 | **Referrer Email Data Source** - Indicates which field/system provided the referrer email  (e.g., 'referrals.referrer_email', 'contacts.email'). Used for data quality tracking and  source attribution. Sourced from referral_referrers source field tracking.
 | `[]` | `{}` |
    | `REFERRER_CREATED_DATE` | 47 | `TIMESTAMP_TZ` | **Referrer Creation Date** - Date when the referrer was first created in the system, using  coalescing logic across multiple sources. Used for referrer tenure analysis and qualification  timing. Sourced from referral_referrers date prioritization.
 | **Referrer Creation Date** - Date when the referrer was first created in the system, using  coalescing logic across multiple sources. Used for referrer tenure analysis and qualification  timing. Sourced from referral_referrers date prioritization.
 | `[]` | `{}` |
    | `REFERRER_ACCOUNT_SOURCE` | 48 | `TEXT` | **Referrer Account Source** - Source classification of the referrer's account (e.g., how they  originally became a Cherry customer). Used for referrer source analysis and attribution patterns.  Sourced from referral_referrers account source tracking.
 | **Referrer Account Source** - Source classification of the referrer's account (e.g., how they  originally became a Cherry customer). Used for referrer source analysis and attribution patterns.  Sourced from referral_referrers account source tracking.
 | `[]` | `{}` |
    | `REFERRER_CAMPAIGN_NAME` | 49 | `TEXT` | **Referrer Campaign Name** - Marketing campaign that originally brought the referrer to Cherry.  Used for campaign effectiveness analysis and referrer source attribution. Sourced from  referral_referrers campaign tracking.
 | **Referrer Campaign Name** - Marketing campaign that originally brought the referrer to Cherry.  Used for campaign effectiveness analysis and referrer source attribution. Sourced from  referral_referrers campaign tracking.
 | `[]` | `{}` |
    | `REFERRER_ACCOUNT_OWNER_ID` | 50 | `TEXT` | **Referrer Account Owner ID** - Salesforce user ID of the account owner for the referrer's  account. Used for referrer relationship management and sales attribution. Sourced from  referral_referrers ownership tracking.
 | **Referrer Account Owner ID** - Salesforce user ID of the account owner for the referrer's  account. Used for referrer relationship management and sales attribution. Sourced from  referral_referrers ownership tracking.
 | `[]` | `{}` |
    | `REFERRER_ACCOUNT_REFERRING_ACCOUNT` | 51 | `TEXT` | **Referrer's Referring Account** - Account ID of who referred the referrer (second-degree  referral tracking). Used for referral chain analysis and network effect measurement. Sourced  from referral_referrers chain tracking.
 | **Referrer's Referring Account** - Account ID of who referred the referrer (second-degree  referral tracking). Used for referral chain analysis and network effect measurement. Sourced  from referral_referrers chain tracking.
 | `[]` | `{}` |
    | `REFERRER_ACCOUNT_OWNER_NAME` | 52 | `TEXT` | **Referrer Account Owner Name** - Full name of the Salesforce user who owns the referrer's  account. Used for referrer relationship management and performance attribution. Sourced from  referral_referrers user data integration.
 | **Referrer Account Owner Name** - Full name of the Salesforce user who owns the referrer's  account. Used for referrer relationship management and performance attribution. Sourced from  referral_referrers user data integration.
 | `[]` | `{}` |
    | `REFERRER_ACCOUNT_OWNER_TEAM` | 53 | `TEXT` | **Referrer Account Owner Team** - Team assignment of the referrer's account owner. Used for  team-level referrer relationship analysis and performance tracking. Sourced from referral_referrers  team data integration.
 | **Referrer Account Owner Team** - Team assignment of the referrer's account owner. Used for  team-level referrer relationship analysis and performance tracking. Sourced from referral_referrers  team data integration.
 | `[]` | `{}` |
    | `TRANSACTIONS_BEFORE_DEADLINE` | 54 | `NUMBER` | **Pre-Deadline Transaction Count** - Number of transactions the referral completed before their  qualification deadline. Used for transaction-based qualification evaluation and analysis.  Sourced from referral_qualification transaction tracking.
 | **Pre-Deadline Transaction Count** - Number of transactions the referral completed before their  qualification deadline. Used for transaction-based qualification evaluation and analysis.  Sourced from referral_qualification transaction tracking.
 | `[]` | `{}` |
    | `GROSS_AMOUNT_BEFORE_DEADLINE` | 55 | `FLOAT` | **Pre-Deadline Gross Amount** - Total loan gross amount the referral generated before their  qualification deadline. Used for amount-based qualification evaluation. Sourced from  referral_qualification amount tracking.
 | **Pre-Deadline Gross Amount** - Total loan gross amount the referral generated before their  qualification deadline. Used for amount-based qualification evaluation. Sourced from  referral_qualification amount tracking.
 | `[]` | `{}` |
    | `MET_DEMO_CRITERIA` | 56 | `BOOLEAN` | **Demo Criteria Met** - Boolean indicating whether demo requirements were satisfied for Dental  Partner Program qualification. Used for demo-based qualification evaluation. Sourced from  referral_qualification demo evaluation.
 | **Demo Criteria Met** - Boolean indicating whether demo requirements were satisfied for Dental  Partner Program qualification. Used for demo-based qualification evaluation. Sourced from  referral_qualification demo evaluation.
 | `[]` | `{}` |
    | `MET_REGISTRATION_CRITERIA` | 57 | `BOOLEAN` | **Registration Criteria Met** - Boolean indicating whether the referral registered before their  deadline_to_register. Critical for Standard Referral Program qualification. Sourced from  referral_qualification compliance evaluation.
 | **Registration Criteria Met** - Boolean indicating whether the referral registered before their  deadline_to_register. Critical for Standard Referral Program qualification. Sourced from  referral_qualification compliance evaluation.
 | `[]` | `{}` |
    | `MET_LOANS_CRITERIA` | 58 | `BOOLEAN` | **Loan Criteria Met** - Boolean indicating whether the referral met loan/transaction requirements  before deadline_to_qualify. Critical for all program qualification evaluation. Sourced from  referral_qualification loan criteria evaluation.
 | **Loan Criteria Met** - Boolean indicating whether the referral met loan/transaction requirements  before deadline_to_qualify. Critical for all program qualification evaluation. Sourced from  referral_qualification loan criteria evaluation.
 | `[]` | `{}` |
    | `CRITERIA_STAGE` | 59 | `TEXT` | **Qualification Stage** - Indicates which criteria stage the referral is in: 'Registration'  (hasn't registered yet) or 'Loans' (registered but working on loan criteria). Used for workflow  management and stage analysis. Sourced from referral_qualification stage logic.
 | **Qualification Stage** - Indicates which criteria stage the referral is in: 'Registration'  (hasn't registered yet) or 'Loans' (registered but working on loan criteria). Used for workflow  management and stage analysis. Sourced from referral_qualification stage logic.
 | `[]` | `{}` |
    | `IS_EXPIRED` | 60 | `BOOLEAN` | **Expiration Status** - Boolean indicating whether a deadline has expired without corresponding  criteria being met. Used for denial determination and eligibility tracking. Sourced from  referral_qualification expiration logic.
 | **Expiration Status** - Boolean indicating whether a deadline has expired without corresponding  criteria being met. Used for denial determination and eligibility tracking. Sourced from  referral_qualification expiration logic.
 | `[]` | `{}` |
    | `IS_QUALIFIED` | 61 | `BOOLEAN` | **Qualification Status** - Boolean indicating whether the referral met all requirements for  reward eligibility. Combines registration, demo, and loan criteria based on program type.  Primary metric for qualification analysis. Sourced from referral_qualification.
 | **Qualification Status** - Boolean indicating whether the referral met all requirements for  reward eligibility. Combines registration, demo, and loan criteria based on program type.  Primary metric for qualification analysis. Sourced from referral_qualification.
 | `[]` | `{}` |
    | `IS_QUALIFIED_PROGRAM1` | 62 | `BOOLEAN` | **Program 1 Qualification Status** - Boolean indicating qualification specifically under program  version 1 rules (qualified AND not denied). Used for program-specific performance analysis.  Derived from program_number and qualification logic.
 | **Program 1 Qualification Status** - Boolean indicating qualification specifically under program  version 1 rules (qualified AND not denied). Used for program-specific performance analysis.  Derived from program_number and qualification logic.
 | `[]` | `{}` |
    | `IS_QUALIFIED_PROGRAM2` | 63 | `BOOLEAN` | **Program 2 Qualification Status** - Boolean indicating qualification specifically under program  version 2 rules (qualified AND not denied). Used for program-specific performance analysis.  Derived from program_number and qualification logic.
 | **Program 2 Qualification Status** - Boolean indicating qualification specifically under program  version 2 rules (qualified AND not denied). Used for program-specific performance analysis.  Derived from program_number and qualification logic.
 | `[]` | `{}` |
    | `IS_QUALIFIED_PROGRAM3` | 64 | `BOOLEAN` | **Program 3 Qualification Status** - Boolean indicating qualification specifically under program  version 3 rules (qualified AND not denied). Used for program-specific performance analysis.  Derived from program_number and qualification logic.
 | **Program 3 Qualification Status** - Boolean indicating qualification specifically under program  version 3 rules (qualified AND not denied). Used for program-specific performance analysis.  Derived from program_number and qualification logic.
 | `[]` | `{}` |
    | `IS_QUALIFIED_PROGRAM4` | 65 | `BOOLEAN` | **Program 4 Qualification Status** - Boolean indicating qualification specifically under program  version 4 rules (qualified AND not denied). Used for program-specific performance analysis.  Derived from program_number and qualification logic.
 | **Program 4 Qualification Status** - Boolean indicating qualification specifically under program  version 4 rules (qualified AND not denied). Used for program-specific performance analysis.  Derived from program_number and qualification logic.
 | `[]` | `{}` |
    | `QUALIFICATION_DATE` | 66 | `TIMESTAMP_NTZ` | **Qualification Achievement Date** - Date when the referral met all qualification criteria.  Used for qualification timeline analysis and payment eligibility determination. NULL for  unqualified referrals. Sourced from referral_qualification.
 | **Qualification Achievement Date** - Date when the referral met all qualification criteria.  Used for qualification timeline analysis and payment eligibility determination. NULL for  unqualified referrals. Sourced from referral_qualification.
 | `[]` | `{}` |
    | `IS_REGISTRATION_DEADLINE_ELAPSED` | 67 | `BOOLEAN` | **Registration Deadline Status** - Boolean indicating whether the registration deadline has passed.  Used for determining registration criteria compliance and denial logic. Sourced from referral_qualification.
 | **Registration Deadline Status** - Boolean indicating whether the registration deadline has passed.  Used for determining registration criteria compliance and denial logic. Sourced from referral_qualification.
 | `[]` | `{}` |
    | `IS_LOANS_DEADLINE_ELAPSED` | 68 | `BOOLEAN` | **Loan Deadline Status** - Boolean indicating whether the loan qualification deadline has passed.  Used for denial logic and qualification window analysis. Sourced from referral_qualification.
 | **Loan Deadline Status** - Boolean indicating whether the loan qualification deadline has passed.  Used for denial logic and qualification window analysis. Sourced from referral_qualification.
 | `[]` | `{}` |
    | `IS_FRAUD` | 69 | `BOOLEAN` | **Fraud Flag Status** - Boolean indicating whether the referral was flagged for fraudulent  activity based on notes or fraud check processes. Used for fraud analysis and disqualification.  Sourced from referral_qualification fraud detection.
 | **Fraud Flag Status** - Boolean indicating whether the referral was flagged for fraudulent  activity based on notes or fraud check processes. Used for fraud analysis and disqualification.  Sourced from referral_qualification fraud detection.
 | `[]` | `{}` |
    | `IS_FRAUD_EVALUATION` | 70 | `TEXT` | **Fraud Detection Details** - Text explanation of fraud flag reasoning and detection details.  Used for fraud investigation and process improvement. Sourced from referral_qualification  fraud evaluation.
 | **Fraud Detection Details** - Text explanation of fraud flag reasoning and detection details.  Used for fraud investigation and process improvement. Sourced from referral_qualification  fraud evaluation.
 | `[]` | `{}` |
    | `IS_DISQUALIFIED` | 71 | `BOOLEAN` | **Disqualification Status** - Boolean indicating whether the referral was manually disqualified  from program eligibility. Used for manual override tracking and analysis. Sourced from  referral_qualification disqualification tracking.
 | **Disqualification Status** - Boolean indicating whether the referral was manually disqualified  from program eligibility. Used for manual override tracking and analysis. Sourced from  referral_qualification disqualification tracking.
 | `[]` | `{}` |
    | `IS_DISQUALIFIED_EVALUATION` | 72 | `TEXT` | **Disqualification Reason** - Text explanation of manual disqualification reasoning. Used for  disqualification analysis and audit trails. Sourced from referral_qualification disqualification  evaluation.
 | **Disqualification Reason** - Text explanation of manual disqualification reasoning. Used for  disqualification analysis and audit trails. Sourced from referral_qualification disqualification  evaluation.
 | `[]` | `{}` |
    | `FRAUD_CHECK_DETAILS` | 73 | `TEXT` | **Fraud Check Details** - Detailed information from fraud checking processes including specific  flags and investigation notes. Used for fraud analysis and compliance tracking. Sourced from  referral_qualification fraud processing.
 | **Fraud Check Details** - Detailed information from fraud checking processes including specific  flags and investigation notes. Used for fraud analysis and compliance tracking. Sourced from  referral_qualification fraud processing.
 | `[]` | `{}` |
    | `IS_DENIED` | 74 | `BOOLEAN` | **Denial Status** - Boolean indicating whether the referral is denied reward eligibility due to  deadline expiration, fraud flags, or other disqualification criteria. Includes complex logic  for subsequent referrals and qualified opportunity timing. Sourced from referral_qualification.
 | **Denial Status** - Boolean indicating whether the referral is denied reward eligibility due to  deadline expiration, fraud flags, or other disqualification criteria. Includes complex logic  for subsequent referrals and qualified opportunity timing. Sourced from referral_qualification.
 | `[]` | `{}` |
    | `IS_DENIED_EVALUATION` | 75 | `TEXT` | **Denial Reason Explanation** - Text explanation of why is_denied is TRUE, providing specific  reason such as deadline expiration, fraud flags, or subsequent referral rules. Used for  denial analysis and appeals processing. Sourced from referral_qualification.
 | **Denial Reason Explanation** - Text explanation of why is_denied is TRUE, providing specific  reason such as deadline expiration, fraud flags, or subsequent referral rules. Used for  denial analysis and appeals processing. Sourced from referral_qualification.
 | `[]` | `{}` |
    | `DENY_IN_REFERRAL_ROCK` | 76 | `BOOLEAN` | **Referral Rock Denial Flag** - Boolean indicating whether Referral Rock referrals should be  denied due to expiration or denial status. Used for Referral Rock payment processing and  status synchronization. Sourced from referral_qualification Referral Rock integration logic. | **Referral Rock Denial Flag** - Boolean indicating whether Referral Rock referrals should be  denied due to expiration or denial status. Used for Referral Rock payment processing and  status synchronization. Sourced from referral_qualification Referral Rock integration logic. | `[]` | `{}` |
    | `TOTAL_REFERRER_DOLLARS` | 77 | `NUMBER` | **Total Referrer Bonus Amount** - Aggregated dollar amount of bonuses eligible to be paid  to the referrer across all cost records for this referral. Used for referrer payment calculation  and cost analysis. Sourced from referral_cost aggregation.
 | **Total Referrer Bonus Amount** - Aggregated dollar amount of bonuses eligible to be paid  to the referrer across all cost records for this referral. Used for referrer payment calculation  and cost analysis. Sourced from referral_cost aggregation.
 | `[]` | `{}` |
    | `TOTAL_REFERRAL_DOLLARS` | 78 | `FLOAT` | **Total Referral Bonus Amount** - Aggregated dollar amount of bonuses eligible to be paid  to the referral (referred merchant) across all cost records. Used for referral payment  calculation and cost analysis. Sourced from referral_cost aggregation.
 | **Total Referral Bonus Amount** - Aggregated dollar amount of bonuses eligible to be paid  to the referral (referred merchant) across all cost records. Used for referral payment  calculation and cost analysis. Sourced from referral_cost aggregation.
 | `[]` | `{}` |
    | `LAST_PAYMENTS_REFRESH_DATE` | 79 | `DATE` | **Payment Data Refresh Date** - Most recent date when payment data was refreshed from external  systems. Used for data freshness validation and payment processing timeline analysis. Sourced  from referral_cost payment system integration.
 | **Payment Data Refresh Date** - Most recent date when payment data was refreshed from external  systems. Used for data freshness validation and payment processing timeline analysis. Sourced  from referral_cost payment system integration.
 | `[]` | `{}` |
    | `NUM_REFERRAL_PAYMENTS` | 80 | `NUMBER` | **Payment Record Count** - Number of separate payment records associated with this referral.  Used for payment complexity analysis and multi-payment tracking. Sourced from referral_cost  payment aggregation.
 | **Payment Record Count** - Number of separate payment records associated with this referral.  Used for payment complexity analysis and multi-payment tracking. Sourced from referral_cost  payment aggregation.
 | `[]` | `{}` |
    | `TOTAL_REFERRAL_COST` | 81 | `FLOAT` | **Total Program Cost** - Total cost of the referral to Cherry including all bonuses and  payments. Primary metric for referral program cost analysis and ROI calculations. Sourced  from referral_cost comprehensive cost calculation.
 | **Total Program Cost** - Total cost of the referral to Cherry including all bonuses and  payments. Primary metric for referral program cost analysis and ROI calculations. Sourced  from referral_cost comprehensive cost calculation.
 | `[]` | `{}` |
    | `REFERRAL_COST_EVALUATIONS` | 82 | `TEXT` | **Cost Calculation Details** - Concatenated list of cost evaluation reasons and calculations  applied to determine the final referral cost. Used for cost logic transparency and audit trails.  Sourced from referral_cost evaluation tracking.
 | **Cost Calculation Details** - Concatenated list of cost evaluation reasons and calculations  applied to determine the final referral cost. Used for cost logic transparency and audit trails.  Sourced from referral_cost evaluation tracking.
 | `[]` | `{}` |
    | `PAYMENT_IDS` | 83 | `TEXT` | **Payment Identifier List** - Comma-separated list of payment IDs associated with this referral  across all payment platforms. Used for payment tracking and reconciliation. Sourced from  referral_payments aggregation.
 | **Payment Identifier List** - Comma-separated list of payment IDs associated with this referral  across all payment platforms. Used for payment tracking and reconciliation. Sourced from  referral_payments aggregation.
 | `[]` | `{}` |
    | `NUM_PAYMENT_IDS` | 84 | `NUMBER` | **Payment Count** - Number of distinct payments made for this referral across all platforms.  Used for payment analysis and multi-payment tracking. Sourced from referral_payments counting.
 | **Payment Count** - Number of distinct payments made for this referral across all platforms.  Used for payment analysis and multi-payment tracking. Sourced from referral_payments counting.
 | `[]` | `{}` |
    | `HAS_PAYMENT` | 85 | `BOOLEAN` | **Payment Exists Flag** - Boolean indicating whether any payments have been made for this  referral. Used for payment status analysis and unpaid referral identification. Derived from  payment_ids existence check.
 | **Payment Exists Flag** - Boolean indicating whether any payments have been made for this  referral. Used for payment status analysis and unpaid referral identification. Derived from  payment_ids existence check.
 | `[]` | `{}` |
    | `PAYMENT_PLATFORMS` | 86 | `TEXT` | **Payment Platform List** - Comma-separated list of platforms used for payments (e.g., 'Modern Treasury',  'Referral Rock'). Used for payment platform analysis and processing method tracking. Sourced  from referral_payments platform aggregation.
 | **Payment Platform List** - Comma-separated list of platforms used for payments (e.g., 'Modern Treasury',  'Referral Rock'). Used for payment platform analysis and processing method tracking. Sourced  from referral_payments platform aggregation.
 | `[]` | `{}` |
    | `FIRST_PAYMENT_DATETIME` | 87 | `TIMESTAMP_TZ` | **First Payment Time** - Timestamp of the earliest payment made for this referral. Used for  payment timing analysis and processing speed measurement. Sourced from referral_payments  chronological analysis.
 | **First Payment Time** - Timestamp of the earliest payment made for this referral. Used for  payment timing analysis and processing speed measurement. Sourced from referral_payments  chronological analysis.
 | `[]` | `{}` |
    | `LAST_PAYMENT_DATETIME` | 88 | `TIMESTAMP_TZ` | **Most Recent Payment Time** - Timestamp of the most recent payment made for this referral.  Used for payment timeline tracking and recent payment activity analysis. Sourced from  referral_payments chronological analysis.
 | **Most Recent Payment Time** - Timestamp of the most recent payment made for this referral.  Used for payment timeline tracking and recent payment activity analysis. Sourced from  referral_payments chronological analysis.
 | `[]` | `{}` |
    | `TOTAL_PAYMENT_AMOUNT` | 89 | `NUMBER` | **Total Payment Amount** - Sum of all payment amounts made for this referral across all  platforms and payment records. Used for payment reconciliation and actual cost tracking.  Sourced from referral_payments amount aggregation.
 | **Total Payment Amount** - Sum of all payment amounts made for this referral across all  platforms and payment records. Used for payment reconciliation and actual cost tracking.  Sourced from referral_payments amount aggregation.
 | `[]` | `{}` |
    | `PAYMENT_STATUSES` | 90 | `TEXT` | **Payment Status List** - Concatenated list of payment statuses across all payment records  for this referral. Used for payment status monitoring and processing issue identification.  Sourced from referral_payments status aggregation.
 | **Payment Status List** - Concatenated list of payment statuses across all payment records  for this referral. Used for payment status monitoring and processing issue identification.  Sourced from referral_payments status aggregation.
 | `[]` | `{}` |
    | `TOTAL_TRANSACTIONS` | 91 | `NUMBER` | **Lifetime Transaction Count** - Total number of loan transactions generated by the referral  merchant across their entire relationship with Cherry. Used for referral value analysis and  merchant performance evaluation. Sourced from referral_revenue lifetime calculations.
 | **Lifetime Transaction Count** - Total number of loan transactions generated by the referral  merchant across their entire relationship with Cherry. Used for referral value analysis and  merchant performance evaluation. Sourced from referral_revenue lifetime calculations.
 | `[]` | `{}` |
    | `TOTAL_GROSS_AMOUNT` | 92 | `FLOAT` | **Lifetime Gross Amount** - Total dollar amount of loan gross volume generated by the referral  merchant across their entire relationship. Primary metric for referral lifetime value calculation.  Sourced from referral_revenue lifetime calculations.
 | **Lifetime Gross Amount** - Total dollar amount of loan gross volume generated by the referral  merchant across their entire relationship. Primary metric for referral lifetime value calculation.  Sourced from referral_revenue lifetime calculations.
 | `[]` | `{}` |
    | `TOTAL_REVENUE` | 93 | `FLOAT` | **Lifetime Revenue Amount** - Total revenue generated by Cherry from the referral merchant  across their entire relationship. Used for referral ROI analysis and program profitability  assessment. Sourced from referral_revenue lifetime calculations.
 | **Lifetime Revenue Amount** - Total revenue generated by Cherry from the referral merchant  across their entire relationship. Used for referral ROI analysis and program profitability  assessment. Sourced from referral_revenue lifetime calculations.
 | `[]` | `{}` |
    | `TRANSACTIONS_14_DAYS` | 94 | `NUMBER` | **14-Day Transaction Count** - Number of transactions by the referral merchant within their  first 14 days after go-live (only for merchants who have been live at least 14 days). Used  for early performance analysis. Sourced from referral_revenue time-windowed calculations.
 | **14-Day Transaction Count** - Number of transactions by the referral merchant within their  first 14 days after go-live (only for merchants who have been live at least 14 days). Used  for early performance analysis. Sourced from referral_revenue time-windowed calculations.
 | `[]` | `{}` |
    | `TRANSACTIONS_30_DAYS` | 95 | `NUMBER` | **30-Day Transaction Count** - Number of transactions by the referral merchant within their  first 30 days after go-live (only for merchants who have been live at least 30 days). Used  for qualification evaluation and early performance analysis. Sourced from referral_revenue.
 | **30-Day Transaction Count** - Number of transactions by the referral merchant within their  first 30 days after go-live (only for merchants who have been live at least 30 days). Used  for qualification evaluation and early performance analysis. Sourced from referral_revenue.
 | `[]` | `{}` |
    | `TRANSACTIONS_60_DAYS` | 96 | `NUMBER` | **60-Day Transaction Count** - Number of transactions by the referral merchant within their  first 60 days after go-live (only for merchants who have been live at least 60 days). Used  for extended performance analysis. Sourced from referral_revenue time-windowed calculations.
 | **60-Day Transaction Count** - Number of transactions by the referral merchant within their  first 60 days after go-live (only for merchants who have been live at least 60 days). Used  for extended performance analysis. Sourced from referral_revenue time-windowed calculations.
 | `[]` | `{}` |
    | `TRANSACTIONS_90_DAYS` | 97 | `NUMBER` | **90-Day Transaction Count** - Number of transactions by the referral merchant within their  first 90 days after go-live (only for merchants who have been live at least 90 days). Used  for quarterly performance analysis. Sourced from referral_revenue time-windowed calculations.
 | **90-Day Transaction Count** - Number of transactions by the referral merchant within their  first 90 days after go-live (only for merchants who have been live at least 90 days). Used  for quarterly performance analysis. Sourced from referral_revenue time-windowed calculations.
 | `[]` | `{}` |
    | `TRANSACTIONS_180_DAYS` | 98 | `NUMBER` | **180-Day Transaction Count** - Number of transactions by the referral merchant within their  first 180 days after go-live (only for merchants who have been live at least 180 days). Used  for extended performance and retention analysis. Sourced from referral_revenue time-windowed calculations.
 | **180-Day Transaction Count** - Number of transactions by the referral merchant within their  first 180 days after go-live (only for merchants who have been live at least 180 days). Used  for extended performance and retention analysis. Sourced from referral_revenue time-windowed calculations.
 | `[]` | `{}` |
    | `GROSS_AMOUNT_14_DAYS` | 99 | `FLOAT` | **14-Day Gross Amount** - Total loan gross amount generated by the referral merchant within  their first 14 days after go-live. Used for early volume analysis and rapid adoption identification.  Sourced from referral_revenue time-windowed calculations.
 | **14-Day Gross Amount** - Total loan gross amount generated by the referral merchant within  their first 14 days after go-live. Used for early volume analysis and rapid adoption identification.  Sourced from referral_revenue time-windowed calculations.
 | `[]` | `{}` |
    | `GROSS_AMOUNT_30_DAYS` | 100 | `FLOAT` | **30-Day Gross Amount** - Total loan gross amount generated by the referral merchant within  their first 30 days after go-live. Used for qualification evaluation and early volume assessment.  Sourced from referral_revenue time-windowed calculations.
 | **30-Day Gross Amount** - Total loan gross amount generated by the referral merchant within  their first 30 days after go-live. Used for qualification evaluation and early volume assessment.  Sourced from referral_revenue time-windowed calculations.
 | `[]` | `{}` |
    | `GROSS_AMOUNT_60_DAYS` | 101 | `FLOAT` | **60-Day Gross Amount** - Total loan gross amount generated by the referral merchant within  their first 60 days after go-live. Used for extended volume analysis and growth pattern assessment.  Sourced from referral_revenue time-windowed calculations.
 | **60-Day Gross Amount** - Total loan gross amount generated by the referral merchant within  their first 60 days after go-live. Used for extended volume analysis and growth pattern assessment.  Sourced from referral_revenue time-windowed calculations.
 | `[]` | `{}` |
    | `GROSS_AMOUNT_90_DAYS` | 102 | `FLOAT` | **90-Day Gross Amount** - Total loan gross amount generated by the referral merchant within  their first 90 days after go-live. Used for quarterly volume analysis and performance benchmarking.  Sourced from referral_revenue time-windowed calculations.
 | **90-Day Gross Amount** - Total loan gross amount generated by the referral merchant within  their first 90 days after go-live. Used for quarterly volume analysis and performance benchmarking.  Sourced from referral_revenue time-windowed calculations.
 | `[]` | `{}` |
    | `GROSS_AMOUNT_180_DAYS` | 103 | `FLOAT` | **180-Day Gross Amount** - Total loan gross amount generated by the referral merchant within  their first 180 days after go-live. Used for extended volume analysis and long-term value assessment.  Sourced from referral_revenue time-windowed calculations.
 | **180-Day Gross Amount** - Total loan gross amount generated by the referral merchant within  their first 180 days after go-live. Used for extended volume analysis and long-term value assessment.  Sourced from referral_revenue time-windowed calculations.
 | `[]` | `{}` |
    | `REVENUE_14_DAYS` | 104 | `FLOAT` | **14-Day Revenue Amount** - Total revenue generated by Cherry from the referral merchant within  their first 14 days after go-live. Used for early revenue analysis and quick ROI assessment.  Sourced from referral_revenue time-windowed calculations.
 | **14-Day Revenue Amount** - Total revenue generated by Cherry from the referral merchant within  their first 14 days after go-live. Used for early revenue analysis and quick ROI assessment.  Sourced from referral_revenue time-windowed calculations.
 | `[]` | `{}` |
    | `REVENUE_30_DAYS` | 105 | `FLOAT` | **30-Day Revenue Amount** - Total revenue generated by Cherry from the referral merchant within  their first 30 days after go-live. Used for early revenue analysis and qualification period ROI.  Sourced from referral_revenue time-windowed calculations.
 | **30-Day Revenue Amount** - Total revenue generated by Cherry from the referral merchant within  their first 30 days after go-live. Used for early revenue analysis and qualification period ROI.  Sourced from referral_revenue time-windowed calculations.
 | `[]` | `{}` |
    | `REVENUE_60_DAYS` | 106 | `FLOAT` | **60-Day Revenue Amount** - Total revenue generated by Cherry from the referral merchant within  their first 60 days after go-live. Used for extended revenue analysis and growth pattern evaluation.  Sourced from referral_revenue time-windowed calculations.
 | **60-Day Revenue Amount** - Total revenue generated by Cherry from the referral merchant within  their first 60 days after go-live. Used for extended revenue analysis and growth pattern evaluation.  Sourced from referral_revenue time-windowed calculations.
 | `[]` | `{}` |
    | `REVENUE_90_DAYS` | 107 | `FLOAT` | **90-Day Revenue Amount** - Total revenue generated by Cherry from the referral merchant within  their first 90 days after go-live. Used for quarterly revenue analysis and performance evaluation.  Sourced from referral_revenue time-windowed calculations.
 | **90-Day Revenue Amount** - Total revenue generated by Cherry from the referral merchant within  their first 90 days after go-live. Used for quarterly revenue analysis and performance evaluation.  Sourced from referral_revenue time-windowed calculations.
 | `[]` | `{}` |
    | `REVENUE_180_DAYS` | 108 | `FLOAT` | **180-Day Revenue Amount** - Total revenue generated by Cherry from the referral merchant within  their first 180 days after go-live. Used for extended revenue analysis and long-term value calculation.  Sourced from referral_revenue time-windowed calculations.
 | **180-Day Revenue Amount** - Total revenue generated by Cherry from the referral merchant within  their first 180 days after go-live. Used for extended revenue analysis and long-term value calculation.  Sourced from referral_revenue time-windowed calculations.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.all_referrals`
    *   `model.cherry_data_model.referral_cost`
    *   `model.cherry_data_model.referral_payments`
    *   `model.cherry_data_model.referral_qualification`
    *   `model.cherry_data_model.referral_referrers`
    *   `model.cherry_data_model.referral_revenue`

---
