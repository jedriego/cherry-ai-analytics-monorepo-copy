## Model: `daily_loan_last_day_record_xf`

`daily_loan_last_day_record_xf`

*   **Unique ID:** `model.cherry_data_model.daily_loan_last_day_record_xf`
*   **FQN:** `prod.risk_marts.daily_loan_last_day_record_xf`
*   **Description:** **End-of-Month Loan Performance Snapshots**
This model provides loan performance data specifically for the last day of each month,  creating a monthly summary view of loan status and balances. These month-end snapshots  are essential for period-over-period analysis, regulatory reporting, and monthly performance  tracking across the loan portfolio.
**Key Business Logic:** - Filters daily_loan_xf to only include records where record_date is the last day of the month - Provides month-end loan status for consistent period reporting - Maintains full daily loan detail structure for month-end analysis
**Primary Use Cases:** - Monthly loan portfolio performance reporting - Period-over-period analysis and trending - Regulatory and compliance month-end reporting - Monthly risk assessment and portfolio review - Investor reporting with consistent month-end metrics
**Materialization:** View (for real-time month-end calculations)
**Grain:** One record per loan per month-end date

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
