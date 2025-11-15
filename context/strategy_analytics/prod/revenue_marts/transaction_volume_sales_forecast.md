## Model: `transaction_volume_sales_forecast`

`transaction_volume_sales_forecast`

*   **Unique ID:** `model.cherry_data_model.transaction_volume_sales_forecast`
*   **FQN:** `prod.revenue_marts.transaction_volume_sales_forecast`
*   **Description:** **Sales Team Transaction Volume Forecasting**
This model provides sales team-focused forecasting with detailed Account Executive attribution,  enabling individual AE performance planning and territory management. It uses sophisticated  historical practice assignment analysis to distribute pipeline forecasts across specific  Account Executives based on their recent practice acquisition patterns.
**Key Enhancements over Base Model:** - **Account Executive Attribution**: Includes full AE organizational hierarchy (department, team, subteam, individual) - **Sophisticated Proportion Logic**: Uses historical user role data + practice counts to calculate AE-specific proportions - **Territory-Based Distribution**: Considers individual AE historical practice volumes for pipeline distribution - **Role History Integration**: Uses sf_user_history to account for team changes and role transitions
**Practice Proportion Methodology:** - Analyzes 90-day historical practice assignment patterns by Account Executive - Calculates practice count per day for each AE using user_history role tracking - Computes AE proportion within industry segments based on historical practice acquisition rates - Applies proportions to distribute pipeline forecasted volumes to specific Account Executives - Accounts for role changes and team transitions using historical user data
**Primary Use Cases:** - Individual Account Executive volume planning and quota setting - Sales territory analysis and capacity planning - AE performance forecasting and goal establishment - Sales team workload balancing and resource allocation - Territory-based volume forecasting and pipeline management
**Data Sources:** - **live_practice_forecasting**: Base forecasting model with AE details preserved - **pipeline_practice_forecasting**: Base pipeline forecasting for distribution - **stg_practices**: Historical practice-AE assignments for proportion analysis - **stg_sf_users & sf_user_history**: User role tracking for accurate proportion calculations

*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `FORECAST_TYPE` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `DATE` | 2 | `DATE` | **Daily Date Dimension**
Specific calendar date for daily-level sales forecasting analysis. Enables daily AE  volume planning, territory analysis, and granular sales forecasting for team management.  Supports daily sales operational planning and territory performance tracking.
 | **Daily Date Dimension**
Specific calendar date for daily-level sales forecasting analysis. Enables daily AE  volume planning, territory analysis, and granular sales forecasting for team management.  Supports daily sales operational planning and territory performance tracking.
 | `[]` | `{}` |
    | `MONTH` | 3 | `DATE` |  |  | `[]` | `{}` |
    | `QUARTER` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `GO_LIVE_MONTH` | 5 | `DATE` |  |  | `[]` | `{}` |
    | `DEPARTMENT_OWNERSHIP` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `ORGANIZATION_AGE` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `PRACTICE_TYPE` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_DEPARTMENT` | 10 | `TEXT` | **Account Executive Department**
Department where the Account Executive is assigned (e.g., 'Sales', 'Account Executives').  For Live records, sourced from live_practice_forecasting; for Pipeline records,  assigned based on practice proportion analysis using historical AE assignments.
 | **Account Executive Department**
Department where the Account Executive is assigned (e.g., 'Sales', 'Account Executives').  For Live records, sourced from live_practice_forecasting; for Pipeline records,  assigned based on practice proportion analysis using historical AE assignments.
 | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_TEAM` | 11 | `TEXT` | **Account Executive Team Assignment**
Specific sales team within the department (e.g., 'Sales Dental', 'Account Executives Aesthetics').  Used for team-level volume planning and territory management within the sales organization.
 | **Account Executive Team Assignment**
Specific sales team within the department (e.g., 'Sales Dental', 'Account Executives Aesthetics').  Used for team-level volume planning and territory management within the sales organization.
 | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_SUBTEAM` | 12 | `TEXT` | **Account Executive Subteam Assignment**
More granular team subdivision within the main sales team for specialized territories  or market focuses. Enables detailed territory analysis and specialized team forecasting.
 | **Account Executive Subteam Assignment**
More granular team subdivision within the main sales team for specialized territories  or market focuses. Enables detailed territory analysis and specialized team forecasting.
 | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE` | 13 | `TEXT` | **Individual Account Executive**
Specific Account Executive responsible for practice relationship and volume generation.  For Live records, represents actual assigned AE; for Pipeline records, assigned using  sophisticated practice proportions calculated from 90-day historical practice acquisition  patterns, user role history, and territory analysis. Enables individual AE volume  planning and performance forecasting. | **Individual Account Executive**
Specific Account Executive responsible for practice relationship and volume generation.  For Live records, represents actual assigned AE; for Pipeline records, assigned using  sophisticated practice proportions calculated from 90-day historical practice acquisition  patterns, user role history, and territory analysis. Enables individual AE volume  planning and performance forecasting. | `[]` | `{}` |
    | `TRANSACTION_VOLUME` | 14 | `FLOAT` |  |  | `[]` | `{}` |
    | `FORECASTED_VOLUME` | 15 | `FLOAT` |  |  | `[]` | `{}` |
    | `TOTAL_VOLUME` | 16 | `FLOAT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.live_practice_forecasting`
    *   `model.cherry_data_model.pipeline_practice_forecasting`
    *   `model.cherry_data_model.sf_user_history`
    *   `model.cherry_data_model.stg_practices`
    *   `model.cherry_data_model.stg_sf_users`

---
