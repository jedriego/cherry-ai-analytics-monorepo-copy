## Model: `practice_applications_xf`

`practice_applications_xf`

*   **Unique ID:** `model.cherry_data_model.practice_applications_xf`
*   **FQN:** `prod.core_marts.practice_applications_xf`
*   **Description:** Comprehensive transformation of practice applications that combines user registration data,  application leads, and application status history to create a complete view of the application  lifecycle. This model tracks practice applications from initial creation through final outcomes,  including timing metrics, status progressions, and decision classifications. It focuses on  initial underwriting applications and provides analytics-ready data for understanding  application performance and user journeys.
This table is created using application_leads and does not include merchant applications. These are applications that are created at the organization level. Any subsequent applications from the same organization are considered merchant applications. For merchant applications, use the `merchant_applications_xf` model.
**Note**: This model is used to track practice applications from initial creation through final outcomes, including timing metrics, status progressions, and decision classifications. It focuses on initial underwriting applications and provides analytics-ready data for understanding application performance and user journeys. **Note**: For shared column definitions that exist in both practice and merchant applications,  refer to `prod-core-marts-doc-blocks.md`. This YAML file contains practice-specific columns  and references shared definitions where applicable.

*   **Tags:** `['core']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `PRACTICE_APPLICATION_ID` | 1 | `TEXT` | Surrogate key uniquely identifying each practice application record, generated from  application_lead_id and user_id combination.
 | Surrogate key uniquely identifying each practice application record, generated from  application_lead_id and user_id combination.
 | `[]` | `{}` |
    | `APPLICATION_LEAD_ID` | 2 | `TEXT` | Foreign key reference to the application lead record. May be null for users who  registered but never started an application.
 | Foreign key reference to the application lead record. May be null for users who  registered but never started an application.
 | `[]` | `{}` |
    | `USER_ID` | 3 | `NUMBER` | Foreign key reference to the user who created or is associated with the application. Used to link application data to user account information. | Foreign key reference to the user who created or is associated with the application. Used to link application data to user account information. | `[]` | `{}` |
    | `USER_FULL_NAME` | 4 | `TEXT` | Full name of the user associated with the application. | Full name of the user associated with the application. | `[]` | `{}` |
    | `USER_STATUS` | 5 | `TEXT` | Current status of the user account (e.g., active, inactive). | Current status of the user account (e.g., active, inactive). | `[]` | `{}` |
    | `USER_PHONE` | 6 | `TEXT` | Phone number associated with the user's account. | Phone number associated with the user's account. | `[]` | `{}` |
    | `USER_EMAIL` | 7 | `TEXT` | Email address associated with the user's account. | Email address associated with the user's account. | `[]` | `{}` |
    | `INDUSTRY` | 8 | `TEXT` | Industry classification of the practice or business applying for services. Used for segmentation and analysis of application patterns across different healthcare and service industries. | Industry classification of the practice or business applying for services. Used for segmentation and analysis of application patterns across different healthcare and service industries. | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 9 | `TEXT` | More granular industry segment classification derived from lead industry segments and owners lookup. Provides detailed categorization within broader industry groups. | More granular industry segment classification derived from lead industry segments and owners lookup. Provides detailed categorization within broader industry groups. | `[]` | `{}` |
    | `SOURCE` | 10 | `TEXT` | Marketing source or channel through which the application was generated. | Marketing source or channel through which the application was generated. | `[]` | `{}` |
    | `SOURCE_REF` | 11 | `TEXT` | Additional reference information about the source, providing more detailed attribution.
 | Additional reference information about the source, providing more detailed attribution.
 | `[]` | `{}` |
    | `APPLICATION_LEAD_BUSINESS_NAME` | 12 | `TEXT` | Business or practice name provided in the application lead. | Business or practice name provided in the application lead. | `[]` | `{}` |
    | `USER_CREATED_AT` | 13 | `TIMESTAMP_NTZ` | UTC timestamp when the user account was created. | UTC timestamp when the user account was created. | `[]` | `{}` |
    | `APPLICATION_CREATED_AT_PT` | 14 | `TIMESTAMP_NTZ` | Pacific Time timestamp when the application was created. Falls back to user creation time if application timestamp is not available. | Pacific Time timestamp when the application was created. Falls back to user creation time if application timestamp is not available. | `[]` | `{}` |
    | `FIRST_SUBMITTED_TIMESTAMP` | 15 | `TIMESTAMP_NTZ` | UTC timestamp when the application was first submitted for review. | UTC timestamp when the application was first submitted for review. | `[]` | `{}` |
    | `FIRST_SUBMITTED_TIMESTAMP_PT` | 16 | `TIMESTAMP_NTZ` | Pacific Time timestamp when the application was first submitted for review.
 | Pacific Time timestamp when the application was first submitted for review.
 | `[]` | `{}` |
    | `LAST_SUBMITTED_TIMESTAMP_PT` | 17 | `TIMESTAMP_NTZ` | Pacific Time timestamp of the most recent submission, in case the application  was resubmitted multiple times.
 | Pacific Time timestamp of the most recent submission, in case the application  was resubmitted multiple times.
 | `[]` | `{}` |
    | `FIRST_IN_REVIEW_TIMESTAMP_PT` | 18 | `TIMESTAMP_NTZ` | Pacific Time timestamp when the application first entered review status.
 | Pacific Time timestamp when the application first entered review status.
 | `[]` | `{}` |
    | `LAST_IN_REVIEW_TIMESTAMP_PT` | 19 | `TIMESTAMP_NTZ` | Pacific Time timestamp of the most recent time the application entered review status.
 | Pacific Time timestamp of the most recent time the application entered review status.
 | `[]` | `{}` |
    | `FINAL_OUTCOME_TIMESTAMP_PT` | 20 | `TIMESTAMP_NTZ` | Pacific Time timestamp of the final outcome status (approved, denied,  conditional approved, or other terminal status).
 | Pacific Time timestamp of the final outcome status (approved, denied,  conditional approved, or other terminal status).
 | `[]` | `{}` |
    | `FIRST_OUTCOME_AFTER_SUBMITTED` | 21 | `TEXT` | The first outcome status (approved, denied, etc.) received after the application was submitted. | The first outcome status (approved, denied, etc.) received after the application was submitted. | `[]` | `{}` |
    | `FIRST_OUTCOME_AFTER_REVIEW` | 22 | `TEXT` | The first outcome status received after the application entered review status. | The first outcome status received after the application entered review status. | `[]` | `{}` |
    | `FINAL_OUTCOME_STATUS` | 23 | `TEXT` | The final outcome status for the application (approved, denied, conditional approved, or other terminal status). | The final outcome status for the application (approved, denied, conditional approved, or other terminal status). | `[]` | `{}` |
    | `ADDITIONAL_INFO_OUTCOME` | 24 | `TEXT` | The outcome status received after additional materials were requested from the applicant. | The outcome status received after additional materials were requested from the applicant. | `[]` | `{}` |
    | `UNIQUE_APPLICATION_LEAD_STATUSES` | 25 | `TEXT` | Comma-separated list of all unique statuses the application has passed through during its lifecycle. | Comma-separated list of all unique statuses the application has passed through during its lifecycle. | `[]` | `{}` |
    | `MOST_RECENT_APPLICATION_STATUS` | 26 | `TEXT` | Current or most recent status of the application. Defaults to 'NOT_INITIALIZED' if no status is available. | Current or most recent status of the application. Defaults to 'NOT_INITIALIZED' if no status is available. | `[]` | `{}` |
    | `DECISION_STATUS` | 27 | `TEXT` | Final decision status for the application, limited to terminal decision states (APPROVED, DENIED, CONDITIONAL_APPROVED). Null if no final decision has been made. | Final decision status for the application, limited to terminal decision states (APPROVED, DENIED, CONDITIONAL_APPROVED). Null if no final decision has been made. | `[]` | `{}` |
    | `FIRST_DECISION_TIMESTAMP_PT` | 28 | `TIMESTAMP_NTZ` | Pacific Time timestamp of the first decision made on the application.
 | Pacific Time timestamp of the first decision made on the application.
 | `[]` | `{}` |
    | `LAST_DECISION_TIMESTAMP_PT` | 29 | `TIMESTAMP_NTZ` | Pacific Time timestamp of the most recent decision made on the application.
 | Pacific Time timestamp of the most recent decision made on the application.
 | `[]` | `{}` |
    | `FIRST_SUBMITTED_TO_FIRST_DECISION_SECONDS` | 30 | `NUMBER` | Duration in seconds from when the application was first submitted to when the first decision was made. | Duration in seconds from when the application was first submitted to when the first decision was made. | `[]` | `{}` |
    | `LAST_SUBMITTED_TO_LAST_DECISION_SECONDS` | 31 | `NUMBER` | Duration in seconds from the most recent submission to the most recent decision. | Duration in seconds from the most recent submission to the most recent decision. | `[]` | `{}` |
    | `ADDITIONAL_INFO_TO_OUTCOME_SECONDS` | 32 | `NUMBER` | Duration in seconds from when additional materials were requested to when an outcome was received. | Duration in seconds from when additional materials were requested to when an outcome was received. | `[]` | `{}` |
    | `IS_REVIEW` | 33 | `BOOLEAN` | Boolean flag indicating whether the application went through a manual review process (true) or received an automated decision (false). | Boolean flag indicating whether the application went through a manual review process (true) or received an automated decision (false). | `[]` | `{}` |
    | `IS_INSTANT_DECISION` | 34 | `BOOLEAN` | Boolean flag indicating whether the application received an instant automated decision within 180 seconds of submission and without manual review. | Boolean flag indicating whether the application received an instant automated decision within 180 seconds of submission and without manual review. | `[]` | `{}` |
    | `IS_ADDITIONAL_INFO_REQUIRED` | 35 | `BOOLEAN` | Boolean flag indicating whether additional materials were requested during the application process. | Boolean flag indicating whether additional materials were requested during the application process. | `[]` | `{}` |
    | `IS_APPLICATION_SUBMITTED` | 36 | `BOOLEAN` | Boolean flag indicating whether the application has been submitted (moved beyond NOT_INITIALIZED, INITIALIZED, or DRAFTED statuses). | Boolean flag indicating whether the application has been submitted (moved beyond NOT_INITIALIZED, INITIALIZED, or DRAFTED statuses). | `[]` | `{}` |
    | `REGISTRATION_TIMESTAMP_PT` | 37 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `IS_REGISTRATION_COMPLETE` | 38 | `BOOLEAN` | Boolean flag indicating whether the application process is complete with a final outcome (APPROVED, DENIED, CONDITIONAL_APPROVED, or ARCHIVED). | Boolean flag indicating whether the application process is complete with a final outcome (APPROVED, DENIED, CONDITIONAL_APPROVED, or ARCHIVED). | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt_utils.generate_surrogate_key`
    *   `model.cherry_data_model.registration_to_industry_mapping`
    *   `model.cherry_data_model.src_cherry_users`
    *   `model.cherry_data_model.stg_application_leads`
    *   `model.cherry_data_model.stg_application_leads_history`

---
