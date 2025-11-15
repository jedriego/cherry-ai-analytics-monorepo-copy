## Model: `loan_statuses_today_xf`

`loan_statuses_today_xf`

*   **Unique ID:** `model.cherry_data_model.loan_statuses_today_xf`
*   **FQN:** `prod.risk_marts.loan_statuses_today_xf`
*   **Description:** **Current Loan Status Snapshot**
This model provides the most recent loan status information for each loan in Cherry's portfolio  by selecting the latest daily record from LoanPro's status archive and enriching it with Cherry's  loan and borrower identifiers. It serves as the primary source for current loan status analysis,  real-time portfolio monitoring, and operational reporting that requires the most up-to-date loan  information.
**Key Business Logic:** - **Latest Record Selection**: For each LoanPro loan ID, identifies the most recent record date 
  from the daily loan status archive to ensure current information
- **Cherry Integration**: Joins LoanPro data with Cherry's loan and borrower ID system for 
  business intelligence and operational workflows
- **Current State Focus**: Unlike historical daily models, this provides only the current 
  snapshot for faster query performance and real-time analytics

**Data Sources:** - **stg_daily_loan**: LoanPro's comprehensive daily loan status archive with payment, balance, 
  and delinquency information
- **int_funded_information_pt**: Cherry's loan identifier mapping for business system integration
**Primary Use Cases:** - Current portfolio status reporting and monitoring - Real-time delinquency and collections management - Customer service loan status inquiries - Risk management and regulatory reporting - Operational dashboards requiring current loan state
**Grain:** One record per loan (most recent status only)

*   **Tags:** `['risk', 'collections_hourly']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `UNIQUE_KEY` | 1 | `TEXT` | Unique identifier combining LoanPro loan ID and record date, ensuring each loan-date  combination is distinct. Used for data integrity and deduplication.
 | Unique identifier combining LoanPro loan ID and record date, ensuring each loan-date  combination is distinct. Used for data integrity and deduplication.
 | `[]` | `{}` |
    | `RECORD_DATE` | 2 | `DATE` | The date when this loan status snapshot was recorded in LoanPro's system. For this  model, represents the most recent available date for each loan.
 | The date when this loan status snapshot was recorded in LoanPro's system. For this  model, represents the most recent available date for each loan.
 | `[]` | `{}` |
    | `WEEK_MONDAY` | 3 | `DATE` | Week starting date (Monday) for the record date, enabling weekly aggregations and  time-based analysis of loan performance trends.
 | Week starting date (Monday) for the record date, enabling weekly aggregations and  time-based analysis of loan performance trends.
 | `[]` | `{}` |
    | `AMOUNT_DUE` | 4 | `NUMBER` | Total amount currently due on the loan, including principal, interest, and fees.  Critical metric for collections and customer payment tracking.
 | Total amount currently due on the loan, including principal, interest, and fees.  Critical metric for collections and customer payment tracking.
 | `[]` | `{}` |
    | `INTEREST_DUE` | 5 | `NUMBER` | Outstanding interest amount due on the loan. Combines original LoanPro data with  reverse archive adjustments for accuracy.
 | Outstanding interest amount due on the loan. Combines original LoanPro data with  reverse archive adjustments for accuracy.
 | `[]` | `{}` |
    | `PRINCIPAL_DUE` | 6 | `NUMBER` | Outstanding principal amount due on the loan. Uses reverse archive data when available  to ensure most accurate balance information.
 | Outstanding principal amount due on the loan. Uses reverse archive data when available  to ensure most accurate balance information.
 | `[]` | `{}` |
    | `FEES_BALANCE` | 7 | `NUMBER` | Current balance of fees owed on the loan, including late fees and other assessed  charges. Important for collections and payment application logic.
 | Current balance of fees owed on the loan, including late fees and other assessed  charges. Important for collections and payment application logic.
 | `[]` | `{}` |
    | `PI_DUE` | 8 | `NUMBER` | Principal and interest due amount, representing the core loan payment obligations  excluding fees and other charges.
 | Principal and interest due amount, representing the core loan payment obligations  excluding fees and other charges.
 | `[]` | `{}` |
    | `PAYOFF_FEES` | 9 | `NUMBER` | Fees that would be assessed if the loan were paid off in full, used for payoff  quote calculations and customer service inquiries.
 | Fees that would be assessed if the loan were paid off in full, used for payoff  quote calculations and customer service inquiries.
 | `[]` | `{}` |
    | `NEXT_PAYMENT_DATE` | 10 | `DATE` | The date when the next scheduled payment is due, critical for payment processing,  customer communications, and delinquency tracking.
 | The date when the next scheduled payment is due, critical for payment processing,  customer communications, and delinquency tracking.
 | `[]` | `{}` |
    | `NEXT_PAYMENT_AMOUNT` | 11 | `NUMBER` | The amount of the next scheduled payment, used for customer notifications and  autopay processing.
 | The amount of the next scheduled payment, used for customer notifications and  autopay processing.
 | `[]` | `{}` |
    | `LAST_PAYMENT_DATE` | 12 | `DATE` | Date when the most recent payment was received and processed, used for payment  history analysis and delinquency calculations.
 | Date when the most recent payment was received and processed, used for payment  history analysis and delinquency calculations.
 | `[]` | `{}` |
    | `PRINCIPAL_BALANCE` | 13 | `NUMBER` | Current outstanding principal balance on the loan. Uses reverse archive data when  available for the most accurate balance information.
 | Current outstanding principal balance on the loan. Uses reverse archive data when  available for the most accurate balance information.
 | `[]` | `{}` |
    | `AMOUNT_PAST_DUE_THIRTY` | 14 | `NUMBER` | Total amount that is 30+ days past due, critical metric for delinquency reporting  and collections prioritization.
 | Total amount that is 30+ days past due, critical metric for delinquency reporting  and collections prioritization.
 | `[]` | `{}` |
    | `DPD` | 15 | `NUMBER` | Days Past Due - number of days since the loan became delinquent. Key metric for  collections workflow, risk assessment, and regulatory reporting.
 | Days Past Due - number of days since the loan became delinquent. Key metric for  collections workflow, risk assessment, and regulatory reporting.
 | `[]` | `{}` |
    | `DATE_LAST_CURRENT` | 16 | `DATE` | Date when the loan was last current (not delinquent), used for delinquency duration  analysis and loss forecasting.
 | Date when the loan was last current (not delinquent), used for delinquency duration  analysis and loss forecasting.
 | `[]` | `{}` |
    | `FIRST_DELINQUENCY_DATE` | 17 | `DATE` | Date when the loan first became 30+ days past due (DQ30). This tracks serious delinquency (30+ DPD), not minor delinquency (1-29 DPD). Used for vintage analysis and collections intervention strategies.
 | Date when the loan first became 30+ days past due (DQ30). This tracks serious delinquency (30+ DPD), not minor delinquency (1-29 DPD). Used for vintage analysis and collections intervention strategies.
 | `[]` | `{}` |
    | `UNIQUE_DELINQUENCIES` | 18 | `NUMBER` | Count of distinct serious delinquency episodes (30+ DPD) for this loan, indicating payment pattern stability and serious default frequency.
 | Count of distinct serious delinquency episodes (30+ DPD) for this loan, indicating payment pattern stability and serious default frequency.
 | `[]` | `{}` |
    | `DELINQUENT_PERC` | 19 | `NUMBER` | Percentage of the loan's life spent in serious delinquency (30+ DPD), used for borrower behavior analysis and serious default risk assessment.
 | Percentage of the loan's life spent in serious delinquency (30+ DPD), used for borrower behavior analysis and serious default risk assessment.
 | `[]` | `{}` |
    | `NUMBER_OF_DAYS_DELINQUENT` | 20 | `NUMBER` | Total cumulative days the loan has been 30+ days past due (DQ30) throughout its lifetime. Counts only serious delinquency days (30+ DPD), not minor delinquency (1-29 DPD). Used for performance tracking and loss modeling.
 | Total cumulative days the loan has been 30+ days past due (DQ30) throughout its lifetime. Counts only serious delinquency days (30+ DPD), not minor delinquency (1-29 DPD). Used for performance tracking and loss modeling.
 | `[]` | `{}` |
    | `PAYOFF` | 21 | `NUMBER` | Current payoff amount if the loan were to be paid in full today, including all  outstanding balances and applicable fees.
 | Current payoff amount if the loan were to be paid in full today, including all  outstanding balances and applicable fees.
 | `[]` | `{}` |
    | `CHARGE_OFF` | 22 | `NUMBER` | Net charge-off amount applied to the loan, indicating losses recognized for accounting  and regulatory purposes. Uses reverse archive adjustments when available.
 | Net charge-off amount applied to the loan, indicating losses recognized for accounting  and regulatory purposes. Uses reverse archive adjustments when available.
 | `[]` | `{}` |
    | `PERDIEM` | 23 | `NUMBER` | Daily interest accrual amount based on the current principal balance and interest rate,  used for interest calculations and payment application.
 | Daily interest accrual amount based on the current principal balance and interest rate,  used for interest calculations and payment application.
 | `[]` | `{}` |
    | `ACCRUED_INTEREST` | 24 | `NUMBER` | Interest that has accrued since the last payment or billing cycle, rounded to 2 decimal  places for financial accuracy.
 | Interest that has accrued since the last payment or billing cycle, rounded to 2 decimal  places for financial accuracy.
 | `[]` | `{}` |
    | `START_PERIOD` | 25 | `DATE` | Beginning date of the current billing or accounting period for this loan status record.
 | Beginning date of the current billing or accounting period for this loan status record.
 | `[]` | `{}` |
    | `END_PERIOD` | 26 | `DATE` | Ending date of the current billing or accounting period for this loan status record.
 | Ending date of the current billing or accounting period for this loan status record.
 | `[]` | `{}` |
    | `LOAN_STATUS` | 27 | `TEXT` | Current loan status from LoanPro (e.g., 'OPEN', 'LATE', 'CLOSED', 'CHARGED_OFF').  Primary field for loan lifecycle management and operational workflows.
 | Current loan status from LoanPro (e.g., 'OPEN', 'LATE', 'CLOSED', 'CHARGED_OFF').  Primary field for loan lifecycle management and operational workflows.
 | `[]` | `{}` |
    | `LOAN_SUBSTATUS` | 28 | `TEXT` | Detailed loan sub-status providing additional context for the main status (e.g.,  'LATE-30', 'LATE-60'). Used for granular workflow management and reporting.
 | Detailed loan sub-status providing additional context for the main status (e.g.,  'LATE-30', 'LATE-60'). Used for granular workflow management and reporting.
 | `[]` | `{}` |
    | `RECENCY` | 29 | `NUMBER` | Metric indicating how recently the loan data was updated or processed, used for data  freshness validation and processing monitoring.
 | Metric indicating how recently the loan data was updated or processed, used for data  freshness validation and processing monitoring.
 | `[]` | `{}` |
    | `DELINQUENCY_BUCKET` | 30 | `NUMBER` | Standardized delinquency category based on days past due, combining original and reverse  archive logic for consistent bucketing across systems.
 | Standardized delinquency category based on days past due, combining original and reverse  archive logic for consistent bucketing across systems.
 | `[]` | `{}` |
    | `LOANPRO_LOAN_ID` | 31 | `NUMBER` | LoanPro's internal loan identifier, used for joining with other LoanPro-sourced data  and maintaining data lineage.
 | LoanPro's internal loan identifier, used for joining with other LoanPro-sourced data  and maintaining data lineage.
 | `[]` | `{}` |
    | `CONTRACT_ID` | 32 | `TEXT` | Cherry's contract identifier that bridges LoanPro and Cherry systems, enabling  cross-system loan tracking and business process integration.
 | Cherry's contract identifier that bridges LoanPro and Cherry systems, enabling  cross-system loan tracking and business process integration.
 | `[]` | `{}` |
    | `DQ_BUCKET` | 33 | `NUMBER` | Calculated delinquency bucket (0-4) based on days past due ranges: 0=Current, 1=1-29 DPD,  2=30-59 DPD, 3=60-89 DPD, 4=90-120 DPD. Used for standardized risk reporting.
 | Calculated delinquency bucket (0-4) based on days past due ranges: 0=Current, 1=1-29 DPD,  2=30-59 DPD, 3=60-89 DPD, 4=90-120 DPD. Used for standardized risk reporting.
 | `[]` | `{}` |
    | `LOAN_ID` | 34 | `NUMBER` | Cherry's internal loan identifier from the funded information table, enabling integration  with Cherry's business systems and customer-facing applications.
 | Cherry's internal loan identifier from the funded information table, enabling integration  with Cherry's business systems and customer-facing applications.
 | `[]` | `{}` |
    | `BORROWER_ID` | 35 | `NUMBER` | Cherry's internal borrower identifier, linking loan status to customer records for  customer service, collections, and business intelligence applications. | Cherry's internal borrower identifier, linking loan status to customer records for  customer service, collections, and business intelligence applications. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.stg_daily_loan`

---
