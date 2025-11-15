## Model: `daily_loan_first_record_xf`

`daily_loan_first_record_xf`

*   **Unique ID:** `model.cherry_data_model.daily_loan_first_record_xf`
*   **FQN:** `prod.risk_marts.daily_loan_first_record_xf`
*   **Description:** **Initial Loan Record Snapshots**
This model captures the very first daily loan record for each loan, representing the initial  state when loans first appear in the LoanPro daily status archive. These records provide  baseline metrics for loan performance analysis, including the initial balance, status, and  payment information at the start of loan tracking.
**Key Business Logic:** - Identifies the minimum record_date for each loan_id in daily_loan_xf - Provides only the first snapshot per loan for baseline analysis - Maintains full loan detail structure from the initial recording
**Primary Use Cases:** - Loan origination analysis and initial state comparison - Baseline metrics for performance trending and cohort analysis - Initial loan health assessment for underwriting model validation - Historical loan inception tracking for vintage analysis
**Grain:** One record per loan (first recorded daily snapshot only)

*   **Tags:** `['risk']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `UNIQUE_KEY` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `RECORD_DATE` | 2 | `DATE` |  |  | `[]` | `{}` |
    | `WEEK_MONDAY` | 3 | `DATE` |  |  | `[]` | `{}` |
    | `AMOUNT_DUE` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `INTEREST_DUE` | 5 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRINCIPAL_DUE` | 6 | `NUMBER` |  |  | `[]` | `{}` |
    | `FEES_BALANCE` | 7 | `NUMBER` |  |  | `[]` | `{}` |
    | `PI_DUE` | 8 | `NUMBER` |  |  | `[]` | `{}` |
    | `PAYOFF_FEES` | 9 | `NUMBER` |  |  | `[]` | `{}` |
    | `NEXT_PAYMENT_DATE` | 10 | `DATE` |  |  | `[]` | `{}` |
    | `NEXT_PAYMENT_AMOUNT` | 11 | `NUMBER` |  |  | `[]` | `{}` |
    | `LAST_PAYMENT_DATE` | 12 | `DATE` |  |  | `[]` | `{}` |
    | `PRINCIPAL_BALANCE` | 13 | `NUMBER` |  |  | `[]` | `{}` |
    | `AMOUNT_PAST_DUE_THIRTY` | 14 | `NUMBER` |  |  | `[]` | `{}` |
    | `DPD` | 15 | `NUMBER` |  |  | `[]` | `{}` |
    | `DATE_LAST_CURRENT` | 16 | `DATE` |  |  | `[]` | `{}` |
    | `FIRST_DELINQUENCY_DATE` | 17 | `DATE` |  |  | `[]` | `{}` |
    | `UNIQUE_DELINQUENCIES` | 18 | `NUMBER` |  |  | `[]` | `{}` |
    | `DELINQUENT_PERC` | 19 | `NUMBER` |  |  | `[]` | `{}` |
    | `NUMBER_OF_DAYS_DELINQUENT` | 20 | `NUMBER` |  |  | `[]` | `{}` |
    | `PAYOFF` | 21 | `NUMBER` |  |  | `[]` | `{}` |
    | `CHARGE_OFF` | 22 | `NUMBER` |  |  | `[]` | `{}` |
    | `PERDIEM` | 23 | `NUMBER` |  |  | `[]` | `{}` |
    | `ACCRUED_INTEREST` | 24 | `NUMBER` |  |  | `[]` | `{}` |
    | `START_PERIOD` | 25 | `DATE` |  |  | `[]` | `{}` |
    | `END_PERIOD` | 26 | `DATE` |  |  | `[]` | `{}` |
    | `LOAN_STATUS` | 27 | `TEXT` |  |  | `[]` | `{}` |
    | `LOAN_SUBSTATUS` | 28 | `TEXT` |  |  | `[]` | `{}` |
    | `RECENCY` | 29 | `NUMBER` |  |  | `[]` | `{}` |
    | `DELINQUENCY_BUCKET` | 30 | `NUMBER` |  |  | `[]` | `{}` |
    | `LOANPRO_LOAN_ID` | 31 | `NUMBER` |  |  | `[]` | `{}` |
    | `CONTRACT_ID` | 32 | `TEXT` |  |  | `[]` | `{}` |
    | `DQ_BUCKET` | 33 | `NUMBER` |  |  | `[]` | `{}` |
    | `LOAN_ID` | 34 | `NUMBER` |  |  | `[]` | `{}` |
    | `BORROWER_ID` | 35 | `NUMBER` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.daily_loan_xf`

---
