## Model: `pivot_outbound_genesys_xf_archive`

`pivot_outbound_genesys_xf_archive`

*   **Unique ID:** `model.cherry_data_model.pivot_outbound_genesys_xf_archive`
*   **FQN:** `prod.archive.pivot_outbound_genesys_xf_archive`
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
    | `MEDIA_TYPE` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `GENESYS_USER_NAME` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `GENESYS_USER_TEAM` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `QUEUE_NAME` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `CHERRY_PHONE` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `EXTERNAL_PHONE` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `CHERRY_EMAIL` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `EXTERNAL_EMAIL` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERACTION_CUSTOMER_ID` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERACTION_CUSTOMER_NAME` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_ONE_TYPE` | 16 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_ONE_DISCONNECT_TYPE` | 17 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_TWO_TYPE` | 18 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_TWO_DISCONNECT_TYPE` | 19 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_THREE_TYPE` | 20 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_THREE_DISCONNECT_TYPE` | 21 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_FOUR_TYPE` | 22 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_FOUR_DISCONNECT_TYPE` | 23 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_FIVE_TYPE` | 24 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_FIVE_DISCONNECT_TYPE` | 25 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_SIX_TYPE` | 26 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_SIX_DISCONNECT_TYPE` | 27 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_SEVEN_TYPE` | 28 | `TEXT` |  |  | `[]` | `{}` |
    | `SEGMENT_SEVEN_DISCONNECT_TYPE` | 29 | `TEXT` |  |  | `[]` | `{}` |
    | `WRAP_UP_SEGMENT_TYPE` | 30 | `TEXT` |  |  | `[]` | `{}` |
    | `WRAP_UP_SEGMENT_DISCONNECT_TYPE` | 31 | `TEXT` |  |  | `[]` | `{}` |
    | `FINAL_SEGMENT_TYPE` | 32 | `TEXT` |  |  | `[]` | `{}` |
    | `WRAP_UP_CODE_ID` | 33 | `TEXT` |  |  | `[]` | `{}` |
    | `WRAP_UP_CODE_NAME` | 34 | `TEXT` |  |  | `[]` | `{}` |
    | `WRAP_UP_CODE_GROUP` | 35 | `TEXT` |  |  | `[]` | `{}` |
    | `RIGHT_PARTY_CONTACT` | 36 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `CONVERSION` | 37 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_CONTACT` | 38 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `CONTACT_TYPE` | 39 | `TEXT` |  |  | `[]` | `{}` |
    | `TACD` | 40 | `NUMBER` |  |  | `[]` | `{}` |
    | `TALERT` | 41 | `NUMBER` |  |  | `[]` | `{}` |
    | `TSHORTABANDON` | 42 | `NUMBER` |  |  | `[]` | `{}` |
    | `TABANDON` | 43 | `NUMBER` |  |  | `[]` | `{}` |
    | `TANSWERED` | 44 | `NUMBER` |  |  | `[]` | `{}` |
    | `TNOTRESPONDING` | 45 | `NUMBER` |  |  | `[]` | `{}` |
    | `TTALKCOMPLETE` | 46 | `NUMBER` |  |  | `[]` | `{}` |
    | `TACW` | 47 | `NUMBER` |  |  | `[]` | `{}` |
    | `TAGENTRESPONSETIME` | 48 | `NUMBER` |  |  | `[]` | `{}` |
    | `THANDLE` | 49 | `NUMBER` |  |  | `[]` | `{}` |
    | `NOVERSLA` | 50 | `NUMBER` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.int_outbound_genesys`

---
