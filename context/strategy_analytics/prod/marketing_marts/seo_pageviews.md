## Model: `seo_pageviews`

`seo_pageviews`

*   **Unique ID:** `model.cherry_data_model.seo_pageviews`
*   **FQN:** `prod.marketing_marts.seo_pageviews`
*   **Description:** (No description provided)
*   **Tags:** `['marketing_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `DAY` | 1 | `DATE` |  |  | `[]` | `{}` |
    | `PAID_SEARCH_SESSIONS` | 2 | `NUMBER` |  |  | `[]` | `{}` |
    | `ORGANIC_SEARCH_SESSIONS` | 3 | `NUMBER` |  |  | `[]` | `{}` |
    | `UNIQUE_VISITORS_FROM_SEARCH_ENGINES` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `UNIQUE_VISITORS_FROM_ORGANIC_SEARCH` | 5 | `NUMBER` |  |  | `[]` | `{}` |
    | `GOOGLE_ORGANIC_SESSIONS` | 6 | `NUMBER` |  |  | `[]` | `{}` |
    | `BING_ORGANIC_SESSIONS` | 7 | `NUMBER` |  |  | `[]` | `{}` |
    | `YAHOO_ORGANIC_SESSIONS` | 8 | `NUMBER` |  |  | `[]` | `{}` |
    | `DUCKDUCKGO_ORGANIC_SESSIONS` | 9 | `NUMBER` |  |  | `[]` | `{}` |
    | `TOTAL_UNIQUE_VISITORS` | 10 | `NUMBER` |  |  | `[]` | `{}` |
    | `ESTIMATED_TOTAL_SESSIONS` | 11 | `NUMBER` |  |  | `[]` | `{}` |
    | `ORGANIC_SEARCH_SESSION_PERCENTAGE` | 12 | `NUMBER` |  |  | `[]` | `{}` |
    | `GOOGLE_SHARE_OF_ORGANIC` | 13 | `NUMBER` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.stg_segment_pageviews`

---
