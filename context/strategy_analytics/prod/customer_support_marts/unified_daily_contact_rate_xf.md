## Model: `unified_daily_contact_rate_xf`

`unified_daily_contact_rate_xf`

*   **Unique ID:** `model.cherry_data_model.unified_daily_contact_rate_xf`
*   **FQN:** `prod.customer_support_marts.unified_daily_contact_rate_xf`
*   **Description:** Unified model that combines NICE and Zendesk daily contact rate metrics. This model calculates the daily contact rate for support and servicing by tracking the proportion of eligible populations making contact with support teams. It provides unified metrics across both contact center platforms, broken down by disposition/wrap-up codes to enable detailed analysis of contact reasons.
Contact rate is defined as the proportion of an eligible population making contact in any manner with either the support or servicing teams at Cherry. This is an important metric for evaluating the effectiveness of experiences before support is contacted and the impact of proactive education initiatives.

*   **Tags:** `['customer_support', 'contact_rate', 'key-metrics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_SYSTEM` | 1 | `TEXT` | Source system for the record ('NICE' or 'ZENDESK') | Source system for the record ('NICE' or 'ZENDESK') | `[]` | `{}` |
    | `REFERENCE_DATE` | 2 | `DATE` | Date for which contact rates are calculated | Date for which contact rates are calculated | `[]` | `{}` |
    | `DISPOSITION_NAME` | 3 | `TEXT` | Unified disposition/wrap-up code field. Maps from disposition_name (NICE) or agent_disposition (Zendesk) | Unified disposition/wrap-up code field. Maps from disposition_name (NICE) or agent_disposition (Zendesk) | `[]` | `{}` |
    | `NUM_PATIENT_CONTACTS` | 4 | `NUMBER` | Number of patient/borrower contacts for this disposition on this date | Number of patient/borrower contacts for this disposition on this date | `[]` | `{}` |
    | `NUM_PRACTICE_CONTACTS` | 5 | `NUMBER` | Number of practice/merchant contacts for this disposition on this date | Number of practice/merchant contacts for this disposition on this date | `[]` | `{}` |
    | `NUM_APPLICANT_CONTACTS` | 6 | `NUMBER` | Number of applicant contacts (currently 0 for both systems as not separately tracked) | Number of applicant contacts (currently 0 for both systems as not separately tracked) | `[]` | `{}` |
    | `NUM_COLLECTIONS_CONTACTS` | 7 | `NUMBER` | Number of collections-related contacts for this disposition on this date | Number of collections-related contacts for this disposition on this date | `[]` | `{}` |
    | `NUM_MISSING_SKILL_NAME_CONTACTS` | 8 | `NUMBER` | Number of contacts with missing skill/queue information | Number of contacts with missing skill/queue information | `[]` | `{}` |
    | `NUM_OTHER_CONTACTS` | 9 | `NUMBER` | Number of other/uncategorized contacts for this disposition on this date | Number of other/uncategorized contacts for this disposition on this date | `[]` | `{}` |
    | `EVAL_WEEK` | 10 | `DATE` | Week (Monday) containing the reference_date for weekly aggregations | Week (Monday) containing the reference_date for weekly aggregations | `[]` | `{}` |
    | `EVAL_MONTH` | 11 | `DATE` | Month containing the reference_date for monthly aggregations | Month containing the reference_date for monthly aggregations | `[]` | `{}` |
    | `IS_WEEKEND` | 12 | `BOOLEAN` | Boolean flag indicating if reference_date is a weekend (Saturday/Sunday) | Boolean flag indicating if reference_date is a weekend (Saturday/Sunday) | `[]` | `{}` |
    | `CUMULATIVE_LIVE_MERCHANTS` | 13 | `NUMBER` | Cumulative count of live merchants as of the reference_date | Cumulative count of live merchants as of the reference_date | `[]` | `{}` |
    | `NUMBER_SERVICING_ELIGIBLE_BORROWERS` | 14 | `NUMBER` | Count of borrowers eligible for servicing contacts on this date | Count of borrowers eligible for servicing contacts on this date | `[]` | `{}` |
    | `DENIED_APPLICANTS` | 15 | `NUMBER` | Count of denied applicants on this date | Count of denied applicants on this date | `[]` | `{}` |
    | `REVIEW_APPLICANTS` | 16 | `NUMBER` | Count of applicants in review status on this date | Count of applicants in review status on this date | `[]` | `{}` |
    | `INITIALIZED_APPLICANTS` | 17 | `NUMBER` | Count of applicants with initialized applications on this date | Count of applicants with initialized applications on this date | `[]` | `{}` |
    | `APPROVED_APPLICANTS` | 18 | `NUMBER` | Count of approved applicants on this date | Count of approved applicants on this date | `[]` | `{}` |
    | `APPROVED_NOT_FUNDED_APPLICANTS` | 19 | `NUMBER` | Count of approved but not yet funded applicants on this date | Count of approved but not yet funded applicants on this date | `[]` | `{}` |
    | `TOTAL_APPLICANTS` | 20 | `NUMBER` | Total count of all applicants on this date | Total count of all applicants on this date | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.nice_daily_contact_rate_xf_archive`
    *   `model.cherry_data_model.zendesk_daily_contact_rate_xf`

---
