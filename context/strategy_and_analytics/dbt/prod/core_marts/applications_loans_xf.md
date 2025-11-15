## Model: `applications_loans_xf`

`applications_loans_xf`

*   **Unique ID:** `model.cherry_data_model.applications_loans_xf`
*   **FQN:** `prod.core_marts.applications_loans_xf`
*   **Description:** **Comprehensive Application-Loan Bridge Table for Core Analytics**
This model creates a comprehensive bridge between applications and loans, providing one record  for every loan with complete application context. It serves as the foundational dataset for  calculating approval rates, funding rates, conversion metrics, and loan performance analytics  across Cherry's lending operations.
**Key Business Logic:** - **Transferable Application Handling**: Uses `int_applications_collapsed` to properly handle 
  parent-child application relationships where applications can be transferred between merchants
- **Demo Filtering**: Excludes all demo applications and loans to ensure production data integrity - **Merchant Hierarchy**: Integrates primary merchant and organization mapping for multi-location analysis - **Timestamp Enrichment**: Adds comprehensive application and loan lifecycle timestamps - **Checkout Journey**: Tracks complete checkout flow from start to completion with timing metrics - **Risk Integration**: Includes credit scores and risk assessment data
**Data Sources:** - `int_applications_collapsed`: Deduplicated applications with transferable application logic - `src_cherry_loans`: Core loan data from Cherry's loan service database - `stg_loan_product_aprs`: Original loan terms and APR calculations including promotional rates - `merchant_account_mapping`: Primary merchant and Salesforce account relationships - `risk_applications`: Credit scores and risk assessment data - `src_cherry_applications_status_history`: Application approval and completion timestamps
**Primary Use Cases:** - Approval rate and conversion funnel analysis - Loan performance and risk analytics - Merchant and organizational performance tracking - Product mix and pricing analysis - Customer journey and checkout optimization

*   **Tags:** `['core', 'core_applications_loans', 'core_hourly']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `UNIQUE_ID` | 1 | `TEXT` | Surrogate key uniquely identifying each application-loan record, generated from the combination  of application_id and loan_id. Serves as the primary key ensuring uniqueness across the  application-loan relationship table.
 | Surrogate key uniquely identifying each application-loan record, generated from the combination  of application_id and loan_id. Serves as the primary key ensuring uniqueness across the  application-loan relationship table.
 | `[]` | `{}` |
    | `APPLICATION_ID` | 2 | `NUMBER` | **Application Identifier** - Foreign key reference to Cherry's application system. Links to  the specific credit application submitted by the borrower. Each application can result in  multiple loans, making this a many-to-one relationship from the loan perspective.
 | **Application Identifier** - Foreign key reference to Cherry's application system. Links to  the specific credit application submitted by the borrower. Each application can result in  multiple loans, making this a many-to-one relationship from the loan perspective.
 | `[]` | `{}` |
    | `PARENT_APPLICATION_ID` | 3 | `NUMBER` | **Parent Application Identifier** - References the original parent application when transferable  applications are involved. NULL for non-transferable applications. Used to track application  lineage when applications are transferred between merchants during the approval process.
 | **Parent Application Identifier** - References the original parent application when transferable  applications are involved. NULL for non-transferable applications. Used to track application  lineage when applications are transferred between merchants during the approval process.
 | `[]` | `{}` |
    | `PARENT_APPLICATION_ID_FILLED` | 4 | `NUMBER` | **Resolved Parent Application Identifier** - Either the parent_application_id (for transferable  applications) or the application_id itself (for non-transferable applications). Provides a  consistent identifier for application grouping regardless of transferable status, derived  from int_applications_collapsed logic.
 | **Resolved Parent Application Identifier** - Either the parent_application_id (for transferable  applications) or the application_id itself (for non-transferable applications). Provides a  consistent identifier for application grouping regardless of transferable status, derived  from int_applications_collapsed logic.
 | `[]` | `{}` |
    | `LOAN_ID` | 5 | `NUMBER` | **Loan Identifier** - Foreign key reference to Cherry's loan system. Links to the specific  loan created from the application. NULL when no loan was created (application without checkout).  Each loan belongs to exactly one application.
 | **Loan Identifier** - Foreign key reference to Cherry's loan system. Links to the specific  loan created from the application. NULL when no loan was created (application without checkout).  Each loan belongs to exactly one application.
 | `[]` | `{}` |
    | `CONTRACT_ID` | 6 | `TEXT` | **Loan Contract Identifier** - Human-readable contract ID used in customer communications  and legal documentation (sourced from loan display_id field). Represents the legal contract  between Cherry and the borrower. NULL when no loan exists.
 | **Loan Contract Identifier** - Human-readable contract ID used in customer communications  and legal documentation (sourced from loan display_id field). Represents the legal contract  between Cherry and the borrower. NULL when no loan exists.
 | `[]` | `{}` |
    | `DISPLAY_ID` | 7 | `TEXT` | **Application Display Identifier** - Human-readable application identifier used in customer  communications and support operations. Provides a user-friendly reference for application  tracking and customer service interactions.
 | **Application Display Identifier** - Human-readable application identifier used in customer  communications and support operations. Provides a user-friendly reference for application  tracking and customer service interactions.
 | `[]` | `{}` |
    | `BORROWER_ID` | 8 | `NUMBER` | **Borrower Identifier** - Foreign key reference to Cherry's borrower system. Links to the  individual who submitted the application. Used for borrower-level analytics, credit history  tracking, and customer relationship management. Sourced from application data.
 | **Borrower Identifier** - Foreign key reference to Cherry's borrower system. Links to the  individual who submitted the application. Used for borrower-level analytics, credit history  tracking, and customer relationship management. Sourced from application data.
 | `[]` | `{}` |
    | `ORGANIZATION_ID` | 9 | `NUMBER` | **Application Organization Identifier** - Organization where the application was originally  submitted. May differ from loan organization for transferable applications. Used for application  source tracking and organizational performance analysis.
 | **Application Organization Identifier** - Organization where the application was originally  submitted. May differ from loan organization for transferable applications. Used for application  source tracking and organizational performance analysis.
 | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_ID` | 10 | `NUMBER` | **Primary Organization Identifier** - Standardized organization identifier used for consistent  organizational grouping. Derived from merchant_account_mapping to handle multi-location practices  and organizational hierarchies consistently across applications and loans.
 | **Primary Organization Identifier** - Standardized organization identifier used for consistent  organizational grouping. Derived from merchant_account_mapping to handle multi-location practices  and organizational hierarchies consistently across applications and loans.
 | `[]` | `{}` |
    | `MERCHANT_ID` | 11 | `NUMBER` | **Merchant Identifier** - The specific merchant location associated with the loan (preferred)  or application. Uses COALESCE(loans.merchant_id, applications.merchant_id) to prioritize  loan-level merchant data when available, falling back to application merchant for non-funded applications.
 | **Merchant Identifier** - The specific merchant location associated with the loan (preferred)  or application. Uses COALESCE(loans.merchant_id, applications.merchant_id) to prioritize  loan-level merchant data when available, falling back to application merchant for non-funded applications.
 | `[]` | `{}` |
    | `PRIMARY_MERCHANT_ID` | 12 | `FLOAT` | **Primary Merchant Identifier** - Standardized merchant identifier for multi-location practice  grouping. Derived from merchant_account_mapping to provide consistent merchant grouping across  different data sources and handle Salesforce account relationships.
 | **Primary Merchant Identifier** - Standardized merchant identifier for multi-location practice  grouping. Derived from merchant_account_mapping to provide consistent merchant grouping across  different data sources and handle Salesforce account relationships.
 | `[]` | `{}` |
    | `SF_ACCOUNT_ID` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `ACTIVE_LOAN_ID` | 14 | `NUMBER` | **Active Loan Reference** - References the currently active loan for the borrower within  the organization. Used for credit line management and determining available balance for  additional lending. Sourced from application data.
 | **Active Loan Reference** - References the currently active loan for the borrower within  the organization. Used for credit line management and determining available balance for  additional lending. Sourced from application data.
 | `[]` | `{}` |
    | `MENU_ID` | 15 | `NUMBER` | **Product Menu Identifier** - Foreign key reference to the pricing menu used for the application.  Determines available loan products, terms, and pricing options presented to the borrower.  Sourced from application data.
 | **Product Menu Identifier** - Foreign key reference to the pricing menu used for the application.  Determines available loan products, terms, and pricing options presented to the borrower.  Sourced from application data.
 | `[]` | `{}` |
    | `INSTALLMENT_PAYMENT_METHOD_ID` | 16 | `NUMBER` | **Installment Payment Method Identifier** - Foreign key reference to the payment method  used for recurring loan payments (e.g., bank account, card). NULL for non-funded loans.  Critical for payment processing and collections operations.
 | **Installment Payment Method Identifier** - Foreign key reference to the payment method  used for recurring loan payments (e.g., bank account, card). NULL for non-funded loans.  Critical for payment processing and collections operations.
 | `[]` | `{}` |
    | `DOWN_PAYMENT_PAYMENT_METHOD_ID` | 17 | `NUMBER` | **Down Payment Method Identifier** - Foreign key reference to the payment method used for  the initial down payment. NULL when no down payment was required or for non-funded loans.  Used for payment processing and reconciliation.
 | **Down Payment Method Identifier** - Foreign key reference to the payment method used for  the initial down payment. NULL when no down payment was required or for non-funded loans.  Used for payment processing and reconciliation.
 | `[]` | `{}` |
    | `PRODUCT_ID` | 18 | `NUMBER` | **Product Identifier** - Foreign key reference to the specific loan product selected.  Determines loan terms, APR, fees, and repayment structure. NULL for non-funded loans.  Critical for product performance analysis and risk management.
 | **Product Identifier** - Foreign key reference to the specific loan product selected.  Determines loan terms, APR, fees, and repayment structure. NULL for non-funded loans.  Critical for product performance analysis and risk management.
 | `[]` | `{}` |
    | `ORGANIZATION_INDUSTRY` | 19 | `TEXT` | **Organization Industry Classification** - Industry category of the practice where the  application was submitted (e.g., 'Dental', 'Medical', 'Veterinary'). Sourced from application  data and used for industry-specific performance analysis and risk assessment.
 | **Organization Industry Classification** - Industry category of the practice where the  application was submitted (e.g., 'Dental', 'Medical', 'Veterinary'). Sourced from application  data and used for industry-specific performance analysis and risk assessment.
 | `[]` | `{}` |
    | `APPLICATION_INDUSTRY_SEGMENT` | 20 | `TEXT` | **Application Industry Segment** - Standardized industry segment grouping used for resource  allocation and performance analysis. Derived from merchant account industry segment with  fallback logic to organization-level segments for consistent categorization.
 | **Application Industry Segment** - Standardized industry segment grouping used for resource  allocation and performance analysis. Derived from merchant account industry segment with  fallback logic to organization-level segments for consistent categorization.
 | `[]` | `{}` |
    | `GO_LIVE_DATE` | 21 | `DATE` | **Merchant Go-Live Date** - Date when the merchant became operational and started processing  applications. Used for merchant maturity analysis, performance benchmarking, and filtering  metrics to operational periods. Sourced from merchant data.
 | **Merchant Go-Live Date** - Date when the merchant became operational and started processing  applications. Used for merchant maturity analysis, performance benchmarking, and filtering  metrics to operational periods. Sourced from merchant data.
 | `[]` | `{}` |
    | `SCHEDULE_STATUS` | 22 | `TEXT` | **Application Schedule Status** - Indicates the scheduling status of the application within  Cherry's workflow (e.g., 'SCHEDULED', 'UNSCHEDULED'). Used for application processing  management and workflow optimization. Sourced from application data.
 | **Application Schedule Status** - Indicates the scheduling status of the application within  Cherry's workflow (e.g., 'SCHEDULED', 'UNSCHEDULED'). Used for application processing  management and workflow optimization. Sourced from application data.
 | `[]` | `{}` |
    | `REASON_CODES` | 23 | `TEXT` | **Application Reason Codes** - Structured codes indicating specific reasons for application  outcomes (approvals, denials, special conditions). Used for decision analysis, compliance  reporting, and underwriting optimization. Sourced from application data.
 | **Application Reason Codes** - Structured codes indicating specific reasons for application  outcomes (approvals, denials, special conditions). Used for decision analysis, compliance  reporting, and underwriting optimization. Sourced from application data.
 | `[]` | `{}` |
    | `VALIDITY` | 24 | `TEXT` | **Application Validity Status** - Indicates whether the application data is considered  valid for processing and analysis. Used for data quality control and filtering invalid  applications from performance metrics. Sourced from application data.
 | **Application Validity Status** - Indicates whether the application data is considered  valid for processing and analysis. Used for data quality control and filtering invalid  applications from performance metrics. Sourced from application data.
 | `[]` | `{}` |
    | `APPLICATION_STATUS` | 25 | `TEXT` | **Application Final Status** - Current status of the application (e.g., 'APPROVED', 'DENIED',  'UNLICENSED', 'FROZEN'). Represents the final underwriting decision and is used for approval  rate calculations and application outcome analysis. Sourced from application data.
 | **Application Final Status** - Current status of the application (e.g., 'APPROVED', 'DENIED',  'UNLICENSED', 'FROZEN'). Represents the final underwriting decision and is used for approval  rate calculations and application outcome analysis. Sourced from application data.
 | `[]` | `{}` |
    | `PRODUCT_OPTION_INDEX` | 26 | `NUMBER` | **Product Option Selection Index** - Numeric index indicating which product option the  borrower selected from the available menu. Used for product selection analysis and understanding  borrower preferences within product offerings. Sourced from application data.
 | **Product Option Selection Index** - Numeric index indicating which product option the  borrower selected from the available menu. Used for product selection analysis and understanding  borrower preferences within product offerings. Sourced from application data.
 | `[]` | `{}` |
    | `API_PARTNER` | 27 | `TEXT` | **API Partner Identifier** - Identifies the partner or integration source when applications  come through API integrations rather than direct Cherry interfaces. Used for partner  performance analysis and integration management. Sourced from application data.
 | **API Partner Identifier** - Identifies the partner or integration source when applications  come through API integrations rather than direct Cherry interfaces. Used for partner  performance analysis and integration management. Sourced from application data.
 | `[]` | `{}` |
    | `CHANNEL` | 28 | `TEXT` | **Application Channel** - The channel through which the application was submitted  (e.g., 'WEB', 'MOBILE', 'API'). Used for channel performance analysis and user experience  optimization. Can be sourced from either application or loan data.
 | **Application Channel** - The channel through which the application was submitted  (e.g., 'WEB', 'MOBILE', 'API'). Used for channel performance analysis and user experience  optimization. Can be sourced from either application or loan data.
 | `[]` | `{}` |
    | `IP_ADDRESS` | 29 | `TEXT` | **Application IP Address** - IP address from which the application was submitted. Used for  fraud detection, geographic analysis, and compliance purposes. Sourced from application data  and may be NULL for privacy or technical reasons.
 | **Application IP Address** - IP address from which the application was submitted. Used for  fraud detection, geographic analysis, and compliance purposes. Sourced from application data  and may be NULL for privacy or technical reasons.
 | `[]` | `{}` |
    | `APPLICATION_FEATURE_SOURCE` | 30 | `TEXT` | **Application Feature Source** - Indicates the source system or feature flag that influenced  the application processing. Used for A/B testing analysis and feature performance evaluation.  Sourced from application data.
 | **Application Feature Source** - Indicates the source system or feature flag that influenced  the application processing. Used for A/B testing analysis and feature performance evaluation.  Sourced from application data.
 | `[]` | `{}` |
    | `APPLICATION_FEATURE_PHONE_NUMBER` | 31 | `TEXT` | **Application Feature Phone Number** - Phone number associated with application feature  tracking or routing. Used for feature-specific communication routing and analysis.  Sourced from application data.
 | **Application Feature Phone Number** - Phone number associated with application feature  tracking or routing. Used for feature-specific communication routing and analysis.  Sourced from application data.
 | `[]` | `{}` |
    | `SOURCE_TYPE` | 32 | `TEXT` | **Application Source Type** - High-level categorization of how the application was initiated  (e.g., 'DIRECT', 'REFERRAL', 'INTEGRATION'). Used for marketing attribution and channel  analysis. Derived from int_applications_collapsed with transferable application logic.
 | **Application Source Type** - High-level categorization of how the application was initiated  (e.g., 'DIRECT', 'REFERRAL', 'INTEGRATION'). Used for marketing attribution and channel  analysis. Derived from int_applications_collapsed with transferable application logic.
 | `[]` | `{}` |
    | `SOURCE_CATEGORY` | 33 | `TEXT` | **Application Source Category** - More specific categorization within the source type,  providing additional detail about application origin. Used for detailed marketing attribution  and performance analysis. Derived from int_applications_collapsed.
 | **Application Source Category** - More specific categorization within the source type,  providing additional detail about application origin. Used for detailed marketing attribution  and performance analysis. Derived from int_applications_collapsed.
 | `[]` | `{}` |
    | `SOURCE_SUBCATEGORY` | 34 | `TEXT` | **Application Source Subcategory** - Most granular level of source classification, providing  detailed information about application origin. Used for precise marketing attribution and  conversion analysis. Derived from int_applications_collapsed.
 | **Application Source Subcategory** - Most granular level of source classification, providing  detailed information about application origin. Used for precise marketing attribution and  conversion analysis. Derived from int_applications_collapsed.
 | `[]` | `{}` |
    | `REFERRAL_MEDIUM` | 35 | `TEXT` | **Referral Medium** - The medium through which the referral was made (e.g., 'EMAIL', 'SMS',  'SOCIAL'). Used for referral program analysis and marketing channel optimization.  Sourced from application data.
 | **Referral Medium** - The medium through which the referral was made (e.g., 'EMAIL', 'SMS',  'SOCIAL'). Used for referral program analysis and marketing channel optimization.  Sourced from application data.
 | `[]` | `{}` |
    | `REFERRAL_SOURCE` | 36 | `TEXT` | **Referral Source** - Specific source of the referral or marketing campaign. Used for  detailed marketing attribution, campaign performance analysis, and referral program tracking.  Derived from int_applications_collapsed.
 | **Referral Source** - Specific source of the referral or marketing campaign. Used for  detailed marketing attribution, campaign performance analysis, and referral program tracking.  Derived from int_applications_collapsed.
 | `[]` | `{}` |
    | `FLOW_TYPE` | 37 | `TEXT` | **Application Flow Type** - Indicates the specific application flow used (e.g., 'HIGH_LINE',  'STANDARD'). Determines the underwriting path and credit limit evaluation process.  Sourced from application data.
 | **Application Flow Type** - Indicates the specific application flow used (e.g., 'HIGH_LINE',  'STANDARD'). Determines the underwriting path and credit limit evaluation process.  Sourced from application data.
 | `[]` | `{}` |
    | `REQUIRED_HIGH_LINE_FLOW` | 38 | `BOOLEAN` | **High Line Flow Required** - Boolean flag indicating whether the application required the  high credit line flow (TRUE when flow_type='HIGH_LINE'). Used for underwriting process  analysis and high-value application tracking.
 | **High Line Flow Required** - Boolean flag indicating whether the application required the  high credit line flow (TRUE when flow_type='HIGH_LINE'). Used for underwriting process  analysis and high-value application tracking.
 | `[]` | `{}` |
    | `STATED_INFO_STATUS` | 39 | `TEXT` | **Stated Information Status** - Status of stated income and employment information provided  by the borrower. Used for income verification workflow management and compliance tracking.  Sourced from application data.
 | **Stated Information Status** - Status of stated income and employment information provided  by the borrower. Used for income verification workflow management and compliance tracking.  Sourced from application data.
 | `[]` | `{}` |
    | `STATED_INCOME` | 40 | `TEXT` | **Stated Annual Income** - Borrower's self-reported annual income in dollars. Used for  debt-to-income calculations, risk assessment, and underwriting decisions. NULL when not  provided. Sourced from application data.
 | **Stated Annual Income** - Borrower's self-reported annual income in dollars. Used for  debt-to-income calculations, risk assessment, and underwriting decisions. NULL when not  provided. Sourced from application data.
 | `[]` | `{}` |
    | `STATED_HOUSING_PAYMENT` | 41 | `TEXT` | **Stated Monthly Housing Payment** - Borrower's self-reported monthly housing payment in dollars.  Used for debt-to-income calculations and affordability analysis. NULL when not provided.  Sourced from application data.
 | **Stated Monthly Housing Payment** - Borrower's self-reported monthly housing payment in dollars.  Used for debt-to-income calculations and affordability analysis. NULL when not provided.  Sourced from application data.
 | `[]` | `{}` |
    | `RETAIL_INSTALLMENT_CONTRACT` | 42 | `BOOLEAN` | **Retail Installment Contract Flag** - Indicates whether this application uses a retail  installment contract structure. Used for contract type analysis and regulatory compliance.  Sourced from application data.
 | **Retail Installment Contract Flag** - Indicates whether this application uses a retail  installment contract structure. Used for contract type analysis and regulatory compliance.  Sourced from application data.
 | `[]` | `{}` |
    | `LOAN_STATUS` | 43 | `TEXT` | **Loan Status** - Current status of the loan (e.g., 'FUNDED', 'AWAITING_FUNDING', 'CANCELLED').  Indicates the loan's position in the funding and lifecycle process. NULL for applications  without loans. Critical for loan performance and operational analysis.
 | **Loan Status** - Current status of the loan (e.g., 'FUNDED', 'AWAITING_FUNDING', 'CANCELLED').  Indicates the loan's position in the funding and lifecycle process. NULL for applications  without loans. Critical for loan performance and operational analysis.
 | `[]` | `{}` |
    | `CREATED_BY` | 44 | `NUMBER` | **Loan Creator** - Identifier of the user or system that created the loan record. Used for  loan origination tracking and operational analysis. NULL for applications without loans.  Sourced from loan data.
 | **Loan Creator** - Identifier of the user or system that created the loan record. Used for  loan origination tracking and operational analysis. NULL for applications without loans.  Sourced from loan data.
 | `[]` | `{}` |
    | `UPDATED_BY` | 45 | `NUMBER` | **Loan Last Updated By** - Identifier of the user or system that last updated the loan record.  Used for change tracking and operational auditing. NULL for applications without loans.  Sourced from loan data.
 | **Loan Last Updated By** - Identifier of the user or system that last updated the loan record.  Used for change tracking and operational auditing. NULL for applications without loans.  Sourced from loan data.
 | `[]` | `{}` |
    | `PROMO_USED` | 46 | `BOOLEAN` | **Promotional Rate Used** - Boolean flag indicating whether a promotional interest rate  was applied to the loan. Used for promotional campaign analysis and pricing strategy evaluation.  NULL for applications without loans. Sourced from loan data.
 | **Promotional Rate Used** - Boolean flag indicating whether a promotional interest rate  was applied to the loan. Used for promotional campaign analysis and pricing strategy evaluation.  NULL for applications without loans. Sourced from loan data.
 | `[]` | `{}` |
    | `LOAN_SUB_STATUS` | 47 | `TEXT` | **Loan Sub-Status** - More granular status information providing additional context about  the loan's current state. Used for detailed operational tracking and loan management.  NULL for applications without loans. Sourced from loan data.
 | **Loan Sub-Status** - More granular status information providing additional context about  the loan's current state. Used for detailed operational tracking and loan management.  NULL for applications without loans. Sourced from loan data.
 | `[]` | `{}` |
    | `MENU_NAME` | 48 | `TEXT` | **Product Menu Name** - Human-readable name of the pricing menu used for the application.  Provides context about the product offering and pricing tier. Sourced from application data  through menu_id relationship.
 | **Product Menu Name** - Human-readable name of the pricing menu used for the application.  Provides context about the product offering and pricing tier. Sourced from application data  through menu_id relationship.
 | `[]` | `{}` |
    | `ORIGINAL_LOAN_TERM` | 49 | `NUMBER` | **Original Loan Term** - Original loan term in months at loan origination. Derived from  stg_loan_product_aprs with adjustments for biweekly payment frequencies (term/2). Used for  loan product analysis and performance tracking. NULL for applications without loans.
 | **Original Loan Term** - Original loan term in months at loan origination. Derived from  stg_loan_product_aprs with adjustments for biweekly payment frequencies (term/2). Used for  loan product analysis and performance tracking. NULL for applications without loans.
 | `[]` | `{}` |
    | `IS_PAY_IN_FOUR` | 50 | `BOOLEAN` | **Pay-in-Four Product Flag** - Boolean flag indicating whether this is a pay-in-four product  (TRUE when original_loan_term = 1.5 months). Used for product-specific analysis and short-term  lending performance tracking.
 | **Pay-in-Four Product Flag** - Boolean flag indicating whether this is a pay-in-four product  (TRUE when original_loan_term = 1.5 months). Used for product-specific analysis and short-term  lending performance tracking.
 | `[]` | `{}` |
    | `ORIGINAL_APR` | 51 | `FLOAT` | **Original APR** - Annual Percentage Rate at loan origination as a decimal (e.g., 0.1899 for 18.99%).  Includes promotional rate logic where applicable. Used for pricing analysis and risk assessment.  NULL for applications without loans. Sourced from stg_loan_product_aprs.
 | **Original APR** - Annual Percentage Rate at loan origination as a decimal (e.g., 0.1899 for 18.99%).  Includes promotional rate logic where applicable. Used for pricing analysis and risk assessment.  NULL for applications without loans. Sourced from stg_loan_product_aprs.
 | `[]` | `{}` |
    | `CURRENT_APR` | 52 | `FLOAT` | **Current APR** - Current Annual Percentage Rate as a decimal, which may differ from original  APR due to rate changes. Used for current loan pricing analysis and revenue calculations.  NULL for applications without loans. Sourced from int_funded_information_pt.
 | **Current APR** - Current Annual Percentage Rate as a decimal, which may differ from original  APR due to rate changes. Used for current loan pricing analysis and revenue calculations.  NULL for applications without loans. Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `APPLICATION_UPDATED_AT` | 53 | `TIMESTAMP_NTZ` | **Application Last Updated** - UTC timestamp when the application was last modified. Used for  application processing timeline analysis and data freshness tracking. Sourced from application data.
 | **Application Last Updated** - UTC timestamp when the application was last modified. Used for  application processing timeline analysis and data freshness tracking. Sourced from application data.
 | `[]` | `{}` |
    | `APPLICATION_UPDATED_AT_PT` | 54 | `TIMESTAMP_NTZ` | **Application Last Updated (Pacific Time)** - Pacific timezone version of application_updated_at.  Used for business hour analysis and operational reporting in Cherry's primary timezone.
 | **Application Last Updated (Pacific Time)** - Pacific timezone version of application_updated_at.  Used for business hour analysis and operational reporting in Cherry's primary timezone.
 | `[]` | `{}` |
    | `EXPIRE_AT` | 55 | `TIMESTAMP_NTZ` | **Application Expiration Time** - UTC timestamp when the application approval expires and  becomes invalid. Used for application lifecycle management and expired approval analysis.  NULL for non-expiring applications.
 | **Application Expiration Time** - UTC timestamp when the application approval expires and  becomes invalid. Used for application lifecycle management and expired approval analysis.  NULL for non-expiring applications.
 | `[]` | `{}` |
    | `EXPIRE_AT_PT` | 56 | `TIMESTAMP_NTZ` | **Application Expiration Time (Pacific Time)** - Pacific timezone version of expire_at.  Used for operational management and time-sensitive application processing.
 | **Application Expiration Time (Pacific Time)** - Pacific timezone version of expire_at.  Used for operational management and time-sensitive application processing.
 | `[]` | `{}` |
    | `APPLICATION_CREATED_AT` | 57 | `TIMESTAMP_NTZ` | **Application Creation Time** - UTC timestamp when the application was first created.  Represents the start of the borrower's journey and is used for application volume analysis  and conversion funnel timing.
 | **Application Creation Time** - UTC timestamp when the application was first created.  Represents the start of the borrower's journey and is used for application volume analysis  and conversion funnel timing.
 | `[]` | `{}` |
    | `APPLICATION_CREATED_AT_PT` | 58 | `TIMESTAMP_NTZ` | **Application Creation Time (Pacific Time)** - Pacific timezone version of application_created_at.  Used for business hour analysis and operational reporting in Cherry's primary timezone.
 | **Application Creation Time (Pacific Time)** - Pacific timezone version of application_created_at.  Used for business hour analysis and operational reporting in Cherry's primary timezone.
 | `[]` | `{}` |
    | `SCHEDULED_AT` | 59 | `TIMESTAMP_NTZ` | **Application Scheduled Time** - Timestamp when the application was scheduled for processing  or review. Used for workflow management and application processing timeline analysis.  NULL for unscheduled applications.
 | **Application Scheduled Time** - Timestamp when the application was scheduled for processing  or review. Used for workflow management and application processing timeline analysis.  NULL for unscheduled applications.
 | `[]` | `{}` |
    | `ORIGINAL_CLOSED_AT` | 60 | `DATE` | **Loan Original Close Time** - Original planned or expected loan closure timestamp. May differ  from actual closure due to modifications or extensions. Used for loan lifecycle planning  and timeline analysis. NULL for applications without loans.
 | **Loan Original Close Time** - Original planned or expected loan closure timestamp. May differ  from actual closure due to modifications or extensions. Used for loan lifecycle planning  and timeline analysis. NULL for applications without loans.
 | `[]` | `{}` |
    | `LOAN_CREATED_AT` | 61 | `TIMESTAMP_NTZ` | **Loan Creation Time** - UTC timestamp when the loan record was created. Represents the  start of the checkout process and is used for conversion timing analysis. NULL for  applications without loans.
 | **Loan Creation Time** - UTC timestamp when the loan record was created. Represents the  start of the checkout process and is used for conversion timing analysis. NULL for  applications without loans.
 | `[]` | `{}` |
    | `LOAN_CREATED_AT_PT` | 62 | `TIMESTAMP_NTZ` | **Loan Creation Time (Pacific Time)** - Pacific timezone version of loan_created_at.  Used for business hour analysis and operational reporting in Cherry's primary timezone.
 | **Loan Creation Time (Pacific Time)** - Pacific timezone version of loan_created_at.  Used for business hour analysis and operational reporting in Cherry's primary timezone.
 | `[]` | `{}` |
    | `LOAN_UPDATED_AT` | 63 | `TIMESTAMP_NTZ` | **Loan Last Updated** - UTC timestamp when the loan was last modified. Used for loan  processing timeline analysis and operational tracking. NULL for applications without loans.
 | **Loan Last Updated** - UTC timestamp when the loan was last modified. Used for loan  processing timeline analysis and operational tracking. NULL for applications without loans.
 | `[]` | `{}` |
    | `LOAN_UPDATED_AT_PT` | 64 | `TIMESTAMP_NTZ` | **Loan Last Updated (Pacific Time)** - Pacific timezone version of loan_updated_at.  Used for operational management and loan processing analysis in Cherry's primary timezone.
 | **Loan Last Updated (Pacific Time)** - Pacific timezone version of loan_updated_at.  Used for operational management and loan processing analysis in Cherry's primary timezone.
 | `[]` | `{}` |
    | `FUNDED_AT` | 65 | `TIMESTAMP_NTZ` | **Loan Funding Time** - UTC timestamp when the loan was successfully funded and funds  were disbursed. Critical for funding rate analysis and revenue recognition timing.  NULL for unfunded loans.
 | **Loan Funding Time** - UTC timestamp when the loan was successfully funded and funds  were disbursed. Critical for funding rate analysis and revenue recognition timing.  NULL for unfunded loans.
 | `[]` | `{}` |
    | `FUNDED_AT_PT` | 66 | `TIMESTAMP_NTZ` | **Loan Funding Time (Pacific Time)** - Pacific timezone version of funded_at. Used for  business hour analysis and operational reporting in Cherry's primary timezone.
 | **Loan Funding Time (Pacific Time)** - Pacific timezone version of funded_at. Used for  business hour analysis and operational reporting in Cherry's primary timezone.
 | `[]` | `{}` |
    | `COMPLETED_AT` | 67 | `TIMESTAMP_NTZ` | **Application Completion Time** - UTC timestamp when the application reached a final  status (APPROVED, DENIED, UNLICENSED, FROZEN). Used for application processing time analysis  and completion rate calculations.
 | **Application Completion Time** - UTC timestamp when the application reached a final  status (APPROVED, DENIED, UNLICENSED, FROZEN). Used for application processing time analysis  and completion rate calculations.
 | `[]` | `{}` |
    | `COMPLETED_AT_PT` | 68 | `TIMESTAMP_NTZ` | **Application Completion Time (Pacific Time)** - Pacific timezone version of completed_at.  Used for business hour analysis and application processing efficiency metrics.
 | **Application Completion Time (Pacific Time)** - Pacific timezone version of completed_at.  Used for business hour analysis and application processing efficiency metrics.
 | `[]` | `{}` |
    | `APPROVED_AT` | 69 | `TIMESTAMP_NTZ` | **Application Approval Time** - UTC timestamp when the application was approved. Used for  approval timing analysis and underwriting process optimization. NULL for non-approved applications.
 | **Application Approval Time** - UTC timestamp when the application was approved. Used for  approval timing analysis and underwriting process optimization. NULL for non-approved applications.
 | `[]` | `{}` |
    | `APPROVED_AT_PT` | 70 | `TIMESTAMP_NTZ` | **Application Approval Time (Pacific Time)** - Pacific timezone version of approved_at.  Used for business hour analysis and approval process timing in Cherry's primary timezone.
 | **Application Approval Time (Pacific Time)** - Pacific timezone version of approved_at.  Used for business hour analysis and approval process timing in Cherry's primary timezone.
 | `[]` | `{}` |
    | `CHECKOUT_START_PT` | 71 | `TIMESTAMP_NTZ` | **Checkout Start Time (Pacific Time)** - Timestamp when the borrower began the checkout  process (checkout landing page load). Used for checkout funnel analysis and conversion  timing. NULL when no checkout was started.
 | **Checkout Start Time (Pacific Time)** - Timestamp when the borrower began the checkout  process (checkout landing page load). Used for checkout funnel analysis and conversion  timing. NULL when no checkout was started.
 | `[]` | `{}` |
    | `CHECKOUT_END_PT` | 72 | `TIMESTAMP_NTZ` | **Checkout Completion Time (Pacific Time)** - Timestamp when the borrower completed checkout  (post-funding page load for funded loans). Used for checkout completion analysis and  funnel optimization. NULL for incomplete checkouts.
 | **Checkout Completion Time (Pacific Time)** - Timestamp when the borrower completed checkout  (post-funding page load for funded loans). Used for checkout completion analysis and  funnel optimization. NULL for incomplete checkouts.
 | `[]` | `{}` |
    | `APPLICATION_TIME_TO_COMPLETE_SEC` | 73 | `NUMBER` | **Application Processing Time (Seconds)** - Time elapsed from application creation to  completion in seconds. Used for processing efficiency analysis and customer experience  optimization. NULL for incomplete applications.
 | **Application Processing Time (Seconds)** - Time elapsed from application creation to  completion in seconds. Used for processing efficiency analysis and customer experience  optimization. NULL for incomplete applications.
 | `[]` | `{}` |
    | `CHECKOUT_TIME_TO_COMPLETE_SEC` | 74 | `NUMBER` | **Checkout Processing Time (Seconds)** - Time elapsed from checkout start to completion  in seconds. Used for checkout optimization and user experience analysis. NULL for  incomplete checkouts or when checkout_end <= checkout_start.
 | **Checkout Processing Time (Seconds)** - Time elapsed from checkout start to completion  in seconds. Used for checkout optimization and user experience analysis. NULL for  incomplete checkouts or when checkout_end <= checkout_start.
 | `[]` | `{}` |
    | `IS_IV_ALLOW_PAYSTUB` | 75 | `BOOLEAN` | **Income Verification Paystub Allowed** - Boolean flag indicating whether paystub income  verification was allowed for this application. Used for income verification process analysis  and policy compliance tracking. Sourced from application data.
 | **Income Verification Paystub Allowed** - Boolean flag indicating whether paystub income  verification was allowed for this application. Used for income verification process analysis  and policy compliance tracking. Sourced from application data.
 | `[]` | `{}` |
    | `IS_PREQUAL` | 76 | `BOOLEAN` | **Pre-qualification Flag** - Boolean flag indicating whether this application went through  the pre-qualification process. Used for prequalification flow analysis and conversion tracking.  Sourced from application data.
 | **Pre-qualification Flag** - Boolean flag indicating whether this application went through  the pre-qualification process. Used for prequalification flow analysis and conversion tracking.  Sourced from application data.
 | `[]` | `{}` |
    | `HAS_PRODUCTS_MANUALLY_EDITED` | 77 | `BOOLEAN` | **Products Manually Edited** - Boolean flag indicating whether loan products were manually  modified during the application process. Used for underwriting analysis and manual intervention  tracking. Sourced from application data.
 | **Products Manually Edited** - Boolean flag indicating whether loan products were manually  modified during the application process. Used for underwriting analysis and manual intervention  tracking. Sourced from application data.
 | `[]` | `{}` |
    | `IS_SELF_CHECKOUT` | 78 | `BOOLEAN` | **Self-Checkout Flag** - Boolean flag indicating whether the borrower completed checkout  without assistance. Used for checkout process analysis and customer experience optimization.  Sourced from application data.
 | **Self-Checkout Flag** - Boolean flag indicating whether the borrower completed checkout  without assistance. Used for checkout process analysis and customer experience optimization.  Sourced from application data.
 | `[]` | `{}` |
    | `IS_APPLICATION_START` | 79 | `BOOLEAN` | **Application Start Flag** - Boolean flag indicating whether this record represents an  application start event. Used for application funnel analysis and start rate calculations.  Sourced from application data.
 | **Application Start Flag** - Boolean flag indicating whether this record represents an  application start event. Used for application funnel analysis and start rate calculations.  Sourced from application data.
 | `[]` | `{}` |
    | `IS_APPLICATION_COMPLETION` | 80 | `BOOLEAN` | **Application Completion Flag** - Boolean flag indicating whether the application was  completed (reached final status). Used for completion rate analysis and funnel optimization.  Sourced from application data.
 | **Application Completion Flag** - Boolean flag indicating whether the application was  completed (reached final status). Used for completion rate analysis and funnel optimization.  Sourced from application data.
 | `[]` | `{}` |
    | `IS_APPLICATION_COMPLETION_BINARY` | 81 | `NUMBER` | **Application Completion Binary** - Numeric binary version of application completion  (1 = completed, 0 = not completed, NULL = not started). Used for mathematical calculations  and aggregations in completion rate analysis.
 | **Application Completion Binary** - Numeric binary version of application completion  (1 = completed, 0 = not completed, NULL = not started). Used for mathematical calculations  and aggregations in completion rate analysis.
 | `[]` | `{}` |
    | `IS_APPLICATION_COMPLETED_IN_ONE_DAY` | 82 | `BOOLEAN` | **Application Completed in One Day** - Boolean flag indicating whether the application  was completed within 24 hours of creation (application_time_to_complete_sec < 86400).  Used for processing efficiency analysis and customer experience metrics.
 | **Application Completed in One Day** - Boolean flag indicating whether the application  was completed within 24 hours of creation (application_time_to_complete_sec < 86400).  Used for processing efficiency analysis and customer experience metrics.
 | `[]` | `{}` |
    | `IS_CHECKOUT_START` | 83 | `BOOLEAN` | **Checkout Start Flag** - Boolean flag indicating whether checkout was initiated  (TRUE when loan_id is not NULL). Used for checkout conversion analysis and funnel tracking.
 | **Checkout Start Flag** - Boolean flag indicating whether checkout was initiated  (TRUE when loan_id is not NULL). Used for checkout conversion analysis and funnel tracking.
 | `[]` | `{}` |
    | `IS_CHECKOUT_COMPLETION` | 84 | `BOOLEAN` | **Checkout Completion Flag** - Boolean flag indicating whether checkout was completed  (TRUE when loan_status in 'FUNDED', 'AWAITING_FUNDING'). Used for checkout completion  rate analysis and funding conversion tracking.
 | **Checkout Completion Flag** - Boolean flag indicating whether checkout was completed  (TRUE when loan_status in 'FUNDED', 'AWAITING_FUNDING'). Used for checkout completion  rate analysis and funding conversion tracking.
 | `[]` | `{}` |
    | `IS_APPLICATION_APPROVAL_BINARY` | 85 | `NUMBER` | **Application Approval Binary** - Numeric binary version of application approval  (1 = approved, 0 = denied, NULL = pending/other). Used for mathematical calculations  and aggregations in approval rate analysis.
 | **Application Approval Binary** - Numeric binary version of application approval  (1 = approved, 0 = denied, NULL = pending/other). Used for mathematical calculations  and aggregations in approval rate analysis.
 | `[]` | `{}` |
    | `IS_SUCCESSFUL_CONTACT` | 86 | `BOOLEAN` | **Successful Contact Flag** - Boolean flag indicating whether successful contact was  made with the borrower for this loan. Used for collections analysis and customer engagement  tracking. NULL for applications without loans. Sourced from loan data.
 | **Successful Contact Flag** - Boolean flag indicating whether successful contact was  made with the borrower for this loan. Used for collections analysis and customer engagement  tracking. NULL for applications without loans. Sourced from loan data.
 | `[]` | `{}` |
    | `IS_AVOIDANCE` | 87 | `BOOLEAN` | **Avoidance Flag** - Boolean flag indicating whether the borrower is exhibiting avoidance  behavior for this loan. Used for collections strategy and risk management. NULL for  applications without loans. Sourced from loan data.
 | **Avoidance Flag** - Boolean flag indicating whether the borrower is exhibiting avoidance  behavior for this loan. Used for collections strategy and risk management. NULL for  applications without loans. Sourced from loan data.
 | `[]` | `{}` |
    | `IS_DO_NOT_CALL` | 88 | `BOOLEAN` | **Do Not Call Flag** - Boolean flag indicating whether the borrower has requested not  to be called for this loan. Used for compliance with communication preferences and  regulatory requirements. NULL for applications without loans. Sourced from loan data.
 | **Do Not Call Flag** - Boolean flag indicating whether the borrower has requested not  to be called for this loan. Used for compliance with communication preferences and  regulatory requirements. NULL for applications without loans. Sourced from loan data.
 | `[]` | `{}` |
    | `IS_FORBEARANCE` | 89 | `BOOLEAN` | **Forbearance Flag** - Boolean flag indicating whether the loan is currently in forbearance  status. Used for loan status tracking and collections management. NULL for applications  without loans. Sourced from loan data.
 | **Forbearance Flag** - Boolean flag indicating whether the loan is currently in forbearance  status. Used for loan status tracking and collections management. NULL for applications  without loans. Sourced from loan data.
 | `[]` | `{}` |
    | `IS_DO_NOT_REPORT` | 90 | `BOOLEAN` | **Do Not Report Flag** - Boolean flag indicating whether the loan should not be reported  to credit bureaus. Used for credit reporting compliance and borrower privacy management.  NULL for applications without loans. Sourced from loan data.
 | **Do Not Report Flag** - Boolean flag indicating whether the loan should not be reported  to credit bureaus. Used for credit reporting compliance and borrower privacy management.  NULL for applications without loans. Sourced from loan data.
 | `[]` | `{}` |
    | `IS_FINANCIAL_HARDSHIP` | 91 | `BOOLEAN` | **Financial Hardship Flag** - Boolean flag indicating whether the borrower has declared  financial hardship for this loan. Used for hardship program management and collections  strategy. NULL for applications without loans. Sourced from loan data.
 | **Financial Hardship Flag** - Boolean flag indicating whether the borrower has declared  financial hardship for this loan. Used for hardship program management and collections  strategy. NULL for applications without loans. Sourced from loan data.
 | `[]` | `{}` |
    | `IS_DISPUTE` | 92 | `BOOLEAN` | **Dispute Flag** - Boolean flag indicating whether there is an active dispute for this  loan. Used for dispute management and customer service tracking. NULL for applications  without loans. Sourced from loan data.
 | **Dispute Flag** - Boolean flag indicating whether there is an active dispute for this  loan. Used for dispute management and customer service tracking. NULL for applications  without loans. Sourced from loan data.
 | `[]` | `{}` |
    | `IS_AUTOPAY` | 93 | `BOOLEAN` | **Autopay Flag** - Boolean flag indicating whether automatic payments are enabled for  this loan. Used for payment method analysis and default risk assessment. NULL for  applications without loans. Sourced from loan data.
 | **Autopay Flag** - Boolean flag indicating whether automatic payments are enabled for  this loan. Used for payment method analysis and default risk assessment. NULL for  applications without loans. Sourced from loan data.
 | `[]` | `{}` |
    | `IS_FRAUD` | 94 | `BOOLEAN` | **Fraud Flag** - Boolean flag indicating whether this loan has been flagged for fraud.  Used for fraud analysis, risk management, and loss prevention. NULL for applications  without loans. Sourced from loan data.
 | **Fraud Flag** - Boolean flag indicating whether this loan has been flagged for fraud.  Used for fraud analysis, risk management, and loss prevention. NULL for applications  without loans. Sourced from loan data.
 | `[]` | `{}` |
    | `BALANCE_AVAILABLE` | 95 | `FLOAT` | **Available Credit Balance** - Dollar amount of available credit remaining for the borrower  within the organization. Used for credit line management and additional lending decisions.  NULL when not applicable. Sourced from application data.
 | **Available Credit Balance** - Dollar amount of available credit remaining for the borrower  within the organization. Used for credit line management and additional lending decisions.  NULL when not applicable. Sourced from application data.
 | `[]` | `{}` |
    | `MAX_ELIGIBLE` | 96 | `FLOAT` | **Maximum Eligible Amount** - Maximum dollar amount the borrower is eligible to borrow  based on underwriting criteria. Used for credit limit analysis and lending capacity assessment.  NULL when not determined. Sourced from application data.
 | **Maximum Eligible Amount** - Maximum dollar amount the borrower is eligible to borrow  based on underwriting criteria. Used for credit limit analysis and lending capacity assessment.  NULL when not determined. Sourced from application data.
 | `[]` | `{}` |
    | `REQUESTED_AMOUNT` | 97 | `FLOAT` | **Credit Line Increase Requested Amount** - Dollar amount requested for credit line increase.  Only populated for credit line increase applications. Used for credit line increase analysis  and approval tracking. Sourced from credit_line_increase data.
 | **Credit Line Increase Requested Amount** - Dollar amount requested for credit line increase.  Only populated for credit line increase applications. Used for credit line increase analysis  and approval tracking. Sourced from credit_line_increase data.
 | `[]` | `{}` |
    | `RISK_SCORE` | 98 | `NUMBER` | **Application Risk Score** - Cherry's internal risk score calculated during application  processing. Used for risk assessment, underwriting decisions, and portfolio analysis.  Range and scale vary by scoring model. Sourced from application data.
 | **Application Risk Score** - Cherry's internal risk score calculated during application  processing. Used for risk assessment, underwriting decisions, and portfolio analysis.  Range and scale vary by scoring model. Sourced from application data.
 | `[]` | `{}` |
    | `VANTAGE_SCORE` | 99 | `FLOAT` | **VantageScore 4.0** - External credit score from VantageScore 4.0 model used for  underwriting decisions. Ranges from 300-850 with higher scores indicating lower risk.  Used for credit risk assessment and pricing decisions. Sourced from risk_applications data.
 | **VantageScore 4.0** - External credit score from VantageScore 4.0 model used for  underwriting decisions. Ranges from 300-850 with higher scores indicating lower risk.  Used for credit risk assessment and pricing decisions. Sourced from risk_applications data.
 | `[]` | `{}` |
    | `APPLICATION_PURCHASE_AMOUNT` | 100 | `FLOAT` | **Application Purchase Amount** - Dollar amount of the initial purchase or loan request  submitted with the application. May differ from final loan amount due to underwriting  adjustments. Used for demand analysis and underwriting comparison. Sourced from application data.
 | **Application Purchase Amount** - Dollar amount of the initial purchase or loan request  submitted with the application. May differ from final loan amount due to underwriting  adjustments. Used for demand analysis and underwriting comparison. Sourced from application data.
 | `[]` | `{}` |
    | `REFUND_AMOUNT` | 101 | `FLOAT` | **Loan Refund Amount** - Dollar amount refunded to the borrower or merchant for this loan.  Used for refund analysis and financial reconciliation. NULL for applications without loans  or loans without refunds. Sourced from loan data.
 | **Loan Refund Amount** - Dollar amount refunded to the borrower or merchant for this loan.  Used for refund analysis and financial reconciliation. NULL for applications without loans  or loans without refunds. Sourced from loan data.
 | `[]` | `{}` |
    | `DOWN_PAYMENT_AMOUNT` | 102 | `FLOAT` | **Down Payment Amount** - Dollar amount paid as a down payment at loan origination.  Used for down payment analysis and cash flow tracking. NULL for loans without down payments.  Sourced from loan data.
 | **Down Payment Amount** - Dollar amount paid as a down payment at loan origination.  Used for down payment analysis and cash flow tracking. NULL for loans without down payments.  Sourced from loan data.
 | `[]` | `{}` |
    | `DOWN_PAYMENT_ATTEMPT` | 103 | `NUMBER` | **Down Payment Attempt Amount** - Dollar amount attempted for down payment processing  (may differ from successful amount). Used for payment processing analysis and failure tracking.  NULL for loans without down payment attempts. Sourced from loan data.
 | **Down Payment Attempt Amount** - Dollar amount attempted for down payment processing  (may differ from successful amount). Used for payment processing analysis and failure tracking.  NULL for loans without down payment attempts. Sourced from loan data.
 | `[]` | `{}` |
    | `MERCHANT_FEE` | 104 | `FLOAT` | **Merchant Fee Amount** - Dollar amount of fees paid by the merchant for this loan.  Used for merchant pricing analysis and revenue calculations. NULL for applications without  loans. Sourced from loan data (merchant_revenue field).
 | **Merchant Fee Amount** - Dollar amount of fees paid by the merchant for this loan.  Used for merchant pricing analysis and revenue calculations. NULL for applications without  loans. Sourced from loan data (merchant_revenue field).
 | `[]` | `{}` |
    | `TOTAL_AMOUNT` | 105 | `FLOAT` | **Total Loan Amount** - Total dollar amount of the loan including principal, interest,  and fees. Represents the total amount the borrower will pay over the loan term. NULL for  applications without loans. Sourced from loan data.
 | **Total Loan Amount** - Total dollar amount of the loan including principal, interest,  and fees. Represents the total amount the borrower will pay over the loan term. NULL for  applications without loans. Sourced from loan data.
 | `[]` | `{}` |
    | `INSTALLMENT_AMOUNT` | 106 | `FLOAT` | **Installment Payment Amount** - Dollar amount of each scheduled payment for the loan.  Used for affordability analysis and payment processing. NULL for applications without loans.  Sourced from loan data.
 | **Installment Payment Amount** - Dollar amount of each scheduled payment for the loan.  Used for affordability analysis and payment processing. NULL for applications without loans.  Sourced from loan data.
 | `[]` | `{}` |
    | `LOAN_PURCHASE_AMOUNT` | 107 | `FLOAT` | **Loan Purchase Amount** - Final dollar amount of the purchase covered by the loan.  May differ from application_purchase_amount due to underwriting adjustments. NULL for  applications without loans. Sourced from loan data.
 | **Loan Purchase Amount** - Final dollar amount of the purchase covered by the loan.  May differ from application_purchase_amount due to underwriting adjustments. NULL for  applications without loans. Sourced from loan data.
 | `[]` | `{}` |
    | `NET_LOAN_AMOUNT` | 108 | `FLOAT` | **Net Loan Amount** - Net dollar amount of the loan after fees and adjustments.  Represents the actual amount borrowed by the borrower. NULL for applications without loans.  Sourced from loan data (amount field).
 | **Net Loan Amount** - Net dollar amount of the loan after fees and adjustments.  Represents the actual amount borrowed by the borrower. NULL for applications without loans.  Sourced from loan data (amount field).
 | `[]` | `{}` |
    | `GROSS_AMOUNT` | 109 | `FLOAT` | **Gross Loan Amount** - Gross dollar amount of the loan before any deductions or adjustments.  Used for gross lending volume analysis and financial reporting. NULL for applications  without loans. Sourced from loan data.
 | **Gross Loan Amount** - Gross dollar amount of the loan before any deductions or adjustments.  Used for gross lending volume analysis and financial reporting. NULL for applications  without loans. Sourced from loan data.
 | `[]` | `{}` |
    | `FINANCE_CHARGE` | 110 | `FLOAT` | **Finance Charge Amount** - Total dollar amount of finance charges for the loan over  its full term. Used for finance charge disclosure and revenue analysis. NULL for  applications without loans. Sourced from loan data.
 | **Finance Charge Amount** - Total dollar amount of finance charges for the loan over  its full term. Used for finance charge disclosure and revenue analysis. NULL for  applications without loans. Sourced from loan data.
 | `[]` | `{}` |
    | `MERCHANT_FUND` | 111 | `FLOAT` | **Merchant Funding Amount** - Dollar amount funded to the merchant for this loan.  Used for merchant settlement analysis and cash flow tracking. NULL for applications  without loans. Sourced from loan data. | **Merchant Funding Amount** - Dollar amount funded to the merchant for this loan.  Used for merchant settlement analysis and cash flow tracking. NULL for applications  without loans. Sourced from loan data. | `[]` | `{}` |
    | `LOAN_ORDER` | 112 | `NUMBER` | **Loan Order Number** - Sequential number indicating the order of loans within an application  (1 = first loan, 2 = second loan, etc.). Calculated using ROW_NUMBER() ordered by  loan_created_at ASC. Used for multi-loan analysis and loan sequence tracking.
 | **Loan Order Number** - Sequential number indicating the order of loans within an application  (1 = first loan, 2 = second loan, etc.). Calculated using ROW_NUMBER() ordered by  loan_created_at ASC. Used for multi-loan analysis and loan sequence tracking.
 | `[]` | `{}` |
    | `LOAN_RECENCY` | 113 | `NUMBER` | **Loan Recency Number** - Sequential number indicating recency of loans within an application  (1 = most recent loan, 2 = second most recent, etc.). Calculated using ROW_NUMBER() ordered by  loan_created_at DESC. Used for identifying the most recent loan per application.
 | **Loan Recency Number** - Sequential number indicating recency of loans within an application  (1 = most recent loan, 2 = second most recent, etc.). Calculated using ROW_NUMBER() ordered by  loan_created_at DESC. Used for identifying the most recent loan per application.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt_utils.generate_surrogate_key`
    *   `model.cherry_data_model.int_applications_collapsed`
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.merchant_account_mapping`
    *   `model.cherry_data_model.risk_applications`
    *   `model.cherry_data_model.src_cherry_applications_status_history`
    *   `model.cherry_data_model.src_cherry_loans`
    *   `model.cherry_data_model.src_credit_line_increase`
    *   `model.cherry_data_model.src_segment_checkout_landing_page_load`
    *   `model.cherry_data_model.src_segment_checkout_post_funding_page_load`
    *   `model.cherry_data_model.stg_loan_product_aprs`
    *   `model.cherry_data_model.stg_merchants`

---
