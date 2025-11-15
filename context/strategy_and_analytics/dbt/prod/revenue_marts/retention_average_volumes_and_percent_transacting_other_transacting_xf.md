## Model: `retention_average_volumes_and_percent_transacting_other_transacting_xf`

`retention_average_volumes_and_percent_transacting_other_transacting_xf`

*   **Unique ID:** `model.cherry_data_model.retention_average_volumes_and_percent_transacting_other_transacting_xf`
*   **FQN:** `prod.revenue_marts.retention_average_volumes_and_percent_transacting_other_transacting_xf`
*   **Description:** **"Other" Segment Transacting Component Model**
Component model calculating engagement-specific metrics for the "Other" segment with lower practice  potential threshold ($4K+) to capture broader engagement patterns while focusing volume analysis  on higher-potential practices through the companion volume model.
**Filtering Differences:** - Practice potential >$4K and ≤$7.5K (engagement-focused threshold) - Same team scope as volume model but broader practice inclusion - Transacting metrics only (percent healthy transacting, transacting targets, trailing averages) - Combined with volume model data in retention_average_volumes_and_percent_transacting_other_xf

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
    | `PRIOR_DAY_HEALTHY_VOLUME_RUN_RATE` | 10 | `FLOAT` | Annualized projection based on previous day's healthy volume (prior day volume * 30 * 12).  Provides forward-looking volume estimate for near-term performance assessment and  early identification of trends or concerns requiring intervention.
 | Annualized projection based on previous day's healthy volume (prior day volume * 30 * 12).  Provides forward-looking volume estimate for near-term performance assessment and  early identification of trends or concerns requiring intervention.
 | `[]` | `{}` |
    | `TOTAL_PRIOR_DAY_HEALTHY_VOLUME` | 11 | `FLOAT` | Total dollar amount of healthy volume generated on the previous day across all practices  for this retention owner/segment. Used for daily volume tracking and short-term  performance monitoring at portfolio level.
 | Total dollar amount of healthy volume generated on the previous day across all practices  for this retention owner/segment. Used for daily volume tracking and short-term  performance monitoring at portfolio level.
 | `[]` | `{}` |
    | `TEST_GROUP_PRIOR_DAY_HEALTHY_VOLUME_RUN_RATE` | 12 | `FLOAT` | Annualized volume projection for Natural Retention Group practices in this segment.  Provides baseline for measuring incremental impact of active retention efforts versus  organic practice performance without intervention.
 | Annualized volume projection for Natural Retention Group practices in this segment.  Provides baseline for measuring incremental impact of active retention efforts versus  organic practice performance without intervention.
 | `[]` | `{}` |
    | `TRAILING_7_DAY_AVERAGE_PERCENT_HEALTHY_TRANSACTING_IN_LAST_30` | 13 | `NUMBER` | Seven-day moving average of the percent healthy transacting metric. Smooths daily  volatility to provide clearer trend identification and more stable performance  assessment for retention team management and goal tracking.
 | Seven-day moving average of the percent healthy transacting metric. Smooths daily  volatility to provide clearer trend identification and more stable performance  assessment for retention team management and goal tracking.
 | `[]` | `{}` |
    | `TEST_GROUP_TRAILING_7_DAY_AVERAGE_PERCENT_HEALTHY_TRANSACTING_IN_LAST_30` | 14 | `NUMBER` | Seven-day moving average of percent healthy transacting for Natural Retention Group  control practices. Used as baseline for calculating target adjustments and measuring  incremental impact of retention activities above organic performance levels.
 | Seven-day moving average of percent healthy transacting for Natural Retention Group  control practices. Used as baseline for calculating target adjustments and measuring  incremental impact of retention activities above organic performance levels.
 | `[]` | `{}` |
    | `TEST_GROUP_TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME` | 15 | `FLOAT` | Seven-day moving average of healthy volume for Natural Retention Group practices.  Critical baseline metric for target setting and measuring retention team value-add  above natural practice performance trends and market conditions.
 | Seven-day moving average of healthy volume for Natural Retention Group practices.  Critical baseline metric for target setting and measuring retention team value-add  above natural practice performance trends and market conditions.
 | `[]` | `{}` |
    | `TRAILING_7_DAY_PERCENT_HEALTHY_TRANSACTING_IN_LAST_30_TARGET` | 16 | `FLOAT` | Monthly target for percent healthy transacting, calculated as test group baseline plus  retention target adjustment from Google Sheets. Provides monthly goal framework for  retention team performance management and accountability tracking.
 | Monthly target for percent healthy transacting, calculated as test group baseline plus  retention target adjustment from Google Sheets. Provides monthly goal framework for  retention team performance management and accountability tracking.
 | `[]` | `{}` |
    | `TRAILING_7_DAY_PERCENT_HEALTHY_TRANSACTING_IN_LAST_30_TARGET_QUARTERLY` | 17 | `FLOAT` | Quarterly target for percent healthy transacting, using quarterly retention targets  for longer-term goal setting. Supports quarterly performance reviews and strategic  retention planning with appropriate seasonal and market adjustments.
 | Quarterly target for percent healthy transacting, using quarterly retention targets  for longer-term goal setting. Supports quarterly performance reviews and strategic  retention planning with appropriate seasonal and market adjustments.
 | `[]` | `{}` |
    | `TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME_TARGET` | 18 | `FLOAT` | Monthly target for average healthy volume per practice, calculated as test group  baseline plus target increment from retention targets. Primary monthly volume goal  for retention team performance evaluation and bonus/incentive calculations.
 | Monthly target for average healthy volume per practice, calculated as test group  baseline plus target increment from retention targets. Primary monthly volume goal  for retention team performance evaluation and bonus/incentive calculations.
 | `[]` | `{}` |
    | `TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME_TARGET_QUARTERLY` | 19 | `FLOAT` | Quarterly target for average healthy volume per practice, supporting longer-term  strategic planning and quarterly performance assessment. Enables more sophisticated  goal setting that accounts for seasonal patterns and market dynamics.
 | Quarterly target for average healthy volume per practice, supporting longer-term  strategic planning and quarterly performance assessment. Enables more sophisticated  goal setting that accounts for seasonal patterns and market dynamics.
 | `[]` | `{}` |
    | `TRAILING_7_DAY_AVERAGE_LAST_30_HEALTHY_VOLUME` | 20 | `FLOAT` | Seven-day moving average of the average healthy volume metric. Smoothed version of  primary performance metric for trend analysis and stable performance assessment,  reducing daily noise for clearer retention effectiveness measurement.
 | Seven-day moving average of the average healthy volume metric. Smoothed version of  primary performance metric for trend analysis and stable performance assessment,  reducing daily noise for clearer retention effectiveness measurement.
 | `[]` | `{}` |
    | `TRANSACTING_PHASE_IN` | 21 | `FLOAT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.loan_info_xf`
    *   `model.cherry_data_model.practice_info_full_xf`
    *   `model.cherry_data_model.src_gsheets_retention_phase_ins`
    *   `model.cherry_data_model.src_gsheets_retention_targets`

---
