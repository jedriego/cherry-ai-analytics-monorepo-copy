## Model: `sf_lead_info_xf`

`sf_lead_info_xf`

*   **Unique ID:** `model.cherry_data_model.sf_lead_info_xf`
*   **FQN:** `prod.salesforce_marts.sf_lead_info_xf`
*   **Description:** This model joins multiple tables to provide a comprehensive view of lead information, enriched with details from Google, Yelp, and other data sources.
*   **Tags:** `['salesforce']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `LEAD_ID` | 1 | `TEXT` | Unique identifier for the lead | Unique identifier for the lead | `[]` | `{}` |
    | `LEAD_CREATED_DATE` | 2 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `DENY_IN_REFERRAL_ROCK` | 4 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_QUALIFIED_PROGRAM4` | 5 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `LAST_ENGAGEMENT_BEFORE_FIRST_DEMO_DATETIME_PT` | 6 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `KNOWN_ENGAGEMENTS` | 7 | `NUMBER` |  |  | `[]` | `{}` |
    | `IS_DENIED` | 8 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `PRACTICE_POTENTIAL_PERFORMANCE_ADJUSTED` | 9 | `FLOAT` |  |  | `[]` | `{}` |
    | `PRACTICE_POTENTIAL_EXTERNAL_DATA` | 10 | `FLOAT` |  |  | `[]` | `{}` |
    | `GOOGLE_PLACE_ID` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `GOOGLE_NAME` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `GOOGLE_STREET` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `GOOGLE_CITY` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `GOOGLE_STATE` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `GOOGLE_POSTAL_CODE` | 16 | `TEXT` |  |  | `[]` | `{}` |
    | `GOOGLE_RATING` | 17 | `FLOAT` |  |  | `[]` | `{}` |
    | `GOOGLE_REVIEW_COUNT` | 18 | `NUMBER` |  |  | `[]` | `{}` |
    | `GOOGLE_BUSINESS_STATUS` | 19 | `TEXT` |  |  | `[]` | `{}` |
    | `GOOGLE_WEBSITE` | 20 | `TEXT` |  |  | `[]` | `{}` |
    | `GOOGLE_WEBSITE_DOMAIN` | 21 | `TEXT` |  |  | `[]` | `{}` |
    | `GOOGLE_WEBSITE_DOMAIN_CREATED` | 22 | `DATE` |  |  | `[]` | `{}` |
    | `GOOGLE_WEBSITE_DOMAIN_AGE_DAYS` | 23 | `FLOAT` |  |  | `[]` | `{}` |
    | `GOOGLE_PHONE_NUMBER` | 24 | `TEXT` |  |  | `[]` | `{}` |
    | `GOOGLE_TOTAL_WEEKLY_HOURS` | 25 | `NUMBER` |  |  | `[]` | `{}` |
    | `GOOGLE_LATITUDE` | 26 | `FLOAT` |  |  | `[]` | `{}` |
    | `GOOGLE_LONGITUDE` | 27 | `FLOAT` |  |  | `[]` | `{}` |
    | `GOOGLE_MATCH_SCORE` | 28 | `FLOAT` |  |  | `[]` | `{}` |
    | `GOOGLE_MATCH_STATUS` | 29 | `TEXT` |  |  | `[]` | `{}` |
    | `YELP_ID` | 30 | `TEXT` |  |  | `[]` | `{}` |
    | `YELP_NAME` | 31 | `TEXT` |  |  | `[]` | `{}` |
    | `YELP_ALIAS` | 32 | `TEXT` |  |  | `[]` | `{}` |
    | `YELP_IS_CLAIMED` | 33 | `TEXT` |  |  | `[]` | `{}` |
    | `YELP_IS_CLOSED` | 34 | `TEXT` |  |  | `[]` | `{}` |
    | `YELP_PHONE` | 35 | `TEXT` |  |  | `[]` | `{}` |
    | `YELP_CATEGORY1` | 36 | `TEXT` |  |  | `[]` | `{}` |
    | `YELP_CATEGORY2` | 37 | `TEXT` |  |  | `[]` | `{}` |
    | `YELP_CATEGORY3` | 38 | `TEXT` |  |  | `[]` | `{}` |
    | `YELP_RATING` | 39 | `FLOAT` |  |  | `[]` | `{}` |
    | `YELP_REVIEW_COUNT` | 40 | `NUMBER` |  |  | `[]` | `{}` |
    | `YELP_TOTAL_WEEKLY_HOURS` | 41 | `NUMBER` |  |  | `[]` | `{}` |
    | `YELP_MATCH_SCORE` | 42 | `FLOAT` |  |  | `[]` | `{}` |
    | `YELP_MATCH_STATUS` | 43 | `TEXT` |  |  | `[]` | `{}` |
    | `QUEUE_ENRICHMENT` | 44 | `BOOLEAN` | Indicator if the lead needs to be enriched. It's TRUE if Google or Yelp details have changed. | Indicator if the lead needs to be enriched. It's TRUE if Google or Yelp details have changed. | `[]` | `{}` |
    | `IS_MARKETING_LEAD` | 45 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ENHANCED_INTERNAL_REFERRER` | 46 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_CONVERTED` | 47 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `RECORD_TYPE_ID` | 48 | `TEXT` |  |  | `[]` | `{}` |
    | `LEAD_ENGAGEMENT_SCORE` | 49 | `FLOAT` |  |  | `[]` | `{}` |
    | `LATEST_CARECREDIT_MONTHLY_VOLUME` | 50 | `NUMBER` |  |  | `[]` | `{}` |
    | `IS_ELIGIBLE_FOR_VERY_COMPETITIVE_MENU` | 51 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `DBT_SCD_ID` | 52 | `TEXT` |  |  | `[]` | `{}` |
    | `DBT_UPDATED_AT` | 53 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `DBT_VALID_FROM` | 54 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `DBT_VALID_TO` | 55 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `snapshot.cherry_data_model.sf_lead_info_snapshot`

---
