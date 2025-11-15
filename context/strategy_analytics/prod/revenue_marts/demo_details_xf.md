## Model: `demo_details_xf`

`demo_details_xf`

*   **Unique ID:** `model.cherry_data_model.demo_details_xf`
*   **FQN:** `prod.revenue_marts.demo_details_xf`
*   **Description:** **Comprehensive Demo Details with Practice Context**
This model serves as the single source of truth for demo activities and their associated practice/lead/merchant information.  It combines demo data from Salesforce events, webinars, and calls with comprehensive business context including lead attribution,  merchant details, loan volumes, and registration information.
**Key Use Cases:** - Analyzing demo performance by team, owner, and booking attribution - Tracking lead progression from demo to registration to go-live - Calculating conversion rates and volume metrics by demo type - Understanding the relationship between demo activities and business outcomes
**Data Sources:** - `stg_demos`: Demo events, webinars, and calls from Salesforce - `lead_details_xf`: Comprehensive lead information with marketing attribution - `stg_merchants`: Merchant account details and industry segments - `stg_registrations`: Registration data with various source types - `merchant_loan_totals`: Loan volume metrics by merchant - `src_sf_opportunities`: Opportunity stage and loss reason data
**Grain:** One record per demo event, with associated practice/lead/merchant context

*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `DEMO_ID` | 1 | `TEXT` | Unique identifier for each demo record, generated as a surrogate key from event_id,  campaign_member_id, and task_id to handle different demo types (events, webinars, calls).
 | Unique identifier for each demo record, generated as a surrogate key from event_id,  campaign_member_id, and task_id to handle different demo types (events, webinars, calls).
 | `[]` | `{}` |
    | `EVENT_ID` | 2 | `TEXT` | Salesforce event ID for traditional demos. Only populated for demos originating from  Salesforce events (meetings, phone calls). NULL for webinar or call-based demos.
 | Salesforce event ID for traditional demos. Only populated for demos originating from  Salesforce events (meetings, phone calls). NULL for webinar or call-based demos.
 | `[]` | `{}` |
    | `CAMPAIGN_MEMBER_ID` | 3 | `TEXT` | Salesforce campaign member ID for webinar demos. Only populated for demos originating from  Salesforce campaigns/webinars. NULL for traditional event-based demos.
 | Salesforce campaign member ID for webinar demos. Only populated for demos originating from  Salesforce campaigns/webinars. NULL for traditional event-based demos.
 | `[]` | `{}` |
    | `CAMPAIGN_NAME` | 4 | `TEXT` | Name of the Salesforce campaign for webinar demos. Describes the specific webinar or  campaign that generated the demo lead.
 | Name of the Salesforce campaign for webinar demos. Describes the specific webinar or  campaign that generated the demo lead.
 | `[]` | `{}` |
    | `TASK_ID` | 5 | `TEXT` | Salesforce task ID for call-based demos. Only populated for demos originating from  Salesforce tasks. NULL for event or webinar-based demos.
 | Salesforce task ID for call-based demos. Only populated for demos originating from  Salesforce tasks. NULL for event or webinar-based demos.
 | `[]` | `{}` |
    | `IS_DEMO_EVALUATION` | 6 | `TEXT` | Explanation of why this record is classified as a demo. Based on subject line keywords  ("demo", "cherry phone call"), meeting types, or business logic for first events of  practices that went live.
 | Explanation of why this record is classified as a demo. Based on subject line keywords  ("demo", "cherry phone call"), meeting types, or business logic for first events of  practices that went live.
 | `[]` | `{}` |
    | `DEMO_CREATED_DATETIME_PT` | 7 | `TIMESTAMP_NTZ` | Timestamp when the demo record was created in Salesforce, in Pacific Time. This differs  from the scheduled start time and represents when the demo was booked.
 | Timestamp when the demo record was created in Salesforce, in Pacific Time. This differs  from the scheduled start time and represents when the demo was booked.
 | `[]` | `{}` |
    | `ACTIVITY_DATETIME_PT` | 8 | `TIMESTAMP_NTZ` | Scheduled datetime for the demo activity in Pacific Time. This is when the demo is  scheduled to occur (for events) or when the campaign started (for webinars).
 | Scheduled datetime for the demo activity in Pacific Time. This is when the demo is  scheduled to occur (for events) or when the campaign started (for webinars).
 | `[]` | `{}` |
    | `START_DATETIME_PT` | 9 | `TIMESTAMP_NTZ` | Start datetime for the demo in Pacific Time. For events, this is the scheduled start time.  For webinars, this equals the campaign start date.
 | Start datetime for the demo in Pacific Time. For events, this is the scheduled start time.  For webinars, this equals the campaign start date.
 | `[]` | `{}` |
    | `DURATION_IN_MINUTES` | 10 | `NUMBER` | Duration of the demo in minutes. Only populated for event-based demos. NULL for webinars  and calls where duration is not tracked.
 | Duration of the demo in minutes. Only populated for event-based demos. NULL for webinars  and calls where duration is not tracked.
 | `[]` | `{}` |
    | `INBOUND_OUTBOUND` | 11 | `TEXT` | Classification of whether the demo was inbound (lead came to Cherry) or outbound (Cherry  reached out to a cold prospect). Uses cascading logic based on lead creation method and timing.
 | Classification of whether the demo was inbound (lead came to Cherry) or outbound (Cherry  reached out to a cold prospect). Uses cascading logic based on lead creation method and timing.
 | `[]` | `{}` |
    | `MEETING_TYPE` | 12 | `TEXT` | Type of meeting/demo from ChiliPiper or manual classification. Examples include "Demo",  "Webinar", "Phone Call". Used to categorize the format of the demo.
 | Type of meeting/demo from ChiliPiper or manual classification. Examples include "Demo",  "Webinar", "Phone Call". Used to categorize the format of the demo.
 | `[]` | `{}` |
    | `EVENT_TYPE` | 13 | `TEXT` | Salesforce event type classification. Provides additional context about the nature of the  demo event within Salesforce's event taxonomy.
 | Salesforce event type classification. Provides additional context about the nature of the  demo event within Salesforce's event taxonomy.
 | `[]` | `{}` |
    | `SUBJECT` | 14 | `TEXT` | Subject line of the demo event. Used for demo classification (must contain "demo" or  "cherry phone call"). For webinars, this is the campaign name.
 | Subject line of the demo event. Used for demo classification (must contain "demo" or  "cherry phone call"). For webinars, this is the campaign name.
 | `[]` | `{}` |
    | `DESCRIPTION` | 15 | `TEXT` | Description or additional details about the demo event. For webinars, this is the  campaign description. May contain notes about the demo content or purpose.
 | Description or additional details about the demo event. For webinars, this is the  campaign description. May contain notes about the demo content or purpose.
 | `[]` | `{}` |
    | `LOCATION` | 16 | `TEXT` | Location of the demo event (e.g., phone, video conference, in-person). Only populated  for event-based demos. NULL for webinars and calls.
 | Location of the demo event (e.g., phone, video conference, in-person). Only populated  for event-based demos. NULL for webinars and calls.
 | `[]` | `{}` |
    | `RESPONSE_STATUS` | 17 | `TEXT` | Response status of the demo attendee. Indicates whether the attendee accepted, declined,  or hasn't responded to the demo invitation.
 | Response status of the demo attendee. Indicates whether the attendee accepted, declined,  or hasn't responded to the demo invitation.
 | `[]` | `{}` |
    | `RESCHEDULED_TIMES` | 18 | `FLOAT` | Number of times the demo has been rescheduled. Used to track demo stability and  scheduling challenges. NULL for webinars where rescheduling doesn't apply.
 | Number of times the demo has been rescheduled. Used to track demo stability and  scheduling challenges. NULL for webinars where rescheduling doesn't apply.
 | `[]` | `{}` |
    | `EVENT_DISPOSITION` | 19 | `TEXT` | Final disposition of the demo event (e.g., "Completed", "Cancelled", "No Show").  Used to determine actual demo outcomes versus scheduled demos.
 | Final disposition of the demo event (e.g., "Completed", "Cancelled", "No Show").  Used to determine actual demo outcomes versus scheduled demos.
 | `[]` | `{}` |
    | `IS_CONFIRMED` | 20 | `BOOLEAN` | Boolean flag indicating whether the demo has been confirmed by the attendee.  TRUE when the demo is confirmed, FALSE otherwise.
 | Boolean flag indicating whether the demo has been confirmed by the attendee.  TRUE when the demo is confirmed, FALSE otherwise.
 | `[]` | `{}` |
    | `IS_CANCELED` | 21 | `BOOLEAN` | Boolean flag indicating whether the demo was cancelled. Uses enhanced logic that checks  event_disposition for "Cancelled" and subject line for "Meeting Canceled" in addition to  the original is_canceled flag.
 | Boolean flag indicating whether the demo was cancelled. Uses enhanced logic that checks  event_disposition for "Cancelled" and subject line for "Meeting Canceled" in addition to  the original is_canceled flag.
 | `[]` | `{}` |
    | `IS_NO_SHOW` | 22 | `BOOLEAN` | Boolean flag indicating whether the scheduled demo resulted in a no-show.  TRUE when the attendee didn't appear for the scheduled demo.
 | Boolean flag indicating whether the scheduled demo resulted in a no-show.  TRUE when the attendee didn't appear for the scheduled demo.
 | `[]` | `{}` |
    | `IS_DEMO_COMPLETED` | 23 | `BOOLEAN` | Boolean flag indicating whether the demo was actually completed. TRUE when the demo  occurred as scheduled and was finished successfully.
 | Boolean flag indicating whether the demo was actually completed. TRUE when the demo  occurred as scheduled and was finished successfully.
 | `[]` | `{}` |
    | `IS_MULTILOCATION` | 24 | `BOOLEAN` | Boolean flag indicating whether the demo is for a multi-location practice.  Used to identify practices with multiple office locations.
 | Boolean flag indicating whether the demo is for a multi-location practice.  Used to identify practices with multiple office locations.
 | `[]` | `{}` |
    | `IS_TRADESHOW` | 25 | `BOOLEAN` | Boolean flag indicating whether the demo originated from a tradeshow or industry event.  Used to track lead generation from in-person marketing events.
 | Boolean flag indicating whether the demo originated from a tradeshow or industry event.  Used to track lead generation from in-person marketing events.
 | `[]` | `{}` |
    | `IS_PRIMARY_DEMO` | 26 | `BOOLEAN` | Boolean flag indicating whether this is the primary demo for the practice. Uses complex  logic prioritizing Sales Development completed demos, then any completed demos, then most recent demo.
 | Boolean flag indicating whether this is the primary demo for the practice. Uses complex  logic prioritizing Sales Development completed demos, then any completed demos, then most recent demo.
 | `[]` | `{}` |
    | `IS_MOST_RECENT_DEMO` | 27 | `BOOLEAN` | Boolean flag indicating whether this is the most recent demo for the practice.  TRUE for the demo with the latest start_datetime_pt per practice.
 | Boolean flag indicating whether this is the most recent demo for the practice.  TRUE for the demo with the latest start_datetime_pt per practice.
 | `[]` | `{}` |
    | `LAST_MODIFIED_DATETIME_PT` | 28 | `TIMESTAMP_NTZ` | Timestamp when the demo record was last modified in Salesforce, in Pacific Time.  Used to track recent changes to demo information.
 | Timestamp when the demo record was last modified in Salesforce, in Pacific Time.  Used to track recent changes to demo information.
 | `[]` | `{}` |
    | `LEAD_DEMO_ORDER` | 29 | `NUMBER` | Sequential number indicating the order of demos for a specific lead (1 = first demo, 2 = second demo, etc.).  Used to analyze lead engagement patterns and demo frequency.
 | Sequential number indicating the order of demos for a specific lead (1 = first demo, 2 = second demo, etc.).  Used to analyze lead engagement patterns and demo frequency.
 | `[]` | `{}` |
    | `IS_SELF_SET` | 30 | `BOOLEAN` | Boolean flag indicating whether the demo was self-scheduled by the lead (typically through  an online booking system like ChiliPiper) versus being scheduled by a sales representative.
 | Boolean flag indicating whether the demo was self-scheduled by the lead (typically through  an online booking system like ChiliPiper) versus being scheduled by a sales representative.
 | `[]` | `{}` |
    | `IS_INBOUND` | 31 | `BOOLEAN` | Boolean flag indicating whether the demo request came from an inbound lead.  Determined by lead source and booking method analysis.
 | Boolean flag indicating whether the demo request came from an inbound lead.  Determined by lead source and booking method analysis.
 | `[]` | `{}` |
    | `DEMO_OWNER_ID` | 32 | `TEXT` | Salesforce user ID of the person who owns/conducted the demo. This is typically the  sales representative or account executive assigned to conduct the demo.
 | Salesforce user ID of the person who owns/conducted the demo. This is typically the  sales representative or account executive assigned to conduct the demo.
 | `[]` | `{}` |
    | `DEMO_OWNER_NAME` | 33 | `TEXT` | Full name of the person who owns/conducted the demo. Used for performance tracking  and assignment analysis.
 | Full name of the person who owns/conducted the demo. Used for performance tracking  and assignment analysis.
 | `[]` | `{}` |
    | `DEMO_OWNER_TITLE` | 34 | `TEXT` | Job title of the demo owner. Examples include "Account Executive", "Sales Development Representative",  "Senior Account Executive". Used for role-based performance analysis.
 | Job title of the demo owner. Examples include "Account Executive", "Sales Development Representative",  "Senior Account Executive". Used for role-based performance analysis.
 | `[]` | `{}` |
    | `DEMO_OWNER_TEAM` | 35 | `TEXT` | Team assignment of the demo owner. Examples include "Sales Development", "Account Executives",  "Marketing". Used for team-based performance tracking.
 | Team assignment of the demo owner. Examples include "Sales Development", "Account Executives",  "Marketing". Used for team-based performance tracking.
 | `[]` | `{}` |
    | `DEMO_OWNER_SUBTEAM` | 36 | `TEXT` | Subteam assignment of the demo owner within their main team. Provides more granular  team organization for performance analysis.
 | Subteam assignment of the demo owner within their main team. Provides more granular  team organization for performance analysis.
 | `[]` | `{}` |
    | `DEMO_OWNER_DEPARTMENT` | 37 | `TEXT` | Department assignment of the demo owner. Higher-level organizational grouping than team,  used for departmental performance analysis.
 | Department assignment of the demo owner. Higher-level organizational grouping than team,  used for departmental performance analysis.
 | `[]` | `{}` |
    | `BOOKED_BY_ID` | 38 | `TEXT` | Salesforce user ID of the person who booked/scheduled the demo. This may differ from  the demo owner if someone else (like an SDR) books demos for account executives.
 | Salesforce user ID of the person who booked/scheduled the demo. This may differ from  the demo owner if someone else (like an SDR) books demos for account executives.
 | `[]` | `{}` |
    | `BOOKED_BY_NAME` | 39 | `TEXT` | Full name of the person who booked the demo. Used to track who is responsible for  demo scheduling and lead conversion.
 | Full name of the person who booked the demo. Used to track who is responsible for  demo scheduling and lead conversion.
 | `[]` | `{}` |
    | `BOOKED_BY_TITLE` | 40 | `TEXT` | Job title of the person who booked the demo. Used to understand which roles are  most effective at booking demos.
 | Job title of the person who booked the demo. Used to understand which roles are  most effective at booking demos.
 | `[]` | `{}` |
    | `BOOKED_BY_TEAM` | 41 | `TEXT` | Team assignment of the person who booked the demo. Used for team-based booking  performance analysis and attribution.
 | Team assignment of the person who booked the demo. Used for team-based booking  performance analysis and attribution.
 | `[]` | `{}` |
    | `BOOKED_BY_SUBTEAM` | 42 | `TEXT` | Subteam assignment of the person who booked the demo. Provides granular team  organization for booking performance analysis.
 | Subteam assignment of the person who booked the demo. Provides granular team  organization for booking performance analysis.
 | `[]` | `{}` |
    | `BOOKED_BY_DEPARTMENT` | 43 | `TEXT` | Department assignment of the person who booked the demo. Used for departmental  booking performance analysis.
 | Department assignment of the person who booked the demo. Used for departmental  booking performance analysis.
 | `[]` | `{}` |
    | `BOOKED_BY_CATEGORY` | 44 | `TEXT` | Categorical attribution of demo booking to specific sources/teams. Examples include  "Sales Development", "Marketing", "Account Executive". Used for high-level attribution analysis.
 | Categorical attribution of demo booking to specific sources/teams. Examples include  "Sales Development", "Marketing", "Account Executive". Used for high-level attribution analysis.
 | `[]` | `{}` |
    | `LEAD_ID` | 45 | `TEXT` | Salesforce lead ID associated with the demo. Links to the lead record that generated  the demo opportunity. May be NULL for demos linked only to accounts.
 | Salesforce lead ID associated with the demo. Links to the lead record that generated  the demo opportunity. May be NULL for demos linked only to accounts.
 | `[]` | `{}` |
    | `CONTACT_ID` | 46 | `TEXT` | Salesforce contact ID associated with the demo. Present when the lead has been converted  to a contact record in Salesforce.
 | Salesforce contact ID associated with the demo. Present when the lead has been converted  to a contact record in Salesforce.
 | `[]` | `{}` |
    | `OPPORTUNITY_ID` | 47 | `TEXT` | Salesforce opportunity ID associated with the demo. Links to the sales opportunity  record, coalesced from merchant or lead opportunity IDs.
 | Salesforce opportunity ID associated with the demo. Links to the sales opportunity  record, coalesced from merchant or lead opportunity IDs.
 | `[]` | `{}` |
    | `ACCOUNT_ID` | 48 | `TEXT` | Salesforce account ID associated with the demo. Links to the account record,  coalesced from demo or lead account IDs.
 | Salesforce account ID associated with the demo. Links to the account record,  coalesced from demo or lead account IDs.
 | `[]` | `{}` |
    | `MERCHANT_ID` | 49 | `FLOAT` | Cherry merchant ID associated with the demo. Links to the internal merchant record,  coalesced from lead or merchant data.
 | Cherry merchant ID associated with the demo. Links to the internal merchant record,  coalesced from lead or merchant data.
 | `[]` | `{}` |
    | `SALESFORCE_URL` | 50 | `TEXT` | Direct URL to the Salesforce account record for this demo. Constructed as a deep link  to the account view in Salesforce Lightning interface.
 | Direct URL to the Salesforce account record for this demo. Constructed as a deep link  to the account view in Salesforce Lightning interface.
 | `[]` | `{}` |
    | `LEAD_CREATED_DATE` | 51 | `TIMESTAMP_NTZ` | Date when the associated lead was created in Salesforce. Used to calculate time from  lead creation to demo and measure lead velocity.
 | Date when the associated lead was created in Salesforce. Used to calculate time from  lead creation to demo and measure lead velocity.
 | `[]` | `{}` |
    | `OPPORTUNITY_CREATED_DATE` | 52 | `TIMESTAMP_TZ` | Date when the associated opportunity was created in Salesforce. Used to track sales  pipeline progression and opportunity management.
 | Date when the associated opportunity was created in Salesforce. Used to track sales  pipeline progression and opportunity management.
 | `[]` | `{}` |
    | `ACCOUNT_CREATED_DATE` | 53 | `TIMESTAMP_NTZ` | Date when the associated account was created in Salesforce. Used for account lifecycle  analysis and segmentation.
 | Date when the associated account was created in Salesforce. Used for account lifecycle  analysis and segmentation.
 | `[]` | `{}` |
    | `COMPANY_NAME` | 54 | `TEXT` | Name of the practice or company associated with the demo. Coalesced from lead company  name or merchant name to provide the most complete practice identification.
 | Name of the practice or company associated with the demo. Coalesced from lead company  name or merchant name to provide the most complete practice identification.
 | `[]` | `{}` |
    | `OWNER_NAME` | 55 | `TEXT` | Name of the lead owner or account executive responsible for the practice. Coalesced  from lead owner or merchant account executive.
 | Name of the lead owner or account executive responsible for the practice. Coalesced  from lead owner or merchant account executive.
 | `[]` | `{}` |
    | `OWNER_TEAM` | 56 | `TEXT` | Team assignment of the practice owner. Coalesced from lead owner team or merchant  account executive team.
 | Team assignment of the practice owner. Coalesced from lead owner team or merchant  account executive team.
 | `[]` | `{}` |
    | `UTM_SOURCE` | 57 | `TEXT` | UTM source parameter from the lead's marketing attribution. Indicates the marketing  source that generated the lead (e.g., Google, Facebook, Direct).
 | UTM source parameter from the lead's marketing attribution. Indicates the marketing  source that generated the lead (e.g., Google, Facebook, Direct).
 | `[]` | `{}` |
    | `UTM_CAMPAIGN` | 58 | `TEXT` | UTM campaign parameter from the lead's marketing attribution. Indicates the specific  marketing campaign that generated the lead.
 | UTM campaign parameter from the lead's marketing attribution. Indicates the specific  marketing campaign that generated the lead.
 | `[]` | `{}` |
    | `UTM_MEDIUM` | 59 | `TEXT` | UTM medium parameter from the lead's marketing attribution. Indicates the marketing  medium used (e.g., CPC, email, social).
 | UTM medium parameter from the lead's marketing attribution. Indicates the marketing  medium used (e.g., CPC, email, social).
 | `[]` | `{}` |
    | `LEAD_SOURCE` | 60 | `TEXT` | Lead source as recorded in Salesforce. Indicates how the lead was generated or  acquired (e.g., web form, referral, cold call).
 | Lead source as recorded in Salesforce. Indicates how the lead was generated or  acquired (e.g., web form, referral, cold call).
 | `[]` | `{}` |
    | `EMAIL` | 61 | `TEXT` | Email address of the lead contact. Primary contact method for communication and  marketing follow-up.
 | Email address of the lead contact. Primary contact method for communication and  marketing follow-up.
 | `[]` | `{}` |
    | `STREET` | 62 | `TEXT` | Street address of the practice. Coalesced from lead street address or merchant  address line one.
 | Street address of the practice. Coalesced from lead street address or merchant  address line one.
 | `[]` | `{}` |
    | `CITY` | 63 | `TEXT` | City where the practice is located. Coalesced from lead city or merchant city name.
 | City where the practice is located. Coalesced from lead city or merchant city name.
 | `[]` | `{}` |
    | `STATE` | 64 | `TEXT` | State where the practice is located. Coalesced from lead state or merchant state  abbreviation.
 | State where the practice is located. Coalesced from lead state or merchant state  abbreviation.
 | `[]` | `{}` |
    | `POSTAL_CODE` | 65 | `TEXT` | Postal code of the practice location. Coalesced from lead postal code or merchant  zipcode.
 | Postal code of the practice location. Coalesced from lead postal code or merchant  zipcode.
 | `[]` | `{}` |
    | `INDUSTRY` | 66 | `TEXT` | Industry classification of the practice. Coalesced from lead industry or merchant  Salesforce industry field.
 | Industry classification of the practice. Coalesced from lead industry or merchant  Salesforce industry field.
 | `[]` | `{}` |
    | `CHERRY_DB_INDUSTRY` | 67 | `TEXT` | Industry classification from Cherry's internal database. Coalesced from lead or  merchant Cherry DB industry fields.
 | Industry classification from Cherry's internal database. Coalesced from lead or  merchant Cherry DB industry fields.
 | `[]` | `{}` |
    | `LEAD_INDUSTRY_SEGMENT` | 68 | `TEXT` | Industry segment classification derived from lead-level data. Used for lead-specific  industry segmentation and resource allocation.
 | Industry segment classification derived from lead-level data. Used for lead-specific  industry segmentation and resource allocation.
 | `[]` | `{}` |
    | `ACCOUNT_INDUSTRY_SEGMENT` | 69 | `TEXT` | Industry segment classification derived from account-level data. Used for account-specific  industry segmentation and resource allocation.
 | Industry segment classification derived from account-level data. Used for account-specific  industry segmentation and resource allocation.
 | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 70 | `TEXT` | Final industry segment classification. Coalesced from lead industry segment coalesce  or merchant account industry segment, providing the most complete industry classification.
 | Final industry segment classification. Coalesced from lead industry segment coalesce  or merchant account industry segment, providing the most complete industry classification.
 | `[]` | `{}` |
    | `STAGE_NAME` | 71 | `TEXT` | Current stage of the associated opportunity. Coalesced from opportunity stage or lead  stage name. Indicates where the practice is in the sales pipeline.
 | Current stage of the associated opportunity. Coalesced from opportunity stage or lead  stage name. Indicates where the practice is in the sales pipeline.
 | `[]` | `{}` |
    | `REGISTRATION_DATE` | 72 | `TIMESTAMP_NTZ` | Date when the practice registered with Cherry. Coalesced from lead or account registration  dates, representing the earliest registration interaction.
 | Date when the practice registered with Cherry. Coalesced from lead or account registration  dates, representing the earliest registration interaction.
 | `[]` | `{}` |
    | `GO_LIVE_DATE` | 73 | `DATE` | Date when the practice went live and became eligible to transact with Cherry.  Coalesced from lead or merchant go-live dates.
 | Date when the practice went live and became eligible to transact with Cherry.  Coalesced from lead or merchant go-live dates.
 | `[]` | `{}` |
    | `ACTIVATION_DATE` | 74 | `DATE` | Date when the practice first funded a loan, representing their first active use of  Cherry's financing platform.
 | Date when the practice first funded a loan, representing their first active use of  Cherry's financing platform.
 | `[]` | `{}` |
    | `GO_LIVE_DATE_EVALUATION` | 75 | `TEXT` | Explanation of how the go_live_date was determined. Provides context about the data  source and methodology used to establish the go-live date.
 | Explanation of how the go_live_date was determined. Provides context about the data  source and methodology used to establish the go-live date.
 | `[]` | `{}` |
    | `TOTAL_GROSS_AMOUNT` | 76 | `FLOAT` | Total gross loan amount for the practice to date. Coalesced from lead or merchant  loan totals to provide complete financial performance.
 | Total gross loan amount for the practice to date. Coalesced from lead or merchant  loan totals to provide complete financial performance.
 | `[]` | `{}` |
    | `FIRST_14_GROSS_AMOUNT` | 77 | `FLOAT` | Gross loan amount in the first 14 days after go-live. Used to measure early practice  adoption and initial success.
 | Gross loan amount in the first 14 days after go-live. Used to measure early practice  adoption and initial success.
 | `[]` | `{}` |
    | `FIRST_30_GROSS_AMOUNT` | 78 | `FLOAT` | Gross loan amount in the first 30 days after go-live. Key metric for early practice  performance and onboarding success.
 | Gross loan amount in the first 30 days after go-live. Key metric for early practice  performance and onboarding success.
 | `[]` | `{}` |
    | `FIRST_60_GROSS_AMOUNT` | 79 | `FLOAT` | Gross loan amount in the first 60 days after go-live. Used for medium-term practice  performance analysis.
 | Gross loan amount in the first 60 days after go-live. Used for medium-term practice  performance analysis.
 | `[]` | `{}` |
    | `FIRST_90_GROSS_AMOUNT` | 80 | `FLOAT` | Gross loan amount in the first 90 days after go-live. Standard quarterly performance  metric for new practices.
 | Gross loan amount in the first 90 days after go-live. Standard quarterly performance  metric for new practices.
 | `[]` | `{}` |
    | `FIRST_120_GROSS_AMOUNT` | 81 | `FLOAT` | Gross loan amount in the first 120 days after go-live. Extended quarterly performance  metric for practice maturity analysis.
 | Gross loan amount in the first 120 days after go-live. Extended quarterly performance  metric for practice maturity analysis.
 | `[]` | `{}` |
    | `LAST_30_GROSS_AMOUNT` | 82 | `FLOAT` | Gross loan amount in the last 30 days. Used to measure current practice activity  and recent performance trends.
 | Gross loan amount in the last 30 days. Used to measure current practice activity  and recent performance trends.
 | `[]` | `{}` |
    | `LAST_60_GROSS_AMOUNT` | 83 | `FLOAT` | Gross loan amount in the last 60 days. Used for medium-term current performance  analysis and trend identification.
 | Gross loan amount in the last 60 days. Used for medium-term current performance  analysis and trend identification.
 | `[]` | `{}` |
    | `LAST_90_GROSS_AMOUNT` | 84 | `FLOAT` | Gross loan amount in the last 90 days. Used for quarterly current performance  analysis and health scoring.
 | Gross loan amount in the last 90 days. Used for quarterly current performance  analysis and health scoring.
 | `[]` | `{}` |
    | `NUMBER_OF_INSTAGRAM_FOLLOWERS` | 85 | `FLOAT` | Number of Instagram followers for the practice. Used to assess social media presence  and potential for marketing success.
 | Number of Instagram followers for the practice. Used to assess social media presence  and potential for marketing success.
 | `[]` | `{}` |
    | `NUMBER_OF_GOOGLE_REVIEWS` | 86 | `FLOAT` | Number of Google reviews for the practice. Used to assess online reputation and  customer satisfaction levels.
 | Number of Google reviews for the practice. Used to assess online reputation and  customer satisfaction levels.
 | `[]` | `{}` |
    | `NUMBER_OF_REVIEWS` | 87 | `FLOAT` | Total number of online reviews for the practice (includes Google and other platforms).  Used for comprehensive reputation analysis.
 | Total number of online reviews for the practice (includes Google and other platforms).  Used for comprehensive reputation analysis.
 | `[]` | `{}` |
    | `NUMBER_OF_EMPLOYEES` | 88 | `NUMBER` | Number of employees at the practice. Used to assess practice size and potential  financing volume.
 | Number of employees at the practice. Used to assess practice size and potential  financing volume.
 | `[]` | `{}` |
    | `REFERRALROCK_MEMBER_URL` | 89 | `TEXT` | URL for the practice's ReferralRock member profile. Used to track referral program  participation and performance.
 | URL for the practice's ReferralRock member profile. Used to track referral program  participation and performance.
 | `[]` | `{}` |
    | `REFERRALROCK_MEMBER_CODE` | 90 | `TEXT` | Unique referral code for the practice in ReferralRock. Used to track referral  attribution and program effectiveness.
 | Unique referral code for the practice in ReferralRock. Used to track referral  attribution and program effectiveness.
 | `[]` | `{}` |
    | `REFERRALROCK_EXTERNALID` | 91 | `TEXT` | External ID for the practice in ReferralRock system. Used for system integration  and referral tracking.
 | External ID for the practice in ReferralRock system. Used for system integration  and referral tracking.
 | `[]` | `{}` |
    | `REFERRALROCK_MEMBER_NAME` | 92 | `TEXT` | Practice name as recorded in ReferralRock. Used for referral program management  and tracking.
 | Practice name as recorded in ReferralRock. Used for referral program management  and tracking.
 | `[]` | `{}` |
    | `REFERRALROCK_MEMBER_EMAIL` | 93 | `TEXT` | Email address for the practice in ReferralRock. Used for referral program  communication and tracking.
 | Email address for the practice in ReferralRock. Used for referral program  communication and tracking.
 | `[]` | `{}` |
    | `REFERRING_ACCOUNT` | 94 | `TEXT` | Account that referred this practice to Cherry. Used for referral attribution  and program performance analysis.
 | Account that referred this practice to Cherry. Used for referral attribution  and program performance analysis.
 | `[]` | `{}` |
    | `LEAD_SCORE` | 95 | `FLOAT` | Calculated lead score based on various lead characteristics and behaviors. Used for  lead prioritization and qualification.
 | Calculated lead score based on various lead characteristics and behaviors. Used for  lead prioritization and qualification.
 | `[]` | `{}` |
    | `INITIATING_REASON` | 96 | `TEXT` | Reason that initiated the lead creation or demo request. Used to understand lead  motivation and qualification.
 | Reason that initiated the lead creation or demo request. Used to understand lead  motivation and qualification.
 | `[]` | `{}` |
    | `FIRST_CAMPAIGN_ID` | 97 | `TEXT` | ID of the first marketing campaign associated with the lead. Used for campaign  attribution and performance analysis.
 | ID of the first marketing campaign associated with the lead. Used for campaign  attribution and performance analysis.
 | `[]` | `{}` |
    | `FIRST_CAMPAIGN_NAME` | 98 | `TEXT` | Name of the first marketing campaign associated with the lead. Used for campaign  attribution and performance analysis.
 | Name of the first marketing campaign associated with the lead. Used for campaign  attribution and performance analysis.
 | `[]` | `{}` |
    | `LOSS_REASON` | 99 | `TEXT` | Reason for opportunity loss if the opportunity was closed lost. Provides insight into  why practices don't convert after demos.
 | Reason for opportunity loss if the opportunity was closed lost. Provides insight into  why practices don't convert after demos.
 | `[]` | `{}` |
    | `LAST_ACTIVITY_DATE` | 100 | `DATE` | Date of the last activity on the associated opportunity. Used to track engagement  recency and identify stale opportunities.
 | Date of the last activity on the associated opportunity. Used to track engagement  recency and identify stale opportunities.
 | `[]` | `{}` |
    | `ESTIMATED_MONTHLY_FINANCING_QUARTILE` | 101 | `TEXT` | Quartile classification of the practice's estimated monthly financing potential from  mystery shopping data. Used for practice potential assessment and resource allocation.
 | Quartile classification of the practice's estimated monthly financing potential from  mystery shopping data. Used for practice potential assessment and resource allocation.
 | `[]` | `{}` |
    | `INITIAL_LOOK_ASSESSMENT` | 102 | `TEXT` | Initial look assessment classification for practices in key industry segments (Dental,  MedSpa, Plastic Surgery, Veterinary) at the time of demo or within 60 days of go-live.
 | Initial look assessment classification for practices in key industry segments (Dental,  MedSpa, Plastic Surgery, Veterinary) at the time of demo or within 60 days of go-live.
 | `[]` | `{}` |
    | `LATEST_LOOK_ASSESSMENT` | 103 | `TEXT` | Most recent look assessment classification for practices in key industry segments,  current as of the demo date or current date if later.
 | Most recent look assessment classification for practices in key industry segments,  current as of the demo date or current date if later.
 | `[]` | `{}` |
    | `INTERNAL_REFERRER_ID` | 104 | `TEXT` | ID of the internal Cherry employee who referred this practice. Coalesced from merchant  or lead internal referrer IDs, used for internal referral tracking and attribution. | ID of the internal Cherry employee who referred this practice. Coalesced from merchant  or lead internal referrer IDs, used for internal referral tracking and attribution. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.lead_details_xf`
    *   `model.cherry_data_model.loan_info_xf`
    *   `model.cherry_data_model.look_assessment_history`
    *   `model.cherry_data_model.merchant_loan_totals`
    *   `model.cherry_data_model.src_sf_opportunities`
    *   `model.cherry_data_model.stg_demos`
    *   `model.cherry_data_model.stg_merchants`
    *   `model.cherry_data_model.stg_mystery_shopping`

---
