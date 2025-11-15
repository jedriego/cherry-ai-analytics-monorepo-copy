## Model: `collections_voice_interactions_xf_archive`

`collections_voice_interactions_xf_archive`

*   **Unique ID:** `model.cherry_data_model.collections_voice_interactions_xf_archive`
*   **FQN:** `prod.archive.collections_voice_interactions_xf_archive`
*   **Description:** (No description provided)
*   **Tags:** `['archive', 'genesys']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CONVERSATION_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `CONVERSATION_START` | 2 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `CONVERSATION_END` | 3 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `CONVERSATION_LENGTH` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `ORIGINATING_DIRECTION` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `GENESYS_USER_NAME` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `QUEUE_NAME` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `CHERRY_PHONE` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `EXTERNAL_PHONE` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_ONE_TYPE` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_ONE_DISCONNECT_TYPE` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_TWO_TYPE` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_TWO_DISCONNECT_TYPE` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_THREE_TYPE` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_THREE_DISCONNECT_TYPE` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_FOUR_TYPE` | 16 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_FOUR_DISCONNECT_TYPE` | 17 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_FIVE_TYPE` | 18 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_FIVE_DISCONNECT_TYPE` | 19 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_SIX_TYPE` | 20 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_SIX_DISCONNECT_TYPE` | 21 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_SEVEN_TYPE` | 22 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_SEVEN_DISCONNECT_TYPE` | 23 | `TEXT` |  |  | `[]` | `{}` |
    | `WRAP_UP_SEGMENT_TYPE` | 24 | `TEXT` |  |  | `[]` | `{}` |
    | `WRAP_UP_SEGMENT_DISCONNECT_TYPE` | 25 | `TEXT` |  |  | `[]` | `{}` |
    | `FINAL_SEGMENT_TYPE` | 26 | `TEXT` |  |  | `[]` | `{}` |
    | `WRAP_UP_CODE_ID` | 27 | `TEXT` |  |  | `[]` | `{}` |
    | `WRAP_UP_CODE_NAME` | 28 | `TEXT` |  |  | `[]` | `{}` |
    | `RIGHT_PARTY_CONTACT` | 29 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `CONVERSION` | 30 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `TACD` | 31 | `NUMBER` |  |  | `[]` | `{}` |
    | `TALERT` | 32 | `NUMBER` |  |  | `[]` | `{}` |
    | `TSHORTABANDON` | 33 | `NUMBER` |  |  | `[]` | `{}` |
    | `TABANDON` | 34 | `NUMBER` |  |  | `[]` | `{}` |
    | `TANSWERED` | 35 | `NUMBER` |  |  | `[]` | `{}` |
    | `TNOTRESPONDING` | 36 | `NUMBER` |  |  | `[]` | `{}` |
    | `TTALKCOMPLETE` | 37 | `NUMBER` |  |  | `[]` | `{}` |
    | `TACW` | 38 | `NUMBER` |  |  | `[]` | `{}` |
    | `TAGENTRESPONSETIME` | 39 | `NUMBER` |  |  | `[]` | `{}` |
    | `THANDLE` | 40 | `NUMBER` |  |  | `[]` | `{}` |
    | `LOAN_ID` | 41 | `NUMBER` |  |  | `[]` | `{}` |
    | `CONTRACT_ID` | 42 | `TEXT` |  |  | `[]` | `{}` |
    | `TIMEZONE` | 43 | `TEXT` |  |  | `[]` | `{}` |
    | `DPD_BEFORE_PMT` | 44 | `NUMBER` |  |  | `[]` | `{}` |
    | `DPD_AFTER_PMT` | 45 | `NUMBER` |  |  | `[]` | `{}` |
    | `IN_OPERATING_HOURS` | 46 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `MAX_DAILY_DPD` | 47 | `NUMBER` |  |  | `[]` | `{}` |
    | `PAYMENT_AMOUNT_ON_DATE` | 48 | `NUMBER` |  |  | `[]` | `{}` |
    | `CALL_LOCAL_TIME` | 49 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.borrowers_merged_emails_xf`
    *   `model.cherry_data_model.pivot_inbound_genesys_voice`
    *   `model.cherry_data_model.pivot_outbound_genesys_voice`
    *   `model.cherry_data_model.stg_borrower_addresses_with_tz`
    *   `model.cherry_data_model.stg_loan_history_and_dq_payments_merged`

---
