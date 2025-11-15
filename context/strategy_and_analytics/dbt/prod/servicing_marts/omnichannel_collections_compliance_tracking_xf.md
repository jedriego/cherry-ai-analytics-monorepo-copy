## Model: `omnichannel_collections_compliance_tracking_xf`

`omnichannel_collections_compliance_tracking_xf`

*   **Unique ID:** `model.cherry_data_model.omnichannel_collections_compliance_tracking_xf`
*   **FQN:** `prod.servicing_marts.omnichannel_collections_compliance_tracking_xf`
*   **Description:** (No description provided)
*   **Tags:** `['servicing_and_collections']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CONTACT_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `MEDIA_TYPE_NAME` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `BORROWER_ID` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `PHONE_NUMBER` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `EMAIL_ADDRESS` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `DIAL_METHOD` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `CONTACT_START_PT` | 7 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `DAY` | 8 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `DPD_OF_LATEST_LOAN` | 9 | `NUMBER` |  |  | `[]` | `{}` |
    | `LOAN_LIST` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `FRAUD_LOAN_LIST` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `DPD_BUCKET` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `BORROWER_CITY` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `BORROWER_STATE` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `BORROWER_TIMEZONE` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `BORROWER_ZIPCODE` | 16 | `NUMBER` |  |  | `[]` | `{}` |
    | `IS_NYC_ZIPCODE` | 17 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `MESSAGE_TITLE` | 18 | `TEXT` |  |  | `[]` | `{}` |
    | `MESSAGE_TEXT` | 19 | `TEXT` |  |  | `[]` | `{}` |
    | `DNC_FLAG_EFFECTIVE_DATE` | 20 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `START_FRAUD` | 21 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `END_FRAUD` | 22 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `START_BANKRUPTCY` | 23 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `END_BANKRUPTCY` | 24 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `DEBT_SOLD_DATE` | 25 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `FORBEARANCE_START_DATE` | 26 | `DATE` |  |  | `[]` | `{}` |
    | `FORBEARANCE_END_DATE` | 27 | `DATE` |  |  | `[]` | `{}` |
    | `FORBEARANCE_CREATE_DATE` | 28 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `LAST_RPC_TIMESTAMP` | 29 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `PHONE_UNSUBSCRIBED_AT_PT` | 30 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `EMAIL_UNSUBSCRIBED_AT_PT` | 31 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `WAS_DO_NOT_CALL_ACTIVE` | 32 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `WAS_CEASE_AND_DESIST_ACTIVE` | 33 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `WAS_DECEASED_ACTIVE` | 34 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `WAS_WRONG_NUMBER_ACTIVE` | 35 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `WAS_LEGAL_ACTION_ACTIVE` | 36 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `WAS_FRAUD_AT_TIME_OF_CONTACT` | 37 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `WAS_BANKRUPTCY_AT_TIME_OF_CONTACT` | 38 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `WAS_DEBT_SOLD_AT_TIME_OF_CONTACT` | 39 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_IN_FORBEARANCE` | 40 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_SMS_UNSUBSCRIBED` | 41 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_EMAIL_UNSUBSCRIBED` | 42 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_RISC_VOICEMAIL_VIOLATION` | 43 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_TCPA_VIOLATED` | 44 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `HAD_RPC_WITHIN_7_DAYS` | 45 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_NON_COMPLIANT_VOICEMAIL` | 46 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NON_COMPLIANT_CA_MD_MN_SD_7DAY_LIMIT` | 47 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NON_COMPLIANT_SC_7DAY_LIMIT` | 48 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NON_COMPLIANT_SC_DAILY_CHANNEL_LIMIT` | 49 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NON_COMPLIANT_DC_LIMITS` | 50 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NON_COMPLIANT_MA_DAILY_LIMIT` | 51 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NON_COMPLIANT_NYC_7DAY_LIMIT` | 52 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NON_COMPLIANT_WV_LIMITS` | 53 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NON_COMPLIANT_CA_HOURS` | 54 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NON_COMPLIANT_IN_HOURS` | 55 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NON_COMPLIANT_OK_HOURS` | 56 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NON_COMPLIANT_SC_HOURS` | 57 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NON_COMPLIANT_MS_HOURS` | 58 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NON_COMPLIANT_NE_HOURS` | 59 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NON_COMPLIANT_TX_HOURS` | 60 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NON_COMPLIANT_TN_HOURS` | 61 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_SUNDAY_CALL_VIOLATION` | 62 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_HOLIDAY_CALL_VIOLATION` | 63 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `CALL_VOICEMAIL_COUNT_7_DAYS` | 64 | `NUMBER` |  |  | `[]` | `{}` |
    | `TOTAL_CONTACT_COUNT_7_DAYS` | 65 | `NUMBER` |  |  | `[]` | `{}` |
    | `TOTAL_CONTACT_COUNT_TODAY` | 66 | `NUMBER` |  |  | `[]` | `{}` |
    | `CALL_SMS_CONTACT_COUNT_TODAY` | 67 | `NUMBER` |  |  | `[]` | `{}` |
    | `SMS_COUNT_7_DAYS` | 68 | `NUMBER` |  |  | `[]` | `{}` |
    | `VOICEMAIL_COUNT_TODAY` | 69 | `NUMBER` |  |  | `[]` | `{}` |
    | `SMS_COUNT_TODAY` | 70 | `NUMBER` |  |  | `[]` | `{}` |
    | `EMAIL_COUNT_TODAY` | 71 | `NUMBER` |  |  | `[]` | `{}` |
    | `IS_COMPLIANT` | 72 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `COMPLIANCE_REASONS_AGG` | 73 | `TEXT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.cherry_data_model.convert_to_pt`
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.int_borrower_timezones`
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.int_nice_inbounds_contact_information_joined`
    *   `model.cherry_data_model.int_nice_outbounds_contact_information_joined`
    *   `model.cherry_data_model.omnichannel_collections_outbounds_xf`
    *   `model.cherry_data_model.src_borrower_flags_aud`
    *   `model.cherry_data_model.src_borrower_old_risc_features`
    *   `model.cherry_data_model.src_borrower_revinfo`
    *   `model.cherry_data_model.src_debt_sale_transactions`
    *   `model.cherry_data_model.src_due_date_changes`
    *   `model.cherry_data_model.src_loan_plan_status_history`
    *   `model.cherry_data_model.src_loan_plans`
    *   `model.cherry_data_model.src_loans_audit`
    *   `model.cherry_data_model.stg_forbearances`
    *   `model.cherry_data_model.unsubscribed_borrowers_xf`
    *   `model.cherry_data_model.zendesk_collections_and_recoveries_eligible_tickets_xf`

---
