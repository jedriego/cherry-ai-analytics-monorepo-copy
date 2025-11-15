## Model: `recovery_events_xf`

`recovery_events_xf`

*   **Unique ID:** `model.cherry_data_model.recovery_events_xf`
*   **FQN:** `prod.risk_marts.recovery_events_xf`
*   **Description:** **Merchant Recovery Event Tracking**
This model provides a comprehensive view of merchant recovery events through Cherry's review and  exception management process. It tracks merchants who have undergone performance reviews, extensions,  and recovery interventions, combining multiple review cycles into unified event records that show  the complete recovery journey for each merchant.
**Key Business Logic:** - **Review Cycles**: Aggregates multiple review periods of the same type into cycles, tracking 
  entry/exit health scores and decisions across the entire cycle
- **Extension Cycles**: Separately tracks extension periods where merchants receive additional 
  time for recovery, with cycle-level aggregation of performance metrics
- **Exception Handling**: Incorporates "look recovery" exceptions that override standard review 
  decisions and timelines for special circumstances
- **Current Status Logic**: Determines real-time status by prioritizing active exceptions, then 
  extensions, then standard review decisions
- **Recovery Determination**: Calculates recovery status based on final review decisions, with 
  'Maintain' indicating successful recovery and 'Low Health' indicating continued risk

**Data Sources:** - **in_review_entry**: Initial review entry records with merchant context and health scores - **in_review_status**: Current review status and updated metrics during active reviews - **in_review_decisions**: Final review decisions with entry/exit health score comparisons - **exceptions**: Special exception records for "look recovery" cases with custom timelines
**Primary Use Cases:** - Merchant recovery program management and tracking - Performance intervention effectiveness analysis - Risk management and merchant health monitoring - Recovery timeline and success rate reporting - Exception case management and tracking
**Grain:** One record per merchant per review cycle (Review or Extension type)

*   **Tags:** `['risk']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `MERCHANT_REVIEW_ID` | 1 | `TEXT` | Unique identifier for each merchant review cycle, generated as a surrogate key combining  merchant ID, review type, and cycle start date. Ensures distinct tracking of each  review or extension cycle.
 | Unique identifier for each merchant review cycle, generated as a surrogate key combining  merchant ID, review type, and cycle start date. Ensures distinct tracking of each  review or extension cycle.
 | `[]` | `{}` |
    | `MERCHANT_ID` | 2 | `NUMBER` | Cherry's internal merchant identifier, linking to the merchant undergoing review or  recovery intervention. Primary key for joining with merchant information and performance data.
 | Cherry's internal merchant identifier, linking to the merchant undergoing review or  recovery intervention. Primary key for joining with merchant information and performance data.
 | `[]` | `{}` |
    | `MERCHANT_NAME` | 3 | `TEXT` | Business name of the merchant, used for reporting and identification purposes in  recovery program management and communication.
 | Business name of the merchant, used for reporting and identification purposes in  recovery program management and communication.
 | `[]` | `{}` |
    | `ORGANIZATION_ID` | 4 | `NUMBER` | Organization identifier that groups related merchants under the same parent entity,  enabling organization-level recovery analysis and health score tracking.
 | Organization identifier that groups related merchants under the same parent entity,  enabling organization-level recovery analysis and health score tracking.
 | `[]` | `{}` |
    | `ACCOUNT_INDUSTRY_SEGMENT` | 5 | `TEXT` | Industry segment classification of the merchant's account (e.g., Dental, Medspa,  Veterinary), used for industry-specific recovery strategies and benchmarking.
 | Industry segment classification of the merchant's account (e.g., Dental, Medspa,  Veterinary), used for industry-specific recovery strategies and benchmarking.
 | `[]` | `{}` |
    | `GO_LIVE_DATE` | 6 | `DATE` | Date when the merchant first went live on Cherry's platform, used for calculating  tenure and contextualizing recovery timelines relative to merchant lifecycle stage.
 | Date when the merchant first went live on Cherry's platform, used for calculating  tenure and contextualizing recovery timelines relative to merchant lifecycle stage.
 | `[]` | `{}` |
    | `REVIEW_TYPE` | 7 | `TEXT` | Type of review cycle: 'Review' for standard performance reviews or 'Extension' for  additional recovery time periods. Determines the recovery intervention strategy and timeline.
 | Type of review cycle: 'Review' for standard performance reviews or 'Extension' for  additional recovery time periods. Determines the recovery intervention strategy and timeline.
 | `[]` | `{}` |
    | `NUM_REVIEWS_IN_CYCLE` | 8 | `NUMBER` | Count of individual review periods within this cycle. For Review cycles, indicates how  many review periods occurred before resolution. For Extension cycles, shows the number  of extension periods granted.
 | Count of individual review periods within this cycle. For Review cycles, indicates how  many review periods occurred before resolution. For Extension cycles, shows the number  of extension periods granted.
 | `[]` | `{}` |
    | `REVIEW_PERIOD_START_DATE` | 9 | `TEXT` | Start date of the review cycle, marking when the merchant first entered the review  or extension process for this particular recovery intervention.
 | Start date of the review cycle, marking when the merchant first entered the review  or extension process for this particular recovery intervention.
 | `[]` | `{}` |
    | `REVIEW_PERIOD_END_DATE` | 10 | `TEXT` | End date of the review cycle, indicating when the review or extension period concluded  with a final decision or transition to the next phase.
 | End date of the review cycle, indicating when the review or extension period concluded  with a final decision or transition to the next phase.
 | `[]` | `{}` |
    | `EXCEPTION_START_DATE` | 11 | `DATE` | Start date of any "look recovery" exception period applied to this merchant, overriding  standard review timelines for special circumstances or interventions.
 | Start date of any "look recovery" exception period applied to this merchant, overriding  standard review timelines for special circumstances or interventions.
 | `[]` | `{}` |
    | `EXCEPTION_END_DATE` | 12 | `DATE` | End date of the exception period, after which standard review processes and decisions  resume for the merchant's recovery tracking.
 | End date of the exception period, after which standard review processes and decisions  resume for the merchant's recovery tracking.
 | `[]` | `{}` |
    | `IS_CURRENTLY_EXTENDED` | 13 | `BOOLEAN` | Boolean flag indicating whether the merchant is currently in an active extension period,  calculated by checking if the current date falls within the extension cycle dates.
 | Boolean flag indicating whether the merchant is currently in an active extension period,  calculated by checking if the current date falls within the extension cycle dates.
 | `[]` | `{}` |
    | `IS_CURRENTLY_EXCEPTION` | 14 | `BOOLEAN` | Boolean flag indicating whether the merchant is currently under an active exception,  calculated by checking if the current date falls within the exception period.
 | Boolean flag indicating whether the merchant is currently under an active exception,  calculated by checking if the current date falls within the exception period.
 | `[]` | `{}` |
    | `HAD_EXCEPTION` | 15 | `BOOLEAN` | Boolean flag indicating whether this merchant ever had an exception applied during their  recovery process, regardless of current status. Used for tracking exception usage patterns.
 | Boolean flag indicating whether this merchant ever had an exception applied during their  recovery process, regardless of current status. Used for tracking exception usage patterns.
 | `[]` | `{}` |
    | `EXCEPTION_NOTES` | 16 | `TEXT` | Free-text notes explaining the reason for the exception and any special circumstances  or interventions applied during the exception period.
 | Free-text notes explaining the reason for the exception and any special circumstances  or interventions applied during the exception period.
 | `[]` | `{}` |
    | `REVIEW_DECISION` | 17 | `TEXT` | Final decision made at the end of the review cycle: 'Maintain' (merchant recovered),  'Low Health' (merchant remains at risk), or other outcomes. Core metric for recovery success.
 | Final decision made at the end of the review cycle: 'Maintain' (merchant recovered),  'Low Health' (merchant remains at risk), or other outcomes. Core metric for recovery success.
 | `[]` | `{}` |
    | `CURRENT_STATUS` | 18 | `TEXT` | Current status of the merchant prioritizing exceptions first, then active review decisions.  Shows 'Exception' for active exceptions, otherwise displays the current or final review decision.
 | Current status of the merchant prioritizing exceptions first, then active review decisions.  Shows 'Exception' for active exceptions, otherwise displays the current or final review decision.
 | `[]` | `{}` |
    | `REVIEW_TREND` | 19 | `TEXT` | Trend assessment showing the direction of merchant performance during the review period:  improving, declining, or stable. Uses exception trend data when merchant is under exception.
 | Trend assessment showing the direction of merchant performance during the review period:  improving, declining, or stable. Uses exception trend data when merchant is under exception.
 | `[]` | `{}` |
    | `ENTRY_HEALTH_SCORE` | 20 | `TEXT` | Health score when the merchant first entered this review cycle, establishing the baseline  performance level that triggered the review or intervention process.
 | Health score when the merchant first entered this review cycle, establishing the baseline  performance level that triggered the review or intervention process.
 | `[]` | `{}` |
    | `EXIT_HEALTH_SCORE` | 21 | `FLOAT` | Health score at the end of the review cycle or current health score for ongoing reviews.  Used to measure recovery progress and effectiveness of interventions.
 | Health score at the end of the review cycle or current health score for ongoing reviews.  Used to measure recovery progress and effectiveness of interventions.
 | `[]` | `{}` |
    | `TRANSACTION_VOLUME_LAST_30D` | 22 | `FLOAT` | Total transaction volume in the last 30 days during the review cycle, providing context  for merchant activity levels and business performance during recovery efforts.
 | Total transaction volume in the last 30 days during the review cycle, providing context  for merchant activity levels and business performance during recovery efforts.
 | `[]` | `{}` |
    | `TRANSACTION_VOLUME_LAST_90D` | 23 | `FLOAT` | Total transaction volume in the last 90 days during the review cycle, offering a longer-term  view of merchant business performance and recovery sustainability.
 | Total transaction volume in the last 90 days during the review cycle, offering a longer-term  view of merchant business performance and recovery sustainability.
 | `[]` | `{}` |
    | `IS_RECOVERED` | 24 | `BOOLEAN` | Boolean indicator of recovery success: TRUE for 'Maintain' decisions (successful recovery),  FALSE for 'Low Health' decisions (unsuccessful recovery), NULL for ongoing or exception cases.  Key metric for measuring recovery program effectiveness. | Boolean indicator of recovery success: TRUE for 'Maintain' decisions (successful recovery),  FALSE for 'Low Health' decisions (unsuccessful recovery), NULL for ongoing or exception cases.  Key metric for measuring recovery program effectiveness. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt_utils.generate_surrogate_key`
    *   `model.cherry_data_model.exceptions`
    *   `model.cherry_data_model.in_review_decisions`
    *   `model.cherry_data_model.in_review_entry`
    *   `model.cherry_data_model.in_review_status`

---
