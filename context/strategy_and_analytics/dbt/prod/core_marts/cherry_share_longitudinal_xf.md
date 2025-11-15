## Model: `cherry_share_longitudinal_xf`

`cherry_share_longitudinal_xf`

*   **Unique ID:** `model.cherry_data_model.cherry_share_longitudinal_xf`
*   **FQN:** `prod.core_marts.cherry_share_longitudinal_xf`
*   **Description:** **Longitudinal Market Share Analysis for Cherry vs CareCredit Competition**
This model extends `stg_cherry_share_longitudinal` by adding scrape iteration ranking to enable  longitudinal analysis of Cherry's competitive positioning against CareCredit across matched healthcare  practices. The model provides both historical (scrape-relative) and current market share calculations,  enabling trend analysis and competitive intelligence over time.
**Key Business Logic:** - Adds `is_latest_full_scrape` flag using rank=2 logic to identify the most recent complete scrape iteration - Inherits complex market share calculations from staging model with go-live date protections - Calculates market share as: Cherry Volume / (Cherry Volume + CareCredit Volume) - Handles new practice ramp-up periods by nulling metrics for practices live < 30 days - Provides dual time perspectives: scrape-date relative vs current-date relative analysis
**Data Sources:** - `stg_cherry_share_longitudinal`: Market share calculations and matched practice data - `stg_care_credit_scrape_data`: Scrape iteration ranking for identifying complete datasets - `loan_info_xf`: Cherry transaction volumes for market share calculations - `stg_merchants`: Practice go-live dates for proper metric timing
**Primary Use Cases:** - Longitudinal competitive positioning analysis - Market share trend tracking over time - Practice-level competitive intelligence - Historical vs current performance comparison

*   **Tags:** `['core', 'competitive_data']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `PRIMARY_MERCHANT_ID` | 1 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_ID` | 2 | `NUMBER` | Cherry's primary organization identifier for the practice, derived from the primary_merchant_id's  organization association. Used for organizational-level competitive analysis and grouping multiple  practice locations under a single parent entity. Critical for understanding multi-location  competitive dynamics and organizational market share.
 | Cherry's primary organization identifier for the practice, derived from the primary_merchant_id's  organization association. Used for organizational-level competitive analysis and grouping multiple  practice locations under a single parent entity. Critical for understanding multi-location  competitive dynamics and organizational market share.
 | `[]` | `{}` |
    | `SF_ACCOUNT_ID` | 3 | `TEXT` | Cherry's Salesforce account identifier for the practice, serving as the primary key for linking  competitive intelligence to Cherry's CRM and sales systems. Used for account management, sales  targeting, and customer relationship analysis in competitive contexts.
 | Cherry's Salesforce account identifier for the practice, serving as the primary key for linking  competitive intelligence to Cherry's CRM and sales systems. Used for account management, sales  targeting, and customer relationship analysis in competitive contexts.
 | `[]` | `{}` |
    | `CHERRY_NAME` | 4 | `TEXT` | Practice name as recorded in Cherry's merchant system. Used for practice identification and  validation of competitive matches. May differ from CareCredit naming due to business name variations,  DBA usage, or data entry differences between the two systems.
 | Practice name as recorded in Cherry's merchant system. Used for practice identification and  validation of competitive matches. May differ from CareCredit naming due to business name variations,  DBA usage, or data entry differences between the two systems.
 | `[]` | `{}` |
    | `GO_LIVE_DATE` | 5 | `DATE` |  |  | `[]` | `{}` |
    | `CARECREDIT_NAME` | 6 | `TEXT` | Practice name as recorded in CareCredit's practice finder system. Used for competitive intelligence  and practice matching validation. Represents how the practice appears to CareCredit customers and  may reflect public-facing branding vs legal business names.
 | Practice name as recorded in CareCredit's practice finder system. Used for competitive intelligence  and practice matching validation. Represents how the practice appears to CareCredit customers and  may reflect public-facing branding vs legal business names.
 | `[]` | `{}` |
    | `PARENT_SF_ID` | 7 | `TEXT` | CareCredit's parent organization identifier, equivalent to Cherry's organization concept. Groups  individual practice locations under parent entities for aggregated competitive analysis. Critical  for understanding organizational-level CareCredit usage and competitive positioning.
 | CareCredit's parent organization identifier, equivalent to Cherry's organization concept. Groups  individual practice locations under parent entities for aggregated competitive analysis. Critical  for understanding organizational-level CareCredit usage and competitive positioning.
 | `[]` | `{}` |
    | `SFID` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `SCRAPE_ITERATION` | 9 | `TEXT` | Identifier for the specific batch or iteration of CareCredit scraping that captured this competitive  intelligence data. Format includes 'crawler3', 'crawler4', 'legacy' iterations. Used for data  lineage tracking and enabling longitudinal analysis across different scrape periods.
 | Identifier for the specific batch or iteration of CareCredit scraping that captured this competitive  intelligence data. Format includes 'crawler3', 'crawler4', 'legacy' iterations. Used for data  lineage tracking and enabling longitudinal analysis across different scrape periods.
 | `[]` | `{}` |
    | `SCRAPE_DATE` | 10 | `TIMESTAMP_NTZ` | Date when the CareCredit competitive intelligence data was collected through Cherry's scraping system.  Serves as the temporal anchor for historical market share calculations and longitudinal trend analysis.  Critical for understanding market conditions and competitive positioning at specific points in time.
 | Date when the CareCredit competitive intelligence data was collected through Cherry's scraping system.  Serves as the temporal anchor for historical market share calculations and longitudinal trend analysis.  Critical for understanding market conditions and competitive positioning at specific points in time.
 | `[]` | `{}` |
    | `SPECIALTIES` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `VERTICAL` | 12 | `TEXT` | Healthcare industry vertical classification derived from CareCredit's profession and specialty  fields. Common values include 'Dental', 'Optometry', 'Cosmetic Surgery', 'General Medicine',  'Veterinary'. Used for vertical-specific competitive analysis and market penetration strategies  across different healthcare segments.
 | Healthcare industry vertical classification derived from CareCredit's profession and specialty  fields. Common values include 'Dental', 'Optometry', 'Cosmetic Surgery', 'General Medicine',  'Veterinary'. Used for vertical-specific competitive analysis and market penetration strategies  across different healthcare segments.
 | `[]` | `{}` |
    | `MATCH_TYPE` | 13 | `TEXT` | Classification of the matching criteria used to associate Cherry practices with CareCredit practices.  Common values include 'Phone', 'Domain', 'Name', 'Name Contain'. Indicates the confidence and  methodology of the competitive match, with different match types having varying reliability levels  for market share analysis.
 | Classification of the matching criteria used to associate Cherry practices with CareCredit practices.  Common values include 'Phone', 'Domain', 'Name', 'Name Contain'. Indicates the confidence and  methodology of the competitive match, with different match types having varying reliability levels  for market share analysis.
 | `[]` | `{}` |
    | `MONTHLY_PRACTICE_CARECREDIT_USAGE_VOLUME` | 14 | `FLOAT` | Estimated monthly CareCredit transaction volume in dollars for the individual practice. Derived  from complex normalization of parent organization usage data across practice locations and  time periods. Represents the competitive baseline for market share calculations and indicates  the total addressable market size for Cherry in each practice.
 | Estimated monthly CareCredit transaction volume in dollars for the individual practice. Derived  from complex normalization of parent organization usage data across practice locations and  time periods. Represents the competitive baseline for market share calculations and indicates  the total addressable market size for Cherry in each practice.
 | `[]` | `{}` |
    | `SCRAPE_30D_CHERRY_VOLUME` | 15 | `FLOAT` | Cherry transaction volume in dollars for the 30 days preceding the scrape_date. Calculated from  loan_info_xf for loans with 'FUNDED' or 'AWAITING_FUNDING' status, filtered to the specific  30-day window relative to when competitive data was collected. NULL for practices that went  live less than 30 days before the scrape date to ensure data quality.
 | Cherry transaction volume in dollars for the 30 days preceding the scrape_date. Calculated from  loan_info_xf for loans with 'FUNDED' or 'AWAITING_FUNDING' status, filtered to the specific  30-day window relative to when competitive data was collected. NULL for practices that went  live less than 30 days before the scrape date to ensure data quality.
 | `[]` | `{}` |
    | `PAST_30D_CHERRY_VOLUME` | 16 | `FLOAT` | Cherry transaction volume in dollars for the 30 days preceding the current date (not scrape date).  Calculated using the same methodology as scrape_30d_cherry_volume but anchored to present day.  NULL for practices that went live less than 30 days ago. Used for current competitive positioning  analysis and real-time market share assessment.
 | Cherry transaction volume in dollars for the 30 days preceding the current date (not scrape date).  Calculated using the same methodology as scrape_30d_cherry_volume but anchored to present day.  NULL for practices that went live less than 30 days ago. Used for current competitive positioning  analysis and real-time market share assessment.
 | `[]` | `{}` |
    | `SCRAPE_30D_CHERRY_SHARE_PCT` | 17 | `FLOAT` | Cherry's market share percentage calculated using the 30-day Cherry volume preceding the scrape_date  divided by the sum of Cherry volume plus estimated monthly CareCredit volume. Formula:  scrape_30d_cherry_volume / (scrape_30d_cherry_volume + monthly_practice_carecredit_usage_volume).  Values range from 0-1 (converted to percentage). NULL for practices with insufficient operating history.  Enables historical competitive positioning analysis.
 | Cherry's market share percentage calculated using the 30-day Cherry volume preceding the scrape_date  divided by the sum of Cherry volume plus estimated monthly CareCredit volume. Formula:  scrape_30d_cherry_volume / (scrape_30d_cherry_volume + monthly_practice_carecredit_usage_volume).  Values range from 0-1 (converted to percentage). NULL for practices with insufficient operating history.  Enables historical competitive positioning analysis.
 | `[]` | `{}` |
    | `PAST_30D_CHERRY_SHARE_PCT` | 18 | `FLOAT` | Cherry's current market share percentage calculated using the most recent 30-day Cherry volume  divided by the sum of Cherry volume plus estimated monthly CareCredit volume. Formula:  past_30d_cherry_volume / (past_30d_cherry_volume + monthly_practice_carecredit_usage_volume).  Values range from 0-1 (converted to percentage). NULL for newly-live practices. Represents  Cherry's current competitive position in each practice.
 | Cherry's current market share percentage calculated using the most recent 30-day Cherry volume  divided by the sum of Cherry volume plus estimated monthly CareCredit volume. Formula:  past_30d_cherry_volume / (past_30d_cherry_volume + monthly_practice_carecredit_usage_volume).  Values range from 0-1 (converted to percentage). NULL for newly-live practices. Represents  Cherry's current competitive position in each practice.
 | `[]` | `{}` |
    | `IS_LATEST_FULL_SCRAPE` | 19 | `BOOLEAN` | Boolean flag indicating whether this record comes from the most recent complete CareCredit  scrape iteration (rank=2 in scrape ranking logic). TRUE means this data represents the latest  available competitive intelligence for the practice. Used for filtering to current competitive  landscape analysis and ensuring data recency in longitudinal studies. FALSE indicates historical  scrape data that may be superseded by more recent competitive intelligence. | Boolean flag indicating whether this record comes from the most recent complete CareCredit  scrape iteration (rank=2 in scrape ranking logic). TRUE means this data represents the latest  available competitive intelligence for the practice. Used for filtering to current competitive  landscape analysis and ensuring data recency in longitudinal studies. FALSE indicates historical  scrape data that may be superseded by more recent competitive intelligence. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.stg_care_credit_scrape_data`
    *   `model.cherry_data_model.stg_cherry_share_longitudinal`

---
