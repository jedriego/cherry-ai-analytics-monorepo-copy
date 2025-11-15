## Model: `zendesk_daily_contact_rate_xf`

`zendesk_daily_contact_rate_xf`

*   **Unique ID:** `model.cherry_data_model.zendesk_daily_contact_rate_xf`
*   **FQN:** `prod.customer_support_marts.zendesk_daily_contact_rate_xf`
*   **Description:** Daily customer support contact rate analysis combining eligible customer populations with categorized contact volumes from the Zendesk ticketing system. This model creates a comprehensive daily view of support ticket patterns by joining reference date eligibility data with Zendesk ticket volumes categorized by contact type (Practice, Patient, Collections). The model filters out abandoned tickets and excludes certain agent dispositions (Transfer, Spam, No Response Needed, Disconnected) to focus on quality support interactions. Unlike the NICE contact rate model, this version uses Zendesk ticket data and does not apply compression factors since tickets are already discrete units. This is essential for customer support capacity planning, ticket volume monitoring, and understanding support demand patterns across different business days and customer types through the Zendesk channel.

*   **Tags:** `['customer_support', 'zendesk_refresh']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `REFERENCE_DATE` | 1 | `DATE` | Primary date dimension for the contact rate analysis. Inherited from stg_daily_contact_rate_eligible and represents the specific date for which all ticket metrics and eligible population counts are calculated. Used for daily analysis and trend monitoring.
 | Primary date dimension for the contact rate analysis. Inherited from stg_daily_contact_rate_eligible and represents the specific date for which all ticket metrics and eligible population counts are calculated. Used for daily analysis and trend monitoring.
 | `[]` | `{}` |
    | `EVAL_WEEK` | 2 | `DATE` | Week dimension created by truncating reference_date to the beginning of the week (Monday). Used for weekly contact rate analysis and aggregation of support metrics across week periods.
 | Week dimension created by truncating reference_date to the beginning of the week (Monday). Used for weekly contact rate analysis and aggregation of support metrics across week periods.
 | `[]` | `{}` |
    | `EVAL_MONTH` | 3 | `DATE` | Month dimension created by truncating reference_date to the beginning of the month. Used for monthly contact rate analysis and longer-term trend analysis of support patterns.
 | Month dimension created by truncating reference_date to the beginning of the month. Used for monthly contact rate analysis and longer-term trend analysis of support patterns.
 | `[]` | `{}` |
    | `IS_WEEKEND` | 4 | `BOOLEAN` | Boolean flag indicating whether the reference_date falls on a weekend (Saturday or Sunday). Used for differentiating weekend vs. weekday ticket creation patterns and support demand analysis.
 | Boolean flag indicating whether the reference_date falls on a weekend (Saturday or Sunday). Used for differentiating weekend vs. weekday ticket creation patterns and support demand analysis.
 | `[]` | `{}` |
    | `CUMULATIVE_LIVE_MERCHANTS` | 5 | `NUMBER` | Total count of live merchants as of the reference_date. Inherited from stg_daily_contact_rate_eligible and represents the eligible merchant population that could potentially generate practice-related support tickets.
 | Total count of live merchants as of the reference_date. Inherited from stg_daily_contact_rate_eligible and represents the eligible merchant population that could potentially generate practice-related support tickets.
 | `[]` | `{}` |
    | `NUMBER_SERVICING_ELIGIBLE_BORROWERS` | 6 | `NUMBER` | Count of borrowers eligible for servicing support as of the reference_date. Inherited from stg_daily_contact_rate_eligible and represents the population of borrowers who could generate servicing-related support tickets.
 | Count of borrowers eligible for servicing support as of the reference_date. Inherited from stg_daily_contact_rate_eligible and represents the population of borrowers who could generate servicing-related support tickets.
 | `[]` | `{}` |
    | `DENIED_APPLICANTS` | 7 | `NUMBER` | Count of applicants with denied status as of the reference_date. Inherited from stg_daily_contact_rate_eligible and represents a population that may generate appeals or inquiry-related support tickets.
 | Count of applicants with denied status as of the reference_date. Inherited from stg_daily_contact_rate_eligible and represents a population that may generate appeals or inquiry-related support tickets.
 | `[]` | `{}` |
    | `REVIEW_APPLICANTS` | 8 | `NUMBER` | Count of applicants currently in review status as of the reference_date. Inherited from stg_daily_contact_rate_eligible and represents applicants who may contact support about their application status.
 | Count of applicants currently in review status as of the reference_date. Inherited from stg_daily_contact_rate_eligible and represents applicants who may contact support about their application status.
 | `[]` | `{}` |
    | `INITIALIZED_APPLICANTS` | 9 | `NUMBER` | Count of applicants who have initialized their applications as of the reference_date. Inherited from stg_daily_contact_rate_eligible and represents early-stage applicants who may need application support.
 | Count of applicants who have initialized their applications as of the reference_date. Inherited from stg_daily_contact_rate_eligible and represents early-stage applicants who may need application support.
 | `[]` | `{}` |
    | `APPROVED_APPLICANTS` | 10 | `NUMBER` | Count of applicants with approved status as of the reference_date. Inherited from stg_daily_contact_rate_eligible and represents applicants who may contact support about next steps or funding processes.
 | Count of applicants with approved status as of the reference_date. Inherited from stg_daily_contact_rate_eligible and represents applicants who may contact support about next steps or funding processes.
 | `[]` | `{}` |
    | `APPROVED_NOT_FUNDED_APPLICANTS` | 11 | `NUMBER` | Count of applicants who are approved but not yet funded as of the reference_date. Inherited from stg_daily_contact_rate_eligible and represents a population that may contact support about funding delays or requirements.
 | Count of applicants who are approved but not yet funded as of the reference_date. Inherited from stg_daily_contact_rate_eligible and represents a population that may contact support about funding delays or requirements.
 | `[]` | `{}` |
    | `TOTAL_APPLICANTS` | 12 | `NUMBER` | Total count of all applicants regardless of status as of the reference_date. Inherited from stg_daily_contact_rate_eligible and represents the complete applicant population eligible to contact support.
 | Total count of all applicants regardless of status as of the reference_date. Inherited from stg_daily_contact_rate_eligible and represents the complete applicant population eligible to contact support.
 | `[]` | `{}` |
    | `AGENT_DISPOSITION` | 13 | `TEXT` | Agent disposition classification for the ticket interaction. Inherited from stg_zendesk_tickets after filtering out excluded dispositions (Transfer, Spam, No Response Needed, Disconnected). Represents the resolution or outcome classification assigned by support agents to tickets.
 | Agent disposition classification for the ticket interaction. Inherited from stg_zendesk_tickets after filtering out excluded dispositions (Transfer, Spam, No Response Needed, Disconnected). Represents the resolution or outcome classification assigned by support agents to tickets.
 | `[]` | `{}` |
    | `NUM_PATIENT_CONTACTS` | 14 | `NUMBER` | Daily count of patient-related support tickets. Calculated by counting tickets where customer_type = 'patient'. No compression factors applied since Zendesk tickets are discrete units. Only includes non-abandoned tickets with valid dispositions for accurate patient support volume tracking.
 | Daily count of patient-related support tickets. Calculated by counting tickets where customer_type = 'patient'. No compression factors applied since Zendesk tickets are discrete units. Only includes non-abandoned tickets with valid dispositions for accurate patient support volume tracking.
 | `[]` | `{}` |
    | `NUM_PRACTICE_CONTACTS` | 15 | `NUMBER` | Daily count of practice-related support tickets. Calculated by counting tickets where customer_type = 'practice' or where customer_type = 'alle' and merchant_id is not null. No compression factors applied since Zendesk tickets are discrete units. Represents practice-facing support volume.
 | Daily count of practice-related support tickets. Calculated by counting tickets where customer_type = 'practice' or where customer_type = 'alle' and merchant_id is not null. No compression factors applied since Zendesk tickets are discrete units. Represents practice-facing support volume.
 | `[]` | `{}` |
    | `NUM_COLLECTIONS_CONTACTS` | 16 | `NUMBER` | Daily count of collections-related support tickets. Calculated by counting tickets where customer_type contains 'collect' or 'recover'. No compression factors applied. Represents tickets related to collections, recovery, and past due account activities.
 | Daily count of collections-related support tickets. Calculated by counting tickets where customer_type contains 'collect' or 'recover'. No compression factors applied. Represents tickets related to collections, recovery, and past due account activities.
 | `[]` | `{}` |
    | `NUM_MISSING_SKILL_NAME_CONTACTS` | 17 | `NUMBER` | Daily count of tickets where the contact type could not be determined due to missing or invalid customer_type information. No compression factors applied. Used for data quality monitoring and identifying tickets that require better categorization or customer type assignment.
 | Daily count of tickets where the contact type could not be determined due to missing or invalid customer_type information. No compression factors applied. Used for data quality monitoring and identifying tickets that require better categorization or customer type assignment.
 | `[]` | `{}` |
    | `NUM_OTHER_CONTACTS` | 18 | `NUMBER` | Daily count of support tickets that don't fall into the standard categories (Patient, Practice, Collections, or Missing Skill Name). No compression factors applied. Represents miscellaneous or uncategorized support tickets that may require additional classification analysis. | Daily count of support tickets that don't fall into the standard categories (Patient, Practice, Collections, or Missing Skill Name). No compression factors applied. Represents miscellaneous or uncategorized support tickets that may require additional classification analysis. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.stg_daily_contact_rate_eligible`
    *   `model.cherry_data_model.stg_zendesk_tickets`

---
