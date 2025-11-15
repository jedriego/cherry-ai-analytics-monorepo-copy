## Model: `daily_loan_xf`

`daily_loan_xf`

*   **Unique ID:** `model.cherry_data_model.daily_loan_xf`
*   **FQN:** `prod.risk_marts.daily_loan_xf`
*   **Description:** **Comprehensive Daily Loan Performance Data with Cherry Integration**
This foundational model combines LoanPro's daily loan status archive with Cherry's loan identification  system, creating the primary data source for loan performance analytics and risk monitoring. The model  joins detailed daily loan snapshots from LoanPro (including balances, payment status, delinquency metrics)  with Cherry's loan and borrower identifiers, enabling comprehensive loan lifecycle analysis.
**Key Features:** - Complete daily loan status history from LoanPro system - Integration with Cherry loan and borrower IDs for business intelligence - Comprehensive balance and payment tracking (principal, interest, fees) - Delinquency monitoring with days past due (DPD) calculations - Charge-off and payoff tracking for portfolio risk analysis
**Primary Use Cases:** - Daily loan portfolio monitoring and performance analysis - Risk management and delinquency tracking - Regulatory reporting and compliance analytics - Capital markets and investor reporting - Collections and servicing operations support
**Data Sources:** - `stg_daily_loan`: Daily loan status snapshots from LoanPro with comprehensive balance and status data - `stg_cherry_loan_ids`: Cherry loan identifiers filtered to active loan statuses
**Grain:** One record per loan per calendar date (daily snapshots)

*   **Tags:** `['risk', 'performance_data', 'loans', 'daily_full_refresh', 'core_hourly']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `UNIQUE_KEY` | 1 | `TEXT` | Surrogate key uniquely identifying each daily loan record, generated from the combination  of loanpro_loan_id and record_date. Serves as the primary key for daily loan snapshots  and ensures uniqueness across the time series data.
 | Surrogate key uniquely identifying each daily loan record, generated from the combination  of loanpro_loan_id and record_date. Serves as the primary key for daily loan snapshots  and ensures uniqueness across the time series data.
 | `[]` | `{}` |
    | `RECORD_DATE` | 2 | `DATE` | Calendar date for the daily loan snapshot. Represents the business date for which the loan  status, balances, and metrics were recorded. Serves as the primary time dimension for  time-series analysis and historical loan performance tracking.
 | Calendar date for the daily loan snapshot. Represents the business date for which the loan  status, balances, and metrics were recorded. Serves as the primary time dimension for  time-series analysis and historical loan performance tracking.
 | `[]` | `{}` |
    | `WEEK_MONDAY` | 3 | `DATE` | Week identifier showing the Monday date of the week containing the record_date. Used for  weekly aggregations, reporting, and trend analysis across loan portfolio performance.
 | Week identifier showing the Monday date of the week containing the record_date. Used for  weekly aggregations, reporting, and trend analysis across loan portfolio performance.
 | `[]` | `{}` |
    | `AMOUNT_DUE` | 4 | `NUMBER` | Total amount currently due on the loan as of the record_date. Represents the sum of all  due amounts (principal, interest, fees) that the borrower needs to pay to bring the loan  current. Critical for collections operations and payment processing.
 | Total amount currently due on the loan as of the record_date. Represents the sum of all  due amounts (principal, interest, fees) that the borrower needs to pay to bring the loan  current. Critical for collections operations and payment processing.
 | `[]` | `{}` |
    | `INTEREST_DUE` | 5 | `NUMBER` | Amount of interest currently due on the loan as of the record_date. This includes accrued  interest that has become due for payment. Important for revenue recognition, collections  prioritization, and borrower payment allocation.
 | Amount of interest currently due on the loan as of the record_date. This includes accrued  interest that has become due for payment. Important for revenue recognition, collections  prioritization, and borrower payment allocation.
 | `[]` | `{}` |
    | `PRINCIPAL_DUE` | 6 | `NUMBER` | Amount of principal currently due on the loan as of the record_date. Represents the principal  portion of scheduled payments that are due for payment. Used for payment processing,  collections strategy, and cash flow analysis.
 | Amount of principal currently due on the loan as of the record_date. Represents the principal  portion of scheduled payments that are due for payment. Used for payment processing,  collections strategy, and cash flow analysis.
 | `[]` | `{}` |
    | `FEES_BALANCE` | 7 | `NUMBER` | Outstanding fees balance on the loan as of the record_date. Includes late fees, processing  fees, and other assessed charges. Important for fee revenue tracking, collections operations,  and total debt calculation.
 | Outstanding fees balance on the loan as of the record_date. Includes late fees, processing  fees, and other assessed charges. Important for fee revenue tracking, collections operations,  and total debt calculation.
 | `[]` | `{}` |
    | `PI_DUE` | 8 | `NUMBER` | Principal and interest due on the loan as of the record_date. Excludes fees and represents  the core payment obligation. Used for payment processing, loan servicing calculations,  and borrower communication.
 | Principal and interest due on the loan as of the record_date. Excludes fees and represents  the core payment obligation. Used for payment processing, loan servicing calculations,  and borrower communication.
 | `[]` | `{}` |
    | `PAYOFF_FEES` | 9 | `NUMBER` | Additional fees that would be charged if the loan were paid off as of the record_date.  These may include prepayment penalties or administrative fees. Important for payoff  quote calculations and revenue recognition.
 | Additional fees that would be charged if the loan were paid off as of the record_date.  These may include prepayment penalties or administrative fees. Important for payoff  quote calculations and revenue recognition.
 | `[]` | `{}` |
    | `NEXT_PAYMENT_DATE` | 10 | `DATE` | Date when the next scheduled payment is due for the loan. Used for payment reminders,  collections scheduling, autopay processing, and borrower communication about upcoming  payment obligations.
 | Date when the next scheduled payment is due for the loan. Used for payment reminders,  collections scheduling, autopay processing, and borrower communication about upcoming  payment obligations.
 | `[]` | `{}` |
    | `NEXT_PAYMENT_AMOUNT` | 11 | `NUMBER` | Dollar amount of the next scheduled payment for the loan. Includes principal, interest,  and any scheduled fees. Essential for autopay processing, payment notifications, and  cash flow forecasting.
 | Dollar amount of the next scheduled payment for the loan. Includes principal, interest,  and any scheduled fees. Essential for autopay processing, payment notifications, and  cash flow forecasting.
 | `[]` | `{}` |
    | `LAST_PAYMENT_DATE` | 12 | `DATE` | Date when the most recent payment was received for the loan. Used for payment tracking,  delinquency calculations, collections strategy, and borrower relationship management.
 | Date when the most recent payment was received for the loan. Used for payment tracking,  delinquency calculations, collections strategy, and borrower relationship management.
 | `[]` | `{}` |
    | `PRINCIPAL_BALANCE` | 13 | `NUMBER` | Outstanding principal balance of the loan as of the record_date. Represents the remaining  loan amount owed by the borrower, excluding interest and fees. Critical for loss calculations,  loan-to-value analysis, and principal paydown tracking.
 | Outstanding principal balance of the loan as of the record_date. Represents the remaining  loan amount owed by the borrower, excluding interest and fees. Critical for loss calculations,  loan-to-value analysis, and principal paydown tracking.
 | `[]` | `{}` |
    | `AMOUNT_PAST_DUE_THIRTY` | 14 | `NUMBER` | Dollar amount of payments that are past due as of the record_date. Represents the total  overdue payment amount and is critical for collections prioritization, cash flow management,  and risk assessment.
 | Dollar amount of payments that are past due as of the record_date. Represents the total  overdue payment amount and is critical for collections prioritization, cash flow management,  and risk assessment.
 | `[]` | `{}` |
    | `DPD` | 15 | `NUMBER` | Days Past Due - number of days the loan payment is overdue as of the record_date. This is  the primary delinquency metric used for risk assessment, collections strategy, regulatory  reporting, and charge-off determination. Values of 0 indicate current loans.
 | Days Past Due - number of days the loan payment is overdue as of the record_date. This is  the primary delinquency metric used for risk assessment, collections strategy, regulatory  reporting, and charge-off determination. Values of 0 indicate current loans.
 | `[]` | `{}` |
    | `DATE_LAST_CURRENT` | 16 | `DATE` | Date when the loan was last in current status (0 days past due). Used for calculating  delinquency duration, collections strategy timing, and understanding payment behavior  patterns for risk assessment.
 | Date when the loan was last in current status (0 days past due). Used for calculating  delinquency duration, collections strategy timing, and understanding payment behavior  patterns for risk assessment.
 | `[]` | `{}` |
    | `FIRST_DELINQUENCY_DATE` | 17 | `DATE` | Date when the loan first became 30+ days past due (DQ30) in its lifecycle. This field tracks the first occurrence of serious delinquency (30+ DPD), not minor delinquency (1+ DPD). Used for collections strategy development, risk assessment, and understanding serious payment issues from origination.
 | Date when the loan first became 30+ days past due (DQ30) in its lifecycle. This field tracks the first occurrence of serious delinquency (30+ DPD), not minor delinquency (1+ DPD). Used for collections strategy development, risk assessment, and understanding serious payment issues from origination.
 | `[]` | `{}` |
    | `UNIQUE_DELINQUENCIES` | 18 | `NUMBER` | Count of distinct serious delinquency events (30+ DPD) for the loan over its lifecycle. Tracks how many separate times the loan has reached 30+ days past due, indicating borrower payment stability and serious default risk profile.
 | Count of distinct serious delinquency events (30+ DPD) for the loan over its lifecycle. Tracks how many separate times the loan has reached 30+ days past due, indicating borrower payment stability and serious default risk profile.
 | `[]` | `{}` |
    | `DELINQUENT_PERC` | 19 | `NUMBER` | Percentage of the loan's lifecycle spent in serious delinquency (30+ DPD). Calculated as days at 30+ DPD divided by total days since origination. Provides a risk assessment metric for borrower payment reliability and serious default frequency.
 | Percentage of the loan's lifecycle spent in serious delinquency (30+ DPD). Calculated as days at 30+ DPD divided by total days since origination. Provides a risk assessment metric for borrower payment reliability and serious default frequency.
 | `[]` | `{}` |
    | `NUMBER_OF_DAYS_DELINQUENT` | 20 | `NUMBER` | Total cumulative number of days the loan has been 30+ days past due (DQ30) throughout its lifecycle. This counts only days when the loan was seriously delinquent (30+ DPD), not minor delinquency days (1-29 DPD). Used for collections cost analysis, serious default risk assessment, and charge-off likelihood evaluation.
 | Total cumulative number of days the loan has been 30+ days past due (DQ30) throughout its lifecycle. This counts only days when the loan was seriously delinquent (30+ DPD), not minor delinquency days (1-29 DPD). Used for collections cost analysis, serious default risk assessment, and charge-off likelihood evaluation.
 | `[]` | `{}` |
    | `PAYOFF` | 21 | `NUMBER` | Total amount required to completely pay off the loan as of the record_date. Includes  all outstanding principal, accrued interest, fees, and any payoff-specific charges.  Critical for loan closure processing and borrower payoff quotes.
 | Total amount required to completely pay off the loan as of the record_date. Includes  all outstanding principal, accrued interest, fees, and any payoff-specific charges.  Critical for loan closure processing and borrower payoff quotes.
 | `[]` | `{}` |
    | `CHARGE_OFF` | 22 | `NUMBER` | Net charge-off amount for the loan as of the record_date. Represents the total amount  charged off minus any recoveries. Positive values indicate net loss, while negative  values may indicate recoveries exceeding original charge-off. Critical for loss reporting  and recovery tracking.
 | Net charge-off amount for the loan as of the record_date. Represents the total amount  charged off minus any recoveries. Positive values indicate net loss, while negative  values may indicate recoveries exceeding original charge-off. Critical for loss reporting  and recovery tracking.
 | `[]` | `{}` |
    | `PERDIEM` | 23 | `NUMBER` | Daily interest accrual amount for the loan as of the record_date. Represents the dollar  amount of interest that accumulates each day on the outstanding balance. Critical for  revenue recognition, interest calculations, and financial reporting.
 | Daily interest accrual amount for the loan as of the record_date. Represents the dollar  amount of interest that accumulates each day on the outstanding balance. Critical for  revenue recognition, interest calculations, and financial reporting.
 | `[]` | `{}` |
    | `ACCRUED_INTEREST` | 24 | `NUMBER` | Amount of interest that has accrued on the loan as of the record_date but may not yet  be due for payment. Used for revenue recognition, financial reporting, and interest  income calculations.
 | Amount of interest that has accrued on the loan as of the record_date but may not yet  be due for payment. Used for revenue recognition, financial reporting, and interest  income calculations.
 | `[]` | `{}` |
    | `START_PERIOD` | 25 | `DATE` | Start date of the billing or accounting period associated with the record_date. Used  for period-based calculations, billing cycle management, and financial reporting that  requires period-specific loan performance data.
 | Start date of the billing or accounting period associated with the record_date. Used  for period-based calculations, billing cycle management, and financial reporting that  requires period-specific loan performance data.
 | `[]` | `{}` |
    | `END_PERIOD` | 26 | `DATE` | End date of the billing or accounting period associated with the record_date. Used  alongside start_period for period-based analysis, billing calculations, and accounting  period reconciliation.
 | End date of the billing or accounting period associated with the record_date. Used  alongside start_period for period-based analysis, billing calculations, and accounting  period reconciliation.
 | `[]` | `{}` |
    | `LOAN_STATUS` | 27 | `TEXT` | Current status of the loan from the LoanPro system as of the record_date. Common values  include 'LATE', 'OPEN', 'Closed', 'Bankruptcy', 'Charged Off'. This is the primary  status field for loan categorization, workflow management, and reporting.
 | Current status of the loan from the LoanPro system as of the record_date. Common values  include 'LATE', 'OPEN', 'Closed', 'Bankruptcy', 'Charged Off'. This is the primary  status field for loan categorization, workflow management, and reporting.
 | `[]` | `{}` |
    | `LOAN_SUBSTATUS` | 28 | `TEXT` | Current sub-status providing additional detail about the loan's operational state.  Examples include 'Settled', 'Deceased', 'Fraud', 'Filed'. Provides granular context  for loan management, collections strategy, and specialized handling requirements.
 | Current sub-status providing additional detail about the loan's operational state.  Examples include 'Settled', 'Deceased', 'Fraud', 'Filed'. Provides granular context  for loan management, collections strategy, and specialized handling requirements.
 | `[]` | `{}` |
    | `RECENCY` | 29 | `NUMBER` | Measure indicating how recent this record is relative to other records for the same loan.  Used for identifying the most current loan information and ensuring proper sequencing  in time-series analysis and reporting.
 | Measure indicating how recent this record is relative to other records for the same loan.  Used for identifying the most current loan information and ensuring proper sequencing  in time-series analysis and reporting.
 | `[]` | `{}` |
    | `DELINQUENCY_BUCKET` | 30 | `NUMBER` | Alternative delinquency bucket classification from LoanPro system. Provides additional  delinquency categorization that may differ from the calculated dq_bucket. Used for  system reconciliation and alternative risk assessment frameworks.
 | Alternative delinquency bucket classification from LoanPro system. Provides additional  delinquency categorization that may differ from the calculated dq_bucket. Used for  system reconciliation and alternative risk assessment frameworks.
 | `[]` | `{}` |
    | `LOANPRO_LOAN_ID` | 31 | `NUMBER` | Foreign key reference to the LoanPro system loan identifier. This is the primary identifier  used within LoanPro for loan servicing, payment processing, and system operations. Essential  for linking to LoanPro transaction data and servicing events.
 | Foreign key reference to the LoanPro system loan identifier. This is the primary identifier  used within LoanPro for loan servicing, payment processing, and system operations. Essential  for linking to LoanPro transaction data and servicing events.
 | `[]` | `{}` |
    | `CONTRACT_ID` | 32 | `TEXT` | Foreign key reference to the loan contract identifier (display ID). This human-readable  identifier is used in customer communications and represents the legal contract between  Cherry and the borrower. Serves as the bridge between Cherry and LoanPro systems.
 | Foreign key reference to the loan contract identifier (display ID). This human-readable  identifier is used in customer communications and represents the legal contract between  Cherry and the borrower. Serves as the bridge between Cherry and LoanPro systems.
 | `[]` | `{}` |
    | `DQ_BUCKET` | 33 | `NUMBER` | Delinquency bucket categorizing the loan based on days past due. Calculated as: 0 (current),  1 (1-29 DPD), 2 (30-59 DPD), 3 (60-89 DPD), 4 (90-120 DPD), 0 (>120 DPD). Used for risk  reporting, collections workflow management, and portfolio segmentation.
 | Delinquency bucket categorizing the loan based on days past due. Calculated as: 0 (current),  1 (1-29 DPD), 2 (30-59 DPD), 3 (60-89 DPD), 4 (90-120 DPD), 0 (>120 DPD). Used for risk  reporting, collections workflow management, and portfolio segmentation.
 | `[]` | `{}` |
    | `LOAN_ID` | 34 | `NUMBER` | Foreign key reference to Cherry's internal loan identifier. This is the primary loan ID  used throughout Cherry's business intelligence and analytics ecosystem, enabling joins  with merchant data, application information, and business reporting models.
 | Foreign key reference to Cherry's internal loan identifier. This is the primary loan ID  used throughout Cherry's business intelligence and analytics ecosystem, enabling joins  with merchant data, application information, and business reporting models.
 | `[]` | `{}` |
    | `BORROWER_ID` | 35 | `NUMBER` | Foreign key reference to Cherry's borrower identifier. Links the loan to borrower-specific  information including contact details, credit history, and account management data across  Cherry's systems.
 | Foreign key reference to Cherry's borrower identifier. Links the loan to borrower-specific  information including contact details, credit history, and account management data across  Cherry's systems.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.is_incremental`
    *   `model.cherry_data_model.stg_cherry_loan_ids`
    *   `model.cherry_data_model.stg_daily_loan`

---
