## Model: `practice_milestones_xf`

`practice_milestones_xf`

*   **Unique ID:** `model.cherry_data_model.practice_milestones_xf`
*   **FQN:** `prod.revenue_marts.practice_milestones_xf`
*   **Description:** **Customer Journey Milestone Tracking and Attribution**
This model provides comprehensive longitudinal tracking of prospect progression through key customer  journey milestones, from initial qualified opportunity through final activation. It transforms wide  milestone data into a long format to enable granular analysis of conversion rates, stage duration,  and bottleneck identification across the sales and onboarding process.
**Key Business Logic:** - **Chronological Consistency**: Uses sophisticated `least_ignore_nulls` logic to ensure milestone dates 
  are chronologically consistent, preventing data quality issues where later milestones could appear 
  before earlier ones
- **Attribution Integration**: Combines prospect attribution data with demo attribution, internal referral 
  tracking, and account executive ownership for comprehensive attribution analysis
- **Milestone Date Calculation**: For each milestone, calculates the earliest valid date from multiple 
  data sources, ensuring completeness while maintaining temporal integrity
- **Long Format Transformation**: Uses `unpivot` to transform 9 milestone columns into individual rows, 
  enabling flexible stage-by-stage analysis and progression tracking

**Milestone Journey Tracked:** 1. **Qualified Opportunity** - Initial prospect qualification and sales engagement 2. **Scheduled Demo** - First demo booking activity 3. **Completed Demo** - Successful demo completion 4. **Registration Start** - Beginning of formal registration process 5. **Registration** - Completed registration with Cherry systems 6. **Underwriting Approval** - Approval for merchant account creation 7. **Onboarding** - Practice setup and implementation phase 8. **Go-Live** - Practice actively using Cherry for patient transactions 9. **Activation** - First contract execution and full platform utilization
**Primary Use Cases:** - Conversion funnel analysis across all customer journey stages - Stage duration analysis and bottleneck identification - Attribution reporting for marketing, sales, and business development - Account executive performance analysis and territory planning - Internal referral tracking and Practice Development team attribution - Customer success milestone reporting and SLA monitoring
**Data Sources:** - `prospect_attribution_summary` - Core prospect data and attribution sources - `demo_details_xf` - Demo scheduling and completion activities - `registration_start` & `stg_registrations_new` - Registration milestone data - `practice_info_full_xf` - Practice onboarding and activation information - `internal_referral_leads_detailed` & `internal_referral_go_lives_detailed` - Internal referral attribution - Various Salesforce objects for ownership and opportunity data

*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `UNIQUE_ID` | 1 | `TEXT` | Primary unique identifier for each prospect, representing either an account_id or lead_id  depending on the prospect type. Serves as the grain for milestone tracking.
 | Primary unique identifier for each prospect, representing either an account_id or lead_id  depending on the prospect type. Serves as the grain for milestone tracking.
 | `[]` | `{}` |
    | `ACCOUNT_ID` | 2 | `TEXT` | Salesforce account ID for prospects that have progressed to account status. NULL for  lead-only prospects who haven't converted to accounts yet.
 | Salesforce account ID for prospects that have progressed to account status. NULL for  lead-only prospects who haven't converted to accounts yet.
 | `[]` | `{}` |
    | `LEAD_ID` | 3 | `TEXT` | Salesforce lead ID for the prospect. Present for all prospects that originated as leads,  may persist even after account conversion for attribution tracking.
 | Salesforce lead ID for the prospect. Present for all prospects that originated as leads,  may persist even after account conversion for attribution tracking.
 | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 4 | `TEXT` | Industry segment classification for the prospect (e.g., 'Dental', 'MedSpa',  'Plastic and Cosmetic Surgery', 'Veterinary'). Used for segment-specific analysis and  performance tracking across different practice types.
 | Industry segment classification for the prospect (e.g., 'Dental', 'MedSpa',  'Plastic and Cosmetic Surgery', 'Veterinary'). Used for segment-specific analysis and  performance tracking across different practice types.
 | `[]` | `{}` |
    | `QUALIFIED_OPPORTUNITY_SOURCE` | 5 | `TEXT` | Attribution source for the qualified opportunity milestone, indicating which team or channel  was responsible for initial prospect qualification (e.g., 'Sales', 'Marketing', 'Sales Development',  'Business Development', 'Alle').
 | Attribution source for the qualified opportunity milestone, indicating which team or channel  was responsible for initial prospect qualification (e.g., 'Sales', 'Marketing', 'Sales Development',  'Business Development', 'Alle').
 | `[]` | `{}` |
    | `FIRST_SCHEDULED_DEMO_SOURCE` | 6 | `TEXT` | Attribution source for the first scheduled demo milestone, identifying which team or channel  was responsible for the initial demo booking activity.
 | Attribution source for the first scheduled demo milestone, identifying which team or channel  was responsible for the initial demo booking activity.
 | `[]` | `{}` |
    | `PRIMARY_DEMO_SOURCE` | 7 | `TEXT` | Attribution source for the primary (typically completed) demo milestone, indicating which  team or channel conducted the main demo presentation.
 | Attribution source for the primary (typically completed) demo milestone, indicating which  team or channel conducted the main demo presentation.
 | `[]` | `{}` |
    | `GO_LIVE_SOURCE` | 8 | `TEXT` | Attribution source for the go-live milestone, identifying which team or channel was  responsible for bringing the practice to active transaction status.
 | Attribution source for the go-live milestone, identifying which team or channel was  responsible for bringing the practice to active transaction status.
 | `[]` | `{}` |
    | `IS_SELF_SET` | 9 | `BOOLEAN` | **[DEPRECATED]** Legacy field indicating whether the demo was self-scheduled by the prospect.  Being phased out in favor of more comprehensive attribution tracking through source fields.
 | **[DEPRECATED]** Legacy field indicating whether the demo was self-scheduled by the prospect.  Being phased out in favor of more comprehensive attribution tracking through source fields.
 | `[]` | `{}` |
    | `DEMO_ATTRIBUTION` | 10 | `TEXT` | **[DEPRECATED]** Legacy demo attribution field (Marketing/Sales/Unknown). Being replaced  by more granular attribution source tracking in the dedicated source fields.
 | **[DEPRECATED]** Legacy demo attribution field (Marketing/Sales/Unknown). Being replaced  by more granular attribution source tracking in the dedicated source fields.
 | `[]` | `{}` |
    | `ALLE_DEMO_SUBJECT` | 11 | `BOOLEAN` | **[DEPRECATED]** Legacy field indicating if the demo subject contained Alle/Allē references.  Used for historical analysis but superseded by more comprehensive Alle tracking.
 | **[DEPRECATED]** Legacy field indicating if the demo subject contained Alle/Allē references.  Used for historical analysis but superseded by more comprehensive Alle tracking.
 | `[]` | `{}` |
    | `DISQUALIFIED_REASON` | 12 | `TEXT` | Reason for lead disqualification if the prospect was marked as disqualified in Salesforce.  Used for loss analysis and process improvement identification.
 | Reason for lead disqualification if the prospect was marked as disqualified in Salesforce.  Used for loss analysis and process improvement identification.
 | `[]` | `{}` |
    | `PRIMARY_LOSS_REASON` | 13 | `TEXT` | Primary reason for opportunity loss if the prospect reached opportunity stage but was  subsequently lost. Used for competitive analysis and process optimization.
 | Primary reason for opportunity loss if the prospect reached opportunity stage but was  subsequently lost. Used for competitive analysis and process optimization.
 | `[]` | `{}` |
    | `ALLE_PRACTICE_TYPE` | 14 | `TEXT` | Classification of the practice's relationship to Alle partnership programs. Values include  'New Practice' (Alle-referred), 'Existing Practice' (established Alle relationship),  'No Alle Integration' (non-Alle practices).
 | Classification of the practice's relationship to Alle partnership programs. Values include  'New Practice' (Alle-referred), 'Existing Practice' (established Alle relationship),  'No Alle Integration' (non-Alle practices).
 | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_DEPARTMENT` | 15 | `TEXT` | Department of the account executive responsible for the prospect, determined using a 30-day  lookback from key milestones or current user information for attribution accuracy.
 | Department of the account executive responsible for the prospect, determined using a 30-day  lookback from key milestones or current user information for attribution accuracy.
 | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_TEAM` | 16 | `TEXT` | Team assignment of the account executive within their department (e.g., specific sales team,  territory, or vertical focus area).
 | Team assignment of the account executive within their department (e.g., specific sales team,  territory, or vertical focus area).
 | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_SUBTEAM` | 17 | `TEXT` | Sub-team or specialized group within the account executive's team, providing granular  organization structure for performance analysis and territory management.
 | Sub-team or specialized group within the account executive's team, providing granular  organization structure for performance analysis and territory management.
 | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_NAME` | 18 | `TEXT` | Full name of the account executive responsible for managing the prospect relationship  and driving progression through the sales process.
 | Full name of the account executive responsible for managing the prospect relationship  and driving progression through the sales process.
 | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_TITLE` | 19 | `TEXT` | Job title of the account executive, indicating their role level and specialization  within the sales organization structure.
 | Job title of the account executive, indicating their role level and specialization  within the sales organization structure.
 | `[]` | `{}` |
    | `INTERNAL_REFERRER` | 20 | `TEXT` | Name of the internal Cherry employee who provided the referral or was instrumental in  the prospect acquisition. Coalesced from practice information, lead referral data, and  go-live attribution to provide comprehensive internal referral tracking.
 | Name of the internal Cherry employee who provided the referral or was instrumental in  the prospect acquisition. Coalesced from practice information, lead referral data, and  go-live attribution to provide comprehensive internal referral tracking.
 | `[]` | `{}` |
    | `STAGE` | 21 | `TEXT` | Human-readable name of the customer journey milestone stage. Mapped from technical field  names to business-friendly labels: - 'Qualified Opportunity' - Initial prospect qualification - 'Scheduled Demo' - Demo booking completed - 'Completed Demo' - Demo successfully conducted - 'Registration Start' - Registration process initiated - 'Registration' - Registration process completed - 'Underwriting Approval' - Credit and business approval obtained - 'Onboarding' - Practice setup and training phase - 'Go-Live' - Practice begins processing transactions - 'Activation' - First contract execution and full utilization
 | Human-readable name of the customer journey milestone stage. Mapped from technical field  names to business-friendly labels: - 'Qualified Opportunity' - Initial prospect qualification - 'Scheduled Demo' - Demo booking completed - 'Completed Demo' - Demo successfully conducted - 'Registration Start' - Registration process initiated - 'Registration' - Registration process completed - 'Underwriting Approval' - Credit and business approval obtained - 'Onboarding' - Practice setup and training phase - 'Go-Live' - Practice begins processing transactions - 'Activation' - First contract execution and full utilization
 | `[]` | `{}` |
    | `STAGE_NUMBER` | 22 | `NUMBER` | Numeric ordering of the milestone stages (1-9) for sequential analysis and progression  tracking. Enables easy calculation of stage advancement and conversion funnel analysis: 1=Qualified Opportunity, 2=Scheduled Demo, 3=Completed Demo, 4=Registration Start,  5=Registration, 6=Underwriting Approval, 7=Onboarding, 8=Go-Live, 9=Activation.
 | Numeric ordering of the milestone stages (1-9) for sequential analysis and progression  tracking. Enables easy calculation of stage advancement and conversion funnel analysis: 1=Qualified Opportunity, 2=Scheduled Demo, 3=Completed Demo, 4=Registration Start,  5=Registration, 6=Underwriting Approval, 7=Onboarding, 8=Go-Live, 9=Activation.
 | `[]` | `{}` |
    | `STAGE_DATE` | 23 | `DATE` | Date when the specific milestone was achieved for this prospect. Calculated using  chronologically consistent logic to ensure later milestones don't precede earlier ones.  Uses the earliest valid date from multiple data sources for each milestone type.
 | Date when the specific milestone was achieved for this prospect. Calculated using  chronologically consistent logic to ensure later milestones don't precede earlier ones.  Uses the earliest valid date from multiple data sources for each milestone type.
 | `[]` | `{}` |
    | `STAGE_DURATION` | 24 | `NUMBER` | Number of days between this milestone and the next milestone in the sequence for this  prospect. Calculated using a lead window function to measure time spent in each stage.  NULL for the final milestone reached or if no subsequent milestone exists.
 | Number of days between this milestone and the next milestone in the sequence for this  prospect. Calculated using a lead window function to measure time spent in each stage.  NULL for the final milestone reached or if no subsequent milestone exists.
 | `[]` | `{}` |
    | `LATEST_STAGE` | 25 | `TEXT` | The furthest milestone stage that this prospect has achieved in their customer journey.  Indicates the current status and progression level, useful for filtering active prospects  and identifying where prospects typically stop in the funnel. | The furthest milestone stage that this prospect has achieved in their customer journey.  Indicates the current status and progression level, useful for filtering active prospects  and identifying where prospects typically stop in the funnel. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.demo_details_xf`
    *   `model.cherry_data_model.internal_referral_go_lives_detailed`
    *   `model.cherry_data_model.internal_referral_leads_detailed`
    *   `model.cherry_data_model.lead_details_xf`
    *   `model.cherry_data_model.practice_info_full_xf`
    *   `model.cherry_data_model.prospect_attribution_summary`
    *   `model.cherry_data_model.registration_start`
    *   `model.cherry_data_model.src_sf_opportunities`
    *   `model.cherry_data_model.stg_registrations_new`
    *   `model.cherry_data_model.stg_sf_users`

---
