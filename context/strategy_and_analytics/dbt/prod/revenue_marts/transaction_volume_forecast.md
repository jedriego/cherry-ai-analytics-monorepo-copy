## Model: `transaction_volume_forecast`

`transaction_volume_forecast`

*   **Unique ID:** `model.cherry_data_model.transaction_volume_forecast`
*   **FQN:** `prod.revenue_marts.transaction_volume_forecast`
*   **Description:** **Foundational Transaction Volume Forecasting Model**
This is the core aggregated view of transaction volume forecasting that combines live practice  performance with pipeline projections at a high level. It serves as the foundational model  for overall volume planning, executive reporting, and strategic analysis without owner-level  attribution details.
**Key Architecture:** - **Live Practice Component**: Aggregates from live_practice_forecasting which applies sophisticated 
  forecasting models (seasonal, day-of-week, holiday, growth adjustments) to existing practices
- **Pipeline Component**: Aggregates from pipeline_practice_forecasting which projects volumes 
  from forecasted future go-live dates using advanced modeling
- **Union Structure**: Combines both components with forecast_type distinction for comprehensive analysis
**Primary Use Cases:** - Executive-level volume forecasting and strategic planning - Industry segment performance analysis and benchmarking - Department ownership volume planning (Account Executive, Handoff, Retention phases) - Quarterly and monthly volume planning across practice types - High-level business intelligence and reporting dashboards
**Data Sources:** - **live_practice_forecasting**: Sophisticated forecasting model for existing practices - **pipeline_practice_forecasting**: Advanced forecasting model for future practices

*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `FORECAST_TYPE` | 1 | `TEXT` | **Live vs Pipeline Classification**
Distinguishes between 'Live' records from existing practices (live_practice_forecasting)  and 'Pipeline' records from forecasted future practices (pipeline_practice_forecasting).  Live records include both historical transaction volume and future forecasted volume,  while Pipeline records contain only forecasted volumes for practices expected to go live.
 | **Live vs Pipeline Classification**
Distinguishes between 'Live' records from existing practices (live_practice_forecasting)  and 'Pipeline' records from forecasted future practices (pipeline_practice_forecasting).  Live records include both historical transaction volume and future forecasted volume,  while Pipeline records contain only forecasted volumes for practices expected to go live.
 | `[]` | `{}` |
    | `QUARTER` | 2 | `TEXT` | **Quarter Identifier**
Quarter identifier in format 'YYYY QX' (e.g., '2024 Q1'). For January dates,  uses previous year convention (January 2024 = '2023 Q4'). Used for quarterly  volume analysis and strategic planning periods.
 | **Quarter Identifier**
Quarter identifier in format 'YYYY QX' (e.g., '2024 Q1'). For January dates,  uses previous year convention (January 2024 = '2023 Q4'). Used for quarterly  volume analysis and strategic planning periods.
 | `[]` | `{}` |
    | `MONTH` | 3 | `DATE` | **Month Identifier**
Month identifier in DATE format truncated to the first of the month.  Primary time dimension for monthly volume analysis, forecasting comparisons,  and seasonal pattern identification across practice portfolios.
 | **Month Identifier**
Month identifier in DATE format truncated to the first of the month.  Primary time dimension for monthly volume analysis, forecasting comparisons,  and seasonal pattern identification across practice portfolios.
 | `[]` | `{}` |
    | `GO_LIVE_MONTH` | 4 | `DATE` | **Practice Go-Live Month**
Month when practice originally went live, used for cohort-based volume analysis.  Critical for understanding practice maturity patterns, lifecycle forecasting,  and cohort performance tracking over time.
 | **Practice Go-Live Month**
Month when practice originally went live, used for cohort-based volume analysis.  Critical for understanding practice maturity patterns, lifecycle forecasting,  and cohort performance tracking over time.
 | `[]` | `{}` |
    | `DEPARTMENT_OWNERSHIP` | 5 | `TEXT` | **Department Ownership Phase**
Operational ownership phase based on practice lifecycle: 'Account Executives'  (0-30 days post go-live), 'Handoff' (31-60 days), 'Retention' (60+ days).  Determines which team is responsible for practice relationship and volume performance.
 | **Department Ownership Phase**
Operational ownership phase based on practice lifecycle: 'Account Executives'  (0-30 days post go-live), 'Handoff' (31-60 days), 'Retention' (60+ days).  Determines which team is responsible for practice relationship and volume performance.
 | `[]` | `{}` |
    | `ORGANIZATION_AGE` | 6 | `TEXT` | **Practice Maturity Classification**
Practice maturity classification: 'First Year' for practices within 12 months  of go-live, 'Over One Year' for established practices. Used in forecasting models  as newer practices have different volume patterns than mature practices.
 | **Practice Maturity Classification**
Practice maturity classification: 'First Year' for practices within 12 months  of go-live, 'Over One Year' for established practices. Used in forecasting models  as newer practices have different volume patterns than mature practices.
 | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 7 | `TEXT` | **Industry Segment Classification**
Strategic industry segment grouping from stg_practices (e.g., 'Dental', 'Veterinary',  'Plastic and Cosmetic Surgery', 'MedSpa'). Used for industry-specific  forecasting models and segment performance analysis.
 | **Industry Segment Classification**
Strategic industry segment grouping from stg_practices (e.g., 'Dental', 'Veterinary',  'Plastic and Cosmetic Surgery', 'MedSpa'). Used for industry-specific  forecasting models and segment performance analysis.
 | `[]` | `{}` |
    | `PRACTICE_TYPE` | 8 | `TEXT` | **Practice Type Classification**
Practice type derived from alle_practice_type: 'Alle' for New Practice partnerships,  'Cherry' for all other practice types. Used for distinguishing partnership-driven  vs standard practice volume in forecasting and analysis.
 | **Practice Type Classification**
Practice type derived from alle_practice_type: 'Alle' for New Practice partnerships,  'Cherry' for all other practice types. Used for distinguishing partnership-driven  vs standard practice volume in forecasting and analysis.
 | `[]` | `{}` |
    | `PRACTICE_POTENTIAL_BUCKET` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT` | 10 | `TEXT` | **Retention Department Assignment**
Department responsible for practice retention management (from stg_practices).  Used in forecasting models for department-specific volume projections and  retention team capacity planning.
 | **Retention Department Assignment**
Department responsible for practice retention management (from stg_practices).  Used in forecasting models for department-specific volume projections and  retention team capacity planning.
 | `[]` | `{}` |
    | `LIVE_PRACTICE_DAYS` | 11 | `FLOAT` | **Active Practice Day Count**
Count of practice-days where practices are active and operational. For Live records,  represents actual active practice days; for Pipeline records, represents forecasted  active practice days from future go-lives. Used for capacity planning and volume normalization.
 | **Active Practice Day Count**
Count of practice-days where practices are active and operational. For Live records,  represents actual active practice days; for Pipeline records, represents forecasted  active practice days from future go-lives. Used for capacity planning and volume normalization.
 | `[]` | `{}` |
    | `TRANSACTION_VOLUME` | 12 | `FLOAT` | **Historical Transaction Volume**
Actual historical transaction volume from funded loans (gross_amount) for dates  before current_date. Only present in Live records (NULL for Pipeline records).  Sourced from loan_info_xf for loans with status 'FUNDED' or 'AWAITING_FUNDING'.  Represents confirmed past performance.
 | **Historical Transaction Volume**
Actual historical transaction volume from funded loans (gross_amount) for dates  before current_date. Only present in Live records (NULL for Pipeline records).  Sourced from loan_info_xf for loans with status 'FUNDED' or 'AWAITING_FUNDING'.  Represents confirmed past performance.
 | `[]` | `{}` |
    | `FORECASTED_VOLUME` | 13 | `FLOAT` | **Forecasted Transaction Volume**
Projected future transaction volume using sophisticated forecasting models that apply  multiple adjustment factors: seasonal adjustments (by month/industry), day-of-week patterns,  holiday impacts, growth adjustments, and practice maturity factors. For Live records,  forecasts future performance of existing practices; for Pipeline records, forecasts  volume from future practice go-lives.
 | **Forecasted Transaction Volume**
Projected future transaction volume using sophisticated forecasting models that apply  multiple adjustment factors: seasonal adjustments (by month/industry), day-of-week patterns,  holiday impacts, growth adjustments, and practice maturity factors. For Live records,  forecasts future performance of existing practices; for Pipeline records, forecasts  volume from future practice go-lives.
 | `[]` | `{}` |
    | `TOTAL_VOLUME` | 14 | `FLOAT` | **Combined Total Volume**
Sum of transaction_volume (historical) + forecasted_volume (projected future).  Provides comprehensive volume view combining actual past performance with  sophisticated forecasting projections. Used for complete business planning  and strategic volume analysis.
 | **Combined Total Volume**
Sum of transaction_volume (historical) + forecasted_volume (projected future).  Provides comprehensive volume view combining actual past performance with  sophisticated forecasting projections. Used for complete business planning  and strategic volume analysis.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.live_practice_forecasting`
    *   `model.cherry_data_model.pipeline_practice_forecasting`

---
