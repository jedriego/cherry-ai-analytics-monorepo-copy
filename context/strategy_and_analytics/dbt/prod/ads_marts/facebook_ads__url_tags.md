## Model: `facebook_ads__url_tags`

`facebook_ads__url_tags`

*   **Unique ID:** `model.facebook_ads.facebook_ads__url_tags`
*   **FQN:** `prod.ads_marts.facebook_ads__url_tags`
*   **Description:** Each record is a unique combination of creative_id and corresponding key, value, type contained in the url_tags field
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` | The source of the record if the unioning functionality is being used. If not this field will be empty. | The source of the record if the unioning functionality is being used. If not this field will be empty. | `[]` | `{}` |
    | `_FIVETRAN_ID` | 2 | `TEXT` | The unique fivetran ID for this record. | The unique fivetran ID for this record. | `[]` | `{}` |
    | `CREATIVE_ID` | 3 | `NUMBER` | The associated creative_id for this record. | The associated creative_id for this record. | `[]` | `{}` |
    | `KEY` | 4 | `TEXT` | The url tag object name e.g. utm_source associated with this record. | The url tag object name e.g. utm_source associated with this record. | `[]` | `{}` |
    | `VALUE` | 5 | `TEXT` | The value assigned to the url tag object associated with this record. | The value assigned to the url tag object associated with this record. | `[]` | `{}` |
    | `TYPE` | 6 | `TEXT` | The type assigned to the url tag object e.g. 'AD_VIDEO'. | The type assigned to the url tag object e.g. 'AD_VIDEO'. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.facebook_ads.get_url_tags_query`
    *   `model.facebook_ads.stg_facebook_ads__creative_history`

---
