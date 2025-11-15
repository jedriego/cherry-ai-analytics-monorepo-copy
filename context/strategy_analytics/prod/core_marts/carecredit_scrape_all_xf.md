## Model: `carecredit_scrape_all_xf`

`carecredit_scrape_all_xf`

*   **Unique ID:** `model.cherry_data_model.carecredit_scrape_all_xf`
*   **FQN:** `prod.core_marts.carecredit_scrape_all_xf`
*   **Description:** **Competitive Intelligence Snapshot from CareCredit Practice Finder**
This model provides all scrape results from CareCredit's practice finder,  serving as Cherry's primary competitive intelligence data source. The model combines scraped  CareCredit practice data with Cherry's own transaction volume to calculate market share and  competitive positioning across healthcare practices.
**Key Business Logic:** - Applies complex volume scaling logic to normalize CareCredit's practice usage dollars to monthly estimates - Accounts for changes in CareCredit's data methodology detected in February 2025 - Matches CareCredit practices to Cherry merchants using multiple criteria (phone, domain, name matching) - Calculates Cherry's market share both relative to current date and scrape date
**Data Sources:** - `stg_care_credit_scrape_data`: Raw CareCredit practice finder data from Cherry's internal crawler - `stg_cherry_share_longitudinal`: Cherry transaction volumes and market share calculations - `stg_care_credit_vertical_mapping_enriched`: Practice classification by healthcare vertical - `stg_feb_2025_care_credit_scrape_response_changes`: Accounts for CareCredit methodology changes
**Primary Use Cases:** - Competitive market analysis and share tracking - Practice targeting and acquisition strategy - Vertical market penetration analysis - Cherry's competitive positioning assessment

*   **Tags:** `['core', 'competitive_data']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SCRAPE_DATE` | 1 | `TIMESTAMP_NTZ` | Date when the CareCredit practice data was collected through Cherry's internal scraping system.  Represents the business date of the scrape iteration and serves as the temporal anchor for all  competitive intelligence analysis. This date is used for time-series analysis, longitudinal  market share tracking, and ensuring data currency in competitive positioning reports. All  practices in this snapshot share the same scrape_date from the selected complete scrape iteration  (rank=2 logic ensures completeness). Critical for calculating time-based metrics like 30-day  volumes relative to the scrape date and understanding market conditions at the time of data collection.
 | Date when the CareCredit practice data was collected through Cherry's internal scraping system.  Represents the business date of the scrape iteration and serves as the temporal anchor for all  competitive intelligence analysis. This date is used for time-series analysis, longitudinal  market share tracking, and ensuring data currency in competitive positioning reports. All  practices in this snapshot share the same scrape_date from the selected complete scrape iteration  (rank=2 logic ensures completeness). Critical for calculating time-based metrics like 30-day  volumes relative to the scrape date and understanding market conditions at the time of data collection.
 | `[]` | `{}` |
    | `SCRAPE_ITERATION` | 2 | `TEXT` | Identifier for the batch or iteration of CareCredit scraping that captured this data. Format  includes 'crawler3', 'crawler4', 'legacy' iterations, etc. Used to track data lineage and  select the most recent complete dataset while filtering out incomplete scrape attempts.
 | Identifier for the batch or iteration of CareCredit scraping that captured this data. Format  includes 'crawler3', 'crawler4', 'legacy' iterations, etc. Used to track data lineage and  select the most recent complete dataset while filtering out incomplete scrape attempts.
 | `[]` | `{}` |
    | `SFID` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRACTICE_PLATE` | 5 | `TEXT` | Alternative unique identifier for individual CareCredit practice locations, potentially serving  as a human-readable practice code within CareCredit's system. Used as a secondary matching  criterion when linking CareCredit practices to Cherry merchants.
 | Alternative unique identifier for individual CareCredit practice locations, potentially serving  as a human-readable practice code within CareCredit's system. Used as a secondary matching  criterion when linking CareCredit practices to Cherry merchants.
 | `[]` | `{}` |
    | `NAME` | 6 | `TEXT` | Practice name as recorded in CareCredit's practice finder system. This is the public-facing  name used for practice identification and matching against Cherry's merchant names. May differ  from the legal business name and is used in name-based matching algorithms.
 | Practice name as recorded in CareCredit's practice finder system. This is the public-facing  name used for practice identification and matching against Cherry's merchant names. May differ  from the legal business name and is used in name-based matching algorithms.
 | `[]` | `{}` |
    | `PHONE` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `EMAIL` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `ADDRESS1` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `CITY` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `STATE` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `POSTAL_CODE` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `LATITUDE` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `LONGITUDE` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `WEBSITE` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `PROFESSIONS` | 16 | `TEXT` |  |  | `[]` | `{}` |
    | `SPECIALTIES` | 17 | `TEXT` |  |  | `[]` | `{}` |
    | `DIVISION` | 18 | `TEXT` |  |  | `[]` | `{}` |
    | `PRACTICE_USAGE_DOLLARS` | 19 | `NUMBER` | Raw CareCredit usage volume in dollars for the practice's parent organization over a historical  time period. The time window varies by scrape date (12-18 months) and methodology changes occurred  in February 2025. This raw amount gets normalized to create monthly estimates and represents total  CareCredit transaction volume before Cherry's market entry.
 | Raw CareCredit usage volume in dollars for the practice's parent organization over a historical  time period. The time window varies by scrape date (12-18 months) and methodology changes occurred  in February 2025. This raw amount gets normalized to create monthly estimates and represents total  CareCredit transaction volume before Cherry's market entry.
 | `[]` | `{}` |
    | `DOCTOR_FIRST_NAME` | 20 | `TEXT` |  |  | `[]` | `{}` |
    | `DOCTOR_LAST_NAME` | 21 | `TEXT` |  |  | `[]` | `{}` |
    | `OFFICE_MANAGER` | 22 | `TEXT` |  |  | `[]` | `{}` |
    | `HASAPPLYENABLED` | 23 | `TEXT` |  |  | `[]` | `{}` |
    | `ISDOCTORLOCATORENABLED` | 24 | `TEXT` |  |  | `[]` | `{}` |
    | `ISINSUFFICIENTUSAGEENABLED` | 25 | `TEXT` |  |  | `[]` | `{}` |
    | `ISPAYMYPROVIDERENABLED` | 26 | `TEXT` |  |  | `[]` | `{}` |
    | `ISONLINEONLYENABLED` | 27 | `TEXT` |  |  | `[]` | `{}` |
    | `ISSPANISHENABLED` | 28 | `TEXT` |  |  | `[]` | `{}` |
    | `ISTRAININGCERTIFIEDENABLED` | 29 | `TEXT` |  |  | `[]` | `{}` |
    | `PREPAYDATECAP` | 30 | `NUMBER` |  |  | `[]` | `{}` |
    | `PAYMENTCAP` | 31 | `NUMBER` |  |  | `[]` | `{}` |
    | `PCGC` | 32 | `TEXT` |  |  | `[]` | `{}` |
    | `POSTPAYDATECONSUMERCAP` | 33 | `NUMBER` |  |  | `[]` | `{}` |
    | `POSTPAYDATEPROVIDERCAP` | 34 | `NUMBER` |  |  | `[]` | `{}` |
    | `PARENT_SF_ID` | 35 | `TEXT` | CareCredit's parent organization identifier that groups individual practices under a single  parent entity (equivalent to Cherry's organization concept). Used for aggregating practice  usage dollars at the organizational level and calculating per-practice volume estimates.  Critical for understanding multi-location practice groups and their total CareCredit utilization.
 | CareCredit's parent organization identifier that groups individual practices under a single  parent entity (equivalent to Cherry's organization concept). Used for aggregating practice  usage dollars at the organizational level and calculating per-practice volume estimates.  Critical for understanding multi-location practice groups and their total CareCredit utilization.
 | `[]` | `{}` |
    | `UNIQUE_ID` | 36 | `TEXT` |  |  | `[]` | `{}` |
    | `VERTICAL` | 37 | `TEXT` | Healthcare industry vertical classification derived from CareCredit's profession and specialty  fields through `stg_care_credit_vertical_mapping_enriched`. Common values include 'Dental',  'Optometry', 'Cosmetic Surgery', 'General Medicine', 'Veterinary', etc. Used for vertical-specific  competitive analysis and market penetration strategies.
 | Healthcare industry vertical classification derived from CareCredit's profession and specialty  fields through `stg_care_credit_vertical_mapping_enriched`. Common values include 'Dental',  'Optometry', 'Cosmetic Surgery', 'General Medicine', 'Veterinary', etc. Used for vertical-specific  competitive analysis and market penetration strategies.
 | `[]` | `{}` |
    | `IS_COMPLETE_SCRAPE` | 38 | `BOOLEAN` | Denotes if the record belongs to a complete scrape. We cannot compute CareCredit usage volume until a scrape is complete as we need to know the total number of accounts with a parent_sf_id and there usage dollar responses to ultimately allocate the dollars based on our hypothesized logic.
 | Denotes if the record belongs to a complete scrape. We cannot compute CareCredit usage volume until a scrape is complete as we need to know the total number of accounts with a parent_sf_id and there usage dollar responses to ultimately allocate the dollars based on our hypothesized logic.
 | `[]` | `{}` |
    | `MONTHLY_PRACTICE_CARECREDIT_USAGE_VOLUME` | 39 | `FLOAT` | Estimated monthly CareCredit transaction volume in dollars for the individual practice. Derived by  normalizing the parent organization's practice_usage_dollars across all practices in the organization  and scaling to monthly amounts using complex time-window logic. Accounts for methodology changes  detected in February 2025 through conditional scaling factors. Used as baseline for market share calculations.
 | Estimated monthly CareCredit transaction volume in dollars for the individual practice. Derived by  normalizing the parent organization's practice_usage_dollars across all practices in the organization  and scaling to monthly amounts using complex time-window logic. Accounts for methodology changes  detected in February 2025 through conditional scaling factors. Used as baseline for market share calculations.
 | `[]` | `{}` |
    | `CHERRY_MERCHANT_ID` | 40 | `NUMBER` | Cherry's primary merchant identifier for the matched practice, sourced from the cherry_share_longitudinal  model. Only populated when a successful match exists between CareCredit and Cherry systems. Used for  joining to Cherry's merchant and transaction data for deeper competitive analysis.
 | Cherry's primary merchant identifier for the matched practice, sourced from the cherry_share_longitudinal  model. Only populated when a successful match exists between CareCredit and Cherry systems. Used for  joining to Cherry's merchant and transaction data for deeper competitive analysis.
 | `[]` | `{}` |
    | `CHERRY_ORGANIZATION_ID` | 41 | `NUMBER` | Cherry's organization identifier for the matched practice, representing the parent organization  in Cherry's system (equivalent to CareCredit's parent_sf_id concept). Only populated for matched  practices and used for organizational-level competitive analysis and multi-location practice management.
 | Cherry's organization identifier for the matched practice, representing the parent organization  in Cherry's system (equivalent to CareCredit's parent_sf_id concept). Only populated for matched  practices and used for organizational-level competitive analysis and multi-location practice management.
 | `[]` | `{}` |
    | `CHERRY_SF_ID` | 42 | `TEXT` | Cherry's Salesforce account identifier for the matched practice, used for CRM integration and  account management. Only populated when a match exists between CareCredit and Cherry systems.  Enables linking competitive intelligence to Cherry's sales and account management processes.
 | Cherry's Salesforce account identifier for the matched practice, used for CRM integration and  account management. Only populated when a match exists between CareCredit and Cherry systems.  Enables linking competitive intelligence to Cherry's sales and account management processes.
 | `[]` | `{}` |
    | `CHERRY_NAME` | 43 | `TEXT` | Practice name as recorded in Cherry's merchant system for matched practices. May differ from  the CareCredit name due to variations in business name usage. Used for validation of practice  matches and understanding naming discrepancies between the two systems. | Practice name as recorded in Cherry's merchant system for matched practices. May differ from  the CareCredit name due to variations in business name usage. Used for validation of practice  matches and understanding naming discrepancies between the two systems. | `[]` | `{}` |
    | `CHERRY_PAST_30D_VOLUME` | 44 | `FLOAT` | Cherry transaction volume in dollars for the practice in the 30 days preceding the current date  (not the scrape date). Calculated from `loan_info_xf` for loans with 'FUNDED' or 'AWAITING_FUNDING'  status. Represents Cherry's recent market capture and is used for current market share analysis.  Zero for practices where Cherry has no presence.
 | Cherry transaction volume in dollars for the practice in the 30 days preceding the current date  (not the scrape date). Calculated from `loan_info_xf` for loans with 'FUNDED' or 'AWAITING_FUNDING'  status. Represents Cherry's recent market capture and is used for current market share analysis.  Zero for practices where Cherry has no presence.
 | `[]` | `{}` |
    | `PAST_30D_CHERRY_SHARE_PCT` | 45 | `FLOAT` | Cherry's market share percentage calculated as Cherry's 30-day volume divided by the sum of  Cherry's volume plus estimated CareCredit monthly volume, based on the most recent 30 days.  Represents Cherry's current competitive position in the practice. Values range from 0-100%,  with higher values indicating stronger Cherry market presence.
 | Cherry's market share percentage calculated as Cherry's 30-day volume divided by the sum of  Cherry's volume plus estimated CareCredit monthly volume, based on the most recent 30 days.  Represents Cherry's current competitive position in the practice. Values range from 0-100%,  with higher values indicating stronger Cherry market presence.
 | `[]` | `{}` |
    | `CHERRY_SCRAPE_30D_VOLUME` | 46 | `FLOAT` | Cherry transaction volume in dollars for the practice in the 30 days preceding the scrape_date  (not current date). Calculated using the same logic as past_30d_volume but anchored to the  historical scrape date. Used for longitudinal market share analysis and understanding Cherry's  competitive position at the time of the scrape.
 | Cherry transaction volume in dollars for the practice in the 30 days preceding the scrape_date  (not current date). Calculated using the same logic as past_30d_volume but anchored to the  historical scrape date. Used for longitudinal market share analysis and understanding Cherry's  competitive position at the time of the scrape.
 | `[]` | `{}` |
    | `SCRAPE_30D_CHERRY_SHARE_PCT` | 47 | `FLOAT` | Cherry's market share percentage calculated using the 30-day volume preceding the scrape_date,  following the same methodology as past_30d_cherry_share_pct but with historical anchoring.  Enables analysis of market share changes over time and evaluation of Cherry's competitive  progress in specific practices. Values range from 0-100%.
 | Cherry's market share percentage calculated using the 30-day volume preceding the scrape_date,  following the same methodology as past_30d_cherry_share_pct but with historical anchoring.  Enables analysis of market share changes over time and evaluation of Cherry's competitive  progress in specific practices. Values range from 0-100%.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.stg_care_credit_scrape_data`
    *   `model.cherry_data_model.stg_care_credit_vertical_mapping_enriched`
    *   `model.cherry_data_model.stg_cherry_share_longitudinal`
    *   `model.cherry_data_model.stg_credit_scrape_usage_volume_parent_sfid`

---
