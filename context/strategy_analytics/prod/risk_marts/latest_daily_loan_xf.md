## Model: `latest_daily_loan_xf`

`latest_daily_loan_xf`

*   **Unique ID:** `model.cherry_data_model.latest_daily_loan_xf`
*   **FQN:** `prod.risk_marts.latest_daily_loan_xf`
*   **Description:** **Recent Daily Loan Performance Data (December 2024 Onwards)**
This model provides the same comprehensive daily loan performance data as `daily_loan_xf` but  filtered to include only records from December 15, 2024, onwards. This focused dataset enables  faster queries and analysis for recent loan performance while maintaining the same rich data  structure and LoanPro-Cherry integration.
**Key Difference from daily_loan_xf:** - **Date Filtering**: Only includes loan records from 2024-12-15 forward - **Use Case**: Optimized for recent performance analysis and faster query execution - **Data Structure**: Identical column structure and business logic as daily_loan_xf
**Primary Use Cases:** - Recent loan performance analysis and trending - Current portfolio health monitoring   - Real-time risk management dashboards - Recent collections and servicing activities
**Grain:** One record per loan per calendar date (daily snapshots from December 15, 2024)

*   **Tags:** `['risk', 'performance_data', 'loans', 'daily_full_refresh', 'core_hourly']`
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
    *   `macro.dbt.is_incremental`
    *   `model.cherry_data_model.daily_loan_xf`

---
