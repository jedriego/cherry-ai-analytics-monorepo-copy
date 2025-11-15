## Model: `revenue_run_rate_historical_xf_archive`

`revenue_run_rate_historical_xf_archive`

*   **Unique ID:** `model.cherry_data_model.revenue_run_rate_historical_xf_archive`
*   **FQN:** `prod.archive.revenue_run_rate_historical_xf_archive`
*   **Description:** Historical daily time series of key revenue and business metrics reconstructed from dbt snapshots. This model creates a comprehensive daily view of business performance from September 30, 2024 to current date by using snapshot tables to reconstruct historical values as they existed on each specific date. The model combines loan revenue metrics, practice counts, and recovery/charge-off data to provide a complete picture of daily business performance over time. This is essential for historical revenue analysis, trend identification, and understanding how key metrics have evolved, particularly useful for revenue run rate calculations and historical business intelligence reporting.

*   **Tags:** `['archive']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CALENDAR_DATE` | 1 | `DATE` | Daily date dimension from September 30, 2024 to current date. Serves as the primary key for this time series table. This date represents the point-in-time for which all other metrics are calculated, showing the values as they existed on that specific date based on snapshot data.
 | Daily date dimension from September 30, 2024 to current date. Serves as the primary key for this time series table. This date represents the point-in-time for which all other metrics are calculated, showing the values as they existed on that specific date based on snapshot data.
 | `[]` | `{}` |
    | `BOOKED_REVENUE` | 2 | `FLOAT` | Total revenue amount as it existed on the calendar date. Reconstructed from the loan_info_xf_snapshot table by summing all revenue values for loans that were active/valid on the specific date. This represents the cumulative booked revenue across all loans as of each historical date, allowing for analysis of revenue growth over time.
 | Total revenue amount as it existed on the calendar date. Reconstructed from the loan_info_xf_snapshot table by summing all revenue values for loans that were active/valid on the specific date. This represents the cumulative booked revenue across all loans as of each historical date, allowing for analysis of revenue growth over time.
 | `[]` | `{}` |
    | `LOAN_AMOUNT` | 3 | `FLOAT` | Total net loan amount as it existed on the calendar date. Reconstructed from the loan_info_xf_snapshot table by summing all net_loan_amount values for loans that were active/valid on the specific date. This represents the cumulative net loan principal across all loans as of each historical date.
 | Total net loan amount as it existed on the calendar date. Reconstructed from the loan_info_xf_snapshot table by summing all net_loan_amount values for loans that were active/valid on the specific date. This represents the cumulative net loan principal across all loans as of each historical date.
 | `[]` | `{}` |
    | `TRANSACTION_VOLUME` | 4 | `FLOAT` | Total gross transaction volume as it existed on the calendar date. Reconstructed from the loan_info_xf_snapshot table by summing all gross_amount values for loans that were active/valid on the specific date. This represents the cumulative gross transaction volume across all loans as of each historical date.
 | Total gross transaction volume as it existed on the calendar date. Reconstructed from the loan_info_xf_snapshot table by summing all gross_amount values for loans that were active/valid on the specific date. This represents the cumulative gross transaction volume across all loans as of each historical date.
 | `[]` | `{}` |
    | `PRACTICE_COUNT` | 5 | `NUMBER` | Total count of distinct practices (by sf_account_id) as it existed on the calendar date. Reconstructed from the practice_info_xf_snapshot table by counting unique Salesforce account IDs that were active/valid on the specific date. This represents the cumulative number of practices in the system as of each historical date, useful for tracking practice growth over time.
 | Total count of distinct practices (by sf_account_id) as it existed on the calendar date. Reconstructed from the practice_info_xf_snapshot table by counting unique Salesforce account IDs that were active/valid on the specific date. This represents the cumulative number of practices in the system as of each historical date, useful for tracking practice growth over time.
 | `[]` | `{}` |
    | `RECOVERY_AMOUNT` | 6 | `NUMBER` | Total recovery amount for the calendar date. Calculated from the monthly_period_xf_snapshot table by summing recoveries for loan periods that were active on the specific date. This represents the amount recovered from previously charged-off or delinquent loans on each date, important for understanding collection performance.
 | Total recovery amount for the calendar date. Calculated from the monthly_period_xf_snapshot table by summing recoveries for loan periods that were active on the specific date. This represents the amount recovered from previously charged-off or delinquent loans on each date, important for understanding collection performance.
 | `[]` | `{}` |
    | `CHARGE_OFF_AMOUNT` | 7 | `NUMBER` | Total charge-off amount (GACO - Generally Accepted Accounting Principles Charge-Off) for the calendar date. Calculated from the monthly_period_xf_snapshot table by summing charge-offs for loan periods that were active on the specific date. This represents the amount of loans written off as uncollectable on each date, critical for understanding credit risk and loss patterns. | Total charge-off amount (GACO - Generally Accepted Accounting Principles Charge-Off) for the calendar date. Calculated from the monthly_period_xf_snapshot table by summing charge-offs for loan periods that were active on the specific date. This represents the amount of loans written off as uncollectable on each date, critical for understanding credit risk and loss patterns. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.calendar_table_xf`
    *   `snapshot.cherry_data_model.loan_info_xf_snapshot`
    *   `snapshot.cherry_data_model.monthly_period_xf_snapshot`
    *   `snapshot.cherry_data_model.practice_info_xf_snapshot`

---
