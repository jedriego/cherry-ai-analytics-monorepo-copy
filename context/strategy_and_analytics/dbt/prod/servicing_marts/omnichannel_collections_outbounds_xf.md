## Model: `omnichannel_collections_outbounds_xf`

`omnichannel_collections_outbounds_xf`

*   **Unique ID:** `model.cherry_data_model.omnichannel_collections_outbounds_xf`
*   **FQN:** `prod.servicing_marts.omnichannel_collections_outbounds_xf`
*   **Description:** (No description provided)
*   **Tags:** `['servicing_and_collections', 'collections_hourly']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CONTACT_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `MEDIA_TYPE_NAME` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `BORROWER_ID` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `DPD_OF_LATEST_LOAN` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `LOAN_LIST` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `DPD_BUCKET` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `PHONE_NUMBER` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `EMAIL_ADDRESS` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `DIAL_METHOD` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `CONTACT_START_PT` | 10 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `DAY` | 11 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `MESSAGE_TITLE` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `MESSAGE_TEXT` | 13 | `TEXT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.collections_outbound_emails`
    *   `model.cherry_data_model.collections_outbound_sms_messages`
    *   `model.cherry_data_model.collections_outbound_voicemails`
    *   `model.cherry_data_model.collections_safe_select_dials_archive`
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.nice_collections_dials_xf_archive`
    *   `model.cherry_data_model.stg_tcn_dials`

---
