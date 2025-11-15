## Model: `daily_merchant_applications_xf`

`daily_merchant_applications_xf`

*   **Unique ID:** `model.cherry_data_model.daily_merchant_applications_xf`
*   **FQN:** `prod.core_marts.daily_merchant_applications_xf`
*   **Description:** Daily grain fact table that combines merchant practice information with application data to create a comprehensive view of application activity by merchant and date. This model creates one row for each application created on each calendar date for each primary merchant, providing rich context about both the merchant practice and the application details. The model spans from August 28, 2019 (earliest application/go-live date) through the current date and includes only application start events for non-demo applications. This enables analysis of application volume, merchant performance, and business trends over time with full merchant context including practice status, industry classification, and organizational hierarchy.

*   **Tags:** `['core']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `DAILY_MERCHANT_APPLICATION_ID` | 1 | `TEXT` | Surrogate key uniquely identifying each daily merchant application record, generated from the combination of calendar_date, primary_merchant_id, and application_id.
 | Surrogate key uniquely identifying each daily merchant application record, generated from the combination of calendar_date, primary_merchant_id, and application_id.
 | `[]` | `{}` |
    | `CALENDAR_DATE` | 2 | `DATE` | Date dimension representing the calendar day. Serves as the primary time dimension for this daily grain table, covering dates from August 28, 2019 through current date. Each date represents a day on which applications may have been created.
 | Date dimension representing the calendar day. Serves as the primary time dimension for this daily grain table, covering dates from August 28, 2019 through current date. Each date represents a day on which applications may have been created.
 | `[]` | `{}` |
    | `PRIMARY_MERCHANT_ID` | 3 | `FLOAT` | Foreign key reference to the primary merchant practice. This represents the main merchant identifier for the practice where applications were created.
 | Foreign key reference to the primary merchant practice. This represents the main merchant identifier for the practice where applications were created.
 | `[]` | `{}` |
    | `PRACTICE_GO_LIVE_DATE` | 4 | `DATE` | Date when the merchant practice went live and became operational. Used as the starting point for including the merchant in daily snapshots - merchants are only included in the date spine from their go-live date forward.
 | Date when the merchant practice went live and became operational. Used as the starting point for including the merchant in daily snapshots - merchants are only included in the date spine from their go-live date forward.
 | `[]` | `{}` |
    | `IS_GO_LIVE_MONTH_BEFORE_CALENDAR_DATE_MONTH` | 5 | `BOOLEAN` | Boolean flag indicating whether the practice go-live date occurred in a month prior to the calendar date month. True when the practice has been live for at least one full month as of the calendar date, useful for identifying seasoned practices.
 | Boolean flag indicating whether the practice go-live date occurred in a month prior to the calendar date month. True when the practice has been live for at least one full month as of the calendar date, useful for identifying seasoned practices.
 | `[]` | `{}` |
    | `IS_GO_LIVE_WEEK_BEFORE_CALENDAR_DATE_WEEK` | 6 | `BOOLEAN` | Boolean flag indicating whether the practice go-live date occurred in a week prior to the calendar date week. True when the practice has been live for at least one full week as of the calendar date, useful for identifying practices past their initial launch period.
 | Boolean flag indicating whether the practice go-live date occurred in a week prior to the calendar date week. True when the practice has been live for at least one full week as of the calendar date, useful for identifying practices past their initial launch period.
 | `[]` | `{}` |
    | `IS_PRACTICE_ACTIVE` | 7 | `BOOLEAN` | Boolean flag indicating whether the merchant practice is currently active and operational, derived from the practice_info_xf model.
 | Boolean flag indicating whether the merchant practice is currently active and operational, derived from the practice_info_xf model.
 | `[]` | `{}` |
    | `IS_ORGANIZATION_ACTIVE` | 8 | `BOOLEAN` | Boolean flag indicating whether the parent organization of the practice is currently active, derived from the is_primary_organization_active field.
 | Boolean flag indicating whether the parent organization of the practice is currently active, derived from the is_primary_organization_active field.
 | `[]` | `{}` |
    | `IS_PRACTICE_TERMINATED` | 9 | `BOOLEAN` | Boolean flag indicating whether the merchant practice has been terminated and is no longer operational.
 | Boolean flag indicating whether the merchant practice has been terminated and is no longer operational.
 | `[]` | `{}` |
    | `PRACTICE_TERMINATION_DATE` | 10 | `DATE` | Date when the merchant practice was terminated, if applicable. Null if the practice has not been terminated.
 | Date when the merchant practice was terminated, if applicable. Null if the practice has not been terminated.
 | `[]` | `{}` |
    | `INDUSTRY` | 11 | `TEXT` | Industry classification of the merchant practice, derived from the primary_organization_industry field. Used for segmentation and analysis of application patterns across different healthcare and service industries.
 | Industry classification of the merchant practice, derived from the primary_organization_industry field. Used for segmentation and analysis of application patterns across different healthcare and service industries.
 | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 12 | `TEXT` | More granular industry segment classification derived from the account_industry_segment field, providing detailed categorization within broader industry groups.
 | More granular industry segment classification derived from the account_industry_segment field, providing detailed categorization within broader industry groups.
 | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_ID` | 13 | `NUMBER` | Foreign key reference to the primary organization that owns this merchant practice, enabling analysis at the organizational level.
 | Foreign key reference to the primary organization that owns this merchant practice, enabling analysis at the organizational level.
 | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_NAME` | 14 | `TEXT` | Name of the primary organization that owns this merchant practice, providing human-readable organizational context.
 | Name of the primary organization that owns this merchant practice, providing human-readable organizational context.
 | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_GROUP_ID` | 15 | `NUMBER` | Foreign key reference to the organization group that the primary organization belongs to, enabling analysis at the highest organizational hierarchy level.
 | Foreign key reference to the organization group that the primary organization belongs to, enabling analysis at the highest organizational hierarchy level.
 | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_GROUP_NAME` | 16 | `TEXT` | Name of the organization group, providing human-readable context for the highest level of organizational hierarchy.
 | Name of the organization group, providing human-readable context for the highest level of organizational hierarchy.
 | `[]` | `{}` |
    | `APPLICATION_ID` | 17 | `NUMBER` | Foreign key reference to the specific application record. May be null for dates when no applications were created for a given merchant.
 | Foreign key reference to the specific application record. May be null for dates when no applications were created for a given merchant.
 | `[]` | `{}` |
    | `IS_PREQUAL` | 18 | `BOOLEAN` | Boolean flag indicating whether this application represents a pre-qualification rather than a full application, used for tracking lead qualification activities.
 | Boolean flag indicating whether this application represents a pre-qualification rather than a full application, used for tracking lead qualification activities.
 | `[]` | `{}` |
    | `SCHEDULE_STATUS` | 19 | `TEXT` | Status of any scheduled appointments or services associated with the application, relevant for applications tied to specific appointment bookings.
 | Status of any scheduled appointments or services associated with the application, relevant for applications tied to specific appointment bookings.
 | `[]` | `{}` |
    | `ACTIVE_LOAN_ID` | 20 | `NUMBER` | Foreign key reference to an active loan if the application has been approved and converted to a loan product.
 | Foreign key reference to an active loan if the application has been approved and converted to a loan product.
 | `[]` | `{}` |
    | `BALANCE_AVAILABLE` | 21 | `FLOAT` | Available credit balance for the borrower on this application, representing the amount they can access for financing.
 | Available credit balance for the borrower on this application, representing the amount they can access for financing.
 | `[]` | `{}` |
    | `MAX_ELIGIBLE` | 22 | `FLOAT` | Maximum amount the borrower is eligible to finance based on underwriting criteria and risk assessment.
 | Maximum amount the borrower is eligible to finance based on underwriting criteria and risk assessment.
 | `[]` | `{}` |
    | `APPLICATION_UPDATED_AT` | 23 | `TIMESTAMP_NTZ` | UTC timestamp when the application was last updated.
 | UTC timestamp when the application was last updated.
 | `[]` | `{}` |
    | `APPLICATION_UPDATED_AT_PT` | 24 | `TIMESTAMP_NTZ` | Pacific Time timestamp when the application was last updated.
 | Pacific Time timestamp when the application was last updated.
 | `[]` | `{}` |
    | `IS_IV_ALLOW_PAYSTUB` | 25 | `BOOLEAN` | Boolean flag indicating whether paystub verification is allowed for income verification on this application.
 | Boolean flag indicating whether paystub verification is allowed for income verification on this application.
 | `[]` | `{}` |
    | `ORGANIZATION_INDUSTRY` | 26 | `TEXT` | Industry classification at the organization level, may differ from practice-level industry classification for multi-industry organizations. | Industry classification at the organization level, may differ from practice-level industry classification for multi-industry organizations. | `[]` | `{}` |
    | `APPLICATION_EXPIRE_AT` | 27 | `TIMESTAMP_NTZ` | UTC timestamp when the application expires and is no longer valid for processing.
 | UTC timestamp when the application expires and is no longer valid for processing.
 | `[]` | `{}` |
    | `APPLICATION_EXPIRE_AT_PT` | 28 | `TIMESTAMP_NTZ` | Pacific Time timestamp when the application expires and is no longer valid for processing.
 | Pacific Time timestamp when the application expires and is no longer valid for processing.
 | `[]` | `{}` |
    | `REASON_CODES` | 29 | `TEXT` | Codes indicating reasons for application status changes, approvals, or denials, used for tracking decision rationale and compliance reporting.
 | Codes indicating reasons for application status changes, approvals, or denials, used for tracking decision rationale and compliance reporting.
 | `[]` | `{}` |
    | `VALIDITY` | 30 | `TEXT` | Validity status of the application, indicating whether the application meets basic requirements and constraints for processing.
 | Validity status of the application, indicating whether the application meets basic requirements and constraints for processing.
 | `[]` | `{}` |
    | `MENU_ID` | 31 | `NUMBER` | Foreign key reference to the product menu or treatment plan associated with the application, linking to specific services or products being financed.
 | Foreign key reference to the product menu or treatment plan associated with the application, linking to specific services or products being financed.
 | `[]` | `{}` |
    | `PRODUCT_OPTION_INDEX` | 32 | `NUMBER` | Index indicating which product option was selected from the available choices, used for tracking product preference and selection patterns.
 | Index indicating which product option was selected from the available choices, used for tracking product preference and selection patterns.
 | `[]` | `{}` |
    | `HAS_PRODUCTS_MANUALLY_EDITED` | 33 | `BOOLEAN` | Boolean flag indicating whether the product options or details were manually edited during the application process, either by the borrower or staff.
 | Boolean flag indicating whether the product options or details were manually edited during the application process, either by the borrower or staff.
 | `[]` | `{}` |
    | `RISK_SCORE` | 34 | `NUMBER` | Calculated risk score for the application, used in underwriting decisions and credit limit determinations.
 | Calculated risk score for the application, used in underwriting decisions and credit limit determinations.
 | `[]` | `{}` |
    | `APPLICATION_CREATED_AT` | 35 | `TIMESTAMP_NTZ` | UTC timestamp when the application was first created in the system.
 | UTC timestamp when the application was first created in the system.
 | `[]` | `{}` |
    | `APPLICATION_CREATED_AT_PT` | 36 | `TIMESTAMP_NTZ` | Pacific Time timestamp when the application was first created in the system.
 | Pacific Time timestamp when the application was first created in the system.
 | `[]` | `{}` |
    | `DISPLAY_ID` | 37 | `TEXT` | Human-readable identifier for the application, typically shown to users and customer service representatives.
 | Human-readable identifier for the application, typically shown to users and customer service representatives.
 | `[]` | `{}` |
    | `PURCHASE_AMOUNT` | 38 | `FLOAT` | Dollar amount of the purchase or service that the application is intended to finance.
 | Dollar amount of the purchase or service that the application is intended to finance.
 | `[]` | `{}` |
    | `BORROWER_ID` | 39 | `NUMBER` | Foreign key reference to the borrower who created the application.
 | Foreign key reference to the borrower who created the application.
 | `[]` | `{}` |
    | `SCHEDULED_AT` | 40 | `TIMESTAMP_NTZ` | Timestamp indicating when any associated services or appointments are scheduled to occur.
 | Timestamp indicating when any associated services or appointments are scheduled to occur.
 | `[]` | `{}` |
    | `IS_SELF_CHECKOUT` | 41 | `BOOLEAN` | Boolean flag indicating whether the application was submitted through a self-service checkout process without staff assistance.
 | Boolean flag indicating whether the application was submitted through a self-service checkout process without staff assistance.
 | `[]` | `{}` |
    | `IS_APPLICATION_START` | 42 | `BOOLEAN` | Boolean flag indicating whether this record represents the start of an application process. Always true in this model due to filtering criteria.
 | Boolean flag indicating whether this record represents the start of an application process. Always true in this model due to filtering criteria.
 | `[]` | `{}` |
    | `IS_APPLICATION_COMPLETION` | 43 | `BOOLEAN` | Boolean flag indicating whether the application process was completed by the borrower, distinguishing between started and completed applications.
 | Boolean flag indicating whether the application process was completed by the borrower, distinguishing between started and completed applications.
 | `[]` | `{}` |
    | `APPLICATION_STATUS` | 44 | `TEXT` | Current status of the application (e.g., approved, pending, denied), indicating the application's position in the review and approval process.
 | Current status of the application (e.g., approved, pending, denied), indicating the application's position in the review and approval process.
 | `[]` | `{}` |
    | `API_PARTNER` | 45 | `TEXT` | Identifier for the API partner or integration source that originated the application, used for tracking application sources and partner performance.
 | Identifier for the API partner or integration source that originated the application, used for tracking application sources and partner performance.
 | `[]` | `{}` |
    | `CHANNEL` | 46 | `TEXT` | Channel through which the application was submitted (e.g., web, mobile, in-person), used for analyzing application source effectiveness.
 | Channel through which the application was submitted (e.g., web, mobile, in-person), used for analyzing application source effectiveness.
 | `[]` | `{}` |
    | `IP_ADDRESS` | 47 | `TEXT` | IP address from which the application was submitted, used for fraud detection and geographic analysis.
 | IP address from which the application was submitted, used for fraud detection and geographic analysis.
 | `[]` | `{}` |
    | `APPROVAL_EXTENDED` | 48 | `BOOLEAN` | Information about any extensions granted to the application approval period, used for tracking approval timeline modifications.
 | Information about any extensions granted to the application approval period, used for tracking approval timeline modifications.
 | `[]` | `{}` |
    | `CREDIT_LINE_INCREASE` | 49 | `TEXT` | Information about any credit line increases applied to the application, used for tracking credit enhancement activities.
 | Information about any credit line increases applied to the application, used for tracking credit enhancement activities.
 | `[]` | `{}` |
    | `APPLICATION_FEATURE_SOURCE` | 50 | `TEXT` | Source system or feature that generated the application, providing context about the application origination point within the platform.
 | Source system or feature that generated the application, providing context about the application origination point within the platform.
 | `[]` | `{}` |
    | `APPLICATION_FEATURE_PHONE_NUMBER` | 51 | `TEXT` | Phone number associated with the application feature or source, used for contact and verification purposes.
 | Phone number associated with the application feature or source, used for contact and verification purposes.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt_utils.generate_surrogate_key`
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.int_applications_collapsed`
    *   `model.cherry_data_model.practice_info_xf`

---
