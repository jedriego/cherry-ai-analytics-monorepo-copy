## Model: `go_live_forecast`

`go_live_forecast`

*   **Unique ID:** `model.cherry_data_model.go_live_forecast`
*   **FQN:** `prod.revenue_marts.go_live_forecast`
*   **Description:** Combined historical and forecasted practice go-live analysis that provides a unified view of actual go-live events alongside sophisticated forecasting predictions. This model unions historical go-live data from stg_practices with forecasted go-live data from forecasted_live_practice_dates to create a comprehensive timeline of practice activations. The historical data captures actual go-live events before current date, while the forecast data projects future go-live volumes using advanced modeling that incorporates seasonal adjustments, day-of-week patterns, holiday impacts, organization age factors, and retention ownership distributions. This is essential for revenue planning, capacity forecasting, sales pipeline management, and understanding both historical trends and future expectations for practice onboarding across different industry segments and practice types.

*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `TYPE` | 1 | `TEXT` | Classification distinguishing between historical and forecasted records. 'Live' indicates actual historical go-live events from stg_practices where the go-live date occurred before current date. 'Forecast' indicates projected future go-live volumes from forecasted_live_practice_dates where the go-live date is current date or later. Used for filtering and analysis scope.
 | Classification distinguishing between historical and forecasted records. 'Live' indicates actual historical go-live events from stg_practices where the go-live date occurred before current date. 'Forecast' indicates projected future go-live volumes from forecasted_live_practice_dates where the go-live date is current date or later. Used for filtering and analysis scope.
 | `[]` | `{}` |
    | `QUARTER` | 2 | `TEXT` | Quarter identifier in format 'YYYY QX' (e.g., '2024 Q1'). For January dates, uses previous year convention (e.g., January 2024 = '2023 Q4'). Derived from calendar_table_xf and used for quarterly go-live analysis and reporting.
 | Quarter identifier in format 'YYYY QX' (e.g., '2024 Q1'). For January dates, uses previous year convention (e.g., January 2024 = '2023 Q4'). Derived from calendar_table_xf and used for quarterly go-live analysis and reporting.
 | `[]` | `{}` |
    | `MONTH` | 3 | `DATE` | Month identifier in DATE format truncated to the first of the month. Used for monthly go-live analysis, trend identification, and forecasting comparisons. Enables month-over-month analysis of go-live patterns.
 | Month identifier in DATE format truncated to the first of the month. Used for monthly go-live analysis, trend identification, and forecasting comparisons. Enables month-over-month analysis of go-live patterns.
 | `[]` | `{}` |
    | `DATE` | 4 | `DATE` | Specific date of the go-live event or forecast. For historical records, this is the actual practice_go_live_date from stg_practices. For forecasted records, this is the projected go-live date from forecasted_live_practice_dates. Serves as the primary date dimension for daily go-live analysis.
 | Specific date of the go-live event or forecast. For historical records, this is the actual practice_go_live_date from stg_practices. For forecasted records, this is the projected go-live date from forecasted_live_practice_dates. Serves as the primary date dimension for daily go-live analysis.
 | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 5 | `TEXT` | Industry segment classification inherited from stg_practices account_industry_segment. Represents strategic industry groupings such as 'Dental', 'Veterinary', 'Plastic and Cosmetic Surgery', 'MedSpa', 'Other', etc. Used for industry-specific go-live analysis and segment-based forecasting.
 | Industry segment classification inherited from stg_practices account_industry_segment. Represents strategic industry groupings such as 'Dental', 'Veterinary', 'Plastic and Cosmetic Surgery', 'MedSpa', 'Other', etc. Used for industry-specific go-live analysis and segment-based forecasting.
 | `[]` | `{}` |
    | `PRACTICE_TYPE` | 6 | `TEXT` | Practice type classification derived from stg_practices alle_practice_type. 'Alle' indicates New Practice type (alle_practice_type = 'New Practice'), 'Cherry' indicates all other practice types. Used for distinguishing between Alle partnership go-lives and standard Cherry practice go-lives in analysis.
 | Practice type classification derived from stg_practices alle_practice_type. 'Alle' indicates New Practice type (alle_practice_type = 'New Practice'), 'Cherry' indicates all other practice types. Used for distinguishing between Alle partnership go-lives and standard Cherry practice go-lives in analysis.
 | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT` | 7 | `TEXT` | Department responsible for practice retention management. Inherited from stg_practices retention_owner_department and used in forecasting models for department-specific go-live projections. Enables retention team workload planning and departmental go-live analysis.
 | Department responsible for practice retention management. Inherited from stg_practices retention_owner_department and used in forecasting models for department-specific go-live projections. Enables retention team workload planning and departmental go-live analysis.
 | `[]` | `{}` |
    | `GO_LIVES` | 8 | `FLOAT` | Count of go-live events for the specific date and dimension combination. For historical records (type = 'Live'), this represents actual count of practices that went live on the specific date, calculated by counting sf_account_id from stg_practices. For forecasted records (type = 'Forecast'), this represents projected go-live volume from forecasted_live_practice_dates, calculated using sophisticated modeling that includes base forecasted averages, seasonal adjustments (by month and industry), day-of-week patterns, holiday impacts, organization age considerations, and retention ownership distributions. The forecasting model applies multiple adjustment factors to generate realistic go-live predictions based on historical patterns and business seasonality. | Count of go-live events for the specific date and dimension combination. For historical records (type = 'Live'), this represents actual count of practices that went live on the specific date, calculated by counting sf_account_id from stg_practices. For forecasted records (type = 'Forecast'), this represents projected go-live volume from forecasted_live_practice_dates, calculated using sophisticated modeling that includes base forecasted averages, seasonal adjustments (by month and industry), day-of-week patterns, holiday impacts, organization age considerations, and retention ownership distributions. The forecasting model applies multiple adjustment factors to generate realistic go-live predictions based on historical patterns and business seasonality. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.forecasted_live_practice_dates`
    *   `model.cherry_data_model.stg_practices`

---
