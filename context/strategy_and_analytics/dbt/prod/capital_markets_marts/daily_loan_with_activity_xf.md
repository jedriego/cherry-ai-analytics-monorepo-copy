## Model: `daily_loan_with_activity_xf`

`daily_loan_with_activity_xf`

*   **Unique ID:** `model.cherry_data_model.daily_loan_with_activity_xf`
*   **FQN:** `prod.capital_markets_marts.daily_loan_with_activity_xf`
*   **Description:** This model serves as a roll-up of the `daily_loan_xf` model combined with the `stg_loan_tx_with_fee_details` and `charged_off_view_xf` models to provide daily details about loan activities.

*   **Tags:** `['performance_data']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `UNIQUE_KEY` | 1 | `TEXT` | Surrogate key uniquely identifying each daily loan record, generated from the combination  of loanpro_loan_id and record_date. Serves as the primary key for daily loan snapshots  and ensures uniqueness across the time series data.
 | Surrogate key uniquely identifying each daily loan record, generated from the combination  of loanpro_loan_id and record_date. Serves as the primary key for daily loan snapshots  and ensures uniqueness across the time series data.
 | `[]` | `{}` |
    | `LOAN_ID` | 2 | `NUMBER` | Foreign key reference to Cherry's internal loan identifier. This is the primary loan ID  used throughout Cherry's business intelligence and analytics ecosystem, enabling joins  with merchant data, application information, and business reporting models.
 | Foreign key reference to Cherry's internal loan identifier. This is the primary loan ID  used throughout Cherry's business intelligence and analytics ecosystem, enabling joins  with merchant data, application information, and business reporting models.
 | `[]` | `{}` |
    | `CONTRACT_ID` | 3 | `TEXT` | Foreign key reference to the loan contract identifier (display ID). This human-readable  identifier is used in customer communications and represents the legal contract between  Cherry and the borrower.
 | Foreign key reference to the loan contract identifier (display ID). This human-readable  identifier is used in customer communications and represents the legal contract between  Cherry and the borrower.
 | `[]` | `{}` |
    | `LOANPRO_LOAN_ID` | 4 | `NUMBER` | Foreign key reference to the LoanPro system loan identifier. This is the primary identifier  used within LoanPro for loan servicing, payment processing, and system operations. Essential  for linking to LoanPro transaction data and servicing events.
 | Foreign key reference to the LoanPro system loan identifier. This is the primary identifier  used within LoanPro for loan servicing, payment processing, and system operations. Essential  for linking to LoanPro transaction data and servicing events.
 | `[]` | `{}` |
    | `BORROWER_ID` | 5 | `NUMBER` | Foreign key reference to Cherry's borrower identifier. Links the loan to borrower-specific  information including contact details, credit history, and account management data.
 | Foreign key reference to Cherry's borrower identifier. Links the loan to borrower-specific  information including contact details, credit history, and account management data.
 | `[]` | `{}` |
    | `RECORD_DATE` | 6 | `DATE` | Calendar date for the daily loan snapshot. Represents the business date for which the loan  status, balances, and metrics were recorded. Serves as the primary time dimension for  time-series analysis and historical loan performance tracking.
 | Calendar date for the daily loan snapshot. Represents the business date for which the loan  status, balances, and metrics were recorded. Serves as the primary time dimension for  time-series analysis and historical loan performance tracking.
 | `[]` | `{}` |
    | `WEEK_MONDAY` | 7 | `DATE` | Week identifier showing the Monday date of the week containing the record_date. Used for  weekly aggregations, reporting, and trend analysis across loan portfolio performance.
 | Week identifier showing the Monday date of the week containing the record_date. Used for  weekly aggregations, reporting, and trend analysis across loan portfolio performance.
 | `[]` | `{}` |
    | `LOAN_STATUS` | 8 | `TEXT` | Current status of the loan from the LoanPro system as of the record_date. Common values  include 'LATE', 'OPEN', 'Closed', 'Bankruptcy', 'Charged Off'. This is the primary  status field for loan categorization, workflow management, and reporting.
 | Current status of the loan from the LoanPro system as of the record_date. Common values  include 'LATE', 'OPEN', 'Closed', 'Bankruptcy', 'Charged Off'. This is the primary  status field for loan categorization, workflow management, and reporting.
 | `[]` | `{}` |
    | `LOAN_SUBSTATUS` | 9 | `TEXT` | Current sub-status providing additional detail about the loan's operational state.  Examples include 'Settled', 'Deceased', 'Fraud', 'Filed'. Provides granular context  for loan management, collections strategy, and specialized handling requirements.
 | Current sub-status providing additional detail about the loan's operational state.  Examples include 'Settled', 'Deceased', 'Fraud', 'Filed'. Provides granular context  for loan management, collections strategy, and specialized handling requirements.
 | `[]` | `{}` |
    | `PAYOFF` | 10 | `NUMBER` | Total amount required to completely pay off the loan as of the record_date. Includes  all outstanding principal, accrued interest, fees, and any payoff-specific charges.  Critical for loan closure processing and borrower payoff quotes.
 | Total amount required to completely pay off the loan as of the record_date. Includes  all outstanding principal, accrued interest, fees, and any payoff-specific charges.  Critical for loan closure processing and borrower payoff quotes.
 | `[]` | `{}` |
    | `PRINCIPAL_BALANCE` | 11 | `NUMBER` | Outstanding principal balance of the loan as of the record_date. Represents the remaining  loan amount owed by the borrower, excluding interest and fees. Critical for loss calculations,  loan-to-value analysis, and principal paydown tracking.
 | Outstanding principal balance of the loan as of the record_date. Represents the remaining  loan amount owed by the borrower, excluding interest and fees. Critical for loss calculations,  loan-to-value analysis, and principal paydown tracking.
 | `[]` | `{}` |
    | `PI_DUE` | 12 | `NUMBER` | Principal and interest due on the loan as of the record_date. Excludes fees and represents  the core payment obligation. Used for payment processing, loan servicing calculations,  and borrower communication.
 | Principal and interest due on the loan as of the record_date. Excludes fees and represents  the core payment obligation. Used for payment processing, loan servicing calculations,  and borrower communication.
 | `[]` | `{}` |
    | `FEES_BALANCE` | 13 | `NUMBER` | Outstanding fees balance on the loan as of the record_date. Includes late fees, processing  fees, and other assessed charges. Important for fee revenue tracking, collections operations,  and total debt calculation.
 | Outstanding fees balance on the loan as of the record_date. Includes late fees, processing  fees, and other assessed charges. Important for fee revenue tracking, collections operations,  and total debt calculation.
 | `[]` | `{}` |
    | `AMOUNT_DUE` | 14 | `NUMBER` | Total amount currently due on the loan as of the record_date. Represents the sum of all  due amounts (principal, interest, fees) that the borrower needs to pay to bring the loan  current. Critical for collections operations and payment processing.
 | Total amount currently due on the loan as of the record_date. Represents the sum of all  due amounts (principal, interest, fees) that the borrower needs to pay to bring the loan  current. Critical for collections operations and payment processing.
 | `[]` | `{}` |
    | `PRINCIPAL_DUE` | 15 | `NUMBER` | Amount of principal currently due on the loan as of the record_date. Represents the principal  portion of scheduled payments that are due for payment. Used for payment processing,  collections strategy, and cash flow analysis.
 | Amount of principal currently due on the loan as of the record_date. Represents the principal  portion of scheduled payments that are due for payment. Used for payment processing,  collections strategy, and cash flow analysis.
 | `[]` | `{}` |
    | `INTEREST_DUE` | 16 | `NUMBER` | Amount of interest currently due on the loan as of the record_date. This includes accrued  interest that has become due for payment. Important for revenue recognition, collections  prioritization, and borrower payment allocation.
 | Amount of interest currently due on the loan as of the record_date. This includes accrued  interest that has become due for payment. Important for revenue recognition, collections  prioritization, and borrower payment allocation.
 | `[]` | `{}` |
    | `DPD` | 17 | `NUMBER` | Days Past Due - number of days the loan payment is overdue as of the record_date. This is  the primary delinquency metric used for risk assessment, collections strategy, regulatory  reporting, and charge-off determination. Values of 0 indicate current loans.
 | Days Past Due - number of days the loan payment is overdue as of the record_date. This is  the primary delinquency metric used for risk assessment, collections strategy, regulatory  reporting, and charge-off determination. Values of 0 indicate current loans.
 | `[]` | `{}` |
    | `NET_CHARGE_OFF_BALANCE` | 18 | `NUMBER` | Net charge-off amount for the loan as of the record_date (aliased from charge_off field).  Represents the total amount charged off minus any recoveries. Positive values indicate net loss,  while negative values may indicate recoveries exceeding original charge-off. Critical for loss  reporting and recovery tracking.
 | Net charge-off amount for the loan as of the record_date (aliased from charge_off field).  Represents the total amount charged off minus any recoveries. Positive values indicate net loss,  while negative values may indicate recoveries exceeding original charge-off. Critical for loss  reporting and recovery tracking.
 | `[]` | `{}` |
    | `DQ_BUCKET` | 19 | `NUMBER` | Delinquency bucket categorizing the loan based on days past due. Calculated as: 0 (current),  1 (1-29 DPD), 2 (30-59 DPD), 3 (60-89 DPD), 4 (90-120 DPD), 0 (>120 DPD). Used for risk  reporting, collections workflow management, and portfolio segmentation.
 | Delinquency bucket categorizing the loan based on days past due. Calculated as: 0 (current),  1 (1-29 DPD), 2 (30-59 DPD), 3 (60-89 DPD), 4 (90-120 DPD), 0 (>120 DPD). Used for risk  reporting, collections workflow management, and portfolio segmentation.
 | `[]` | `{}` |
    | `DAILY_ACCRUED_INTEREST` | 20 | `NUMBER` | Daily interest accrual amount for the loan as of the record_date. Derived as COALESCE(accrued_interest, perdiem),  representing the dollar amount of interest that accumulates each day on the outstanding balance.  Critical for revenue recognition, interest calculations, and financial reporting.
 | Daily interest accrual amount for the loan as of the record_date. Derived as COALESCE(accrued_interest, perdiem),  representing the dollar amount of interest that accumulates each day on the outstanding balance.  Critical for revenue recognition, interest calculations, and financial reporting.
 | `[]` | `{}` |
    | `PAYMENT_AMOUNT` | 21 | `NUMBER` | Total payment amount received on the record_date for transactions classified as 'payment'.  Aggregated from stg_loan_tx_with_fee_details and represents the gross amount paid by borrowers.  Zero when no payments were received on the date. Used for cash flow analysis and payment tracking.
 | Total payment amount received on the record_date for transactions classified as 'payment'.  Aggregated from stg_loan_tx_with_fee_details and represents the gross amount paid by borrowers.  Zero when no payments were received on the date. Used for cash flow analysis and payment tracking.
 | `[]` | `{}` |
    | `PRINCIPAL_PAID` | 22 | `NUMBER` | Amount of principal paid on the record_date from payment transactions. Represents the portion  of payments that reduced the outstanding loan balance. Zero when no payments were received.  Critical for principal paydown analysis and loan amortization tracking.
 | Amount of principal paid on the record_date from payment transactions. Represents the portion  of payments that reduced the outstanding loan balance. Zero when no payments were received.  Critical for principal paydown analysis and loan amortization tracking.
 | `[]` | `{}` |
    | `INTEREST_PAID` | 23 | `NUMBER` | Amount of interest paid on the record_date from payment transactions. Represents interest  revenue collected from borrower payments. Zero when no payments were received. Important  for revenue recognition and interest income tracking.
 | Amount of interest paid on the record_date from payment transactions. Represents interest  revenue collected from borrower payments. Zero when no payments were received. Important  for revenue recognition and interest income tracking.
 | `[]` | `{}` |
    | `FEES_PAID` | 24 | `NUMBER` | Amount of fees paid on the record_date from payment transactions. Includes late fees,  processing fees, and other charges collected through borrower payments. Zero when no  payments were received. Important for fee revenue tracking and collections analysis.
 | Amount of fees paid on the record_date from payment transactions. Includes late fees,  processing fees, and other charges collected through borrower payments. Zero when no  payments were received. Important for fee revenue tracking and collections analysis.
 | `[]` | `{}` |
    | `CREDIT_AMOUNT` | 25 | `NUMBER` | Total credit amount applied on the record_date for transactions classified as 'credit'.  Represents adjustments, refunds, or credits applied to the loan account. Zero when no  credits were applied. Used for account adjustment tracking and customer service analysis.
 | Total credit amount applied on the record_date for transactions classified as 'credit'.  Represents adjustments, refunds, or credits applied to the loan account. Zero when no  credits were applied. Used for account adjustment tracking and customer service analysis.
 | `[]` | `{}` |
    | `PRINCIPAL_CREDIT` | 26 | `NUMBER` | Amount of principal credited on the record_date from credit transactions. Represents  principal balance reductions due to adjustments or refunds. Zero when no credits were  applied. Used for account reconciliation and adjustment tracking.
 | Amount of principal credited on the record_date from credit transactions. Represents  principal balance reductions due to adjustments or refunds. Zero when no credits were  applied. Used for account reconciliation and adjustment tracking.
 | `[]` | `{}` |
    | `INTEREST_CREDIT` | 27 | `NUMBER` | Amount of interest credited on the record_date from credit transactions. Represents  interest adjustments or refunds applied to the account. Zero when no credits were applied.  Used for revenue adjustments and customer service resolution tracking.
 | Amount of interest credited on the record_date from credit transactions. Represents  interest adjustments or refunds applied to the account. Zero when no credits were applied.  Used for revenue adjustments and customer service resolution tracking.
 | `[]` | `{}` |
    | `FEES_CREDIT` | 28 | `NUMBER` | Amount of fees credited on the record_date from credit transactions. Represents fee  adjustments, waivers, or refunds applied to the account. Zero when no credits were applied.  Used for fee adjustment tracking and customer service analysis.
 | Amount of fees credited on the record_date from credit transactions. Represents fee  adjustments, waivers, or refunds applied to the account. Zero when no credits were applied.  Used for fee adjustment tracking and customer service analysis.
 | `[]` | `{}` |
    | `ADVANCEMENT_AMOUNT` | 29 | `NUMBER` | Total advancement amount on the record_date for transactions classified as 'advancement'.  Represents additional funds advanced to the borrower beyond the original loan amount.  Zero when no advancements were made. Used for loan modification and additional funding analysis.
 | Total advancement amount on the record_date for transactions classified as 'advancement'.  Represents additional funds advanced to the borrower beyond the original loan amount.  Zero when no advancements were made. Used for loan modification and additional funding analysis.
 | `[]` | `{}` |
    | `FEES_ASSESSED` | 30 | `NUMBER` | Total fees assessed on the record_date for transactions classified as 'fee'. Represents  new fees charged to the loan account, such as late fees or processing fees. Zero when no  fees were assessed. Important for fee revenue recognition and borrower account management.
 | Total fees assessed on the record_date for transactions classified as 'fee'. Represents  new fees charged to the loan account, such as late fees or processing fees. Zero when no  fees were assessed. Important for fee revenue recognition and borrower account management.
 | `[]` | `{}` |
    | `UNADJUSTED_CHARGE_OFF_AMOUNT` | 31 | `NUMBER` | Gross Unpaid Charge Off (GUCO) amount if the loan was charged off on the record_date.  Represents the total outstanding balance charged off including principal, interest, and fees.  This is the full amount of loss recognized at charge-off before any adjustments. Zero for  non-charge-off dates. Critical for loss calculations and provisioning.
 | Gross Unpaid Charge Off (GUCO) amount if the loan was charged off on the record_date.  Represents the total outstanding balance charged off including principal, interest, and fees.  This is the full amount of loss recognized at charge-off before any adjustments. Zero for  non-charge-off dates. Critical for loss calculations and provisioning.
 | `[]` | `{}` |
    | `ADJUSTED_CHARGE_OFF_AMOUNT` | 32 | `NUMBER` | Gross Adjusted Charge Off (GACO) amount if the loan was charged off on the record_date.  Represents the principal balance portion of the charge-off, excluding accrued interest and fees.  This adjusted amount may be used for certain regulatory or capital market reporting purposes.  Zero for non-charge-off dates. Used for specialized loss reporting and analysis. | Gross Adjusted Charge Off (GACO) amount if the loan was charged off on the record_date.  Represents the principal balance portion of the charge-off, excluding accrued interest and fees.  This adjusted amount may be used for certain regulatory or capital market reporting purposes.  Zero for non-charge-off dates. Used for specialized loss reporting and analysis. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.charged_off_view_xf`
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.stg_loan_tx_with_fee_details`

---
