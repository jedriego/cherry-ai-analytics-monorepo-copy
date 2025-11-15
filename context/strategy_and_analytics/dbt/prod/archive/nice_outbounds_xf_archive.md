## Model: `nice_outbounds_xf_archive`

`nice_outbounds_xf_archive`

*   **Unique ID:** `model.cherry_data_model.nice_outbounds_xf_archive`
*   **FQN:** `prod.archive.nice_outbounds_xf_archive`
*   **Description:** (No description provided)
*   **Tags:** `['archive']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CONTACT_ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `CONTACT_START_PT` | 2 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `CONTACT_END_PT` | 3 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `CONTACT_LENGTH` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `DIRECTION` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `MEDIA_TYPE_NAME` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `INITIAL_AGENT_NAME` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `INITIAL_SKILL_NAME` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `INITIAL_TEAM_NAME` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `FINAL_AGENT_NAME` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `FINAL_SKILL_NAME` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `FINAL_TEAM_NAME` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `NUM_SEGMENTS` | 13 | `NUMBER` |  |  | `[]` | `{}` |
    | `END_REASON` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `DISPOSITION_NAME` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_RIGHT_PARTY_CONTACT` | 16 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_CONVERSION` | 17 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_CONTACT` | 18 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ELIGIBLE_FOR_CSAT_SURVEY` | 19 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `SECONDARY_DISPOSITION_NAME` | 20 | `TEXT` |  |  | `[]` | `{}` |
    | `DISPOSITION_NOTES` | 21 | `TEXT` |  |  | `[]` | `{}` |
    | `TAG_NAME` | 22 | `TEXT` |  |  | `[]` | `{}` |
    | `SERVICE_LEVEL_CATEGORY` | 23 | `TEXT` |  |  | `[]` | `{}` |
    | `OWNING_TEAM` | 24 | `TEXT` |  |  | `[]` | `{}` |
    | `INITIAL_AGENT_PHONE` | 25 | `TEXT` |  |  | `[]` | `{}` |
    | `FINAL_AGENT_PHONE` | 26 | `TEXT` |  |  | `[]` | `{}` |
    | `FROM_ADDRESS` | 27 | `TEXT` |  |  | `[]` | `{}` |
    | `TO_ADDRESS` | 28 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERACTION_PHONE_NUMBER` | 29 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERACTION_IP_ADDRESS` | 30 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERACTION_EMAIL` | 31 | `TEXT` |  |  | `[]` | `{}` |
    | `CAMPAIGN_ID` | 32 | `NUMBER` |  |  | `[]` | `{}` |
    | `MASTER_CONTACT_ID` | 33 | `NUMBER` |  |  | `[]` | `{}` |
    | `POINT_OF_CONTACT_ID` | 34 | `NUMBER` |  |  | `[]` | `{}` |
    | `POINT_OF_CONTACT_NAME` | 35 | `TEXT` |  |  | `[]` | `{}` |
    | `WAS_ABANDONED` | 36 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `WAS_SHORT_ABANDON` | 37 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `WAS_REFUSED` | 38 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `REFUSE_REASON` | 39 | `TEXT` |  |  | `[]` | `{}` |
    | `REFUSE_TIME_PT` | 40 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `WAS_TAKEOVER` | 41 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `T_ABANDON` | 42 | `NUMBER` |  |  | `[]` | `{}` |
    | `T_ACW` | 43 | `NUMBER` |  |  | `[]` | `{}` |
    | `T_HANDLE` | 44 | `NUMBER` |  |  | `[]` | `{}` |
    | `T_WAITING_FOR_CALLBACK` | 45 | `NUMBER` |  |  | `[]` | `{}` |
    | `T_CONFERENCE` | 46 | `NUMBER` |  |  | `[]` | `{}` |
    | `T_HOLD` | 47 | `NUMBER` |  |  | `[]` | `{}` |
    | `T_PRE_QUEUE` | 48 | `NUMBER` |  |  | `[]` | `{}` |
    | `T_IN_QUEUE` | 49 | `NUMBER` |  |  | `[]` | `{}` |
    | `T_POST_QUEUE` | 50 | `NUMBER` |  |  | `[]` | `{}` |
    | `T_RELEASE` | 51 | `NUMBER` |  |  | `[]` | `{}` |
    | `T_ROUTING` | 52 | `NUMBER` |  |  | `[]` | `{}` |
    | `SERVICE_LEVEL_FLAG` | 53 | `NUMBER` |  |  | `[]` | `{}` |
    | `TRANSFER_INDICATOR_NAME` | 54 | `TEXT` |  |  | `[]` | `{}` |
    | `HOLD_COUNT` | 55 | `NUMBER` |  |  | `[]` | `{}` |
    | `LAST_UPDATED_PT` | 56 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.stg_nice_contacts`

---
