## Model: `transaction_volume_retention_forecast`

`transaction_volume_retention_forecast`

*   **Unique ID:** `model.cherry_data_model.transaction_volume_retention_forecast`
*   **FQN:** `prod.revenue_marts.transaction_volume_retention_forecast`
*   **Description:** **Retention Team Transaction Volume Forecasting**
This model extends the foundational forecasting with detailed retention owner attribution,  enabling team-specific volume planning and individual contributor performance analysis.  It uses recent practice ownership patterns to distribute pipeline forecasts across specific  retention team members, providing granular forecasting for capacity planning and quota setting.
**Key Enhancements over Base Model:** - **Individual Owner Attribution**: Includes retention_owner_team and retention_owner details - **Practice Proportion Logic**: Uses 90-day historical practice ownership to distribute pipeline forecasts - **Team-Level Granularity**: Enables individual contributor and team-level volume planning - **Daily Date Dimension**: Includes date field for daily forecasting analysis
**Practice Proportion Methodology:** - Analyzes retention ownership patterns from last 90 days of practice go-lives - Calculates proportion of practices owned by each retention owner within department/industry combinations - Applies these proportions to distribute pipeline forecasted volumes to specific owners - Ensures pipeline forecasts align with recent ownership assignment patterns
**Primary Use Cases:** - Individual retention team member volume planning and quota setting - Team capacity analysis and workload balancing - Retention owner performance forecasting and goal setting - Department-level retention volume planning with owner attribution - Daily retention team forecasting and resource allocation
**Data Sources:** - **live_practice_forecasting**: Base forecasting model with owner details preserved - **pipeline_practice_forecasting**: Base pipeline forecasting for distribution - **stg_practices**: Recent practice ownership patterns for proportion calculations

*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `FORECAST_TYPE` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `DATE` | 2 | `DATE` | **Daily Date Dimension**
Specific calendar date for daily-level forecasting analysis. Enables daily volume  planning, trend analysis, and granular forecasting for retention team management.  Supports daily operational planning and short-term capacity management.
 | **Daily Date Dimension**
Specific calendar date for daily-level forecasting analysis. Enables daily volume  planning, trend analysis, and granular forecasting for retention team management.  Supports daily operational planning and short-term capacity management.
 | `[]` | `{}` |
    | `MONTH` | 3 | `DATE` |  |  | `[]` | `{}` |
    | `QUARTER` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `GO_LIVE_MONTH` | 5 | `DATE` |  |  | `[]` | `{}` |
    | `DEPARTMENT_OWNERSHIP` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `ORGANIZATION_AGE` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `PRACTICE_TYPE` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_TEAM` | 11 | `TEXT` | **Retention Owner Team Assignment**
Specific retention team within the retention department (e.g., 'Dental', 'Aesthetics',  'Veterinary'). For Live records, comes directly from live_practice_forecasting;  for Pipeline records, assigned based on practice proportion analysis of recent  ownership patterns within department/industry combinations.
 | **Retention Owner Team Assignment**
Specific retention team within the retention department (e.g., 'Dental', 'Aesthetics',  'Veterinary'). For Live records, comes directly from live_practice_forecasting;  for Pipeline records, assigned based on practice proportion analysis of recent  ownership patterns within department/industry combinations.
 | `[]` | `{}` |
    | `RETENTION_OWNER` | 12 | `TEXT` | **Individual Retention Owner**
Specific retention team member responsible for practice relationship. For Live records,  represents actual assigned retention owner; for Pipeline records, assigned using  practice proportions calculated from 90-day historical ownership patterns. Enables  individual contributor volume planning and performance forecasting.
 | **Individual Retention Owner**
Specific retention team member responsible for practice relationship. For Live records,  represents actual assigned retention owner; for Pipeline records, assigned using  practice proportions calculated from 90-day historical ownership patterns. Enables  individual contributor volume planning and performance forecasting.
 | `[]` | `{}` |
    | `TRANSACTION_VOLUME` | 13 | `FLOAT` |  |  | `[]` | `{}` |
    | `FORECASTED_VOLUME` | 14 | `FLOAT` |  |  | `[]` | `{}` |
    | `TOTAL_VOLUME` | 15 | `FLOAT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.live_practice_forecasting`
    *   `model.cherry_data_model.pipeline_practice_forecasting`
    *   `model.cherry_data_model.stg_practices`

---
