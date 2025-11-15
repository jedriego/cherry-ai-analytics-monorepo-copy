## Model: `monitoring_marketing_daily_metrics_archive`

`monitoring_marketing_daily_metrics_archive`

*   **Unique ID:** `model.cherry_data_model.monitoring_marketing_daily_metrics_archive`
*   **FQN:** `prod.archive.monitoring_marketing_daily_metrics_archive`
*   **Description:** This model tracks key Marketing metrics and alerts if performance is outside normal ranges.

*   **Tags:** `['archive', 'marketing', 'metrics', 'anomalies', 'tracking', 'alerts']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `DATE_DAY` | 1 | `DATE` | Aggregates metrics per day | Aggregates metrics per day | `[]` | `{}` |
    | `DAY_NAME` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `DAYS_AGO` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `LEADS_CREATED` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `LEADS_CREATED_10TH_PERCENTILE` | 5 | `FLOAT` |  |  | `[]` | `{}` |
    | `LEADS_CREATED_95TH_PERCENTILE` | 6 | `FLOAT` |  |  | `[]` | `{}` |
    | `FLAG_LOW_LEADS_CREATED` | 7 | `BOOLEAN` | Volume of leads created is below our lower bound | Volume of leads created is below our lower bound | `[]` | `{}` |
    | `FLAG_HIGH_LEADS_CREATED` | 8 | `BOOLEAN` | Volume of leads created is above our upper bound | Volume of leads created is above our upper bound | `[]` | `{}` |
    | `LEADS_BOOKED_DEMO_RATE` | 9 | `NUMBER` |  |  | `[]` | `{}` |
    | `LEADS_BOOKED_DEMO_RATE_10TH_PERCENTILE` | 10 | `FLOAT` |  |  | `[]` | `{}` |
    | `LEADS_BOOKED_DEMO_RATE_95TH_PERCENTILE` | 11 | `FLOAT` |  |  | `[]` | `{}` |
    | `FLAG_LOW_LEADS_BOOKED_DEMO_RATE` | 12 | `BOOLEAN` | Rate of leads booking demos is below our lower bound | Rate of leads booking demos is below our lower bound | `[]` | `{}` |
    | `FLAG_HIGH_LEADS_BOOKED_DEMO_RATE` | 13 | `BOOLEAN` | Rate of leads booking demos is above our upper bound | Rate of leads booking demos is above our upper bound | `[]` | `{}` |
    | `LEADS_MISSING_INDUSTRY_RATE` | 14 | `NUMBER` |  |  | `[]` | `{}` |
    | `LEADS_MISSING_INDUSTRY_RATE_98TH_PERCENTILE` | 15 | `FLOAT` |  |  | `[]` | `{}` |
    | `FLAG_HIGH_LEADS_MISSING_INDUSTRY_RATE` | 16 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `REFERRALS_CREATED` | 17 | `NUMBER` |  |  | `[]` | `{}` |
    | `REFERRALS_CREATED_10TH_PERCENTILE` | 18 | `FLOAT` |  |  | `[]` | `{}` |
    | `REFERRALS_CREATED_95TH_PERCENTILE` | 19 | `FLOAT` |  |  | `[]` | `{}` |
    | `FLAG_LOW_REFERRALS_CREATED` | 20 | `BOOLEAN` | Volume of referrals created is below our lower bound | Volume of referrals created is below our lower bound | `[]` | `{}` |
    | `FLAG_HIGH_REFERRALS_CREATED` | 21 | `BOOLEAN` | Volume of referrals created is above our upper bound | Volume of referrals created is above our upper bound | `[]` | `{}` |
    | `DEMOS_CREATED` | 22 | `NUMBER` |  |  | `[]` | `{}` |
    | `DEMOS_CREATED_10TH_PERCENTILE` | 23 | `FLOAT` |  |  | `[]` | `{}` |
    | `DEMOS_CREATED_95TH_PERCENTILE` | 24 | `FLOAT` |  |  | `[]` | `{}` |
    | `FLAG_LOW_DEMOS_CREATED` | 25 | `BOOLEAN` | Volume of demos created is below our lower bound | Volume of demos created is below our lower bound | `[]` | `{}` |
    | `FLAG_HIGH_DEMOS_CREATED` | 26 | `BOOLEAN` | Volume of leads created is above our upper bound | Volume of leads created is above our upper bound | `[]` | `{}` |
    | `PARTIAL_SUBMISSION_RATE` | 27 | `NUMBER` |  |  | `[]` | `{}` |
    | `PARTIAL_SUBMISSION_RATE_98TH_PERCENTILE` | 28 | `FLOAT` |  |  | `[]` | `{}` |
    | `FLAG_HIGH_PARTIAL_SUBMISSIONS_RATE` | 29 | `BOOLEAN` | The rate of partial forms submissions is above our upper bound | The rate of partial forms submissions is above our upper bound | `[]` | `{}` |
    | `FORMS_MISSING_EMAIL_RATE` | 30 | `NUMBER` |  |  | `[]` | `{}` |
    | `FORMS_MISSING_EMAIL_RATE_98TH_PERCENTILE` | 31 | `FLOAT` |  |  | `[]` | `{}` |
    | `FLAG_HIGH_FORMS_MISSING_EMAIL_RATE` | 32 | `BOOLEAN` | The rate of form submissions missing email values is above our upper bound | The rate of form submissions missing email values is above our upper bound | `[]` | `{}` |
    | `FORMS_MISSING_INDUSTRY_RATE` | 33 | `NUMBER` |  |  | `[]` | `{}` |
    | `FORMS_MISSING_INDUSTRY_RATE_98TH_PERCENTILE` | 34 | `FLOAT` |  |  | `[]` | `{}` |
    | `FLAG_HIGH_FORMS_MISSING_INDUSTRY_RATE` | 35 | `BOOLEAN` | The rate of form submissions missing industry values is above our upper bound | The rate of form submissions missing industry values is above our upper bound | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.lead_details_xf`
    *   `model.cherry_data_model.referral_details_xf`
    *   `model.cherry_data_model.stg_demos`
    *   `model.cherry_data_model.stg_paperform_submissions`

---
