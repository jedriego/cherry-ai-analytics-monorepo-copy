## Model: `loan_info_xf`

`loan_info_xf`

*   **Unique ID:** `model.cherry_data_model.loan_info_xf`
*   **FQN:** `prod.core_marts.loan_info_xf`
*   **Description:** **Comprehensive Loan Information Mart for Holistic Analytics**
This model serves as Cherry's primary loan analytics table, combining funded loan data with  comprehensive merchant information, revenue forecasting, ownership attribution, and operational  context. It provides a complete 360-degree view of each loan for performance analysis, revenue  tracking, ownership attribution, and business intelligence across Cherry's lending operations.
**Key Business Logic:** - **Loan Filtering**: Includes only funded, awaiting funding, refunded, or voided loans (excludes demos) - **Revenue Forecasting**: Integrates complex revenue calculations from loan_revenue_details including 
  forecasted interest, fees, and contribution margins based on risk scores and loan terms
- **Ownership Attribution**: Provides point-in-time ownership assignment for onboarding, opportunity, 
  and retention teams based on loan funding date using complex historical user data
- **Merchant Hierarchy**: Complete merchant and organizational context including industry segments, 
  pricing tiers, and account relationships
- **Activation Tracking**: Identifies first loans per merchant for activation analysis
**Data Sources:** - `int_funded_information_pt`: Core funded loan data combining Cherry and LoanPro systems - `loan_revenue_details`: Revenue forecasting with risk-based calculations and contribution margins - `stg_merchants`: Comprehensive merchant hierarchy, industry segments, and account relationships - `stg_loan_product_aprs`: Original loan terms and APR calculations including promotional rates - `sf_user_history`: Historical Salesforce user data for point-in-time ownership attribution - `opportunity_owner_history`: Historical opportunity ownership for credit assignment - `retention_daily_ownership`: Daily retention ownership assignments
**Primary Use Cases:** - Loan performance analysis and portfolio management - Revenue forecasting and contribution margin analysis - Sales attribution and commission calculations - Merchant relationship management and retention analysis - Operational reporting and business intelligence

*   **Tags:** `['core', 'core_loans', 'core_hourly']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `LOAN_ID` | 1 | `NUMBER` | **Loan Identifier** - Primary key uniquely identifying each loan record. Foreign key reference  to Cherry's loan system and serves as the foundation for all loan-related analytics and reporting.  Sourced from int_funded_information_pt.
 | **Loan Identifier** - Primary key uniquely identifying each loan record. Foreign key reference  to Cherry's loan system and serves as the foundation for all loan-related analytics and reporting.  Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `CONTRACT_ID` | 2 | `TEXT` | **Loan Contract Identifier** - Human-readable contract ID used in customer communications  and legal documentation. Represents the legal contract between Cherry and the borrower, distinct  from the internal loan_id. Sourced from int_funded_information_pt (Cherry loans data).
 | **Loan Contract Identifier** - Human-readable contract ID used in customer communications  and legal documentation. Represents the legal contract between Cherry and the borrower, distinct  from the internal loan_id. Sourced from int_funded_information_pt (Cherry loans data).
 | `[]` | `{}` |
    | `BORROWER_ID` | 3 | `NUMBER` | **Borrower Identifier** - Foreign key reference to Cherry's borrower system. Links to the  individual who received the loan. Used for borrower-level analytics, credit history tracking,  and customer relationship management. Sourced from int_funded_information_pt.
 | **Borrower Identifier** - Foreign key reference to Cherry's borrower system. Links to the  individual who received the loan. Used for borrower-level analytics, credit history tracking,  and customer relationship management. Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `APPLICATION_ID` | 4 | `NUMBER` | **Application Identifier** - Foreign key reference to Cherry's application system. Links the  funded loan back to the original credit application submitted by the borrower for conversion  analysis and application performance tracking. Sourced from int_funded_information_pt.
 | **Application Identifier** - Foreign key reference to Cherry's application system. Links the  funded loan back to the original credit application submitted by the borrower for conversion  analysis and application performance tracking. Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `PRODUCT_ID` | 5 | `NUMBER` | **Product Identifier** - Foreign key reference to the specific loan product selected.  Determines loan terms, APR, fees, and repayment structure. Critical for product performance  analysis and risk management. Sourced from int_funded_information_pt.
 | **Product Identifier** - Foreign key reference to the specific loan product selected.  Determines loan terms, APR, fees, and repayment structure. Critical for product performance  analysis and risk management. Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `CHANNEL` | 6 | `TEXT` | **Application Channel** - The channel through which the application was submitted  (e.g., 'WEB', 'MOBILE', 'API'). Used for channel performance analysis and user experience  optimization. Sourced from int_funded_information_pt (Cherry loans data).
 | **Application Channel** - The channel through which the application was submitted  (e.g., 'WEB', 'MOBILE', 'API'). Used for channel performance analysis and user experience  optimization. Sourced from int_funded_information_pt (Cherry loans data).
 | `[]` | `{}` |
    | `API_PARTNER` | 7 | `TEXT` | **API Partner Identifier** - Identifies the partner or integration source when applications  come through API integrations rather than direct Cherry interfaces. Used for partner  performance analysis and integration management. Sourced from int_funded_information_pt.
 | **API Partner Identifier** - Identifies the partner or integration source when applications  come through API integrations rather than direct Cherry interfaces. Used for partner  performance analysis and integration management. Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `PROMO_USED` | 8 | `BOOLEAN` | **Promotional Rate Used** - Boolean flag indicating whether a promotional interest rate  was applied to the loan. Used for promotional campaign analysis and pricing strategy evaluation.  Sourced from int_funded_information_pt (Cherry loans data).
 | **Promotional Rate Used** - Boolean flag indicating whether a promotional interest rate  was applied to the loan. Used for promotional campaign analysis and pricing strategy evaluation.  Sourced from int_funded_information_pt (Cherry loans data).
 | `[]` | `{}` |
    | `LOAN_TERM` | 9 | `NUMBER` | **Current Loan Term** - Current loan term in months from LoanPro loan plans. May differ from  original term due to modifications. Used for current loan servicing and payment calculations.  Sourced from int_funded_information_pt (loan plans data).
 | **Current Loan Term** - Current loan term in months from LoanPro loan plans. May differ from  original term due to modifications. Used for current loan servicing and payment calculations.  Sourced from int_funded_information_pt (loan plans data).
 | `[]` | `{}` |
    | `CURRENT_APR` | 10 | `FLOAT` | **Current APR** - Current Annual Percentage Rate as a decimal, which may differ from original  APR due to rate changes. Used for current loan pricing analysis and revenue calculations.  Sourced from int_funded_information_pt.
 | **Current APR** - Current Annual Percentage Rate as a decimal, which may differ from original  APR due to rate changes. Used for current loan pricing analysis and revenue calculations.  Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `ORIGINAL_APR` | 11 | `FLOAT` | **Original APR** - Annual Percentage Rate at loan origination as a decimal (e.g., 0.1899 for 18.99%).  Includes promotional rate logic where applicable. Used for pricing analysis and loan origination  performance tracking. Sourced from stg_loan_product_aprs.
 | **Original APR** - Annual Percentage Rate at loan origination as a decimal (e.g., 0.1899 for 18.99%).  Includes promotional rate logic where applicable. Used for pricing analysis and loan origination  performance tracking. Sourced from stg_loan_product_aprs.
 | `[]` | `{}` |
    | `ORIGINAL_LOAN_TERM` | 12 | `NUMBER` | **Original Loan Term** - Original loan term in months at loan origination. Derived from  stg_loan_product_aprs with adjustments for biweekly payment frequencies (term/2). Used for  loan product analysis and performance tracking across different term offerings.
 | **Original Loan Term** - Original loan term in months at loan origination. Derived from  stg_loan_product_aprs with adjustments for biweekly payment frequencies (term/2). Used for  loan product analysis and performance tracking across different term offerings.
 | `[]` | `{}` |
    | `MENU_NAME` | 13 | `TEXT` | **Product Menu Name** - Human-readable name of the pricing menu used for the application.  Provides context about the product offering and pricing tier. Sourced from stg_loan_product_aprs  through menu relationship.
 | **Product Menu Name** - Human-readable name of the pricing menu used for the application.  Provides context about the product offering and pricing tier. Sourced from stg_loan_product_aprs  through menu relationship.
 | `[]` | `{}` |
    | `IS_PAY_IN_FOUR` | 14 | `BOOLEAN` | **Pay-in-Four Product Flag** - Boolean flag indicating whether this is a pay-in-four product  (TRUE when original_loan_term = 1.5 months). Used for product-specific analysis and short-term  lending performance tracking. Derived from original_loan_term logic.
 | **Pay-in-Four Product Flag** - Boolean flag indicating whether this is a pay-in-four product  (TRUE when original_loan_term = 1.5 months). Used for product-specific analysis and short-term  lending performance tracking. Derived from original_loan_term logic.
 | `[]` | `{}` |
    | `PURCHASE_AMOUNT` | 15 | `FLOAT` | **Purchase Amount** - Dollar amount of the purchase covered by the loan. Represents the  value of goods/services financed for the borrower. Used for loan sizing analysis and merchant  transaction volume tracking. Sourced from int_funded_information_pt.
 | **Purchase Amount** - Dollar amount of the purchase covered by the loan. Represents the  value of goods/services financed for the borrower. Used for loan sizing analysis and merchant  transaction volume tracking. Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `MERCHANT_FEE` | 16 | `FLOAT` | **Merchant Fee Amount** - Dollar amount of fees paid by the merchant for this loan.  Used for merchant pricing analysis and revenue calculations. Sourced from loan_revenue_details (adjusted).
 | **Merchant Fee Amount** - Dollar amount of fees paid by the merchant for this loan.  Used for merchant pricing analysis and revenue calculations. Sourced from loan_revenue_details (adjusted).
 | `[]` | `{}` |
    | `MERCHANT_FUND` | 17 | `FLOAT` | **Merchant Funding Amount** - Dollar amount funded to the merchant for this loan.  Used for merchant settlement analysis and cash flow tracking.  Sourced from int_funded_information_pt.
 | **Merchant Funding Amount** - Dollar amount funded to the merchant for this loan.  Used for merchant settlement analysis and cash flow tracking.  Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `GROSS_AMOUNT` | 18 | `FLOAT` | **Gross Loan Amount** - Gross dollar amount of the loan before any deductions or adjustments.  Used for gross lending volume analysis and financial reporting. Serves as basis for revenue and fee  calculations. Sourced from int_funded_information_pt.
 | **Gross Loan Amount** - Gross dollar amount of the loan before any deductions or adjustments.  Used for gross lending volume analysis and financial reporting. Serves as basis for revenue and fee  calculations. Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `DOWN_PAYMENT_AMOUNT` | 19 | `FLOAT` | **Down Payment Amount** - Dollar amount paid as a down payment at loan origination.  Used for down payment analysis and cash flow tracking. Sourced from int_funded_information_pt.
 | **Down Payment Amount** - Dollar amount paid as a down payment at loan origination.  Used for down payment analysis and cash flow tracking. Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `NET_LOAN_AMOUNT` | 20 | `FLOAT` | **Net Loan Amount** - Net dollar amount of the loan after fees and adjustments.  Represents the actual amount borrowed by the borrower. Sourced from int_funded_information_pt.
 | **Net Loan Amount** - Net dollar amount of the loan after fees and adjustments.  Represents the actual amount borrowed by the borrower. Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `FINANCE_CHARGE` | 21 | `FLOAT` | **Finance Charge Amount** - Total dollar amount of finance charges for the loan over  its full term. Used for finance charge disclosure and revenue analysis. Sourced from  int_funded_information_pt (Cherry loans data).
 | **Finance Charge Amount** - Total dollar amount of finance charges for the loan over  its full term. Used for finance charge disclosure and revenue analysis. Sourced from  int_funded_information_pt (Cherry loans data).
 | `[]` | `{}` |
    | `TOTAL_AMOUNT` | 22 | `FLOAT` | **Total Loan Amount** - Total dollar amount of the loan including principal, interest,  and fees. Represents the total amount the borrower will pay over the loan term.  Sourced from int_funded_information_pt.
 | **Total Loan Amount** - Total dollar amount of the loan including principal, interest,  and fees. Represents the total amount the borrower will pay over the loan term.  Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `INSTALLMENT_AMOUNT` | 23 | `FLOAT` | **Installment Payment Amount** - Dollar amount of each scheduled payment for the loan.  Used for affordability analysis and payment processing. Sourced from int_funded_information_pt.
 | **Installment Payment Amount** - Dollar amount of each scheduled payment for the loan.  Used for affordability analysis and payment processing. Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `LOAN_PLAN_STATUS` | 24 | `TEXT` | **Current Loan Status** - Current status of the loan from LoanPro loan plans (e.g., 'ACTIVE',  'PAID_OFF', 'CHARGED_OFF'). Represents the most current operational status for loan servicing  and portfolio management. Sourced from int_funded_information_pt (loan plans).
 | **Current Loan Status** - Current status of the loan from LoanPro loan plans (e.g., 'ACTIVE',  'PAID_OFF', 'CHARGED_OFF'). Represents the most current operational status for loan servicing  and portfolio management. Sourced from int_funded_information_pt (loan plans).
 | `[]` | `{}` |
    | `LOAN_PLAN_SUBSTATUS` | 25 | `TEXT` | **Current Loan Sub-Status** - Current sub-status providing additional detail about the loan's  operational state from LoanPro. Provides granular context for loan management and collections  strategy. Sourced from int_funded_information_pt (loan plans).
 | **Current Loan Sub-Status** - Current sub-status providing additional detail about the loan's  operational state from LoanPro. Provides granular context for loan management and collections  strategy. Sourced from int_funded_information_pt (loan plans).
 | `[]` | `{}` |
    | `OUTSTANDING_BALANCE` | 26 | `FLOAT` | **Outstanding Balance** - Current outstanding balance on the loan from LoanPro loan plans.  Represents the remaining amount owed by the borrower and is critical for portfolio valuation  and loss calculations. Sourced from int_funded_information_pt (loan_plan_balance).
 | **Outstanding Balance** - Current outstanding balance on the loan from LoanPro loan plans.  Represents the remaining amount owed by the borrower and is critical for portfolio valuation  and loss calculations. Sourced from int_funded_information_pt (loan_plan_balance).
 | `[]` | `{}` |
    | `IS_AUTOPAY` | 27 | `BOOLEAN` | **Autopay Flag** - Boolean flag indicating whether automatic payments are enabled for  this loan. Used for payment method analysis and default risk assessment.  Sourced from int_funded_information_pt.
 | **Autopay Flag** - Boolean flag indicating whether automatic payments are enabled for  this loan. Used for payment method analysis and default risk assessment.  Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `IS_FRAUD` | 28 | `BOOLEAN` | **Fraud Flag** - Boolean flag indicating whether this loan has been flagged for fraud.  Used for fraud analysis, risk management, and loss prevention.  Sourced from int_funded_information_pt.
 | **Fraud Flag** - Boolean flag indicating whether this loan has been flagged for fraud.  Used for fraud analysis, risk management, and loss prevention.  Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `IS_DO_NOT_REPORT` | 29 | `BOOLEAN` | **Do Not Report Flag** - Boolean flag indicating whether the loan should not be reported  to credit bureaus. Used for credit reporting compliance and borrower privacy management.  Sourced from int_funded_information_pt.
 | **Do Not Report Flag** - Boolean flag indicating whether the loan should not be reported  to credit bureaus. Used for credit reporting compliance and borrower privacy management.  Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `IS_DO_NOT_CALL` | 30 | `BOOLEAN` | **Do Not Call Flag** - Boolean flag indicating whether the borrower has requested not  to be called for this loan. Used for compliance with communication preferences and  regulatory requirements. Sourced from int_funded_information_pt.
 | **Do Not Call Flag** - Boolean flag indicating whether the borrower has requested not  to be called for this loan. Used for compliance with communication preferences and  regulatory requirements. Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `IS_OUTSOURCED` | 31 | `BOOLEAN` | **Outsourced Flag** - Boolean flag indicating whether the loan has been outsourced to a third-party  servicer or collections agency. Used for loan servicing management and operational tracking.  Sourced from int_funded_information_pt.
 | **Outsourced Flag** - Boolean flag indicating whether the loan has been outsourced to a third-party  servicer or collections agency. Used for loan servicing management and operational tracking.  Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `IS_ACTIVATION` | 32 | `BOOLEAN` | **Activation Loan Flag** - Boolean flag indicating whether this is the first loan for the merchant  (activation loan). Determined by comparing with MIN_BY(loan_id, funded_at_pt) per primary_merchant_id.  Used for merchant activation analysis and onboarding performance tracking. Derived from activations CTE.
 | **Activation Loan Flag** - Boolean flag indicating whether this is the first loan for the merchant  (activation loan). Determined by comparing with MIN_BY(loan_id, funded_at_pt) per primary_merchant_id.  Used for merchant activation analysis and onboarding performance tracking. Derived from activations CTE.
 | `[]` | `{}` |
    | `LOAN_STATUS` | 33 | `TEXT` | **Loan Status** - Current status of the loan (e.g., 'FUNDED', 'AWAITING_FUNDING', 'CANCELLED').  Indicates the loan's position in the funding and lifecycle process. Used for loan performance  and operational analysis. Sourced from int_funded_information_pt.
 | **Loan Status** - Current status of the loan (e.g., 'FUNDED', 'AWAITING_FUNDING', 'CANCELLED').  Indicates the loan's position in the funding and lifecycle process. Used for loan performance  and operational analysis. Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `REFUND_AMOUNT` | 34 | `FLOAT` | **Loan Refund Amount** - Dollar amount refunded to the borrower or merchant for this loan.  Used for refund analysis and financial reconciliation. COALESCED to 0 when no refund exists.  Sourced from int_funded_information_pt.
 | **Loan Refund Amount** - Dollar amount refunded to the borrower or merchant for this loan.  Used for refund analysis and financial reconciliation. COALESCED to 0 when no refund exists.  Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `FUNDED_AT_PT` | 35 | `TIMESTAMP_NTZ` | **Loan Funding Time (Pacific Time)** - Pacific timezone timestamp when the loan was successfully funded and funds  were disbursed. Critical for funding rate analysis and revenue recognition timing.  Sourced from int_funded_information_pt.
 | **Loan Funding Time (Pacific Time)** - Pacific timezone timestamp when the loan was successfully funded and funds  were disbursed. Critical for funding rate analysis and revenue recognition timing.  Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `FUNDED_QUARTER` | 36 | `TEXT` | **Funding Quarter** - Calendar quarter when the loan was funded (e.g., 'Q1 2024'). Derived from  funded_at_pt date using calendar_table_xf quarter mapping. Used for quarterly reporting and  performance analysis. Calculated from quarter_dates CTE.
 | **Funding Quarter** - Calendar quarter when the loan was funded (e.g., 'Q1 2024'). Derived from  funded_at_pt date using calendar_table_xf quarter mapping. Used for quarterly reporting and  performance analysis. Calculated from quarter_dates CTE.
 | `[]` | `{}` |
    | `LOANPRO_LOAN_ID` | 37 | `NUMBER` | **LoanPro Loan Identifier** - Foreign key reference to the loan record in LoanPro servicing system.  Used for linking to LoanPro transaction data and loan servicing operations. Sourced from  int_funded_information_pt.
 | **LoanPro Loan Identifier** - Foreign key reference to the loan record in LoanPro servicing system.  Used for linking to LoanPro transaction data and loan servicing operations. Sourced from  int_funded_information_pt.
 | `[]` | `{}` |
    | `CREATED_AT_PT` | 38 | `TIMESTAMP_NTZ` | **Loan Creation Time (Pacific Time)** - Pacific timezone timestamp when the loan record was created.  Represents the start of the checkout process and is used for conversion timing analysis.  Sourced from int_funded_information_pt.
 | **Loan Creation Time (Pacific Time)** - Pacific timezone timestamp when the loan record was created.  Represents the start of the checkout process and is used for conversion timing analysis.  Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `CREATED_BY_NAME` | 39 | `TEXT` | **Created By Name** - Full name of the Cherry user who created the loan record. Used for loan  origination tracking and operational analysis. COALESCED to 'Unknown' when user not found.  Sourced from int_funded_information_pt (Cherry users lookup).
 | **Created By Name** - Full name of the Cherry user who created the loan record. Used for loan  origination tracking and operational analysis. COALESCED to 'Unknown' when user not found.  Sourced from int_funded_information_pt (Cherry users lookup).
 | `[]` | `{}` |
    | `CREATED_BY_EMAIL` | 40 | `TEXT` | **Created By Email** - Email address of the Cherry user who created the loan record. Used for  operational tracking and user activity analysis. COALESCED to 'Unknown' when user not found.  Sourced from int_funded_information_pt (Cherry users lookup).
 | **Created By Email** - Email address of the Cherry user who created the loan record. Used for  operational tracking and user activity analysis. COALESCED to 'Unknown' when user not found.  Sourced from int_funded_information_pt (Cherry users lookup).
 | `[]` | `{}` |
    | `UPDATED_AT_PT` | 41 | `TIMESTAMP_NTZ` | **Loan Last Updated (Pacific Time)** - Pacific timezone timestamp when the loan was last modified.  Used for loan processing timeline analysis and operational tracking.  Sourced from int_funded_information_pt.
 | **Loan Last Updated (Pacific Time)** - Pacific timezone timestamp when the loan was last modified.  Used for loan processing timeline analysis and operational tracking.  Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `UPDATED_BY_NAME` | 42 | `TEXT` | **Updated By Name** - Full name of the Cherry user who last updated the loan record. Used for  change tracking and operational analysis. COALESCED to 'Unknown' when user not found. Sourced  from int_funded_information_pt (Cherry users lookup).
 | **Updated By Name** - Full name of the Cherry user who last updated the loan record. Used for  change tracking and operational analysis. COALESCED to 'Unknown' when user not found. Sourced  from int_funded_information_pt (Cherry users lookup).
 | `[]` | `{}` |
    | `UPDATED_BY_EMAIL` | 43 | `TEXT` | **Updated By Email** - Email address of the Cherry user who last updated the loan record. Used  for operational tracking and audit trails. COALESCED to 'Unknown' when user not found. Sourced  from int_funded_information_pt (Cherry users lookup).
 | **Updated By Email** - Email address of the Cherry user who last updated the loan record. Used  for operational tracking and audit trails. COALESCED to 'Unknown' when user not found. Sourced  from int_funded_information_pt (Cherry users lookup).
 | `[]` | `{}` |
    | `RISK_SCORE` | 44 | `NUMBER` | **Application Risk Score** - Cherry's internal risk score calculated during application  processing. Used for risk assessment, underwriting decisions, and portfolio analysis.  Range and scale vary by scoring model. Sourced from loan_revenue_details.
 | **Application Risk Score** - Cherry's internal risk score calculated during application  processing. Used for risk assessment, underwriting decisions, and portfolio analysis.  Range and scale vary by scoring model. Sourced from loan_revenue_details.
 | `[]` | `{}` |
    | `VINTAGE` | 45 | `TEXT` | **Loan Vintage** - Month-year when the loan was funded, formatted as 'MM-YY' (e.g., '03-24').  Used for vintage analysis, cohort tracking, and loan portfolio performance over time. Derived  from funded_at_pt date. Sourced from loan_revenue_details.
 | **Loan Vintage** - Month-year when the loan was funded, formatted as 'MM-YY' (e.g., '03-24').  Used for vintage analysis, cohort tracking, and loan portfolio performance over time. Derived  from funded_at_pt date. Sourced from loan_revenue_details.
 | `[]` | `{}` |
    | `MERCHANT_FEE_RATE` | 46 | `FLOAT` | **Merchant Fee Rate** - Merchant fee as a percentage of gross loan amount (merchant_fee / gross_amount).  Used for merchant pricing analysis and rate comparisons across different loan sizes and merchants.  Calculated in loan_revenue_details.
 | **Merchant Fee Rate** - Merchant fee as a percentage of gross loan amount (merchant_fee / gross_amount).  Used for merchant pricing analysis and rate comparisons across different loan sizes and merchants.  Calculated in loan_revenue_details.
 | `[]` | `{}` |
    | `FORECASTED_INTEREST` | 47 | `FLOAT` | **Forecasted Interest Revenue** - Projected dollar amount of interest revenue for the loan over  its full term. Calculated as APR × gross_amount × forecast_interest_rate based on risk score and  loan characteristics. Used for revenue forecasting. Sourced from loan_revenue_details.
 | **Forecasted Interest Revenue** - Projected dollar amount of interest revenue for the loan over  its full term. Calculated as APR × gross_amount × forecast_interest_rate based on risk score and  loan characteristics. Used for revenue forecasting. Sourced from loan_revenue_details.
 | `[]` | `{}` |
    | `FORECASTED_FEES` | 48 | `FLOAT` | **Forecasted Fee Revenue** - Projected dollar amount of fee revenue (late fees, processing fees)  for the loan over its term. Calculated as loan_term × forecast_fees × scalar factors. Used for  revenue forecasting and fee analysis. Sourced from loan_revenue_details.
 | **Forecasted Fee Revenue** - Projected dollar amount of fee revenue (late fees, processing fees)  for the loan over its term. Calculated as loan_term × forecast_fees × scalar factors. Used for  revenue forecasting and fee analysis. Sourced from loan_revenue_details.
 | `[]` | `{}` |
    | `FORECASTED_SERVICING_FEE` | 49 | `FLOAT` | **Forecasted Servicing Fee** - Legacy field for projected servicing fees paid by bank partners  to Cherry. Not included in revenue calculations due to accounting practices but useful for  operational cost analysis. Sourced from loan_revenue_details.
 | **Forecasted Servicing Fee** - Legacy field for projected servicing fees paid by bank partners  to Cherry. Not included in revenue calculations due to accounting practices but useful for  operational cost analysis. Sourced from loan_revenue_details.
 | `[]` | `{}` |
    | `REVENUE` | 50 | `FLOAT` | **Total Forecasted Revenue** - Total projected revenue for the loan calculated as merchant_fee +  forecasted_interest + forecasted_fees. Represents Cherry's total expected revenue from the loan  over its lifetime. Primary metric for revenue analysis. Sourced from loan_revenue_details.
 | **Total Forecasted Revenue** - Total projected revenue for the loan calculated as merchant_fee +  forecasted_interest + forecasted_fees. Represents Cherry's total expected revenue from the loan  over its lifetime. Primary metric for revenue analysis. Sourced from loan_revenue_details.
 | `[]` | `{}` |
    | `CONTRIBUTION_MARGIN` | 51 | `FLOAT` | **Contribution Margin** - Dollar amount of contribution margin for the loan calculated as  revenue × contribution_margin_percent. Represents profit after variable costs and is used for  profitability analysis and business case evaluation. Sourced from loan_revenue_details.
 | **Contribution Margin** - Dollar amount of contribution margin for the loan calculated as  revenue × contribution_margin_percent. Represents profit after variable costs and is used for  profitability analysis and business case evaluation. Sourced from loan_revenue_details.
 | `[]` | `{}` |
    | `MERCHANT_ID` | 52 | `NUMBER` | **Merchant Identifier** - Foreign key reference to the specific merchant location where the loan  originated. May differ from primary_merchant_id for merchants with multiple locations. Used for  location-specific analysis and merchant performance tracking. Sourced from int_funded_information_pt.
 | **Merchant Identifier** - Foreign key reference to the specific merchant location where the loan  originated. May differ from primary_merchant_id for merchants with multiple locations. Used for  location-specific analysis and merchant performance tracking. Sourced from int_funded_information_pt.
 | `[]` | `{}` |
    | `MERCHANT_NAME` | 53 | `TEXT` | **Merchant Name** - Human-readable name of the merchant location. Used for merchant identification  and reporting displays. Sourced from stg_merchants through merchant hierarchy joins.
 | **Merchant Name** - Human-readable name of the merchant location. Used for merchant identification  and reporting displays. Sourced from stg_merchants through merchant hierarchy joins.
 | `[]` | `{}` |
    | `MERCHANT_TYPE` | 54 | `TEXT` | **Merchant Type** - Classification of the merchant (e.g., 'Cherry', 'Alle'). Used for merchant  type analysis and business unit segmentation. Sourced from stg_merchants.
 | **Merchant Type** - Classification of the merchant (e.g., 'Cherry', 'Alle'). Used for merchant  type analysis and business unit segmentation. Sourced from stg_merchants.
 | `[]` | `{}` |
    | `SF_ACCOUNT_ID` | 55 | `TEXT` | **Salesforce Account Identifier** - Foreign key reference to the Salesforce account record.  Includes special case mapping for merchant_id 12033. Used for CRM integration and sales process  tracking. Sourced from stg_merchants with conditional logic.
 | **Salesforce Account Identifier** - Foreign key reference to the Salesforce account record.  Includes special case mapping for merchant_id 12033. Used for CRM integration and sales process  tracking. Sourced from stg_merchants with conditional logic.
 | `[]` | `{}` |
    | `SF_ACCOUNT_NAME` | 56 | `TEXT` | **Salesforce Account Name** - Human-readable name of the Salesforce account. Used for sales  reporting and account management. Sourced from stg_merchants.
 | **Salesforce Account Name** - Human-readable name of the Salesforce account. Used for sales  reporting and account management. Sourced from stg_merchants.
 | `[]` | `{}` |
    | `PRIMARY_MERCHANT_ID` | 57 | `FLOAT` | **Primary Merchant Identifier** - Main merchant ID that represents the account level for  merchants with multiple locations. Used for account-level aggregations and relationship management.  Sourced from stg_merchants.
 | **Primary Merchant Identifier** - Main merchant ID that represents the account level for  merchants with multiple locations. Used for account-level aggregations and relationship management.  Sourced from stg_merchants.
 | `[]` | `{}` |
    | `INDUSTRY` | 58 | `TEXT` | **Industry Classification** - Cherry's internal industry classification for the merchant  (e.g., 'Dental', 'Medical', 'Veterinary'). Used for industry-specific analysis and market  segmentation. Sourced from stg_merchants.
 | **Industry Classification** - Cherry's internal industry classification for the merchant  (e.g., 'Dental', 'Medical', 'Veterinary'). Used for industry-specific analysis and market  segmentation. Sourced from stg_merchants.
 | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 59 | `TEXT` | **Industry Segment** - Higher-level grouping of industries for resource allocation and strategic  analysis (e.g., 'Dental', 'MedSpa'). Used for business unit reporting and resource  planning. Sourced from stg_merchants.
 | **Industry Segment** - Higher-level grouping of industries for resource allocation and strategic  analysis (e.g., 'Dental', 'MedSpa'). Used for business unit reporting and resource  planning. Sourced from stg_merchants.
 | `[]` | `{}` |
    | `PRACTICE_SEGMENT` | 60 | `TEXT` |  |  | `[]` | `{}` |
    | `MARKET_SIZE` | 61 | `TEXT` |  |  | `[]` | `{}` |
    | `PRICING_TIER` | 62 | `TEXT` | **Pricing Tier** - Pricing tier assigned to the merchant's organization based on volume and  relationship status. Determines fee structures and rate offerings. Used for pricing analysis  and revenue optimization. Sourced from pricing_tiers CTE.
 | **Pricing Tier** - Pricing tier assigned to the merchant's organization based on volume and  relationship status. Determines fee structures and rate offerings. Used for pricing analysis  and revenue optimization. Sourced from pricing_tiers CTE.
 | `[]` | `{}` |
    | `GO_LIVE_DATE` | 63 | `DATE` | **Merchant Go-Live Date** - Date when the merchant first went live with Cherry services. Used  for merchant lifecycle analysis, tenure calculations, and performance tracking relative to onboarding.  Sourced from stg_merchants.
 | **Merchant Go-Live Date** - Date when the merchant first went live with Cherry services. Used  for merchant lifecycle analysis, tenure calculations, and performance tracking relative to onboarding.  Sourced from stg_merchants.
 | `[]` | `{}` |
    | `ORGANIZATION_GO_LIVE_DATE` | 64 | `DATE` | **Organization Go-Live Date** - Date when the merchant's organization first went live with Cherry.  May differ from merchant go_live_date for multi-location organizations. Used for organization-level  tenure analysis. Sourced from stg_merchants.
 | **Organization Go-Live Date** - Date when the merchant's organization first went live with Cherry.  May differ from merchant go_live_date for multi-location organizations. Used for organization-level  tenure analysis. Sourced from stg_merchants.
 | `[]` | `{}` |
    | `PRACTICE_SEGMENT_START_DATE` | 65 | `DATE` |  |  | `[]` | `{}` |
    | `MERCHANT_TERMINATED_BY_RISK` | 66 | `BOOLEAN` | **Risk Termination Flag** - Boolean flag indicating whether the merchant was terminated by Cherry's  risk team and the loan was funded after the termination date. Used for risk analysis and portfolio  quality assessment. Calculated with termination date logic.
 | **Risk Termination Flag** - Boolean flag indicating whether the merchant was terminated by Cherry's  risk team and the loan was funded after the termination date. Used for risk analysis and portfolio  quality assessment. Calculated with termination date logic.
 | `[]` | `{}` |
    | `ORGANIZATION_ID` | 67 | `NUMBER` | **Organization Identifier** - Foreign key reference to the merchant's organization. Multiple  merchants can belong to the same organization for multi-location businesses. Used for organization-level  analysis and relationship management. Sourced from stg_merchants.
 | **Organization Identifier** - Foreign key reference to the merchant's organization. Multiple  merchants can belong to the same organization for multi-location businesses. Used for organization-level  analysis and relationship management. Sourced from stg_merchants.
 | `[]` | `{}` |
    | `ORGANIZATION_NAME` | 68 | `TEXT` | **Organization Name** - Human-readable name of the merchant's organization. Used for organization-level  reporting and relationship management. Sourced from stg_merchants.
 | **Organization Name** - Human-readable name of the merchant's organization. Used for organization-level  reporting and relationship management. Sourced from stg_merchants.
 | `[]` | `{}` |
    | `ORGANIZATION_GROUP_ID` | 69 | `NUMBER` | **Organization Group Identifier** - Foreign key reference to the organization group for large  multi-organization entities. Used for enterprise-level analysis and relationship management.  NULL for organizations not part of larger groups. Sourced from stg_merchants.
 | **Organization Group Identifier** - Foreign key reference to the organization group for large  multi-organization entities. Used for enterprise-level analysis and relationship management.  NULL for organizations not part of larger groups. Sourced from stg_merchants.
 | `[]` | `{}` |
    | `ORGANIZATION_GROUP_NAME` | 70 | `TEXT` | **Organization Group Name** - Human-readable name of the organization group for enterprise  accounts. Used for enterprise-level reporting and strategic account management. NULL for  organizations not part of larger groups. Sourced from stg_merchants.
 | **Organization Group Name** - Human-readable name of the organization group for enterprise  accounts. Used for enterprise-level reporting and strategic account management. NULL for  organizations not part of larger groups. Sourced from stg_merchants.
 | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT_CURRENT` | 71 | `TEXT` | **Current Retention Department** - Current department assignment for retention ownership from  stg_merchants static data. COALESCED to 'Unassigned' when NULL. Used for current organizational  structure analysis. Sourced from stg_merchants.
 | **Current Retention Department** - Current department assignment for retention ownership from  stg_merchants static data. COALESCED to 'Unassigned' when NULL. Used for current organizational  structure analysis. Sourced from stg_merchants.
 | `[]` | `{}` |
    | `RETENTION_OWNER_TEAM_CURRENT` | 72 | `TEXT` | **Current Retention Team** - Current team assignment for retention ownership from stg_merchants  static data. COALESCED to 'Unassigned' when NULL. Used for current team structure analysis.  Sourced from stg_merchants.
 | **Current Retention Team** - Current team assignment for retention ownership from stg_merchants  static data. COALESCED to 'Unassigned' when NULL. Used for current team structure analysis.  Sourced from stg_merchants.
 | `[]` | `{}` |
    | `RETENTION_OWNER_CURRENT` | 73 | `TEXT` | **Current Retention Owner** - Current retention owner name from stg_merchants static data.  COALESCED to 'Unassigned' when NULL. Used for current ownership tracking and workload distribution.  Sourced from stg_merchants.
 | **Current Retention Owner** - Current retention owner name from stg_merchants static data.  COALESCED to 'Unassigned' when NULL. Used for current ownership tracking and workload distribution.  Sourced from stg_merchants.
 | `[]` | `{}` |
    | `ACCOUNT_TERRITORY_CURRENT` | 74 | `TEXT` | **Current Account Territory** - Current territory assignment from stg_merchants static data.  COALESCED to 'Unassigned' when NULL. Used for territory-based analysis and geographic distribution.  Sourced from stg_merchants.
 | **Current Account Territory** - Current territory assignment from stg_merchants static data.  COALESCED to 'Unassigned' when NULL. Used for territory-based analysis and geographic distribution.  Sourced from stg_merchants.
 | `[]` | `{}` |
    | `CURRENT_PARTNERSHIP_HEALTH_SCORE` | 75 | `FLOAT` | **Current Partnership Health Score** - Current health score for the merchant partnership, using  first_60_days model for new merchants (≤60 days from go_live) and standard model for established  merchants. Ranges from 0-100 with higher scores indicating healthier relationships. Used for  account management prioritization. Sourced from daily_health_scores.
 | **Current Partnership Health Score** - Current health score for the merchant partnership, using  first_60_days model for new merchants (≤60 days from go_live) and standard model for established  merchants. Ranges from 0-100 with higher scores indicating healthier relationships. Used for  account management prioritization. Sourced from daily_health_scores.
 | `[]` | `{}` |
    | `ALLE_PRACTICE_TYPE` | 76 | `TEXT` | **Allē Practice Type** - Classification of the practice type for Allē merchants (e.g., 'New Practice',  'Existing Practice'). Used for Allē-specific analysis and practice development tracking. Sourced  from stg_practices.
 | **Allē Practice Type** - Classification of the practice type for Allē merchants (e.g., 'New Practice',  'Existing Practice'). Used for Allē-specific analysis and practice development tracking. Sourced  from stg_practices.
 | `[]` | `{}` |
    | `ONBOARDING_OWNER_ID` | 77 | `TEXT` | **Onboarding Owner Identifier** - Foreign key reference to the Salesforce user who was responsible  for merchant onboarding at the time of loan funding. Used for onboarding performance analysis and  attribution. Sourced from stg_merchants.
 | **Onboarding Owner Identifier** - Foreign key reference to the Salesforce user who was responsible  for merchant onboarding at the time of loan funding. Used for onboarding performance analysis and  attribution. Sourced from stg_merchants.
 | `[]` | `{}` |
    | `ONBOARDING_OWNER_NAME` | 78 | `TEXT` | **Onboarding Owner Name** - Full name of the onboarding specialist responsible for the merchant at  loan funding time. Prioritizes seed data over Salesforce historical data using IFF logic. Used for  onboarding attribution and performance tracking. Sourced from sf_user_history with seed priority.
 | **Onboarding Owner Name** - Full name of the onboarding specialist responsible for the merchant at  loan funding time. Prioritizes seed data over Salesforce historical data using IFF logic. Used for  onboarding attribution and performance tracking. Sourced from sf_user_history with seed priority.
 | `[]` | `{}` |
    | `ONBOARDING_OWNER_DEPARTMENT` | 79 | `TEXT` | **Onboarding Owner Department** - Department of the onboarding specialist at loan funding time.  Used for departmental performance analysis and organizational structure tracking. Sourced from  sf_user_history with seed data prioritization.
 | **Onboarding Owner Department** - Department of the onboarding specialist at loan funding time.  Used for departmental performance analysis and organizational structure tracking. Sourced from  sf_user_history with seed data prioritization.
 | `[]` | `{}` |
    | `ONBOARDING_OWNER_TEAM` | 80 | `TEXT` | **Onboarding Owner Team** - Team assignment of the onboarding specialist at loan funding time.  Used for team-level performance analysis and workload distribution tracking. Sourced from  sf_user_history with seed data prioritization.
 | **Onboarding Owner Team** - Team assignment of the onboarding specialist at loan funding time.  Used for team-level performance analysis and workload distribution tracking. Sourced from  sf_user_history with seed data prioritization.
 | `[]` | `{}` |
    | `ONBOARDING_OWNER_SUBTEAM` | 81 | `TEXT` | **Onboarding Owner Subteam** - Subteam assignment of the onboarding specialist at loan funding time.  Provides granular team structure for detailed performance analysis. Sourced from sf_user_history  with seed data prioritization.
 | **Onboarding Owner Subteam** - Subteam assignment of the onboarding specialist at loan funding time.  Provides granular team structure for detailed performance analysis. Sourced from sf_user_history  with seed data prioritization.
 | `[]` | `{}` |
    | `ONBOARDING_OWNER_TITLE` | 82 | `TEXT` | **Onboarding Owner Title** - Job title of the onboarding specialist at loan funding time. Used for  role-based analysis and organizational hierarchy tracking. Sourced from sf_user_history with seed  data prioritization.
 | **Onboarding Owner Title** - Job title of the onboarding specialist at loan funding time. Used for  role-based analysis and organizational hierarchy tracking. Sourced from sf_user_history with seed  data prioritization.
 | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_ID` | 83 | `TEXT` | **Opportunity Owner Identifier** - Foreign key reference to the Salesforce user who owned the sales  opportunity at loan funding time. Uses historical override when available, otherwise uses opportunity  history. Used for sales attribution and commission calculations. Derived from opportunities and  opportunity_history CTEs.
 | **Opportunity Owner Identifier** - Foreign key reference to the Salesforce user who owned the sales  opportunity at loan funding time. Uses historical override when available, otherwise uses opportunity  history. Used for sales attribution and commission calculations. Derived from opportunities and  opportunity_history CTEs.
 | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_NAME` | 84 | `TEXT` | **Opportunity Owner Name** - Full name of the sales representative who owned the opportunity at loan  funding time. Prioritizes seed data over Salesforce historical data. Used for sales attribution and  performance tracking. Sourced from sf_user_history with seed priority.
 | **Opportunity Owner Name** - Full name of the sales representative who owned the opportunity at loan  funding time. Prioritizes seed data over Salesforce historical data. Used for sales attribution and  performance tracking. Sourced from sf_user_history with seed priority.
 | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_DEPARTMENT` | 85 | `TEXT` | **Opportunity Owner Department** - Department of the opportunity owner at loan funding time. Used for  departmental sales performance analysis and organizational structure tracking. Sourced from  sf_user_history with seed data prioritization.
 | **Opportunity Owner Department** - Department of the opportunity owner at loan funding time. Used for  departmental sales performance analysis and organizational structure tracking. Sourced from  sf_user_history with seed data prioritization.
 | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_TEAM` | 86 | `TEXT` | **Opportunity Owner Team** - Team assignment of the opportunity owner at loan funding time. Used for  team-level sales performance analysis and territory management. Sourced from sf_user_history with  seed data prioritization.
 | **Opportunity Owner Team** - Team assignment of the opportunity owner at loan funding time. Used for  team-level sales performance analysis and territory management. Sourced from sf_user_history with  seed data prioritization.
 | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_SUBTEAM` | 87 | `TEXT` | **Opportunity Owner Subteam** - Subteam assignment of the opportunity owner at loan funding time.  Provides granular team structure for detailed sales analysis. Sourced from sf_user_history with  seed data prioritization.
 | **Opportunity Owner Subteam** - Subteam assignment of the opportunity owner at loan funding time.  Provides granular team structure for detailed sales analysis. Sourced from sf_user_history with  seed data prioritization.
 | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_TITLE` | 88 | `TEXT` | **Opportunity Owner Title** - Job title of the opportunity owner at loan funding time. Used for  role-based sales analysis and organizational hierarchy tracking. Sourced from sf_user_history with  seed data prioritization.
 | **Opportunity Owner Title** - Job title of the opportunity owner at loan funding time. Used for  role-based sales analysis and organizational hierarchy tracking. Sourced from sf_user_history with  seed data prioritization.
 | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_CREDIT_PERCENT` | 89 | `FLOAT` | **Opportunity Owner Credit Percentage** - Percentage of credit attributed to the opportunity owner  for this loan, calculated as (1.0 - assistor_credit_percent). Used for commission calculations and  split attribution. Defaults to 1.0 when no assistor exists. Derived from opportunity_history.
 | **Opportunity Owner Credit Percentage** - Percentage of credit attributed to the opportunity owner  for this loan, calculated as (1.0 - assistor_credit_percent). Used for commission calculations and  split attribution. Defaults to 1.0 when no assistor exists. Derived from opportunity_history.
 | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_GROSS_AMOUNT` | 90 | `FLOAT` | **Opportunity Owner Gross Amount** - Dollar amount of gross loan value attributed to the opportunity  owner for commission purposes, calculated as gross_amount × opportunity_owner_credit_percent. Used  for commission calculations and sales performance analysis. Calculated field.
 | **Opportunity Owner Gross Amount** - Dollar amount of gross loan value attributed to the opportunity  owner for commission purposes, calculated as gross_amount × opportunity_owner_credit_percent. Used  for commission calculations and sales performance analysis. Calculated field.
 | `[]` | `{}` |
    | `OPPORTUNITY_ASSISTOR_ID` | 91 | `TEXT` | **Opportunity Assistor Identifier** - Foreign key reference to the Salesforce user who assisted with  the sales opportunity at loan funding time. Used for split commission attribution and sales support  analysis. NULL when no assistor exists. Sourced from opportunity_history.
 | **Opportunity Assistor Identifier** - Foreign key reference to the Salesforce user who assisted with  the sales opportunity at loan funding time. Used for split commission attribution and sales support  analysis. NULL when no assistor exists. Sourced from opportunity_history.
 | `[]` | `{}` |
    | `OPPORTUNITY_ASSISTOR_NAME` | 92 | `TEXT` | **Opportunity Assistor Name** - Full name of the sales assistant who supported the opportunity at  loan funding time. Prioritizes seed data over Salesforce historical data. Used for sales support  attribution. NULL when no assistor. Sourced from sf_user_history with seed priority.
 | **Opportunity Assistor Name** - Full name of the sales assistant who supported the opportunity at  loan funding time. Prioritizes seed data over Salesforce historical data. Used for sales support  attribution. NULL when no assistor. Sourced from sf_user_history with seed priority.
 | `[]` | `{}` |
    | `OPPORTUNITY_ASSISTOR_DEPARTMENT` | 93 | `TEXT` | **Opportunity Assistor Department** - Department of the opportunity assistor at loan funding time.  Used for departmental support analysis. NULL when no assistor exists. Sourced from sf_user_history  with seed data prioritization.
 | **Opportunity Assistor Department** - Department of the opportunity assistor at loan funding time.  Used for departmental support analysis. NULL when no assistor exists. Sourced from sf_user_history  with seed data prioritization.
 | `[]` | `{}` |
    | `OPPORTUNITY_ASSISTOR_TEAM` | 94 | `TEXT` | **Opportunity Assistor Team** - Team assignment of the opportunity assistor at loan funding time.  Used for team-level support analysis. NULL when no assistor exists. Sourced from sf_user_history  with seed data prioritization.
 | **Opportunity Assistor Team** - Team assignment of the opportunity assistor at loan funding time.  Used for team-level support analysis. NULL when no assistor exists. Sourced from sf_user_history  with seed data prioritization.
 | `[]` | `{}` |
    | `OPPORTUNITY_ASSISTOR_SUBTEAM` | 95 | `TEXT` | **Opportunity Assistor Subteam** - Subteam assignment of the opportunity assistor at loan funding time.  Provides granular team structure for support analysis. NULL when no assistor. Sourced from sf_user_history  with seed data prioritization.
 | **Opportunity Assistor Subteam** - Subteam assignment of the opportunity assistor at loan funding time.  Provides granular team structure for support analysis. NULL when no assistor. Sourced from sf_user_history  with seed data prioritization.
 | `[]` | `{}` |
    | `OPPORTUNITY_ASSISTOR_TITLE` | 96 | `TEXT` | **Opportunity Assistor Title** - Job title of the opportunity assistor at loan funding time. Used for  role-based support analysis. NULL when no assistor exists. Sourced from sf_user_history with seed  data prioritization.
 | **Opportunity Assistor Title** - Job title of the opportunity assistor at loan funding time. Used for  role-based support analysis. NULL when no assistor exists. Sourced from sf_user_history with seed  data prioritization.
 | `[]` | `{}` |
    | `OPPORTUNITY_ASSISTOR_CREDIT_PERCENT` | 97 | `FLOAT` | **Opportunity Assistor Credit Percentage** - Percentage of credit attributed to the opportunity assistor  for this loan. Used for split commission calculations. NULL when no assistor exists. Sourced from  opportunity_history (assistor_credit_percent).
 | **Opportunity Assistor Credit Percentage** - Percentage of credit attributed to the opportunity assistor  for this loan. Used for split commission calculations. NULL when no assistor exists. Sourced from  opportunity_history (assistor_credit_percent).
 | `[]` | `{}` |
    | `OPPORTUNITY_ASSISTOR_GROSS_AMOUNT` | 98 | `FLOAT` | **Opportunity Assistor Gross Amount** - Dollar amount of gross loan value attributed to the opportunity  assistor for commission purposes, calculated as gross_amount × opportunity_assistor_credit_percent.  Used for split commission calculations. NULL when no assistor. Calculated field.
 | **Opportunity Assistor Gross Amount** - Dollar amount of gross loan value attributed to the opportunity  assistor for commission purposes, calculated as gross_amount × opportunity_assistor_credit_percent.  Used for split commission calculations. NULL when no assistor. Calculated field.
 | `[]` | `{}` |
    | `RETENTION_OWNER_ID` | 99 | `TEXT` | **Retention Owner Identifier** - Foreign key reference to the Salesforce user who was responsible  for account retention at loan funding time. Used for retention attribution and account management  analysis. Sourced from retention_history.
 | **Retention Owner Identifier** - Foreign key reference to the Salesforce user who was responsible  for account retention at loan funding time. Used for retention attribution and account management  analysis. Sourced from retention_history.
 | `[]` | `{}` |
    | `RETENTION_OWNER_NAME` | 100 | `TEXT` | **Retention Owner Name** - Full name of the retention specialist responsible for the account at loan  funding time. Uses daily ownership data when available, then falls back to historical user data with  seed prioritization. COALESCED to 'Unassigned' when no owner found. Used for retention attribution.
 | **Retention Owner Name** - Full name of the retention specialist responsible for the account at loan  funding time. Uses daily ownership data when available, then falls back to historical user data with  seed prioritization. COALESCED to 'Unassigned' when no owner found. Used for retention attribution.
 | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT` | 101 | `TEXT` | **Retention Owner Department** - Department of the retention owner at loan funding time. Uses daily  ownership data when available, then historical user data. COALESCED to 'Unassigned' when not found.  Used for departmental retention analysis.
 | **Retention Owner Department** - Department of the retention owner at loan funding time. Uses daily  ownership data when available, then historical user data. COALESCED to 'Unassigned' when not found.  Used for departmental retention analysis.
 | `[]` | `{}` |
    | `RETENTION_OWNER_TEAM` | 102 | `TEXT` | **Retention Owner Team** - Team assignment of the retention owner at loan funding time. Uses daily  ownership data when available, then historical user data. COALESCED to 'Unassigned' when not found.  Used for team-level retention analysis.
 | **Retention Owner Team** - Team assignment of the retention owner at loan funding time. Uses daily  ownership data when available, then historical user data. COALESCED to 'Unassigned' when not found.  Used for team-level retention analysis.
 | `[]` | `{}` |
    | `RETENTION_OWNER_TITLE` | 103 | `TEXT` | **Retention Owner Title** - Job title of the retention owner at loan funding time. Uses daily ownership  data when available, then historical user data. Used for role-based retention analysis. May be NULL  when title not available.
 | **Retention Owner Title** - Job title of the retention owner at loan funding time. Uses daily ownership  data when available, then historical user data. Used for role-based retention analysis. May be NULL  when title not available.
 | `[]` | `{}` |
    | `ACCOUNT_TERRITORY` | 104 | `TEXT` | **Account Territory** - Territory assignment for the account at loan funding time. Uses daily ownership  data when available. COALESCED to 'Unassigned' when not found. Used for territorial analysis and  geographic performance tracking.
 | **Account Territory** - Territory assignment for the account at loan funding time. Uses daily ownership  data when available. COALESCED to 'Unassigned' when not found. Used for territorial analysis and  geographic performance tracking.
 | `[]` | `{}` |
    | `DEPARTMENT_OWNERSHIP` | 105 | `TEXT` | **Department Ownership** - Lifecycle-based department assignment determined by days between merchant  go_live_date and loan funding: 'Account Executives' (0-30 days), 'Handoff' (31-60 days), 'Retention'  (>60 days). Used for lifecycle analysis and departmental responsibility tracking. Calculated field.
 | **Department Ownership** - Lifecycle-based department assignment determined by days between merchant  go_live_date and loan funding: 'Account Executives' (0-30 days), 'Handoff' (31-60 days), 'Retention'  (>60 days). Used for lifecycle analysis and departmental responsibility tracking. Calculated field.
 | `[]` | `{}` |
    | `ORGANIZATION_AGE` | 106 | `TEXT` | **Organization Age Category** - Classification of organization maturity at loan funding time:  'First Year' (before organization_second_year_start_date) or 'Over One Year'. Used for organization  lifecycle analysis and performance tracking by tenure. Calculated from organization dates.
 | **Organization Age Category** - Classification of organization maturity at loan funding time:  'First Year' (before organization_second_year_start_date) or 'Over One Year'. Used for organization  lifecycle analysis and performance tracking by tenure. Calculated from organization dates.
 | `[]` | `{}` |
    | `INITIAL_LOOK_ASSESSMENT` | 107 | `TEXT` | **Initial Look Assessment** - Initial practice assessment classification at 60 days post go-live or  quarter end for eligible industry segments (Dental, MedSpa, Plastic and Cosmetic Surgery,  Veterinary). COALESCED to 'Unclassified' when not assessed. Used for initial assessment analysis.  Sourced from look_assessment_history.
 | **Initial Look Assessment** - Initial practice assessment classification at 60 days post go-live or  quarter end for eligible industry segments (Dental, MedSpa, Plastic and Cosmetic Surgery,  Veterinary). COALESCED to 'Unclassified' when not assessed. Used for initial assessment analysis.  Sourced from look_assessment_history.
 | `[]` | `{}` |
    | `LATEST_LOOK_ASSESSMENT` | 108 | `TEXT` | **Latest Look Assessment** - Most recent practice assessment classification for eligible industry  segments. COALESCED to 'Unclassified' when not assessed. Used for current practice evaluation and  performance tracking. Sourced from look_assessment_history.
 | **Latest Look Assessment** - Most recent practice assessment classification for eligible industry  segments. COALESCED to 'Unclassified' when not assessed. Used for current practice evaluation and  performance tracking. Sourced from look_assessment_history.
 | `[]` | `{}` |
    | `LATEST_LOOK_ASSESSMENT_NEW_VET_MODEL` | 109 | `TEXT` |  |  | `[]` | `{}` |
    | `STATE_ABBREVIATION` | 110 | `TEXT` | **Practice State** - Two-letter state abbreviation for the practice location. Used for geographic  analysis, compliance tracking, and regional performance analysis. Sourced from stg_practices. | **Practice State** - Two-letter state abbreviation for the practice location. Used for geographic  analysis, compliance tracking, and regional performance analysis. Sourced from stg_practices. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.daily_health_scores`
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.loan_revenue_details`
    *   `model.cherry_data_model.look_assessment_history`
    *   `model.cherry_data_model.look_assessment_history_new_vet_model`
    *   `model.cherry_data_model.opportunity_owner_history`
    *   `model.cherry_data_model.retention_daily_ownership`
    *   `model.cherry_data_model.retention_owner_history`
    *   `model.cherry_data_model.sf_user_history`
    *   `model.cherry_data_model.src_menu_tiers`
    *   `model.cherry_data_model.src_organization_tiers`
    *   `model.cherry_data_model.src_sf_opportunities`
    *   `model.cherry_data_model.stg_loan_product_aprs`
    *   `model.cherry_data_model.stg_merchants`
    *   `model.cherry_data_model.stg_practices`

---
