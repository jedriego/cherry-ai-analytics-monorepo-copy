## Model: `prospect_engagement_xf_archive`

`prospect_engagement_xf_archive`

*   **Unique ID:** `model.cherry_data_model.prospect_engagement_xf_archive`
*   **FQN:** `prod.archive.prospect_engagement_xf_archive`
*   **Description:** (No description provided)
*   **Tags:** `['archive']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `LEAD_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `LEAD_CREATED_DATETIME_PT` | 2 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `DEMO_CREATED_DATETIME_PT` | 3 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `TIMESTAMP_PT` | 4 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `SESSION_START` | 5 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `SESSION_ORDER` | 6 | `NUMBER` |  |  | `[]` | `{}` |
    | `SESSION_RECENCY` | 7 | `NUMBER` |  |  | `[]` | `{}` |
    | `LEAD_ENGAGEMENT_ORDER` | 8 | `NUMBER` |  |  | `[]` | `{}` |
    | `LEAD_ENGAGEMENT_RECENCY` | 9 | `NUMBER` |  |  | `[]` | `{}` |
    | `LEAD_SESSION_ENGAGEMENT_ORDER` | 10 | `NUMBER` |  |  | `[]` | `{}` |
    | `LEAD_SESSION_ENGAGEMENT_RECENCY` | 11 | `NUMBER` |  |  | `[]` | `{}` |
    | `ENGAGEMENT_CATEGORY` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `ENGAGEMENT_TYPE` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `ENGAGEMENT_DETAIL` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `ENGAGEMENT_ID` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `ENGAGEMENT_CHANNEL` | 16 | `TEXT` |  |  | `[]` | `{}` |
    | `ENGAGEMENT_CHANNEL_EVALUATION` | 17 | `TEXT` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.prospect_engagement`

---
