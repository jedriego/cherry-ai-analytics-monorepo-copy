## Model: `user_product_use_xf`

`user_product_use_xf`

*   **Unique ID:** `model.cherry_data_model.user_product_use_xf`
*   **FQN:** `prod.core_marts.user_product_use_xf`
*   **Description:** Comprehensive daily user activity and engagement model that combines product usage metrics with customer support interaction data. This model enhances the base user product usage data from stg_user_product_use with support ticket information from Zendesk, creating a complete view of user engagement across both product usage and support channels. The model matches users to support interactions using phone and email identifiers, aggregating inbound support tickets and calls per user per date. This is essential for understanding user behavior patterns, identifying users who need additional support, and analyzing the relationship between product usage and support needs for customer success and retention strategies.

*   **Tags:** `['core']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `FULL_DATE` | 1 | `DATE` | Date dimension for the user activity record. This serves as part of the compound key along with user_id, representing the specific date for which all usage metrics and support interactions are aggregated.
 | Date dimension for the user activity record. This serves as part of the compound key along with user_id, representing the specific date for which all usage metrics and support interactions are aggregated.
 | `[]` | `{}` |
    | `USER_ID` | 2 | `NUMBER` | Unique identifier for the user. This serves as part of the compound key along with full_date, representing the specific user for which all activity metrics are captured on the given date.
 | Unique identifier for the user. This serves as part of the compound key along with full_date, representing the specific user for which all activity metrics are captured on the given date.
 | `[]` | `{}` |
    | `FIRST_NAME` | 3 | `TEXT` | First name of the user. Inherited from the staging model, used for user identification and personalization in reporting and analysis.
 | First name of the user. Inherited from the staging model, used for user identification and personalization in reporting and analysis.
 | `[]` | `{}` |
    | `LAST_NAME` | 4 | `TEXT` | Last name of the user. Inherited from the staging model, used for user identification and personalization in reporting and analysis.
 | Last name of the user. Inherited from the staging model, used for user identification and personalization in reporting and analysis.
 | `[]` | `{}` |
    | `FULL_NAME` | 5 | `TEXT` | Complete name of the user (combination of first and last name). Inherited from the staging model, used for user identification in reporting and customer service contexts.
 | Complete name of the user (combination of first and last name). Inherited from the staging model, used for user identification in reporting and customer service contexts.
 | `[]` | `{}` |
    | `USER_STATUS` | 6 | `TEXT` | Current status of the user account. Inherited from the staging model, indicates whether the user is active, inactive, or has other status classifications that affect their access and usage patterns.
 | Current status of the user account. Inherited from the staging model, indicates whether the user is active, inactive, or has other status classifications that affect their access and usage patterns.
 | `[]` | `{}` |
    | `CREATED_AT_PT` | 7 | `TIMESTAMP_NTZ` | Timestamp when the user account was created (Pacific Time). Inherited from the staging model, used for user cohort analysis and understanding user lifecycle stages.
 | Timestamp when the user account was created (Pacific Time). Inherited from the staging model, used for user cohort analysis and understanding user lifecycle stages.
 | `[]` | `{}` |
    | `PHONE` | 8 | `TEXT` | Phone number associated with the user account. Inherited from the staging model and used as a key identifier for matching users to support interactions in the Zendesk system.
 | Phone number associated with the user account. Inherited from the staging model and used as a key identifier for matching users to support interactions in the Zendesk system.
 | `[]` | `{}` |
    | `EMAIL` | 9 | `TEXT` | Email address associated with the user account. Inherited from the staging model and used as a key identifier for matching users to support interactions in the Zendesk system.
 | Email address associated with the user account. Inherited from the staging model and used as a key identifier for matching users to support interactions in the Zendesk system.
 | `[]` | `{}` |
    | `DAYS_SINCE_CREATION` | 10 | `NUMBER` | Number of days since the user account was created as of the full_date. Inherited from the staging model, used for user lifecycle analysis and understanding user maturity and engagement patterns over time.
 | Number of days since the user account was created as of the full_date. Inherited from the staging model, used for user lifecycle analysis and understanding user maturity and engagement patterns over time.
 | `[]` | `{}` |
    | `MONTHS_SINCE_CREATION` | 11 | `NUMBER` | Number of months since the user account was created as of the full_date. Inherited from the staging model, used for cohort analysis and long-term user lifecycle tracking.
 | Number of months since the user account was created as of the full_date. Inherited from the staging model, used for cohort analysis and long-term user lifecycle tracking.
 | `[]` | `{}` |
    | `WAS_ACTIVE` | 12 | `BOOLEAN` | Boolean flag indicating whether the user was active on the full_date. Inherited from the staging model, used for measuring daily active users and understanding engagement patterns.
 | Boolean flag indicating whether the user was active on the full_date. Inherited from the staging model, used for measuring daily active users and understanding engagement patterns.
 | `[]` | `{}` |
    | `DAYS_SINCE_LAST_ACTIVE` | 13 | `NUMBER` | Number of days since the user was last active as of the full_date. Inherited from the staging model, used for identifying dormant users and measuring user engagement recency.
 | Number of days since the user was last active as of the full_date. Inherited from the staging model, used for identifying dormant users and measuring user engagement recency.
 | `[]` | `{}` |
    | `LAST_ACTIVE_DATE` | 14 | `DATE` | Date when the user was last active. Inherited from the staging model, used for calculating days_since_last_active and understanding user engagement patterns and retention.
 | Date when the user was last active. Inherited from the staging model, used for calculating days_since_last_active and understanding user engagement patterns and retention.
 | `[]` | `{}` |
    | `COUNT_PREAPPROVAL_STARTS` | 15 | `NUMBER` | Count of preapproval processes initiated by the user on the full_date. Inherited from the staging model, measures user engagement with the preapproval feature and early-stage financing activity.
 | Count of preapproval processes initiated by the user on the full_date. Inherited from the staging model, measures user engagement with the preapproval feature and early-stage financing activity.
 | `[]` | `{}` |
    | `COUNT_APPLY_WITH_PATIENT_STARTS` | 16 | `NUMBER` | Count of "apply with patient" processes initiated by the user on the full_date. Inherited from the staging model, measures user engagement with patient-assisted application processes.
 | Count of "apply with patient" processes initiated by the user on the full_date. Inherited from the staging model, measures user engagement with patient-assisted application processes.
 | `[]` | `{}` |
    | `COUNT_CHECKOUT_WITH_PATIENT_STARTS` | 17 | `NUMBER` | Count of "checkout with patient" processes initiated by the user on the full_date. Inherited from the staging model, measures user engagement with patient-assisted checkout processes.
 | Count of "checkout with patient" processes initiated by the user on the full_date. Inherited from the staging model, measures user engagement with patient-assisted checkout processes.
 | `[]` | `{}` |
    | `COUNT_TREATMENT_PLANS_CREATED` | 18 | `NUMBER` | Count of treatment plans created by the user on the full_date. Inherited from the staging model, measures user engagement with treatment planning functionality and clinical workflow integration.
 | Count of treatment plans created by the user on the full_date. Inherited from the staging model, measures user engagement with treatment planning functionality and clinical workflow integration.
 | `[]` | `{}` |
    | `COUNT_APPLICATION_LINKS_SENT` | 19 | `NUMBER` | Count of application links sent by the user on the full_date. Inherited from the staging model, measures user engagement with patient outreach and application distribution functionality.
 | Count of application links sent by the user on the full_date. Inherited from the staging model, measures user engagement with patient outreach and application distribution functionality.
 | `[]` | `{}` |
    | `COUNT_APPLICATIONS_PAGE_LOADS` | 20 | `NUMBER` | Count of applications page loads by the user on the full_date. Inherited from the staging model, measures user engagement with application management and review functionality.
 | Count of applications page loads by the user on the full_date. Inherited from the staging model, measures user engagement with application management and review functionality.
 | `[]` | `{}` |
    | `COUNT_STATEMENTS_PAGE_LOADS` | 21 | `NUMBER` | Count of statements page loads by the user on the full_date. Inherited from the staging model, measures user engagement with financial statement and billing information.
 | Count of statements page loads by the user on the full_date. Inherited from the staging model, measures user engagement with financial statement and billing information.
 | `[]` | `{}` |
    | `COUNT_TRANSACTION_PAGE_LOADS` | 22 | `NUMBER` | Count of transaction page loads by the user on the full_date. Inherited from the staging model, measures user engagement with transaction history and financial tracking functionality.
 | Count of transaction page loads by the user on the full_date. Inherited from the staging model, measures user engagement with transaction history and financial tracking functionality.
 | `[]` | `{}` |
    | `COUNT_DOC_REQUESTS_PAGE_LOADS` | 23 | `NUMBER` | Count of document request page loads by the user on the full_date. Inherited from the staging model, measures user engagement with document management and compliance functionality.
 | Count of document request page loads by the user on the full_date. Inherited from the staging model, measures user engagement with document management and compliance functionality.
 | `[]` | `{}` |
    | `COUNT_REPORTING_PAGE_LOADS` | 24 | `NUMBER` | Count of reporting page loads by the user on the full_date. Inherited from the staging model, measures user engagement with analytics and reporting functionality.
 | Count of reporting page loads by the user on the full_date. Inherited from the staging model, measures user engagement with analytics and reporting functionality.
 | `[]` | `{}` |
    | `COUNT_TRAINING_PAGE_LOADS` | 25 | `NUMBER` | Count of training page loads by the user on the full_date. Inherited from the staging model, measures user engagement with training materials and educational content.
 | Count of training page loads by the user on the full_date. Inherited from the staging model, measures user engagement with training materials and educational content.
 | `[]` | `{}` |
    | `COUNT_HELP_PAGE_LOADS` | 26 | `NUMBER` | Count of help page loads by the user on the full_date. Inherited from the staging model, measures user engagement with self-service support and help documentation.
 | Count of help page loads by the user on the full_date. Inherited from the staging model, measures user engagement with self-service support and help documentation.
 | `[]` | `{}` |
    | `TOTAL_INBOUNDS` | 27 | `NUMBER` | Total count of inbound support tickets created by the user on the full_date. Calculated by joining Zendesk support ticket data using phone and email matching, filtered for inbound, non-abandoned, solved/closed tickets. Uses zeroifnull to ensure zero values when no support interactions occurred.
 | Total count of inbound support tickets created by the user on the full_date. Calculated by joining Zendesk support ticket data using phone and email matching, filtered for inbound, non-abandoned, solved/closed tickets. Uses zeroifnull to ensure zero values when no support interactions occurred.
 | `[]` | `{}` |
    | `INBOUND_CALLS` | 28 | `NUMBER` | Count of inbound support calls made by the user on the full_date. Calculated by joining Zendesk support ticket data and filtering for media_type_name = 'Call', using phone and email matching. Represents voice-based support interactions specifically, subset of total_inbounds.
 | Count of inbound support calls made by the user on the full_date. Calculated by joining Zendesk support ticket data and filtering for media_type_name = 'Call', using phone and email matching. Represents voice-based support interactions specifically, subset of total_inbounds.
 | `[]` | `{}` |
    | `CONTACT_REASONS` | 29 | `TEXT` | Concatenated list of contact reasons (note_outcome) for all support interactions on the full_date. Created using listagg function with ' | ' separator from Zendesk ticket data. Provides qualitative context about why users contacted support, useful for identifying common issues and support patterns. | Concatenated list of contact reasons (note_outcome) for all support interactions on the full_date. Created using listagg function with ' | ' separator from Zendesk ticket data. Provides qualitative context about why users contacted support, useful for identifying common issues and support patterns. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.stg_user_product_use`
    *   `model.cherry_data_model.zendesk_support_eligible_tickets_xf`

---
