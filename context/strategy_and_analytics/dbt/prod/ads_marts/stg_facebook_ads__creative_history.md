## Model: `stg_facebook_ads__creative_history`

`stg_facebook_ads__creative_history`

*   **Unique ID:** `model.facebook_ads.stg_facebook_ads__creative_history`
*   **FQN:** `prod.ads_marts.stg_facebook_ads__creative_history`
*   **Description:** Each record in this table reflects a Facebook creative.
*   **Tags:** `[]`
*   **Meta:** `{'staging': {'+schema': 'facebook_ads_staging', '+database': 'prep'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_RELATION` | 1 | `TEXT` | The source of the record if the unioning functionality is being used. If not this field will be empty. | The source of the record if the unioning functionality is being used. If not this field will be empty. | `[]` | `{}` |
    | `_FIVETRAN_ID` | 2 | `TEXT` | Unique record identifier | Unique record identifier | `[]` | `{}` |
    | `_FIVETRAN_SYNCED` | 3 | `TIMESTAMP_TZ` | When the record was last synced by Fivetran. | When the record was last synced by Fivetran. | `[]` | `{}` |
    | `CREATIVE_ID` | 4 | `NUMBER` | Unique ID for an ad creative. | Unique ID for an ad creative. | `[]` | `{}` |
    | `ACCOUNT_ID` | 5 | `NUMBER` | Ad account ID for the account this ad creative belongs to. | Ad account ID for the account this ad creative belongs to. | `[]` | `{}` |
    | `CREATIVE_NAME` | 6 | `TEXT` | Name of this ad creative as seen in the ad account's library. | Name of this ad creative as seen in the ad account's library. | `[]` | `{}` |
    | `PAGE_LINK` | 7 | `TEXT` | Link for the page. | Link for the page. | `[]` | `{}` |
    | `TEMPLATE_PAGE_LINK` | 8 | `TEXT` | URL destination of Facebook dynamic ads. | URL destination of Facebook dynamic ads. | `[]` | `{}` |
    | `URL_TAGS` | 9 | `VARIANT` | A set of query string parameters which will replace or be appended to urls clicked from page post ads, message of the post, and canvas app install creatives only. | A set of query string parameters which will replace or be appended to urls clicked from page post ads, message of the post, and canvas app install creatives only. | `[]` | `{}` |
    | `ASSET_FEED_SPEC_LINK_URLS` | 10 | `VARIANT` | Link to the asset feed spec | Link to the asset feed spec | `[]` | `{}` |
    | `OBJECT_STORY_LINK_DATA_CHILD_ATTACHMENTS` | 11 | `VARIANT` | Link of the object story child attachments | Link of the object story child attachments | `[]` | `{}` |
    | `OBJECT_STORY_LINK_DATA_CAPTION` | 12 | `TEXT` | Link of the object story caption | Link of the object story caption | `[]` | `{}` |
    | `OBJECT_STORY_LINK_DATA_DESCRIPTION` | 13 | `TEXT` | Link of the object story description | Link of the object story description | `[]` | `{}` |
    | `OBJECT_STORY_LINK_DATA_LINK` | 14 | `TEXT` | Link of the object story link | Link of the object story link | `[]` | `{}` |
    | `OBJECT_STORY_LINK_DATA_MESSAGE` | 15 | `TEXT` | Link of the object story message | Link of the object story message | `[]` | `{}` |
    | `TEMPLATE_APP_LINK_SPEC_IOS` | 16 | `VARIANT` | Link of the object story spec for ios | Link of the object story spec for ios | `[]` | `{}` |
    | `TEMPLATE_APP_LINK_SPEC_IPAD` | 17 | `VARIANT` | Link of the template app spec for ipad | Link of the template app spec for ipad | `[]` | `{}` |
    | `TEMPLATE_APP_LINK_SPEC_ANDROID` | 18 | `VARIANT` | Link of the template app for android | Link of the template app for android | `[]` | `{}` |
    | `TEMPLATE_APP_LINK_SPEC_IPHONE` | 19 | `VARIANT` | Link of the template app for iphone | Link of the template app for iphone | `[]` | `{}` |
    | `IS_MOST_RECENT_RECORD` | 20 | `BOOLEAN` | Indicates whether a record is the most recent version of that record. | Indicates whether a record is the most recent version of that record. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt.type_bigint`
    *   `macro.facebook_ads.get_creative_history_columns`
    *   `macro.fivetran_utils.fill_staging_columns`
    *   `macro.fivetran_utils.source_relation`
    *   `model.facebook_ads.stg_facebook_ads__creative_history_tmp`

---
