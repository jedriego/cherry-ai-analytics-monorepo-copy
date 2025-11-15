## Model: `daily_aprs_xf`

`daily_aprs_xf`

*   **Unique ID:** `model.cherry_data_model.daily_aprs_xf`
*   **FQN:** `prod.risk_marts.daily_aprs_xf`
*   **Description:** **Daily APR Point-in-Time History**
This model provides a comprehensive daily time series of Annual Percentage Rate (APR) values  for each loan in Cherry's portfolio, enabling point-in-time analysis of interest rate changes  and their impact on loan performance. The model reconstructs the historical APR for every loan  on every calendar date from funding through the current date, accounting for all APR modifications  that occurred during the loan's lifecycle.
**Key Business Logic:** - **Point-in-Time Reconstruction**: For each loan and date combination, determines what the APR 
  was on that specific date by finding the most recent APR change that occurred on or before that date
- **Complete Date Coverage**: Uses calendar spine to ensure no gaps in the time series, providing 
  daily APR values even when no changes occurred
- **Funding Date Boundary**: Only includes dates on or after the loan's funding date, ensuring 
  APR tracking begins when the loan becomes active
- **Change Event Tracking**: Captures APR modifications from LoanPro system notes that record 
  both old and new values when rates are adjusted

**Primary Use Cases:** - Regulatory reporting requiring historical APR documentation - Risk analysis correlating APR changes with loan performance - Revenue impact analysis of rate modifications - Compliance auditing for rate change documentation - Portfolio analytics examining rate sensitivity and trends - Capital markets reporting for investor transparency
**Data Sources:** - `stg_loanpro_apr_changes`: APR modification events parsed from LoanPro system notes - `calendar_table_xf`: Complete date spine for time series construction   - `int_funded_information_pt`: Loan funding dates and Cherry-LoanPro ID mapping
**Deduplication Logic:** Uses QUALIFY with ROW_NUMBER to ensure only the most recent APR  change is applied for each loan on each date when multiple changes occur on the same day
**Grain:** One record per loan per calendar date, from funding date through current date

*   **Tags:** `['risk', 'loans', 'daily_full_refresh']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `FULL_DATE` | 1 | `DATE` | Calendar date for which the APR value is recorded. Serves as the primary time dimension  for this daily time series. The date range spans from each loan's funding date through  the current date, providing complete historical coverage of APR values over the loan's  active lifecycle. This enables point-in-time analysis of what the APR was on any given  date for regulatory, risk, and performance reporting purposes.
 | Calendar date for which the APR value is recorded. Serves as the primary time dimension  for this daily time series. The date range spans from each loan's funding date through  the current date, providing complete historical coverage of APR values over the loan's  active lifecycle. This enables point-in-time analysis of what the APR was on any given  date for regulatory, risk, and performance reporting purposes.
 | `[]` | `{}` |
    | `LOANPRO_LOAN_ID` | 2 | `NUMBER` | Foreign key reference to the LoanPro system loan identifier. This is the primary identifier  used within the LoanPro servicing system and serves as the link to loan servicing data,  payment history, and system notes where APR changes are recorded. Essential for joining  with other LoanPro-sourced data and tracking system-level events.
 | Foreign key reference to the LoanPro system loan identifier. This is the primary identifier  used within the LoanPro servicing system and serves as the link to loan servicing data,  payment history, and system notes where APR changes are recorded. Essential for joining  with other LoanPro-sourced data and tracking system-level events.
 | `[]` | `{}` |
    | `LOAN_ID` | 3 | `NUMBER` | Foreign key reference to the Cherry loan identifier. This is Cherry's internal loan ID  used throughout the business intelligence and analytics ecosystem. Provides the connection  to Cherry's loan data, merchant information, and business intelligence reporting. Critical  for joining with other Cherry analytics models and business reporting.
 | Foreign key reference to the Cherry loan identifier. This is Cherry's internal loan ID  used throughout the business intelligence and analytics ecosystem. Provides the connection  to Cherry's loan data, merchant information, and business intelligence reporting. Critical  for joining with other Cherry analytics models and business reporting.
 | `[]` | `{}` |
    | `APR` | 4 | `FLOAT` | Annual Percentage Rate (APR) that was effective for the loan on the given date, expressed  as a decimal value (e.g., 0.15 for 15% APR). This represents the point-in-time APR by  identifying the most recent APR change that occurred on or before the record date. The value  is derived using COALESCE logic that prioritizes the new APR value from rate changes, falling  back to the old value when new value is not available. This field is essential for regulatory  compliance, revenue calculations, risk analysis, and understanding how rate modifications  impact loan performance over time. NULL values are filtered out to ensure clean reporting. | Annual Percentage Rate (APR) that was effective for the loan on the given date, expressed  as a decimal value (e.g., 0.15 for 15% APR). This represents the point-in-time APR by  identifying the most recent APR change that occurred on or before the record date. The value  is derived using COALESCE logic that prioritizes the new APR value from rate changes, falling  back to the old value when new value is not available. This field is essential for regulatory  compliance, revenue calculations, risk analysis, and understanding how rate modifications  impact loan performance over time. NULL values are filtered out to ensure clean reporting. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.is_incremental`
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.stg_loanpro_apr_changes`

---
