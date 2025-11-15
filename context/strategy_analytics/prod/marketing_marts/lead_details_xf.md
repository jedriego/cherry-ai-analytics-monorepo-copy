## Model: `lead_details_xf`

`lead_details_xf`

*   **Unique ID:** `model.cherry_data_model.lead_details_xf`
*   **FQN:** `prod.marketing_marts.lead_details_xf`
*   **Description:** **Comprehensive Lead Analytics Foundation Table (Legacy Architecture)**
This model serves as Cherry's foundational source for lead-level marketing analytics, combining  Salesforce lead data with comprehensive attribution modeling, cost analysis, and performance  tracking. It provides complete visibility into lead acquisition, conversion, and lifetime value  across Cherry's marketing operations.
**⚠️ Legacy Architecture Notice:** This model represents legacy lead-centric analytics infrastructure. Cherry is transitioning to  account-based marketing analytics as the primary framework. This model will be refactored as  part of the migration away from lead-level analysis toward account-level marketing attribution  and performance measurement.
**Key Business Logic:** - **Lead Integration**: Combines Salesforce lead data with opportunity, account, and merchant information - **Multi-Touch Attribution**: Incorporates sophisticated attribution modeling with viewthrough credit 
  and fractional channel weights across up to 5 channels per lead
- **Cost Attribution**: Calculates attributed marketing costs across Facebook, Google, experimental 
  channels, and referral programs with both attributed and unattributed cost allocation
- **Performance Tracking**: Tracks lead progression through demos, opportunities, go-live, and 
  loan performance with time-based volume calculations
- **Channel Classification**: Legacy channel attribution logic based on UTM codes and lead sources - **Industry Segmentation**: Multi-level industry classification for resource allocation and targeting
**Critical Data Sources:** - `stg_leads`: Core Salesforce lead data with UTM tracking, lead sources, and demographic information - `lead_attribution_with_viewthrough`: Multi-touch attribution with fractional channel weights 
  and viewthrough credit distribution across marketing channels
- `stg_marketing_cost`: Marketing cost attribution combining attributed spend and unattributed 
  cost allocation per lead across channels
- `merchant_loan_totals`: Aggregated loan performance metrics by time periods (14, 30, 60, 90, 120 days) - `lead_channel`: Legacy channel attribution logic based on UTM codes and lead source classification - `prospect_engagement_summary`: Engagement tracking between lead creation and first demo - `lead_demos_summary`: Demo scheduling, completion, and performance metrics - `merchant_lifetime_value`: LTV calculations for merchant performance analysis
**Attribution Methodology:** - First-touch and last-touch engagement attribution with weighted scoring - Multi-channel fractional attribution across up to 5 channels per lead - Viewthrough credit for Google and Facebook advertising with volume-based multipliers - Email engagement attribution with delivery discounting - Referral program attribution with cost reconciliation
**Performance Metrics Coverage:** - Lead acquisition and conversion tracking across marketing channels - Demo scheduling and completion with marketing vs. outbound classification - Go-live conversion and time-to-activation analysis - Loan volume performance in multiple time windows post-go-live - Marketing cost efficiency and ROI calculation - Lifetime value attribution and forecasting
**Primary Use Cases:** - Lead acquisition analysis and channel performance optimization - Marketing attribution and cost per acquisition calculation - Conversion funnel analysis from lead to funded merchant - Industry segment performance and resource allocation - Marketing ROI measurement and budget optimization - Sales team attribution and commission calculation
**External Resources:** - [Guru Documentation](https://app.getguru.com/card/T9AGLxMc/Lead-Details-Table) - Marketing attribution methodology documentation - Cost allocation and budget planning processes

*   **Tags:** `['marketing_analytics', 'marketing', 'leads', 'cohort']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `LEAD_ID` | 1 | `TEXT` | **Salesforce Lead Identifier** - Primary key and unique identifier for the Salesforce lead object.  Critical for lead tracking and joining with other Salesforce objects. Never NULL as this is the  primary key for the model. Sourced from stg_leads.
 | **Salesforce Lead Identifier** - Primary key and unique identifier for the Salesforce lead object.  Critical for lead tracking and joining with other Salesforce objects. Never NULL as this is the  primary key for the model. Sourced from stg_leads.
 | `[]` | `{}` |
    | `SEGMENT_ANONYMOUS_ID` | 2 | `TEXT` | **Segment Anonymous Visitor ID** - Unique identifier from Segment for anonymous website visitors  before lead creation. Used for pre-lead engagement tracking and attribution modeling. Can be NULL  for leads created outside web forms. Sourced from stg_leads.
 | **Segment Anonymous Visitor ID** - Unique identifier from Segment for anonymous website visitors  before lead creation. Used for pre-lead engagement tracking and attribution modeling. Can be NULL  for leads created outside web forms. Sourced from stg_leads.
 | `[]` | `{}` |
    | `FORM_SUBMISSION_ID` | 3 | `TEXT` | **Paperform Submission ID** - Identifier linking lead to specific form submission in Paperform.  Used for form performance analysis and lead source validation. NULL when lead wasn't created  via web form submission. Sourced from stg_leads via form submission matching.
 | **Paperform Submission ID** - Identifier linking lead to specific form submission in Paperform.  Used for form performance analysis and lead source validation. NULL when lead wasn't created  via web form submission. Sourced from stg_leads via form submission matching.
 | `[]` | `{}` |
    | `CONTACT_ID` | 4 | `TEXT` | **Salesforce Contact ID** - Converted contact ID when lead converts to contact in Salesforce.  NULL for unconverted leads. Used for post-conversion tracking and customer journey analysis.  Sourced from stg_leads converted contact mapping.
 | **Salesforce Contact ID** - Converted contact ID when lead converts to contact in Salesforce.  NULL for unconverted leads. Used for post-conversion tracking and customer journey analysis.  Sourced from stg_leads converted contact mapping.
 | `[]` | `{}` |
    | `OPPORTUNITY_ID` | 5 | `TEXT` | **Salesforce Opportunity ID** - Associated sales opportunity ID when lead progresses to opportunity  stage. NULL for leads without opportunities. Critical for sales funnel analysis and conversion  tracking. Sourced from stg_leads opportunity relationship.
 | **Salesforce Opportunity ID** - Associated sales opportunity ID when lead progresses to opportunity  stage. NULL for leads without opportunities. Critical for sales funnel analysis and conversion  tracking. Sourced from stg_leads opportunity relationship.
 | `[]` | `{}` |
    | `ACCOUNT_ID` | 6 | `TEXT` | **Salesforce Account ID** - Associated account ID when lead converts or is linked to existing  account. NULL for unconverted leads without account association. Used for account-level analysis  and customer relationship tracking. Sourced from stg_leads account mapping.
 | **Salesforce Account ID** - Associated account ID when lead converts or is linked to existing  account. NULL for unconverted leads without account association. Used for account-level analysis  and customer relationship tracking. Sourced from stg_leads account mapping.
 | `[]` | `{}` |
    | `MERCHANT_ID` | 7 | `FLOAT` | **Cherry Merchant ID** - Internal Cherry identifier for the practice/merchant. NULL until lead  becomes paying merchant. Essential for loan performance and revenue analysis. Sourced from  stg_leads merchant relationship.
 | **Cherry Merchant ID** - Internal Cherry identifier for the practice/merchant. NULL until lead  becomes paying merchant. Essential for loan performance and revenue analysis. Sourced from  stg_leads merchant relationship.
 | `[]` | `{}` |
    | `REFERRALROCK_REFERRAL_ID` | 8 | `TEXT` | **Referral Rock ID** - Unique identifier from Referral Rock platform for leads from referral  program. NULL for non-referral leads. Used for referral program tracking and cost attribution.  Sourced from stg_leads referral integration.
 | **Referral Rock ID** - Unique identifier from Referral Rock platform for leads from referral  program. NULL for non-referral leads. Used for referral program tracking and cost attribution.  Sourced from stg_leads referral integration.
 | `[]` | `{}` |
    | `REFERRALROCK_EXTERNALID` | 9 | `TEXT` | **Referral Rock External ID** - Additional Referral Rock identifier for cross-platform tracking.  NULL for non-referral leads. Used for referral attribution and reward processing. Sourced from  stg_leads referral data.
 | **Referral Rock External ID** - Additional Referral Rock identifier for cross-platform tracking.  NULL for non-referral leads. Used for referral attribution and reward processing. Sourced from  stg_leads referral data.
 | `[]` | `{}` |
    | `FIRST_CAMPAIGN_ID` | 10 | `TEXT` | **First Campaign ID** - Salesforce campaign ID for the first campaign associated with the lead.  Used for first-touch campaign attribution and source tracking. NULL when no campaigns associated.  Sourced from lead_campaigns with ranking logic.
 | **First Campaign ID** - Salesforce campaign ID for the first campaign associated with the lead.  Used for first-touch campaign attribution and source tracking. NULL when no campaigns associated.  Sourced from lead_campaigns with ranking logic.
 | `[]` | `{}` |
    | `LEAD_CREATED_DATE` | 11 | `TIMESTAMP_NTZ` | **Lead Creation Date (Pacific)** - Pacific Time date when lead was created in Salesforce.  Fundamental timestamp for all lead lifecycle analysis, cohort analysis, and time-based performance  tracking. Never NULL. Sourced from stg_leads Salesforce creation timestamp.
 | **Lead Creation Date (Pacific)** - Pacific Time date when lead was created in Salesforce.  Fundamental timestamp for all lead lifecycle analysis, cohort analysis, and time-based performance  tracking. Never NULL. Sourced from stg_leads Salesforce creation timestamp.
 | `[]` | `{}` |
    | `REGISTERED_DATE` | 12 | `TIMESTAMP_NTZ` | **Best Registration Date** - Most accurate registration date derived from multiple data sources  including Cherry applications, Salesforce data, and form submissions. Uses sophisticated matching  logic across phones, emails, and addresses. Used for attribution timing and conversion analysis.  Sourced from stg_registrations with prioritization logic.
 | **Best Registration Date** - Most accurate registration date derived from multiple data sources  including Cherry applications, Salesforce data, and form submissions. Uses sophisticated matching  logic across phones, emails, and addresses. Used for attribution timing and conversion analysis.  Sourced from stg_registrations with prioritization logic.
 | `[]` | `{}` |
    | `MARKETING_ATTRIBUTABLE_DATE` | 13 | `TIMESTAMP_TZ` | **Marketing Attribution Date** - Date when lead becomes attributable to marketing efforts,  potentially different from creation date. Used for marketing attribution timing and cost allocation.  NULL when not applicable. Sourced from stg_leads marketing attribution logic.
 | **Marketing Attribution Date** - Date when lead becomes attributable to marketing efforts,  potentially different from creation date. Used for marketing attribution timing and cost allocation.  NULL when not applicable. Sourced from stg_leads marketing attribution logic.
 | `[]` | `{}` |
    | `COMMISSION_ELIGIBILITY_START_DATE` | 14 | `DATE` | **Commission Eligibility Date** - Official date when merchant becomes eligible for commissions  and can transact with Cherry. Used for sales attribution and go-live analysis. NULL until  merchant activation. Sourced from stg_leads opportunity/account data.
 | **Commission Eligibility Date** - Official date when merchant becomes eligible for commissions  and can transact with Cherry. Used for sales attribution and go-live analysis. NULL until  merchant activation. Sourced from stg_leads opportunity/account data.
 | `[]` | `{}` |
    | `OPPORTUNITY_CREATED_DATE` | 15 | `TIMESTAMP_TZ` | **Opportunity Creation Date** - Date when Salesforce opportunity was created for the lead.  Used for sales funnel timing analysis and lead-to-opportunity conversion tracking. NULL for  leads without opportunities. Sourced from stg_leads opportunity relationship.
 | **Opportunity Creation Date** - Date when Salesforce opportunity was created for the lead.  Used for sales funnel timing analysis and lead-to-opportunity conversion tracking. NULL for  leads without opportunities. Sourced from stg_leads opportunity relationship.
 | `[]` | `{}` |
    | `ACCOUNT_CREATED_DATE` | 16 | `TIMESTAMP_NTZ` | **Account Creation Date** - Date when Salesforce account was created. Used for account lifecycle  analysis and conversion timing. NULL for unconverted leads. Sourced from stg_leads account  relationship.
 | **Account Creation Date** - Date when Salesforce account was created. Used for account lifecycle  analysis and conversion timing. NULL for unconverted leads. Sourced from stg_leads account  relationship.
 | `[]` | `{}` |
    | `GO_LIVE_DATE` | 17 | `DATE` | **Merchant Go-Live Date** - Best available date when merchant became operational with Cherry.  Uses commission_eligibility_start_date when available, falls back to other relevant dates.  Critical for loan performance timing and merchant activation analysis. Sourced from stg_leads  with fallback logic.
 | **Merchant Go-Live Date** - Best available date when merchant became operational with Cherry.  Uses commission_eligibility_start_date when available, falls back to other relevant dates.  Critical for loan performance timing and merchant activation analysis. Sourced from stg_leads  with fallback logic.
 | `[]` | `{}` |
    | `FIRST_DEMO_SCHEDULE_DATETIME_PT` | 18 | `TIMESTAMP_NTZ` | **First Demo Scheduled Time (Pacific)** - Pacific Time when first demo was scheduled for the lead.  Critical for demo conversion analysis and sales funnel timing. NULL for leads without demos.  Sourced from lead_demos_summary.
 | **First Demo Scheduled Time (Pacific)** - Pacific Time when first demo was scheduled for the lead.  Critical for demo conversion analysis and sales funnel timing. NULL for leads without demos.  Sourced from lead_demos_summary.
 | `[]` | `{}` |
    | `FIRST_DEMO_ACTIVITY_DATETIME_PT` | 19 | `TIMESTAMP_NTZ` | **First Demo Activity Time (Pacific)** - Pacific Time when first demo actually occurred (not just  scheduled). Used for demo completion analysis and sales process effectiveness. NULL for unattended  demos. Sourced from lead_demos_summary.
 | **First Demo Activity Time (Pacific)** - Pacific Time when first demo actually occurred (not just  scheduled). Used for demo completion analysis and sales process effectiveness. NULL for unattended  demos. Sourced from lead_demos_summary.
 | `[]` | `{}` |
    | `FIRST_DEMO_COMPLETED_DATETIME_PT` | 20 | `TIMESTAMP_NTZ` | **First Demo Completion Time (Pacific)** - Pacific Time when first demo was marked as completed.  Used for demo success tracking and conversion analysis. NULL for incomplete demos. Sourced from  lead_demos_summary.
 | **First Demo Completion Time (Pacific)** - Pacific Time when first demo was marked as completed.  Used for demo success tracking and conversion analysis. NULL for incomplete demos. Sourced from  lead_demos_summary.
 | `[]` | `{}` |
    | `LAST_DEMO_SCHEDULE_DATETIME_PT` | 21 | `TIMESTAMP_NTZ` | **Last Demo Scheduled Time (Pacific)** - Pacific Time when most recent demo was scheduled. Used  for lead persistence analysis and follow-up tracking. NULL for leads without demos. Sourced from  lead_demos_summary.
 | **Last Demo Scheduled Time (Pacific)** - Pacific Time when most recent demo was scheduled. Used  for lead persistence analysis and follow-up tracking. NULL for leads without demos. Sourced from  lead_demos_summary.
 | `[]` | `{}` |
    | `LAST_DEMO_ACTIVITY_DATETIME_PT` | 22 | `TIMESTAMP_NTZ` | **Last Demo Activity Time (Pacific)** - Pacific Time when most recent demo occurred. Used for  engagement recency analysis and lead scoring. NULL for leads without completed demos. Sourced  from lead_demos_summary.
 | **Last Demo Activity Time (Pacific)** - Pacific Time when most recent demo occurred. Used for  engagement recency analysis and lead scoring. NULL for leads without completed demos. Sourced  from lead_demos_summary.
 | `[]` | `{}` |
    | `REGISTERED_DATE_SOURCE_FIELD` | 23 | `TEXT` | **Registration Date Source** - Text field explaining which data source was used to determine  the registered_date (e.g., 'Cherry application', 'Salesforce lead', 'Form submission'). Used  for data quality analysis and source validation. Sourced from stg_registrations derivation logic.
 | **Registration Date Source** - Text field explaining which data source was used to determine  the registered_date (e.g., 'Cherry application', 'Salesforce lead', 'Form submission'). Used  for data quality analysis and source validation. Sourced from stg_registrations derivation logic.
 | `[]` | `{}` |
    | `LEAD_OWNER_TYPE` | 24 | `TEXT` | **Lead Owner Type** - Classification of lead owner as 'User' (individual) or 'Queue' (team queue).  Used for ownership analysis and routing effectiveness measurement. Derived from Salesforce owner  ID type detection in stg_leads.
 | **Lead Owner Type** - Classification of lead owner as 'User' (individual) or 'Queue' (team queue).  Used for ownership analysis and routing effectiveness measurement. Derived from Salesforce owner  ID type detection in stg_leads.
 | `[]` | `{}` |
    | `LEAD_OWNER_NAME` | 25 | `TEXT` | **Lead Owner Name** - Name of individual user or queue assigned as lead owner. Used for performance  attribution and territory analysis. Sourced from stg_leads via Salesforce user/queue data.
 | **Lead Owner Name** - Name of individual user or queue assigned as lead owner. Used for performance  attribution and territory analysis. Sourced from stg_leads via Salesforce user/queue data.
 | `[]` | `{}` |
    | `LEAD_OWNER_TEAM` | 26 | `TEXT` | **Lead Owner Team** - Team assignment of the lead owner (e.g., 'Sales Development', 'Account  Executives'). Used for team performance analysis and resource allocation. Sourced from stg_leads  via user team mapping.
 | **Lead Owner Team** - Team assignment of the lead owner (e.g., 'Sales Development', 'Account  Executives'). Used for team performance analysis and resource allocation. Sourced from stg_leads  via user team mapping.
 | `[]` | `{}` |
    | `UTM_SOURCE` | 27 | `TEXT` | **UTM Source Parameter** - Marketing source parameter from URL tracking (e.g., 'google', 'facebook').  Core component of marketing attribution and channel analysis. NULL when no UTM tracking available.  Lowercased for consistency. Sourced from stg_leads UTM field standardization.
 | **UTM Source Parameter** - Marketing source parameter from URL tracking (e.g., 'google', 'facebook').  Core component of marketing attribution and channel analysis. NULL when no UTM tracking available.  Lowercased for consistency. Sourced from stg_leads UTM field standardization.
 | `[]` | `{}` |
    | `LEAD_GEN_PROGRAM` | 28 | `TEXT` | **Lead Generation Program** - Categorizes leads into specific programs: 'Practice Finder'  (practice-finder, suggest-a-provider UTM sources), 'Dental Partner Program', or 'Normal Inbound'.  Used for program-specific performance analysis. Derived from utm_source classification logic.
 | **Lead Generation Program** - Categorizes leads into specific programs: 'Practice Finder'  (practice-finder, suggest-a-provider UTM sources), 'Dental Partner Program', or 'Normal Inbound'.  Used for program-specific performance analysis. Derived from utm_source classification logic.
 | `[]` | `{}` |
    | `UTM_CAMPAIGN` | 29 | `TEXT` | **UTM Campaign Parameter** - Marketing campaign parameter from URL tracking. Used for campaign  performance analysis and ROI measurement. NULL when no UTM tracking. Lowercased for consistency.  Sourced from stg_leads UTM field standardization.
 | **UTM Campaign Parameter** - Marketing campaign parameter from URL tracking. Used for campaign  performance analysis and ROI measurement. NULL when no UTM tracking. Lowercased for consistency.  Sourced from stg_leads UTM field standardization.
 | `[]` | `{}` |
    | `UTM_MEDIUM` | 30 | `TEXT` | **UTM Medium Parameter** - Marketing medium parameter from URL tracking (e.g., 'cpc', 'email').  Used for medium-level performance analysis and channel classification. NULL when no UTM tracking.  Lowercased for consistency. Sourced from stg_leads UTM field standardization.
 | **UTM Medium Parameter** - Marketing medium parameter from URL tracking (e.g., 'cpc', 'email').  Used for medium-level performance analysis and channel classification. NULL when no UTM tracking.  Lowercased for consistency. Sourced from stg_leads UTM field standardization.
 | `[]` | `{}` |
    | `LEAD_SOURCE` | 31 | `TEXT` | **Salesforce Lead Source** - Lead source value manually entered by sales reps in Salesforce.  Used for source attribution and lead quality analysis. Often differs from UTM-based attribution.  Lowercased for consistency. Sourced from stg_leads Salesforce field.
 | **Salesforce Lead Source** - Lead source value manually entered by sales reps in Salesforce.  Used for source attribution and lead quality analysis. Often differs from UTM-based attribution.  Lowercased for consistency. Sourced from stg_leads Salesforce field.
 | `[]` | `{}` |
    | `LEAD_FORM_SOURCE` | 32 | `TEXT` | **Lead Form Source** - Specific form or source where lead was created. Used for form performance  analysis and conversion optimization. NULL for non-form leads. Sourced from stg_leads form  tracking integration.
 | **Lead Form Source** - Specific form or source where lead was created. Used for form performance  analysis and conversion optimization. NULL for non-form leads. Sourced from stg_leads form  tracking integration.
 | `[]` | `{}` |
    | `EMAIL` | 33 | `TEXT` | **Lead Email Address** - Primary email address for the lead. Used for lead matching, communication  tracking, and duplicate detection. Critical for email marketing attribution. Sourced from stg_leads  Salesforce contact information.
 | **Lead Email Address** - Primary email address for the lead. Used for lead matching, communication  tracking, and duplicate detection. Critical for email marketing attribution. Sourced from stg_leads  Salesforce contact information.
 | `[]` | `{}` |
    | `STREET` | 34 | `TEXT` | **Street Address** - Street address of the lead's practice/business. Used for geographic analysis  and territory assignment. Can be NULL. Sourced from stg_leads Salesforce address fields.
 | **Street Address** - Street address of the lead's practice/business. Used for geographic analysis  and territory assignment. Can be NULL. Sourced from stg_leads Salesforce address fields.
 | `[]` | `{}` |
    | `CITY` | 35 | `TEXT` | **City** - City location of the lead's practice/business. Used for geographic analysis and  territory optimization. Can be NULL. Sourced from stg_leads Salesforce address fields.
 | **City** - City location of the lead's practice/business. Used for geographic analysis and  territory optimization. Can be NULL. Sourced from stg_leads Salesforce address fields.
 | `[]` | `{}` |
    | `STATE` | 36 | `TEXT` | **State** - State location of the lead's practice/business. Used for state-level performance  analysis and regulatory compliance. Can be NULL. Sourced from stg_leads Salesforce address fields.
 | **State** - State location of the lead's practice/business. Used for state-level performance  analysis and regulatory compliance. Can be NULL. Sourced from stg_leads Salesforce address fields.
 | `[]` | `{}` |
    | `POSTAL_CODE` | 37 | `TEXT` | **Postal Code** - ZIP/postal code of the lead's practice location. Used for geographic clustering  and market analysis. Can be NULL. Sourced from stg_leads Salesforce address fields.
 | **Postal Code** - ZIP/postal code of the lead's practice location. Used for geographic clustering  and market analysis. Can be NULL. Sourced from stg_leads Salesforce address fields.
 | `[]` | `{}` |
    | `WEBSITE` | 38 | `TEXT` | **Practice Website** - Website URL for the lead's practice/business. Used for business validation  and online presence analysis. Can be NULL. Sourced from stg_leads Salesforce contact information.
 | **Practice Website** - Website URL for the lead's practice/business. Used for business validation  and online presence analysis. Can be NULL. Sourced from stg_leads Salesforce contact information.
 | `[]` | `{}` |
    | `PHONE` | 39 | `TEXT` | **Practice Phone Number** - Primary phone number for the lead's practice/business. Used for  communication tracking and lead matching. Can be NULL. Sourced from stg_leads Salesforce  contact information.
 | **Practice Phone Number** - Primary phone number for the lead's practice/business. Used for  communication tracking and lead matching. Can be NULL. Sourced from stg_leads Salesforce  contact information.
 | `[]` | `{}` |
    | `INDUSTRY` | 40 | `TEXT` | **Lead Industry** - Industry classification from Salesforce lead data. Used for industry-specific  analysis and segmentation. Can be NULL. Sourced from stg_leads Salesforce industry field.
 | **Lead Industry** - Industry classification from Salesforce lead data. Used for industry-specific  analysis and segmentation. Can be NULL. Sourced from stg_leads Salesforce industry field.
 | `[]` | `{}` |
    | `CHERRY_DB_INDUSTRY` | 41 | `TEXT` | **Cherry Database Industry** - Industry classification from Cherry's internal database. Often  more accurate than Salesforce industry field. Used for refined industry analysis. Can be NULL.  Sourced from stg_merchants via merchant relationship.
 | **Cherry Database Industry** - Industry classification from Cherry's internal database. Often  more accurate than Salesforce industry field. Used for refined industry analysis. Can be NULL.  Sourced from stg_merchants via merchant relationship.
 | `[]` | `{}` |
    | `LEAD_INDUSTRY_SEGMENT` | 42 | `TEXT` | **Lead Industry Segment** - Cherry's industry grouping for resource allocation based on lead  data: 'Dental', 'Veterinary', 'Plastic and Cosmetic Surgery', 'Other'. Used for team assignment  and performance analysis. Sourced from stg_leads industry classification logic.
 | **Lead Industry Segment** - Cherry's industry grouping for resource allocation based on lead  data: 'Dental', 'Veterinary', 'Plastic and Cosmetic Surgery', 'Other'. Used for team assignment  and performance analysis. Sourced from stg_leads industry classification logic.
 | `[]` | `{}` |
    | `LEAD_INDUSTRY_SEGMENT_EVALUATION` | 43 | `TEXT` | **Lead Segment Evaluation Logic** - Text explanation of the business rules used to determine  lead_industry_segment. Used for data quality validation and segment logic auditing. Sourced  from stg_leads classification derivation.
 | **Lead Segment Evaluation Logic** - Text explanation of the business rules used to determine  lead_industry_segment. Used for data quality validation and segment logic auditing. Sourced  from stg_leads classification derivation.
 | `[]` | `{}` |
    | `ACCOUNT_INDUSTRY_SEGMENT` | 44 | `TEXT` | **Account Industry Segment** - Industry segment determined from account data when available.  Often more accurate than lead-based classification. Used for account-level industry analysis.  NULL for unconverted leads. Sourced from stg_merchants via account relationship.
 | **Account Industry Segment** - Industry segment determined from account data when available.  Often more accurate than lead-based classification. Used for account-level industry analysis.  NULL for unconverted leads. Sourced from stg_merchants via account relationship.
 | `[]` | `{}` |
    | `ACCOUNT_INDUSTRY_SEGMENT_EVALUATION` | 45 | `TEXT` | **Account Segment Evaluation Logic** - Text explanation of business rules used for account  industry segment classification. Used for segment logic validation. NULL for unconverted leads.  Sourced from stg_merchants classification logic.
 | **Account Segment Evaluation Logic** - Text explanation of business rules used for account  industry segment classification. Used for segment logic validation. NULL for unconverted leads.  Sourced from stg_merchants classification logic.
 | `[]` | `{}` |
    | `INDUSTRY_SEGMENT_COALESCE` | 46 | `TEXT` | **Best Industry Segment** - Preferred industry segment using account data when available,  falling back to lead data. Provides most accurate industry classification for analysis.  Used for unified industry reporting. Derived from coalescing account and lead segments.
 | **Best Industry Segment** - Preferred industry segment using account data when available,  falling back to lead data. Provides most accurate industry classification for analysis.  Used for unified industry reporting. Derived from coalescing account and lead segments.
 | `[]` | `{}` |
    | `CHILIPIPER_BOOKING_STATUS` | 47 | `TEXT` | **ChiliPiper Booking Status** - Status from ChiliPiper scheduling platform for demo booking  workflow. Used for booking funnel analysis and scheduling optimization. NULL when ChiliPiper  not used. Sourced from stg_leads ChiliPiper integration.
 | **ChiliPiper Booking Status** - Status from ChiliPiper scheduling platform for demo booking  workflow. Used for booking funnel analysis and scheduling optimization. NULL when ChiliPiper  not used. Sourced from stg_leads ChiliPiper integration.
 | `[]` | `{}` |
    | `CHILIPIPER_MEETING_TYPE` | 48 | `TEXT` | **ChiliPiper Meeting Type** - Type of meeting requested through ChiliPiper scheduling. Used  for meeting type analysis and resource allocation. NULL when ChiliPiper not used. Sourced  from stg_leads ChiliPiper integration.
 | **ChiliPiper Meeting Type** - Type of meeting requested through ChiliPiper scheduling. Used  for meeting type analysis and resource allocation. NULL when ChiliPiper not used. Sourced  from stg_leads ChiliPiper integration.
 | `[]` | `{}` |
    | `STAGE_NAME` | 49 | `TEXT` | **Opportunity Stage** - Current stage of associated sales opportunity in Salesforce pipeline.  Used for pipeline analysis and conversion tracking. NULL for leads without opportunities.  Sourced from stg_leads opportunity stage relationship.
 | **Opportunity Stage** - Current stage of associated sales opportunity in Salesforce pipeline.  Used for pipeline analysis and conversion tracking. NULL for leads without opportunities.  Sourced from stg_leads opportunity stage relationship.
 | `[]` | `{}` |
    | `REFERRALROCK_MEMBER_URL` | 50 | `TEXT` |  |  | `[]` | `{}` |
    | `REFERRALROCK_MEMBER_CODE` | 51 | `TEXT` |  |  | `[]` | `{}` |
    | `REFERRALROCK_MEMBER_NAME` | 52 | `TEXT` |  |  | `[]` | `{}` |
    | `REFERRING_ACCOUNT` | 53 | `TEXT` |  |  | `[]` | `{}` |
    | `REFERRALROCK_MEMBER_EMAIL` | 54 | `TEXT` |  |  | `[]` | `{}` |
    | `GO_LIVE_DATE_EVALUATION` | 55 | `TEXT` |  |  | `[]` | `{}` |
    | `COMPANY_NAME` | 56 | `TEXT` |  |  | `[]` | `{}` |
    | `FIRST_DEMO_MEETING_TYPE` | 57 | `TEXT` |  |  | `[]` | `{}` |
    | `FIRST_DEMO_OWNER_TEAM` | 58 | `TEXT` |  |  | `[]` | `{}` |
    | `FIRST_CAMPAIGN_NAME` | 59 | `TEXT` |  |  | `[]` | `{}` |
    | `OWNER_ASSIGNMENT_DATETIME_PT` | 60 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `FIRST_OUTBOUND_COMMUNICATION_AFTER_OWNER_ASSIGNMENT_DATETIME_PT` | 61 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `HAS_FORM_SUBMISSION` | 62 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_UPLOADED_LEAD_SOURCE` | 63 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_OUTBOUND_LEAD_SOURCE` | 64 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_MARKETING_LEAD` | 65 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TOTAL_GROSS_AMOUNT` | 66 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_14_GROSS_AMOUNT` | 67 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_30_GROSS_AMOUNT` | 68 | `FLOAT` | **30-Day Loan Volume** - Total gross loan amount funded within first 30 days after merchant  go-live. Key metric for early merchant success and activation analysis. Zero when no early loans.  Measured in USD. Sourced from merchant_loan_totals time-window aggregation.
 | **30-Day Loan Volume** - Total gross loan amount funded within first 30 days after merchant  go-live. Key metric for early merchant success and activation analysis. Zero when no early loans.  Measured in USD. Sourced from merchant_loan_totals time-window aggregation.
 | `[]` | `{}` |
    | `FIRST_60_GROSS_AMOUNT` | 69 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_90_GROSS_AMOUNT` | 70 | `FLOAT` |  |  | `[]` | `{}` |
    | `FIRST_120_GROSS_AMOUNT` | 71 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_30_GROSS_AMOUNT` | 72 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_60_GROSS_AMOUNT` | 73 | `FLOAT` |  |  | `[]` | `{}` |
    | `LAST_90_GROSS_AMOUNT` | 74 | `FLOAT` |  |  | `[]` | `{}` |
    | `MERCHANT_POTENTIAL_SOCIAL` | 75 | `TEXT` |  |  | `[]` | `{}` |
    | `UNDERWRITING_MERCHANT_POTENTIAL` | 76 | `TEXT` |  |  | `[]` | `{}` |
    | `NUMBER_OF_INSTAGRAM_FOLLOWERS` | 77 | `FLOAT` |  |  | `[]` | `{}` |
    | `BUZZBOARD_SOCIAL_SCORE` | 78 | `FLOAT` |  |  | `[]` | `{}` |
    | `IS_OUTBOUND_CALL_LEAD` | 79 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NUMBER_OF_GOOGLE_REVIEWS` | 80 | `FLOAT` |  |  | `[]` | `{}` |
    | `NUMBER_OF_REVIEWS` | 81 | `FLOAT` |  |  | `[]` | `{}` |
    | `NUMBER_OF_EMPLOYEES` | 82 | `NUMBER` |  |  | `[]` | `{}` |
    | `LEAD_EMAIL_ORDER` | 83 | `NUMBER` |  |  | `[]` | `{}` |
    | `LEAD_ACCOUNT_ORDER` | 84 | `NUMBER` |  |  | `[]` | `{}` |
    | `LIFETIME_VALUE` | 85 | `FLOAT` | **Merchant Lifetime Value** - Projected or calculated lifetime value of the merchant to Cherry.  Uses actual performance for established merchants, estimates for new merchants. Used for customer  value analysis and marketing ROI. NULL for non-converted leads. Measured in USD. Sourced from  merchant_lifetime_value calculations. | **Merchant Lifetime Value** - Projected or calculated lifetime value of the merchant to Cherry.  Uses actual performance for established merchants, estimates for new merchants. Used for customer  value analysis and marketing ROI. NULL for non-converted leads. Measured in USD. Sourced from  merchant_lifetime_value calculations. | `[]` | `{}` |
    | `WAS_PROSPECT` | 86 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `DEMOS_SCHEDULED` | 87 | `NUMBER` |  |  | `[]` | `{}` |
    | `FIRST_DEMO_IS_MARKETING_DEMO` | 88 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `QUEUE_NAME_CHILIPIPER` | 89 | `TEXT` |  |  | `[]` | `{}` |
    | `SUBJECT` | 90 | `TEXT` |  |  | `[]` | `{}` |
    | `DAYS_TO_FIRST_DEMO_SCHEDULE` | 91 | `NUMBER` |  |  | `[]` | `{}` |
    | `DAYS_TO_FIRST_DEMO_ACTIVITY` | 92 | `NUMBER` |  |  | `[]` | `{}` |
    | `DAYS_FROM_FIRST_DEMO_SCHEDULE_TO_ACTIVITY` | 93 | `NUMBER` |  |  | `[]` | `{}` |
    | `HAS_DEMO_COMPLETED` | 94 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `HAS_INBOUND_DEMO` | 95 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `HAS_OUTBOUND_DEMO` | 96 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `LEAD_SCORE` | 97 | `FLOAT` |  |  | `[]` | `{}` |
    | `INITIATING_REASON` | 98 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_CONVERTED` | 99 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `DISQUALIFIED_REASON` | 100 | `TEXT` |  |  | `[]` | `{}` |
    | `RECORD_TYPE_ID` | 101 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERNAL_REFERRER_ID` | 102 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERNAL_REFERRER_NAME` | 103 | `TEXT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.enhanced_practice_potential_v2`
    *   `model.cherry_data_model.internal_referral_leads_detailed`
    *   `model.cherry_data_model.lead_campaigns`
    *   `model.cherry_data_model.lead_demos_summary`
    *   `model.cherry_data_model.merchant_lifetime_value`
    *   `model.cherry_data_model.merchant_loan_totals`
    *   `model.cherry_data_model.prospects`
    *   `model.cherry_data_model.src_sf_users`
    *   `model.cherry_data_model.stg_leads`
    *   `model.cherry_data_model.stg_merchants`
    *   `model.cherry_data_model.stg_registrations`
    *   `model.cherry_data_model.what_id_communications_summary`

---
