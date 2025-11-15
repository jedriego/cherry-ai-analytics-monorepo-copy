## Model: `retention_average_volumes_and_percent_transacting_pdm_xf`

`retention_average_volumes_and_percent_transacting_pdm_xf`

*   **Unique ID:** `model.cherry_data_model.retention_average_volumes_and_percent_transacting_pdm_xf`
*   **FQN:** `prod.revenue_marts.retention_average_volumes_and_percent_transacting_pdm_xf`
*   **Description:** **Practice Development Team Performance Analytics**
This foundational model tracks retention performance for the Practice Development (PDM) team,  focusing on Dental, MedSpa, and Plastic Surgery practices. PDM team manages  higher-potential practices (>$10K monthly potential) and operates with specialized expertise  in practice growth and optimization strategies.
**Team Scope & Filtering:** - Practice Development department and Natural Retention Group control - MedSpa, Plastic Surgery, and Dental industry segments - Practice potential >$10K or Plastic Surgery practices (all included) - Excludes specific test accounts and Customer Support assignments
**Special Segmentation:** - Plastic Surgery practices split into 2% (top-tier) and 98% (standard) cohorts - Calvin Bohn's practices segmented into PDM Aesthetics vs PDM East Dental - Team and department totals included for hierarchical performance analysis
**Performance Tracking:** - Individual rep, team, and department aggregation levels - 7-day trailing averages for trend identification and performance smoothing - Monthly and quarterly target integration from Google Sheets retention targets - Test group baseline comparison for incremental impact measurement

*   **Tags:** `['revenue_analytics', 'revenue', 'hourly', 'revenue_hourly']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `FULL_DATE` | 1 | `DATE` | Calendar date for the performance metrics. All models track daily data from 2024-11-01  through current date, providing complete historical performance tracking and trend analysis.
 | Calendar date for the performance metrics. All models track daily data from 2024-11-01  through current date, providing complete historical performance tracking and trend analysis.
 | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT` | 2 | `TEXT` | Department responsible for retention activities ('Practice Development', 'Customer Success',  'Natural Retention Group'). Primary organizational dimension for team performance analysis  and department-level goal setting and accountability.
 | Department responsible for retention activities ('Practice Development', 'Customer Success',  'Natural Retention Group'). Primary organizational dimension for team performance analysis  and department-level goal setting and accountability.
 | `[]` | `{}` |
    | `RETENTION_OWNER_TEAM` | 3 | `TEXT` | Specific team within the retention department (e.g., 'PDM East Dental', 'Customer Success  Aesthetics', 'Customer Success Dental'). Enables team-level performance tracking and  specialized segment analysis within departments.
 | Specific team within the retention department (e.g., 'PDM East Dental', 'Customer Success  Aesthetics', 'Customer Success Dental'). Enables team-level performance tracking and  specialized segment analysis within departments.
 | `[]` | `{}` |
    | `RETENTION_OWNER` | 4 | `TEXT` | Individual retention specialist or account manager responsible for practice relationships.  Includes individual names for rep-level analysis and team totals (prefixed with '-- Team Total:'  or '-- Department Total:') for aggregated performance tracking.
 | Individual retention specialist or account manager responsible for practice relationships.  Includes individual names for rep-level analysis and team totals (prefixed with '-- Team Total:'  or '-- Department Total:') for aggregated performance tracking.
 | `[]` | `{}` |
    | `SEGMENT` | 5 | `TEXT` | Industry or practice classification used for segmentation ('Dental', 'MedSpa',  'Plastic and Cosmetic Surgery', 'Veterinary', 'Other', 'Aesthetics', 'Combined Core').  Enables industry-specific performance analysis and specialized retention strategies.
 | Industry or practice classification used for segmentation ('Dental', 'MedSpa',  'Plastic and Cosmetic Surgery', 'Veterinary', 'Other', 'Aesthetics', 'Combined Core').  Enables industry-specific performance analysis and specialized retention strategies.
 | `[]` | `{}` |
    | `PRACTICE_COUNT` | 6 | `NUMBER` | Number of practices eligible for retention tracking (30+ days post go-live) under this  retention owner/segment combination. Used for calculating per-practice averages and  understanding portfolio size for workload and performance context.
 | Number of practices eligible for retention tracking (30+ days post go-live) under this  retention owner/segment combination. Used for calculating per-practice averages and  understanding portfolio size for workload and performance context.
 | `[]` | `{}` |
    | `TEST_GROUP_PRACTICE_COUNT` | 7 | `NUMBER` | Number of practices in the Natural Retention Group control segment for this industry/segment.  Used as baseline for calculating performance deltas and target adjustments relative to  organic practice performance without active retention intervention.
 | Number of practices in the Natural Retention Group control segment for this industry/segment.  Used as baseline for calculating performance deltas and target adjustments relative to  organic practice performance without active retention intervention.
 | `[]` | `{}` |
    | `PERCENT_HEALTHY_TRANSACTING_IN_LAST_30_DAYS` | 8 | `NUMBER` | Percentage of eligible practices that had at least one "healthy" transaction in the last  30 days. Healthy transactions exclude Alle merchants and practices with At-Risk health  assessments. Core engagement metric for measuring retention effectiveness and practice activation.
 | Percentage of eligible practices that had at least one "healthy" transaction in the last  30 days. Healthy transactions exclude Alle merchants and practices with At-Risk health  assessments. Core engagement metric for measuring retention effectiveness and practice activation.
 | `[]` | `{}` |
    | `AVERAGE_LAST_30_HEALTHY_VOLUME` | 9 | `FLOAT` | Average gross loan amount per practice over the last 30 days, including only "healthy"  transactions. Primary volume performance metric for retention team effectiveness and  practice growth measurement, excluding At-Risk and Alle volume.
 | Average gross loan amount per practice over the last 30 days, including only "healthy"  transactions. Primary volume performance metric for retention team effectiveness and  practice growth measurement, excluding At-Risk and Alle volume.
 | `[]` | `{}` |
    | `AVERAGE_LAST_30_HEALTHY_VOLUME_UNCAPPED` | 10 | `FLOAT` |  |  | `[]` | `{}` |
    | `PRIOR_DAY_HEALTHY_VOLUME_RUN_RATE` | 11 | `FLOAT` | Annualized projection based on previous day's healthy volume (prior day volume * 30 * 12).  Provides forward-looking volume estimate for near-term performance assessment and  early identification of trends or concerns requiring intervention.
 | Annualized projection based on previous day's healthy volume (prior day volume * 30 * 12).  Provides forward-looking volume estimate for near-term performance assessment and  early identification of trends or concerns requiring intervention.
 | `[]` | `{}` |
    | `TOTAL_PRIOR_DAY_HEALTHY_VOLUME` | 12 | `FLOAT` | Total dollar amount of healthy volume generated on the previous day across all practices  for this retention owner/segment. Used for daily volume tracking and short-term  performance monitoring at portfolio level.
 | Total dollar amount of healthy volume generated on the previous day across all practices  for this retention owner/segment. Used for daily volume tracking and short-term  performance monitoring at portfolio level.
 | `[]` | `{}` |
    | `TEST_GROUP_PRIOR_DAY_HEALTHY_VOLUME_RUN_RATE` | 13 | `FLOAT` | Annualized volume projection for Natural Retention Group practices in this segment.  Provides baseline for measuring incremental impact of active retention efforts versus  organic practice performance without intervention.
 | Annualized volume projection for Natural Retention Group practices in this segment.  Provides baseline for measuring incremental impact of active retention efforts versus  organic practice performance without intervention.
 | `[]` | `{}` |
    | `TRAILING_7_DAY_AVERAGE_PERCENT_HEALTHY_TRANSACTING_IN_LAST_30` | 14 | `NUMBER` | Seven-day moving average of the percent healthy transacting metric. Smooths daily  volatility to provide clearer trend identification and more stable performance  assessment for retention team management and goal tracking.
 | Seven-day moving average of the percent healthy transacting metric. Smooths daily  volatility to provide clearer trend identification and more stable performance  assessment for retention team management and goal tracking.
 | `[]` | `{}` |
    | `TEST_GROUP_TRAILING_7_DAY_AVERAGE_PERCENT_HEALTHY_TRANSACTING_IN_LAST_30` | 15 | `NUMBER` | Seven-day moving average of percent healthy transacting for Natural Retention Group  control practices. Used as baseline for calculating target adjustments and measuring  incremental impact of retention activities above organic performance levels.
 | Seven-day moving average of percent healthy transacting for Natural Retention Group  control practices. Used as baseline for calculating target adjustments and measuring  incremental impact of retention activities above organic performance levels.
 | `[]` | `{}` |
    | `TEST_GROUP_TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME` | 16 | `FLOAT` | Seven-day moving average of healthy volume for Natural Retention Group practices.  Critical baseline metric for target setting and measuring retention team value-add  above natural practice performance trends and market conditions.
 | Seven-day moving average of healthy volume for Natural Retention Group practices.  Critical baseline metric for target setting and measuring retention team value-add  above natural practice performance trends and market conditions.
 | `[]` | `{}` |
    | `TEST_GROUP_TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME_UNCAPPED` | 17 | `FLOAT` |  |  | `[]` | `{}` |
    | `TRAILING_7_DAY_PERCENT_HEALTHY_TRANSACTING_IN_LAST_30_TARGET` | 18 | `FLOAT` | Monthly target for percent healthy transacting, calculated as test group baseline plus  retention target adjustment from Google Sheets. Provides monthly goal framework for  retention team performance management and accountability tracking.
 | Monthly target for percent healthy transacting, calculated as test group baseline plus  retention target adjustment from Google Sheets. Provides monthly goal framework for  retention team performance management and accountability tracking.
 | `[]` | `{}` |
    | `TRAILING_7_DAY_PERCENT_HEALTHY_TRANSACTING_IN_LAST_30_TARGET_QUARTERLY` | 19 | `FLOAT` | Quarterly target for percent healthy transacting, using quarterly retention targets  for longer-term goal setting. Supports quarterly performance reviews and strategic  retention planning with appropriate seasonal and market adjustments.
 | Quarterly target for percent healthy transacting, using quarterly retention targets  for longer-term goal setting. Supports quarterly performance reviews and strategic  retention planning with appropriate seasonal and market adjustments.
 | `[]` | `{}` |
    | `TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME_TARGET` | 20 | `FLOAT` | Monthly target for average healthy volume per practice, calculated as test group  baseline plus target increment from retention targets. Primary monthly volume goal  for retention team performance evaluation and bonus/incentive calculations.
 | Monthly target for average healthy volume per practice, calculated as test group  baseline plus target increment from retention targets. Primary monthly volume goal  for retention team performance evaluation and bonus/incentive calculations.
 | `[]` | `{}` |
    | `TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME_TARGET_QUARTERLY` | 21 | `FLOAT` | Quarterly target for average healthy volume per practice, supporting longer-term  strategic planning and quarterly performance assessment. Enables more sophisticated  goal setting that accounts for seasonal patterns and market dynamics.
 | Quarterly target for average healthy volume per practice, supporting longer-term  strategic planning and quarterly performance assessment. Enables more sophisticated  goal setting that accounts for seasonal patterns and market dynamics.
 | `[]` | `{}` |
    | `TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME` | 22 | `FLOAT` | Seven-day moving average of the average healthy volume metric. Smoothed version of  primary performance metric for trend analysis and stable performance assessment,  reducing daily noise for clearer retention effectiveness measurement.
 | Seven-day moving average of the average healthy volume metric. Smoothed version of  primary performance metric for trend analysis and stable performance assessment,  reducing daily noise for clearer retention effectiveness measurement.
 | `[]` | `{}` |
    | `TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME_UNCAPPED` | 23 | `FLOAT` |  |  | `[]` | `{}` |
    | `VOLUME_PHASE_IN` | 24 | `FLOAT` |  |  | `[]` | `{}` |
    | `TRANSACTING_PHASE_IN` | 25 | `FLOAT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.loan_info_xf`
    *   `model.cherry_data_model.practice_info_full_xf`
    *   `model.cherry_data_model.src_gsheets_eligible_retention_territories`
    *   `model.cherry_data_model.src_gsheets_patientfi_bounty_practices_q4`
    *   `model.cherry_data_model.src_gsheets_retention_phase_ins`
    *   `model.cherry_data_model.src_gsheets_retention_targets`
    *   `model.cherry_data_model.stg_sf_users`

---
