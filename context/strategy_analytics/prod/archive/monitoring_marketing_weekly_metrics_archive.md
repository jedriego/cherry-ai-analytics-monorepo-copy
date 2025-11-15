## Model: `monitoring_marketing_weekly_metrics_archive`

`monitoring_marketing_weekly_metrics_archive`

*   **Unique ID:** `model.cherry_data_model.monitoring_marketing_weekly_metrics_archive`
*   **FQN:** `prod.archive.monitoring_marketing_weekly_metrics_archive`
*   **Description:** This model tracks key Marketing metrics and alerts if performance is outside normal ranges.

*   **Tags:** `['archive', 'marketing', 'metrics', 'anomalies', 'tracking', 'alerts']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `DATE_WEEK` | 1 | `DATE` | Aggregates metrics per week | Aggregates metrics per week | `[]` | `{}` |
    | `WEEKS_AGO` | 2 | `NUMBER` |  |  | `[]` | `{}` |
    | `LEADS_CREATED` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `LEADS_CREATED_10TH_PERCENTILE` | 4 | `FLOAT` |  |  | `[]` | `{}` |
    | `LEADS_CREATED_90TH_PERCENTILE` | 5 | `FLOAT` |  |  | `[]` | `{}` |
    | `FLAG_LOW_LEADS_CREATED` | 6 | `BOOLEAN` | Volume of leads created is below our lower bound | Volume of leads created is below our lower bound | `[]` | `{}` |
    | `FLAG_HIGH_LEADS_CREATED` | 7 | `BOOLEAN` | Volume of leads created is above our upper bound | Volume of leads created is above our upper bound | `[]` | `{}` |
    | `LEADS_BOOKED_DEMO_RATE` | 8 | `NUMBER` |  |  | `[]` | `{}` |
    | `LEADS_BOOKED_DEMO_RATE_10TH_PERCENTILE` | 9 | `FLOAT` |  |  | `[]` | `{}` |
    | `LEADS_BOOKED_DEMO_RATE_95TH_PERCENTILE` | 10 | `FLOAT` |  |  | `[]` | `{}` |
    | `FLAG_LOW_LEADS_BOOKED_DEMO_RATE` | 11 | `BOOLEAN` | Rate of leads booking demos is below our lower bound | Rate of leads booking demos is below our lower bound | `[]` | `{}` |
    | `FLAG_HIGH_LEADS_BOOKED_DEMO_RATE` | 12 | `BOOLEAN` | Rate of leads booking demos is above our upper bound | Rate of leads booking demos is above our upper bound | `[]` | `{}` |
    | `REFERRALS_CREATED` | 13 | `NUMBER` |  |  | `[]` | `{}` |
    | `REFERRALS_CREATED_10TH_PERCENTILE` | 14 | `FLOAT` |  |  | `[]` | `{}` |
    | `REFERRALS_CREATED_95TH_PERCENTILE` | 15 | `FLOAT` |  |  | `[]` | `{}` |
    | `FLAG_LOW_REFERRALS_CREATED` | 16 | `BOOLEAN` | Volume of referrals created is below our lower bound | Volume of referrals created is below our lower bound | `[]` | `{}` |
    | `FLAG_HIGH_REFERRALS_CREATED` | 17 | `BOOLEAN` | Volume of referrals created is above our upper bound | Volume of referrals created is above our upper bound | `[]` | `{}` |
    | `DEMOS_CREATED` | 18 | `NUMBER` |  |  | `[]` | `{}` |
    | `DEMOS_CREATED_10TH_PERCENTILE` | 19 | `FLOAT` |  |  | `[]` | `{}` |
    | `DEMOS_CREATED_95TH_PERCENTILE` | 20 | `FLOAT` |  |  | `[]` | `{}` |
    | `FLAG_LOW_DEMOS_CREATED` | 21 | `BOOLEAN` | Volume of demos created is below our lower bound | Volume of demos created is below our lower bound | `[]` | `{}` |
    | `FLAG_HIGH_DEMOS_CREATED` | 22 | `BOOLEAN` | Volume of leads created is above our upper bound | Volume of leads created is above our upper bound | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.lead_details_xf`
    *   `model.cherry_data_model.referral_details_xf`
    *   `model.cherry_data_model.stg_demos`

---
