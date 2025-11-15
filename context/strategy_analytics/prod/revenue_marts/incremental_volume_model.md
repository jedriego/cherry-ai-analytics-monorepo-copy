## Model: `incremental_volume_model`

`incremental_volume_model`

*   **Unique ID:** `model.cherry_data_model.incremental_volume_model`
*   **FQN:** `prod.revenue_marts.incremental_volume_model`
*   **Description:** **Predictive Analytics Model for Retention Intervention Impact**
This model leverages machine learning regression analysis to predict the incremental volume impact  of various retention interventions on practice performance. It combines practice characteristics,  health assessment data, and historical volume patterns to generate data-driven predictions for  retention strategy optimization.
**Key Business Logic:** - Segments practices into "aesthetics" (MedSpa, Plastic and Cosmetic Surgery, Other) and "dental" cohorts - Calculates 7-day health score trends and categorizes practices across multiple performance dimensions - Applies industry-specific regression models with hardcoded coefficients derived from historical analysis - Generates predictions for multiple intervention types: PDM visits, test group participation, and CSM interactions - Includes both original (v1) and refined (v2) model versions for enhanced accuracy
**Intervention Types Modeled:** - **PDM Visit Impact**: Expected volume increase from Practice Development Manager on-site visits - **Test Group Impact**: Expected volume increase from participation in retention test programs - **CSM Interaction Impact**: Expected volume increase from Customer Success Manager interactions - **Version 2 Models**: Refined predictions incorporating additional practice history variables
**Model Segmentation:** - **Aesthetics Practices**: MedSpa, Plastic and Cosmetic Surgery, Other (separate regression coefficients) - **Dental Practices**: Unified regression model with dental-specific thresholds and variables - **Practice Maturity Filter**: Excludes practices with <30 days post go-live for model stability
**Data Sources:** - `practice_info_xf`: Practice characteristics, volume history, and retention ownership - `daily_health_scores`: Partnership health scores and assessment trends from risk intelligence - Multiple regression models trained on historical intervention outcomes
**Use Cases:** - Prioritizing retention interventions based on predicted ROI - Resource allocation for PDM visits and CSM interactions - A/B testing framework for retention strategy optimization - Performance forecasting for retention team planning
**Technical Notes:** - Uses dummy variable encoding for categorical predictors - Applies different regression formulas based on industry segment - Includes practice potential gap analysis and volume trend calculations - Filters to practices >30 days post go-live for model reliability

*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SF_ACCOUNT_ID` | 1 | `TEXT` | Salesforce account identifier for the practice. Primary key linking to CRM data and serving  as the unique identifier for practice-level predictions and intervention tracking.
 | Salesforce account identifier for the practice. Primary key linking to CRM data and serving  as the unique identifier for practice-level predictions and intervention tracking.
 | `[]` | `{}` |
    | `SF_ACCOUNT_NAME` | 2 | `TEXT` | Human-readable practice name from Salesforce. Used for reporting and identification purposes  in retention team dashboards and intervention planning workflows.
 | Human-readable practice name from Salesforce. Used for reporting and identification purposes  in retention team dashboards and intervention planning workflows.
 | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT` | 3 | `TEXT` | Department responsible for retention activities (e.g., "Customer Success", "Practice Development").  Used for segmenting predictions by organizational structure and resource allocation planning.
 | Department responsible for retention activities (e.g., "Customer Success", "Practice Development").  Used for segmenting predictions by organizational structure and resource allocation planning.
 | `[]` | `{}` |
    | `RETENTION_OWNER` | 4 | `TEXT` | Individual retention specialist or manager assigned to the practice. Used for personal  accountability tracking and individual performance optimization in retention activities.
 | Individual retention specialist or manager assigned to the practice. Used for personal  accountability tracking and individual performance optimization in retention activities.
 | `[]` | `{}` |
    | `RETENTION_OWNER_TEAM` | 5 | `TEXT` | Specific team within the retention department managing the practice relationship. Enables  team-level performance analysis and workload distribution for intervention execution.
 | Specific team within the retention department managing the practice relationship. Enables  team-level performance analysis and workload distribution for intervention execution.
 | `[]` | `{}` |
    | `LATEST_HEALTH_ASSESSMENT` | 6 | `TEXT` | Most recent qualitative health assessment classification for the practice (e.g., "Healthy",  "At-Risk", "Optimal"). Provides business context for interpreting quantitative prediction  results and intervention prioritization.
 | Most recent qualitative health assessment classification for the practice (e.g., "Healthy",  "At-Risk", "Optimal"). Provides business context for interpreting quantitative prediction  results and intervention prioritization.
 | `[]` | `{}` |
    | `PRACTICE_LAST_30_GROSS_AMOUNT` | 7 | `FLOAT` | Total gross loan volume generated by the practice in the last 30 days. Key input variable  for regression models and baseline for measuring predicted incremental impact. Used as  recent performance indicator in volume trend analysis.
 | Total gross loan volume generated by the practice in the last 30 days. Key input variable  for regression models and baseline for measuring predicted incremental impact. Used as  recent performance indicator in volume trend analysis.
 | `[]` | `{}` |
    | `PRACTICE_LAST_90_GROSS_AMOUNT` | 8 | `FLOAT` | Total gross loan volume generated by the practice in the last 90 days. Extended performance  indicator used in v2 regression models to capture longer-term volume trends and seasonality  patterns for more accurate incremental volume predictions.
 | Total gross loan volume generated by the practice in the last 90 days. Extended performance  indicator used in v2 regression models to capture longer-term volume trends and seasonality  patterns for more accurate incremental volume predictions.
 | `[]` | `{}` |
    | `PDM_VISIT_IMPACT` | 9 | `FLOAT` | Predicted incremental monthly volume increase from a Practice Development Manager (PDM) on-site visit,  calculated using industry-specific regression models. Based on practice characteristics including  health scores, practice potential, and recent volume trends. Uses original regression coefficients  derived from historical intervention analysis.
 | Predicted incremental monthly volume increase from a Practice Development Manager (PDM) on-site visit,  calculated using industry-specific regression models. Based on practice characteristics including  health scores, practice potential, and recent volume trends. Uses original regression coefficients  derived from historical intervention analysis.
 | `[]` | `{}` |
    | `TEST_GROUP_IMPACT` | 10 | `FLOAT` | Predicted incremental monthly volume increase from participation in retention test group programs,  calculated using industry-specific regression models. Represents expected uplift from enhanced  retention strategies and interventions applied to test group participants. Uses original model  coefficients with practice-specific variables.
 | Predicted incremental monthly volume increase from participation in retention test group programs,  calculated using industry-specific regression models. Represents expected uplift from enhanced  retention strategies and interventions applied to test group participants. Uses original model  coefficients with practice-specific variables.
 | `[]` | `{}` |
    | `CSM_INTERACTION_IMPACT` | 11 | `FLOAT` | Predicted incremental monthly volume increase from Customer Success Manager (CSM) interactions  and engagement activities, calculated using industry-specific regression models. Reflects expected  impact of proactive customer success outreach and relationship management interventions.
 | Predicted incremental monthly volume increase from Customer Success Manager (CSM) interactions  and engagement activities, calculated using industry-specific regression models. Reflects expected  impact of proactive customer success outreach and relationship management interventions.
 | `[]` | `{}` |
    | `PDM_VISIT_IMPACT_V2` | 12 | `FLOAT` | Enhanced prediction of incremental monthly volume increase from PDM on-site visits using refined  regression models that incorporate additional practice history variables including 90-day volume  trends. Provides more accurate predictions by considering longer-term performance patterns and  seasonal adjustments.
 | Enhanced prediction of incremental monthly volume increase from PDM on-site visits using refined  regression models that incorporate additional practice history variables including 90-day volume  trends. Provides more accurate predictions by considering longer-term performance patterns and  seasonal adjustments.
 | `[]` | `{}` |
    | `TEST_GROUP_IMPACT_V2` | 13 | `FLOAT` | Enhanced prediction of incremental monthly volume increase from retention test group participation  using refined regression models. Incorporates additional practice characteristics and extended  volume history for improved accuracy in predicting intervention outcomes and ROI optimization.
 | Enhanced prediction of incremental monthly volume increase from retention test group participation  using refined regression models. Incorporates additional practice characteristics and extended  volume history for improved accuracy in predicting intervention outcomes and ROI optimization.
 | `[]` | `{}` |
    | `CSM_INTERACTION_IMPACT_V2` | 14 | `FLOAT` | Enhanced prediction of incremental monthly volume increase from CSM interactions using refined  regression models that incorporate extended practice history and additional performance variables.  Provides more nuanced predictions for customer success intervention planning and resource allocation. | Enhanced prediction of incremental monthly volume increase from CSM interactions using refined  regression models that incorporate extended practice history and additional performance variables.  Provides more nuanced predictions for customer success intervention planning and resource allocation. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.daily_health_scores`
    *   `model.cherry_data_model.practice_info_xf`

---
