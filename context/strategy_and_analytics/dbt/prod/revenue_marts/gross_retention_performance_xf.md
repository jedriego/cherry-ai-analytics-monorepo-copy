## Model: `gross_retention_performance_xf`

`gross_retention_performance_xf`

*   **Unique ID:** `model.cherry_data_model.gross_retention_performance_xf`
*   **FQN:** `prod.revenue_marts.gross_retention_performance_xf`
*   **Description:** **Gross Retention Performance Analysis**
This model provides comprehensive analysis of gross retention performance by combining retention volume  data with transaction volume data to evaluate how well practices are retaining and growing their business  over time. It serves as a key performance indicator for measuring the effectiveness of retention strategies  and identifying trends in practice engagement and transaction activity.
**Key Business Logic:** - Combines retention volume (from retention_volume model) with actual transaction volume (from loan_info_xf) - Filters to department ownership of 'Handoff' and 'Retention' to focus on post-initial onboarding periods - Provides transaction volume split between total volume and "healthy" volume (excluding At-Risk assessments) - Aggregates data by time periods (year, quarter, month) and organizational dimensions
**Primary Use Cases:** - Evaluating retention team performance across different time periods - Analyzing practice retention trends by industry segment and organization age - Comparing retention volume expectations against actual transaction performance - Identifying practices with healthy vs. at-risk transaction patterns - Supporting retention strategy optimization and resource allocation decisions
**Data Sources:** - `retention_volume`: Daily unadjusted retention volume for each account based on organization age and historical volume - `practice_info_full_xf`: Comprehensive practice information with retention owner details and organizational context - `loan_info_xf`: Complete loan transaction data with funding details and risk assessments
**Reporting Grain:** Monthly aggregation by retention owner department, industry segment, organization age, and primary organization

*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `YEAR` | 1 | `NUMBER` | Calendar year extracted from the retention volume month. Serves as the primary time dimension  for annual retention performance analysis and year-over-year trend comparison.
 | Calendar year extracted from the retention volume month. Serves as the primary time dimension  for annual retention performance analysis and year-over-year trend comparison.
 | `[]` | `{}` |
    | `QUARTER` | 2 | `TEXT` | Calendar quarter from the retention volume data (e.g., "2024-Q1"). Used for quarterly  performance analysis and seasonal trend identification in retention activities.
 | Calendar quarter from the retention volume data (e.g., "2024-Q1"). Used for quarterly  performance analysis and seasonal trend identification in retention activities.
 | `[]` | `{}` |
    | `MONTH` | 3 | `DATE` | Calendar month from the retention volume data as a date (e.g., "2024-01-01"). Primary  time dimension for monthly retention performance tracking and month-over-month analysis.
 | Calendar month from the retention volume data as a date (e.g., "2024-01-01"). Primary  time dimension for monthly retention performance tracking and month-over-month analysis.
 | `[]` | `{}` |
    | `ORGANIZATION_AGE` | 4 | `TEXT` | Age classification of the practice organization, typically "First Year" or "Over One Year"  based on the organization's go-live date. Used for segmenting retention strategies and  performance expectations based on practice maturity and lifecycle stage.
 | Age classification of the practice organization, typically "First Year" or "Over One Year"  based on the organization's go-live date. Used for segmenting retention strategies and  performance expectations based on practice maturity and lifecycle stage.
 | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 5 | `TEXT` | Industry segment classification of the practice (e.g., "Dental", "Veterinary", "Plastic and Cosmetic Surgery",  "MedSpa", "Other"). Used for industry-specific retention analysis and  performance benchmarking within similar practice types.
 | Industry segment classification of the practice (e.g., "Dental", "Veterinary", "Plastic and Cosmetic Surgery",  "MedSpa", "Other"). Used for industry-specific retention analysis and  performance benchmarking within similar practice types.
 | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_ID` | 6 | `NUMBER` | Primary organization identifier used for grouping multiple merchant locations under a single  organizational entity. Enables organization-level retention performance analysis and supports  multi-location practice management and reporting.
 | Primary organization identifier used for grouping multiple merchant locations under a single  organizational entity. Enables organization-level retention performance analysis and supports  multi-location practice management and reporting.
 | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT` | 7 | `TEXT` | Department responsible for retention activities for the practice, derived from the practice_info_full_xf  model using the latest_true_retention_owner_department field. Used for departmental performance  analysis and retention strategy accountability across organizational units.
 | Department responsible for retention activities for the practice, derived from the practice_info_full_xf  model using the latest_true_retention_owner_department field. Used for departmental performance  analysis and retention strategy accountability across organizational units.
 | `[]` | `{}` |
    | `PRACTICE_TERMINATED_BY_RISK` | 8 | `BOOLEAN` | Boolean flag indicating whether the practice has been terminated due to risk-related issues.  Used for filtering risk-terminated practices from retention performance analysis and understanding  the impact of risk terminations on retention metrics.
 | Boolean flag indicating whether the practice has been terminated due to risk-related issues.  Used for filtering risk-terminated practices from retention performance analysis and understanding  the impact of risk terminations on retention metrics.
 | `[]` | `{}` |
    | `RETENTION_VOLUME` | 9 | `FLOAT` | Total retention volume amount aggregated from the retention_volume model. This represents the  unadjusted daily retention volume summed across all relevant time periods and practices.  Used as the baseline expectation for measuring retention performance and setting volume targets.
 | Total retention volume amount aggregated from the retention_volume model. This represents the  unadjusted daily retention volume summed across all relevant time periods and practices.  Used as the baseline expectation for measuring retention performance and setting volume targets.
 | `[]` | `{}` |
    | `TRANSACTION_VOLUME` | 10 | `FLOAT` | Total gross transaction volume from funded loans during the specified time period. Sourced from  loan_info_xf where loan_status is 'FUNDED' or 'AWAITING_FUNDING' and department_ownership is  'Handoff' or 'Retention'. Represents actual business volume generated during the retention period.
 | Total gross transaction volume from funded loans during the specified time period. Sourced from  loan_info_xf where loan_status is 'FUNDED' or 'AWAITING_FUNDING' and department_ownership is  'Handoff' or 'Retention'. Represents actual business volume generated during the retention period.
 | `[]` | `{}` |
    | `TRANSACTION_VOLUME_HEALTHY` | 11 | `FLOAT` | Total gross transaction volume excluding loans with At-Risk assessments. Calculated by filtering  out transactions where latest_look_assessment contains 'At-Risk' from the total transaction volume.  Provides a cleaner view of sustainable, healthy business volume for retention performance evaluation. | Total gross transaction volume excluding loans with At-Risk assessments. Calculated by filtering  out transactions where latest_look_assessment contains 'At-Risk' from the total transaction volume.  Provides a cleaner view of sustainable, healthy business volume for retention performance evaluation. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.loan_info_xf`
    *   `model.cherry_data_model.practice_info_full_xf`
    *   `model.cherry_data_model.retention_volume`

---
