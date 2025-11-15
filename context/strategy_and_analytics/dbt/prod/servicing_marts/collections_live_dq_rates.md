## Model: `collections_live_dq_rates`

`collections_live_dq_rates`

*   **Unique ID:** `model.cherry_data_model.collections_live_dq_rates`
*   **FQN:** `prod.servicing_marts.collections_live_dq_rates`
*   **Description:** **Real-Time Portfolio Delinquency Rate Analytics**
This model provides live, balance-weighted delinquency rates across standardized DPD (Days Past Due)  buckets for Cherry's active loan portfolio. It serves as a critical portfolio health monitoring tool  by calculating the percentage of active loan balances in each delinquency stage, enabling real-time  risk assessment and regulatory reporting. The model creates point-in-time snapshots that can be  tracked over time to monitor portfolio performance trends and early warning indicators.
**Key Business Logic:** - **Balance-Weighted Calculations**: Uses loan balances rather than loan counts to provide a more 
  accurate representation of portfolio risk exposure, as larger loans have greater financial impact
- **Active Portfolio Focus**: Only includes loans with 'OPEN' or 'LATE' status to focus on loans 
  requiring active management and exclude closed/settled accounts
- **Standardized DPD Buckets**: Groups delinquency into industry-standard ranges (1-15 DPD, 16-30 DPD, 
  30-59 DPD, 60-89 DPD, 90-119 DPD) for consistent reporting and benchmarking
- **Real-Time Snapshot**: Pulls current loan status data from the loan_plans table which is synced 
  daily or when loan actions occur (payments, fees, status changes)
- **Percentage Format**: Converts rates to percentage format with 2 decimal places for dashboard display
**Data Sources:** - **loan_plans**: Cherry's servicing database table containing current loan status, balances, and 
  delinquency information synced from LoanPro. Updated daily or when loan events occur.

**Primary Use Cases:** - Real-time portfolio health monitoring and executive dashboards - Regulatory reporting and compliance with delinquency rate requirements - Risk management and early warning system for portfolio deterioration - Performance benchmarking against industry standards and historical trends - Investor reporting and due diligence for funding facilities
**Grain:** One snapshot record per execution timestamp (typically daily)

*   **Tags:** `['servicing_and_collections']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `UNIQUE_KEY` | 1 | `NUMBER` | **Snapshot Unique Identifier**
Unique identifier for each snapshot record, calculated as the epoch timestamp (seconds since  1970-01-01) converted to Pacific Time. Ensures each snapshot execution creates a distinct  record for time series analysis and prevents duplicate records in snapshot tables.
 | **Snapshot Unique Identifier**
Unique identifier for each snapshot record, calculated as the epoch timestamp (seconds since  1970-01-01) converted to Pacific Time. Ensures each snapshot execution creates a distinct  record for time series analysis and prevents duplicate records in snapshot tables.
 | `[]` | `{}` |
    | `SNAPSHOT_DATE` | 2 | `DATE` | **Snapshot Date**
Date when the delinquency rate snapshot was taken, converted to Pacific Time for consistent  business reporting. Used as the primary date dimension for tracking delinquency rate trends  over time and daily portfolio monitoring.
 | **Snapshot Date**
Date when the delinquency rate snapshot was taken, converted to Pacific Time for consistent  business reporting. Used as the primary date dimension for tracking delinquency rate trends  over time and daily portfolio monitoring.
 | `[]` | `{}` |
    | `SNAPSHOT_TIMESTAMP_PT` | 3 | `TIMESTAMP_NTZ` | **Snapshot Timestamp (Pacific Time)**
Precise timestamp when the delinquency rate calculation was executed, converted to Pacific Time.  Provides granular timing information for intraday analysis and ensuring data freshness for  real-time monitoring applications.
 | **Snapshot Timestamp (Pacific Time)**
Precise timestamp when the delinquency rate calculation was executed, converted to Pacific Time.  Provides granular timing information for intraday analysis and ensuring data freshness for  real-time monitoring applications.
 | `[]` | `{}` |
    | `ONE_TO_THIRTY_DQ_RATE` | 4 | `TEXT` | **1-30 Days Past Due Rate**
Percentage of active loan balances that are 1-30 days past due, calculated as the sum of  balances with 'LATE_1' and 'LATE_15' sub-statuses divided by total active balances (OPEN + LATE).  Represents early-stage delinquency and is a key indicator of portfolio quality and borrower  payment behavior. Formatted as percentage with 2 decimal places.
 | **1-30 Days Past Due Rate**
Percentage of active loan balances that are 1-30 days past due, calculated as the sum of  balances with 'LATE_1' and 'LATE_15' sub-statuses divided by total active balances (OPEN + LATE).  Represents early-stage delinquency and is a key indicator of portfolio quality and borrower  payment behavior. Formatted as percentage with 2 decimal places.
 | `[]` | `{}` |
    | `ONE_TO_FIFTEEN_DQ_RATE` | 5 | `TEXT` | **1-15 Days Past Due Rate**
Percentage of active loan balances that are 1-15 days past due, calculated as the sum of  balances with 'LATE_1' sub-status divided by total active balances. Represents the earliest  stage of delinquency and provides insight into immediate payment timing issues. Used for  early intervention strategies and portfolio monitoring.
 | **1-15 Days Past Due Rate**
Percentage of active loan balances that are 1-15 days past due, calculated as the sum of  balances with 'LATE_1' sub-status divided by total active balances. Represents the earliest  stage of delinquency and provides insight into immediate payment timing issues. Used for  early intervention strategies and portfolio monitoring.
 | `[]` | `{}` |
    | `SIXTEEN_TO_THIRTY_DQ_RATE` | 6 | `TEXT` | **16-30 Days Past Due Rate**
Percentage of active loan balances that are 16-30 days past due, calculated as the sum of  balances with 'LATE_15' sub-status divided by total active balances. Represents borrowers  who have moved beyond the initial grace period and may require more intensive collections  efforts. Critical metric for collections strategy optimization.
 | **16-30 Days Past Due Rate**
Percentage of active loan balances that are 16-30 days past due, calculated as the sum of  balances with 'LATE_15' sub-status divided by total active balances. Represents borrowers  who have moved beyond the initial grace period and may require more intensive collections  efforts. Critical metric for collections strategy optimization.
 | `[]` | `{}` |
    | `THIRTY_TO_FIFTYNINE_DQ_RATE` | 7 | `TEXT` | **30-59 Days Past Due Rate**
Percentage of active loan balances that are 30-59 days past due, calculated as the sum of  balances with 'LATE_30' sub-status divided by total active balances. Represents borrowers  entering more serious delinquency requiring escalated collections efforts. Important metric  for regulatory reporting and loss provisioning calculations.
 | **30-59 Days Past Due Rate**
Percentage of active loan balances that are 30-59 days past due, calculated as the sum of  balances with 'LATE_30' sub-status divided by total active balances. Represents borrowers  entering more serious delinquency requiring escalated collections efforts. Important metric  for regulatory reporting and loss provisioning calculations.
 | `[]` | `{}` |
    | `SIXTY_TO_EIGHTYNINE_DQ_RATE` | 8 | `TEXT` | **60-89 Days Past Due Rate**
Percentage of active loan balances that are 60-89 days past due, calculated as the sum of  balances with 'LATE_60' sub-status divided by total active balances. Represents borrowers  in serious delinquency requiring intensive collections efforts and potential charge-off  preparation. Key metric for loss forecasting and risk management.
 | **60-89 Days Past Due Rate**
Percentage of active loan balances that are 60-89 days past due, calculated as the sum of  balances with 'LATE_60' sub-status divided by total active balances. Represents borrowers  in serious delinquency requiring intensive collections efforts and potential charge-off  preparation. Key metric for loss forecasting and risk management.
 | `[]` | `{}` |
    | `NINETY_TO_ONEHUNDRED_NINETEEN_DQ_RATE` | 9 | `TEXT` | **90-119 Days Past Due Rate**
Percentage of active loan balances that are 90-119 days past due, calculated as the sum of  balances with 'LATE_90' sub-status divided by total active balances. Represents borrowers  approaching typical charge-off thresholds (120 days) and requiring final collection efforts  before potential charge-off. Critical metric for imminent loss identification and charge-off  planning. | **90-119 Days Past Due Rate**
Percentage of active loan balances that are 90-119 days past due, calculated as the sum of  balances with 'LATE_90' sub-status divided by total active balances. Represents borrowers  approaching typical charge-off thresholds (120 days) and requiring final collection efforts  before potential charge-off. Critical metric for imminent loss identification and charge-off  planning. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `source.cherry_data_model.cherry_data.loan_plans`

---
