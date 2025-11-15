## Model: `daily_active_loans_count`

`daily_active_loans_count`

*   **Unique ID:** `model.cherry_data_model.daily_active_loans_count`
*   **FQN:** `prod.risk_marts.daily_active_loans_count`
*   **Description:** **Daily Active Loan Portfolio Tracking**
This incremental model provides a daily time series of active loan counts across Cherry's  portfolio, serving as a key metric for portfolio monitoring, regulatory reporting, and  business intelligence. The model implements sophisticated business logic to accurately  define "active" loans by excluding settled loans entirely while applying a 180-day grace  period for closed loans to account for potential reactivations or status changes.
**Active Loan Definition:** - **Excluded Entirely**: Loans with 'Settled' status (considered permanently inactive) - **Conditional Exclusion**: Loans with 'Closed' status are only excluded if they have been 
  closed for more than 180 days, allowing for potential reactivations within the grace period
- **Included**: All other loan statuses including 'LATE', 'OPEN', 'Bankruptcy', etc.
**Key Business Logic:** - Uses complete date spine from `calendar_table_xf` to ensure no missing dates - Tracks first closure date per loan to implement 180-day business rule - Incremental refresh strategy updates last 60 days to handle historical corrections - Normalizes counts per 100,000 for comparative analysis across time periods
**Primary Use Cases:** - Daily portfolio monitoring and trend analysis - Regulatory reporting requiring active loan counts - Business intelligence dashboards and executive reporting - Risk management and portfolio health assessment - Historical trend analysis and forecasting
**Data Sources:** - `calendar_table_xf`: Complete date spine with business calendar context - `stg_daily_loan`: Daily loan status snapshots from LoanPro system
**Refresh Strategy:** Incremental model refreshing the most recent 60 days to handle  late-arriving updates and status corrections
**Grain:** One record per calendar date with aggregated loan counts

*   **Tags:** `['risk']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `RECORD_DATE` | 1 | `DATE` | Calendar date for which the active loan count is calculated. Serves as the primary  key and time dimension for this daily time series. The date range spans from the  earliest available loan data through the current date, providing a complete  historical view of portfolio size over time.
 | Calendar date for which the active loan count is calculated. Serves as the primary  key and time dimension for this daily time series. The date range spans from the  earliest available loan data through the current date, providing a complete  historical view of portfolio size over time.
 | `[]` | `{}` |
    | `ACTIVE_LOAN_COUNT` | 2 | `NUMBER` | Total count of distinct active loans on the given date. This represents the core  portfolio size metric, calculated by counting unique loanpro_loan_id values that  meet the active loan criteria. Active loans include all loan statuses except  'Settled' (permanently excluded) and 'Closed' loans that have been closed for  more than 180 days. This metric is essential for portfolio tracking, regulatory  reporting, and business performance monitoring.
 | Total count of distinct active loans on the given date. This represents the core  portfolio size metric, calculated by counting unique loanpro_loan_id values that  meet the active loan criteria. Active loans include all loan statuses except  'Settled' (permanently excluded) and 'Closed' loans that have been closed for  more than 180 days. This metric is essential for portfolio tracking, regulatory  reporting, and business performance monitoring.
 | `[]` | `{}` |
    | `LOANS_PER_100K` | 3 | `NUMBER` | Normalized active loan count per 100,000, calculated as active_loan_count divided  by 100,000. This standardized metric enables comparative analysis across different  time periods and facilitates trend analysis by removing the impact of absolute  scale differences. The normalization is particularly useful for executive reporting,  industry benchmarking, and statistical analysis where relative portfolio size  changes are more meaningful than absolute counts. | Normalized active loan count per 100,000, calculated as active_loan_count divided  by 100,000. This standardized metric enables comparative analysis across different  time periods and facilitates trend analysis by removing the impact of absolute  scale differences. The normalization is particularly useful for executive reporting,  industry benchmarking, and statistical analysis where relative portfolio size  changes are more meaningful than absolute counts. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.is_incremental`
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.stg_daily_loan`

---
