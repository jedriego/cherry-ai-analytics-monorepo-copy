## Model: `statsig_daily_import`

`statsig_daily_import`

*   **Unique ID:** `model.cherry_data_model.statsig_daily_import`
*   **FQN:** `prod.statsig.statsig_daily_import`
*   **Description:** Daily Statsig-compatible metrics at two grains (borrowerId and organizationId). The model normalizes multiple upstream event sources into a single wide-ish fact table with (dateid, id_type, unit_id, metric_name, metric_value, numerator, denominator). It is incremental with a configurable lookback window (var('inc_lookback_days', 2)) so late-arriving data can be re-merged. Timezone normalization uses PT for certain events and UTC for others (see SQL for convert_timezone details).

*   **Tags:** `['statsig', 'daily']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `UNIT_ID` | 1 | `NUMBER` | Identifier of the unit for the given id_type (borrower_id or organization_id). | Identifier of the unit for the given id_type (borrower_id or organization_id). | `[]` | `{}` |
    | `ID_TYPE` | 2 | `TEXT` | Type of unit identifier. One of: 'borrowerId', 'organizationId'. | Type of unit identifier. One of: 'borrowerId', 'organizationId'. | `[]` | `{}` |
    | `DATEID` | 3 | `DATE` | Event date (day) in PT/UTC as normalized in the CTEs as GMT-8; primary date key. | Event date (day) in PT/UTC as normalized in the CTEs as GMT-8; primary date key. | `[]` | `{}` |
    | `METRIC_NAME` | 4 | `TEXT` | The metric captured for the (dateid, id_type, unit_id) tuple. Possible values include: gross_volume, num_application_starts, num_application_completions, num_approvals, num_checkout_starts, num_checkout_completions, num_app_funded,  median_application_time_to_complete_sec, median_checkout_time_to_complete, and various dollar collection/recovery metrics.
 | The metric captured for the (dateid, id_type, unit_id) tuple. Possible values include: gross_volume, num_application_starts, num_application_completions, num_approvals, num_checkout_starts, num_checkout_completions, num_app_funded,  median_application_time_to_complete_sec, median_checkout_time_to_complete, and various dollar collection/recovery metrics.
 | `[]` | `{}` |
    | `METRIC_VALUE` | 5 | `FLOAT` | Numeric value of the metric_name for the tuple; DOUBLE. | Numeric value of the metric_name for the tuple; DOUBLE. | `[]` | `{}` |
    | `NUMERATOR` | 6 | `FLOAT` | Optional numerator used for ratio metrics (NULL for count/sum metrics). | Optional numerator used for ratio metrics (NULL for count/sum metrics). | `[]` | `{}` |
    | `DENOMINATOR` | 7 | `FLOAT` | Optional denominator used for ratio metrics (NULL for count/sum metrics). | Optional denominator used for ratio metrics (NULL for count/sum metrics). | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.is_incremental`
    *   `model.cherry_data_model.applications_loans_xf`
    *   `model.cherry_data_model.loan_info_xf`
    *   `model.cherry_data_model.merchant_account_mapping`
    *   `model.cherry_data_model.sendgrid_event_details`
    *   `model.cherry_data_model.src_loan_offers`
    *   `model.cherry_data_model.stg_cherry_loan_ids`
    *   `model.cherry_data_model.stg_payment_tape`
    *   `model.cherry_data_model.stg_sms_notifications`
    *   `model.cherry_data_model.stg_zendesk_tickets`
    *   `source.cherry_data_model.segment_prod.patient_portal_sign_ins`

---
