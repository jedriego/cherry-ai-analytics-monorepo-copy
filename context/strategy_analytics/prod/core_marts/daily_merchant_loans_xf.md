## Model: `daily_merchant_loans_xf`

`daily_merchant_loans_xf`

*   **Unique ID:** `model.cherry_data_model.daily_merchant_loans_xf`
*   **FQN:** `prod.core_marts.daily_merchant_loans_xf`
*   **Description:** Daily grain fact table that combines merchant information with loan data to create a comprehensive view of loan funding activity by merchant and date. This model creates one row for each loan funded on each calendar date for each merchant, providing rich context about both the merchant practice and the loan details. The model spans from August 28, 2019 (earliest loan funded/merchant go-live date) through the current date and includes loans funded on specific dates. This enables analysis of loan volume, merchant performance, revenue metrics, and business trends over time with full merchant context including operational status, industry classification, organizational hierarchy, and retention ownership.

*   **Tags:** `['core']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `DAILY_MERCHANT_LOAN_ID` | 1 | `TEXT` | Surrogate key uniquely identifying each daily merchant loan record, generated from the combination of calendar_date, merchant_id, and loan_id.
 | Surrogate key uniquely identifying each daily merchant loan record, generated from the combination of calendar_date, merchant_id, and loan_id.
 | `[]` | `{}` |
    | `CALENDAR_DATE` | 2 | `DATE` | Date dimension representing the calendar day. Serves as the primary time dimension for this daily grain table, covering dates from August 28, 2019 through current date. Each date represents a day on which loans may have been funded.
 | Date dimension representing the calendar day. Serves as the primary time dimension for this daily grain table, covering dates from August 28, 2019 through current date. Each date represents a day on which loans may have been funded.
 | `[]` | `{}` |
    | `MERCHANT_ID` | 3 | `NUMBER` | Foreign key reference to the specific merchant location or practice where loans were funded. This is the primary merchant identifier for the individual practice.
 | Foreign key reference to the specific merchant location or practice where loans were funded. This is the primary merchant identifier for the individual practice.
 | `[]` | `{}` |
    | `PRIMARY_MERCHANT_ID` | 4 | `FLOAT` | Foreign key reference to the primary merchant identifier, used for grouping multiple merchant locations under a single primary practice entity.
 | Foreign key reference to the primary merchant identifier, used for grouping multiple merchant locations under a single primary practice entity.
 | `[]` | `{}` |
    | `SF_ACCOUNT_ID` | 5 | `TEXT` | Foreign key reference to the Salesforce account ID associated with the merchant, used for CRM integration and account management.
 | Foreign key reference to the Salesforce account ID associated with the merchant, used for CRM integration and account management.
 | `[]` | `{}` |
    | `GO_LIVE_DATE` | 6 | `DATE` | Date when the merchant went live and became operational. Used as the starting point for including the merchant in daily snapshots - merchants are only included in the date spine from their go-live date forward.
 | Date when the merchant went live and became operational. Used as the starting point for including the merchant in daily snapshots - merchants are only included in the date spine from their go-live date forward.
 | `[]` | `{}` |
    | `IS_GO_LIVE_MONTH_BEFORE_CALENDAR_DATE_MONTH` | 7 | `BOOLEAN` | Boolean flag indicating whether the merchant go-live date occurred in a month prior to the calendar date month. True when the merchant has been live for at least one full month as of the calendar date, useful for identifying seasoned merchants.
 | Boolean flag indicating whether the merchant go-live date occurred in a month prior to the calendar date month. True when the merchant has been live for at least one full month as of the calendar date, useful for identifying seasoned merchants.
 | `[]` | `{}` |
    | `IS_GO_LIVE_WEEK_BEFORE_CALENDAR_DATE_WEEK` | 8 | `BOOLEAN` | Boolean flag indicating whether the merchant go-live date occurred in a week prior to the calendar date week. True when the merchant has been live for at least one full week as of the calendar date, useful for identifying merchants past their initial launch period.
 | Boolean flag indicating whether the merchant go-live date occurred in a week prior to the calendar date week. True when the merchant has been live for at least one full week as of the calendar date, useful for identifying merchants past their initial launch period.
 | `[]` | `{}` |
    | `IS_ACTIVE` | 9 | `BOOLEAN` | Boolean flag indicating whether the merchant is currently active and operational, derived from the merchant_info_full_xf model.
 | Boolean flag indicating whether the merchant is currently active and operational, derived from the merchant_info_full_xf model.
 | `[]` | `{}` |
    | `IS_TERMINATED` | 10 | `BOOLEAN` | Boolean flag indicating whether the merchant has been terminated and is no longer operational.
 | Boolean flag indicating whether the merchant has been terminated and is no longer operational.
 | `[]` | `{}` |
    | `INDUSTRY` | 11 | `TEXT` | Industry classification of the merchant practice, derived from the cherry_db_industry field. Used for segmentation and analysis of loan patterns across different healthcare and service industries.
 | Industry classification of the merchant practice, derived from the cherry_db_industry field. Used for segmentation and analysis of loan patterns across different healthcare and service industries.
 | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 12 | `TEXT` | More granular industry segment classification derived from the account_industry_segment field, providing detailed categorization within broader industry groups.
 | More granular industry segment classification derived from the account_industry_segment field, providing detailed categorization within broader industry groups.
 | `[]` | `{}` |
    | `ORGANIZATION_ID` | 13 | `NUMBER` | Foreign key reference to the organization that owns this merchant practice, enabling analysis at the organizational level.
 | Foreign key reference to the organization that owns this merchant practice, enabling analysis at the organizational level.
 | `[]` | `{}` |
    | `ORGANIZATION_NAME` | 14 | `TEXT` | Name of the organization that owns this merchant practice, providing human-readable organizational context.
 | Name of the organization that owns this merchant practice, providing human-readable organizational context.
 | `[]` | `{}` |
    | `ORGANIZATION_GROUP_ID` | 15 | `NUMBER` | Foreign key reference to the organization group that the organization belongs to, enabling analysis at the highest organizational hierarchy level.
 | Foreign key reference to the organization group that the organization belongs to, enabling analysis at the highest organizational hierarchy level.
 | `[]` | `{}` |
    | `ORGANIZATION_GROUP_NAME` | 16 | `TEXT` | Name of the organization group, providing human-readable context for the highest level of organizational hierarchy.
 | Name of the organization group, providing human-readable context for the highest level of organizational hierarchy.
 | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT` | 17 | `TEXT` | Department responsible for merchant retention and relationship management, used for assigning retention responsibilities and performance tracking.
 | Department responsible for merchant retention and relationship management, used for assigning retention responsibilities and performance tracking.
 | `[]` | `{}` |
    | `RETENTION_OWNER_TEAM` | 18 | `TEXT` | Specific team within the retention department that owns the merchant relationship, providing more granular ownership assignment.
 | Specific team within the retention department that owns the merchant relationship, providing more granular ownership assignment.
 | `[]` | `{}` |
    | `RETENTION_OWNER` | 19 | `TEXT` | Individual retention specialist or account manager responsible for maintaining the merchant relationship and ensuring continued engagement.
 | Individual retention specialist or account manager responsible for maintaining the merchant relationship and ensuring continued engagement.
 | `[]` | `{}` |
    | `LOAN_ID` | 20 | `NUMBER` | Foreign key reference to the specific loan record. May be null for dates when no loans were funded for a given merchant.
 | Foreign key reference to the specific loan record. May be null for dates when no loans were funded for a given merchant.
 | `[]` | `{}` |
    | `CONTRACT_ID` | 21 | `TEXT` | Foreign key reference to the contract associated with the loan, linking to the legal agreement terms and conditions.
 | Foreign key reference to the contract associated with the loan, linking to the legal agreement terms and conditions.
 | `[]` | `{}` |
    | `BORROWER_ID` | 22 | `NUMBER` | Foreign key reference to the borrower who received the loan.
 | Foreign key reference to the borrower who received the loan.
 | `[]` | `{}` |
    | `APPLICATION_ID` | 23 | `NUMBER` | Foreign key reference to the application that resulted in this loan, linking the loan back to the original application process.
 | Foreign key reference to the application that resulted in this loan, linking the loan back to the original application process.
 | `[]` | `{}` |
    | `PRODUCT_ID` | 24 | `NUMBER` | Foreign key reference to the specific loan product or program used for this loan, indicating the terms and structure of the financing.
 | Foreign key reference to the specific loan product or program used for this loan, indicating the terms and structure of the financing.
 | `[]` | `{}` |
    | `CHANNEL` | 25 | `TEXT` | Channel through which the loan was originated (e.g., web, mobile, in-person), used for analyzing channel effectiveness and performance.
 | Channel through which the loan was originated (e.g., web, mobile, in-person), used for analyzing channel effectiveness and performance.
 | `[]` | `{}` |
    | `API_PARTNER` | 26 | `TEXT` | Identifier for the API partner or integration source that originated the loan, used for tracking partner performance and attribution.
 | Identifier for the API partner or integration source that originated the loan, used for tracking partner performance and attribution.
 | `[]` | `{}` |
    | `PROMO_USED` | 27 | `BOOLEAN` | Promotional code or offer applied to the loan, used for tracking marketing campaign effectiveness and promotional program usage.
 | Promotional code or offer applied to the loan, used for tracking marketing campaign effectiveness and promotional program usage.
 | `[]` | `{}` |
    | `PURCHASE_AMOUNT` | 28 | `FLOAT` | Total dollar amount of the purchase or service being financed by the loan.
 | Total dollar amount of the purchase or service being financed by the loan.
 | `[]` | `{}` |
    | `MERCHANT_FEE` | 29 | `FLOAT` | Dollar amount of fees charged to the merchant for the loan, representing the merchant's cost for providing financing options.
 | Dollar amount of fees charged to the merchant for the loan, representing the merchant's cost for providing financing options.
 | `[]` | `{}` |
    | `MERCHANT_FUND` | 30 | `FLOAT` | Dollar amount funded to the merchant, representing the amount the merchant receives after fees and discounts.
 | Dollar amount funded to the merchant, representing the amount the merchant receives after fees and discounts.
 | `[]` | `{}` |
    | `GROSS_AMOUNT` | 31 | `FLOAT` | Gross dollar amount of the loan before any adjustments or deductions.
 | Gross dollar amount of the loan before any adjustments or deductions.
 | `[]` | `{}` |
    | `DOWN_PAYMENT_AMOUNT` | 32 | `FLOAT` | Dollar amount of any down payment made by the borrower, reducing the financed amount.
 | Dollar amount of any down payment made by the borrower, reducing the financed amount.
 | `[]` | `{}` |
    | `NET_LOAN_AMOUNT` | 33 | `FLOAT` | Net dollar amount actually financed after down payments and adjustments, representing the principal balance of the loan.
 | Net dollar amount actually financed after down payments and adjustments, representing the principal balance of the loan.
 | `[]` | `{}` |
    | `FINANCE_CHARGE` | 34 | `FLOAT` | Total finance charges applied to the loan, representing the cost of borrowing for the customer.
 | Total finance charges applied to the loan, representing the cost of borrowing for the customer.
 | `[]` | `{}` |
    | `TOTAL_AMOUNT` | 35 | `FLOAT` | Total dollar amount the borrower will pay over the life of the loan, including principal and all charges.
 | Total dollar amount the borrower will pay over the life of the loan, including principal and all charges.
 | `[]` | `{}` |
    | `INSTALLMENT_AMOUNT` | 36 | `FLOAT` | Dollar amount of each scheduled payment installment for the loan.
 | Dollar amount of each scheduled payment installment for the loan.
 | `[]` | `{}` |
    | `IS_AUTOPAY` | 37 | `BOOLEAN` | Boolean flag indicating whether the loan is enrolled in automatic payment processing, used for tracking payment automation adoption.
 | Boolean flag indicating whether the loan is enrolled in automatic payment processing, used for tracking payment automation adoption.
 | `[]` | `{}` |
    | `IS_FRAUD` | 38 | `BOOLEAN` | Boolean flag indicating whether the loan has been flagged as fraudulent, used for fraud tracking and loss analysis.
 | Boolean flag indicating whether the loan has been flagged as fraudulent, used for fraud tracking and loss analysis.
 | `[]` | `{}` |
    | `IS_DO_NOT_REPORT` | 39 | `BOOLEAN` | Boolean flag indicating whether the loan should be excluded from credit bureau reporting, typically for special circumstances or agreements.
 | Boolean flag indicating whether the loan should be excluded from credit bureau reporting, typically for special circumstances or agreements.
 | `[]` | `{}` |
    | `IS_DO_NOT_CALL` | 40 | `BOOLEAN` | Boolean flag indicating whether the borrower has requested not to be contacted by phone, used for compliance with communication preferences.
 | Boolean flag indicating whether the borrower has requested not to be contacted by phone, used for compliance with communication preferences.
 | `[]` | `{}` |
    | `IS_OUTSOURCED` | 41 | `BOOLEAN` | Boolean flag indicating whether the loan servicing or collections have been outsourced to a third-party provider.
 | Boolean flag indicating whether the loan servicing or collections have been outsourced to a third-party provider.
 | `[]` | `{}` |
    | `IS_ACTIVATION` | 42 | `BOOLEAN` | Boolean flag indicating whether this loan represents an activation or reactivation of a previously inactive account.
 | Boolean flag indicating whether this loan represents an activation or reactivation of a previously inactive account.
 | `[]` | `{}` |
    | `LOAN_STATUS` | 43 | `TEXT` | Current status of the loan (e.g., open, closed, charged off, paid in full), indicating the loan's position in its lifecycle.
 | Current status of the loan (e.g., open, closed, charged off, paid in full), indicating the loan's position in its lifecycle.
 | `[]` | `{}` |
    | `REFUND_AMOUNT` | 44 | `FLOAT` | Dollar amount of any refunds processed for the loan, typically due to returns or cancellations.
 | Dollar amount of any refunds processed for the loan, typically due to returns or cancellations.
 | `[]` | `{}` |
    | `FUNDED_AT_PT` | 45 | `TIMESTAMP_NTZ` | Pacific Time timestamp when the loan was funded and disbursed.
 | Pacific Time timestamp when the loan was funded and disbursed.
 | `[]` | `{}` |
    | `LOANPRO_LOAN_ID` | 46 | `NUMBER` | Foreign key reference to the loan record in the LoanPro system, used for loan servicing and payment processing integration.
 | Foreign key reference to the loan record in the LoanPro system, used for loan servicing and payment processing integration.
 | `[]` | `{}` |
    | `CREATED_AT_PT` | 47 | `TIMESTAMP_NTZ` | Pacific Time timestamp when the loan record was first created in the system.
 | Pacific Time timestamp when the loan record was first created in the system.
 | `[]` | `{}` |
    | `CREATED_BY_NAME` | 48 | `TEXT` | Name of the user who created the loan record, used for audit trail and accountability tracking.
 | Name of the user who created the loan record, used for audit trail and accountability tracking.
 | `[]` | `{}` |
    | `CREATED_BY_EMAIL` | 49 | `TEXT` | Email address of the user who created the loan record, providing contact information for audit purposes.
 | Email address of the user who created the loan record, providing contact information for audit purposes.
 | `[]` | `{}` |
    | `UPDATED_AT_PT` | 50 | `TIMESTAMP_NTZ` | Pacific Time timestamp when the loan record was last updated.
 | Pacific Time timestamp when the loan record was last updated.
 | `[]` | `{}` |
    | `UPDATED_BY_NAME` | 51 | `TEXT` | Name of the user who last updated the loan record, used for audit trail and change tracking.
 | Name of the user who last updated the loan record, used for audit trail and change tracking.
 | `[]` | `{}` |
    | `UPDATED_BY_EMAIL` | 52 | `TEXT` | Email address of the user who last updated the loan record, providing contact information for audit purposes. | Email address of the user who last updated the loan record, providing contact information for audit purposes. | `[]` | `{}` |
    | `RISK_SCORE` | 53 | `NUMBER` | Calculated risk score for the loan at origination, used for risk assessment and portfolio management.
 | Calculated risk score for the loan at origination, used for risk assessment and portfolio management.
 | `[]` | `{}` |
    | `VINTAGE` | 54 | `TEXT` | Time period or cohort identifier for the loan, typically based on origination date, used for cohort analysis and vintage performance tracking.
 | Time period or cohort identifier for the loan, typically based on origination date, used for cohort analysis and vintage performance tracking.
 | `[]` | `{}` |
    | `MERCHANT_FEE_RATE` | 55 | `FLOAT` | Percentage rate charged to the merchant as a fee for the loan, calculated as merchant_fee divided by loan amount.
 | Percentage rate charged to the merchant as a fee for the loan, calculated as merchant_fee divided by loan amount.
 | `[]` | `{}` |
    | `FORECASTED_INTEREST` | 56 | `FLOAT` | Projected interest revenue expected to be earned over the life of the loan, used for revenue forecasting and profitability analysis.
 | Projected interest revenue expected to be earned over the life of the loan, used for revenue forecasting and profitability analysis.
 | `[]` | `{}` |
    | `FORECASTED_FEES` | 57 | `FLOAT` | Projected fee revenue expected to be earned over the life of the loan, including late fees and other charges.
 | Projected fee revenue expected to be earned over the life of the loan, including late fees and other charges.
 | `[]` | `{}` |
    | `FORECASTED_SERVICING_FEE` | 58 | `FLOAT` | Projected servicing fee revenue expected to be earned for loan administration and payment processing over the loan term.
 | Projected servicing fee revenue expected to be earned for loan administration and payment processing over the loan term.
 | `[]` | `{}` |
    | `REVENUE` | 59 | `FLOAT` | Total revenue generated or expected to be generated from the loan, including interest, fees, and other income sources.
 | Total revenue generated or expected to be generated from the loan, including interest, fees, and other income sources.
 | `[]` | `{}` |
    | `CONTRIBUTION_MARGIN` | 60 | `FLOAT` | Contribution margin for the loan, calculated as revenue minus variable costs, representing the loan's contribution to covering fixed costs and profit.
 | Contribution margin for the loan, calculated as revenue minus variable costs, representing the loan's contribution to covering fixed costs and profit.
 | `[]` | `{}` |
    | `MERCHANT_TERMINATED_BY_RISK` | 61 | `BOOLEAN` | Boolean flag indicating whether the merchant relationship was terminated due to risk factors, used for risk management and loss analysis.
 | Boolean flag indicating whether the merchant relationship was terminated due to risk factors, used for risk management and loss analysis.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt_utils.generate_surrogate_key`
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.loan_info_xf`
    *   `model.cherry_data_model.merchant_info_full_xf`

---
