## Model: `tagged_servicing_customer_satisfaction_responses_xf_archive`

`tagged_servicing_customer_satisfaction_responses_xf_archive`

*   **Unique ID:** `model.cherry_data_model.tagged_servicing_customer_satisfaction_responses_xf_archive`
*   **FQN:** `prod.archive.tagged_servicing_customer_satisfaction_responses_xf_archive`
*   **Description:** This model uses Delighted tag information left by a specialist to:
  1. update the specialist to whom that survey score is assigned
  2. update the score left by the survey recipient due to accidental misscoring

*   **Tags:** `['archive', 'customer_satisfaction', 'servicing', 'core_operating_results']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `PERSON_ID` | 1 | `NUMBER` |  | The unique ID associated with a Delighted person | `[]` | `{}` |
    | `PERSON_NAME` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `PERSON_EMAIL` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `PERSON_PHONE_COPY` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `SURVEY_TYPE` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `RESPONSE_ID` | 6 | `NUMBER` |  | The unique ID associated with a Delighted response | `[]` | `{}` |
    | `RESPONSE_SCORE` | 7 | `NUMBER` |  |  | `[]` | `{}` |
    | `CREATED_AT` | 8 | `TIMESTAMP_TZ` |  | The time at which the record was created in UTC | `[]` | `{}` |
    | `CREATED_AT_PT` | 9 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `SURVEY_CHANNEL` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERACTION_QUEUE` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERACTION_CHANNEL` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `SERVICING_TEAM_MEMBER` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `RESPONSE_COMMENT` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `FULL_TAGS` | 15 | `TEXT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.int_aggregated_servicing_satisfaction_responses`

---
