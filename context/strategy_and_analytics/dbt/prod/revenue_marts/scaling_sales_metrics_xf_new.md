## Model: `scaling_sales_metrics_xf_new`

`scaling_sales_metrics_xf_new`

*   **Unique ID:** `model.cherry_data_model.scaling_sales_metrics_xf_new`
*   **FQN:** `prod.revenue_marts.scaling_sales_metrics_xf_new`
*   **Description:** **Comprehensive Daily Sales Performance Analytics Dashboard**
This model provides a complete daily time series of sales performance metrics across industry segments  and attribution sources, designed to support executive-level sales performance monitoring and scaling  analysis. It combines team capacity tracking, qualified opportunity generation, and conversion rate  analysis into a unified performance dashboard.
**Key Business Logic:** - **Complete Time Series**: Creates scaffold with every date for every industry segment to ensure consistent reporting - **Team Capacity Tracking**: Daily Account Executive counts by industry segment using historical role data - **Attribution Mapping**: Maps 6 attribution sources (Sales, Alle, Sales Development, Marketing, Business Development, Other) using engagement scoring - **Multi-Window Conversion**: Tracks go-live conversion rates at 14, 30, and 60-day windows from qualified opportunity - **Industry Segment Logic**: Maps Salesforce teams to business-relevant industry segments with specific rules
**Attribution Sources:** - **Sales**: Direct sales team generated opportunities - **Alle**: Partnership-driven opportunities from Alle collaboration - **Sales Development**: SDR/BDR generated qualified opportunities - **Marketing**: Marketing-driven inbound and campaign opportunities - **Business Development**: Strategic partnership and channel opportunities - **Other**: Miscellaneous sources not fitting primary categories
**Primary Use Cases:** - Executive sales performance dashboards and KPI tracking - Team capacity planning and scaling analysis - Attribution source performance comparison and optimization - Conversion funnel analysis across industry segments - Go-live rate benchmarking and trend analysis - Resource allocation and territory performance evaluation
**Data Sources:** - **calendar_table_xf**: Complete calendar dimension for time series construction - **stg_sf_users & sf_user_history**: Salesforce user data with historical role tracking - **pursuit_engagement_summary**: Pursuit-level engagement attribution and milestone tracking - **prospect_attribution_summary**: Prospect-level attribution rolled up from pursuits

*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `DATE` | 1 | `DATE` | **Calendar Date**
Primary time dimension for the daily time series, sourced from calendar_table_xf.  Every date from the earliest data through current_date is included to ensure  complete time series consistency for trending and performance analysis.
 | **Calendar Date**
Primary time dimension for the daily time series, sourced from calendar_table_xf.  Every date from the earliest data through current_date is included to ensure  complete time series consistency for trending and performance analysis.
 | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 2 | `TEXT` | **Industry Segment Classification**
Business-relevant industry grouping mapped from Salesforce team assignments using specific logic: - **'MedSpa'**: Core Aesthetics and Account Executives Aesthetics teams - **'Plastic and Cosmetic Surgery'**: Plastic and Cosmetic Surgery focused teams   - **'Dental'**: Dental-focused sales teams - **'Veterinary'**: Veterinary-focused sales teams - **'Other'**: Webinar teams and miscellaneous segments
This mapping enables industry-specific performance analysis and benchmarking.
 | **Industry Segment Classification**
Business-relevant industry grouping mapped from Salesforce team assignments using specific logic: - **'MedSpa'**: Core Aesthetics and Account Executives Aesthetics teams - **'Plastic and Cosmetic Surgery'**: Plastic and Cosmetic Surgery focused teams   - **'Dental'**: Dental-focused sales teams - **'Veterinary'**: Veterinary-focused sales teams - **'Other'**: Webinar teams and miscellaneous segments
This mapping enables industry-specific performance analysis and benchmarking.
 | `[]` | `{}` |
    | `TOTAL_USERS` | 3 | `NUMBER` | **Daily Account Executive Count**
Number of active Account Executives assigned to this industry segment on this date,  calculated using historical role data to track team capacity over time. Only includes  users in Sales/Account Executive departments with active status and Account Executive titles.
 | **Daily Account Executive Count**
Number of active Account Executives assigned to this industry segment on this date,  calculated using historical role data to track team capacity over time. Only includes  users in Sales/Account Executive departments with active status and Account Executive titles.
 | `[]` | `{}` |
    | `TOTAL_QUALIFIED_OPPORTUNITIES` | 4 | `NUMBER` | **Total Daily Qualified Opportunities**
Total count of qualified opportunities created on this date for this industry segment,  aggregated across all attribution sources. Represents the top of the conversion funnel  and key input metric for sales performance analysis.
 | **Total Daily Qualified Opportunities**
Total count of qualified opportunities created on this date for this industry segment,  aggregated across all attribution sources. Represents the top of the conversion funnel  and key input metric for sales performance analysis.
 | `[]` | `{}` |
    | `SALES_QUALIFIED_OPPORTUNITIES` | 5 | `NUMBER` | **Sales Team Qualified Opportunities**
Count of qualified opportunities attributed to the direct Sales team on this date.  Attribution determined by engagement scoring system that evaluates all prospect  interactions leading up to the qualified opportunity milestone.
 | **Sales Team Qualified Opportunities**
Count of qualified opportunities attributed to the direct Sales team on this date.  Attribution determined by engagement scoring system that evaluates all prospect  interactions leading up to the qualified opportunity milestone.
 | `[]` | `{}` |
    | `ALLE_QUALIFIED_OPPORTUNITIES` | 6 | `NUMBER` | **Alle Partnership Qualified Opportunities**
Count of qualified opportunities attributed to the Alle partnership channel on this date.  Represents opportunities generated through the strategic Alle collaboration and  co-marketing initiatives.
 | **Alle Partnership Qualified Opportunities**
Count of qualified opportunities attributed to the Alle partnership channel on this date.  Represents opportunities generated through the strategic Alle collaboration and  co-marketing initiatives.
 | `[]` | `{}` |
    | `SALES_DEVELOPMENT_QUALIFIED_OPPORTUNITIES` | 7 | `NUMBER` | **Sales Development Qualified Opportunities**
Count of qualified opportunities attributed to the Sales Development (SDR/BDR) team on this date.  Represents opportunities generated through outbound prospecting, lead qualification,  and early-stage nurturing activities.
 | **Sales Development Qualified Opportunities**
Count of qualified opportunities attributed to the Sales Development (SDR/BDR) team on this date.  Represents opportunities generated through outbound prospecting, lead qualification,  and early-stage nurturing activities.
 | `[]` | `{}` |
    | `MARKETING_QUALIFIED_OPPORTUNITIES` | 8 | `NUMBER` | **Marketing Qualified Opportunities**
Count of qualified opportunities attributed to Marketing efforts on this date.  Includes opportunities from inbound campaigns, content marketing, paid advertising,  and other marketing-driven engagement activities.
 | **Marketing Qualified Opportunities**
Count of qualified opportunities attributed to Marketing efforts on this date.  Includes opportunities from inbound campaigns, content marketing, paid advertising,  and other marketing-driven engagement activities.
 | `[]` | `{}` |
    | `BUSINESS_DEVELOPMENT_QUALIFIED_OPPORTUNITIES` | 9 | `NUMBER` | **Business Development Qualified Opportunities**
Count of qualified opportunities attributed to Business Development activities on this date.  Represents opportunities from strategic partnerships, channel relationships,  and business development initiatives outside of direct sales efforts.
 | **Business Development Qualified Opportunities**
Count of qualified opportunities attributed to Business Development activities on this date.  Represents opportunities from strategic partnerships, channel relationships,  and business development initiatives outside of direct sales efforts.
 | `[]` | `{}` |
    | `PRACTICE_DEVELOPMENT_QUALIFIED_OPPORTUNITIES` | 10 | `NUMBER` |  |  | `[]` | `{}` |
    | `OTHER_QUALIFIED_OPPORTUNITIES` | 11 | `NUMBER` | **Other Attribution Source Qualified Opportunities**
Count of qualified opportunities attributed to miscellaneous sources not fitting  the primary attribution categories (Sales, Alle, Sales Development, Marketing,  Business Development) on this date.
 | **Other Attribution Source Qualified Opportunities**
Count of qualified opportunities attributed to miscellaneous sources not fitting  the primary attribution categories (Sales, Alle, Sales Development, Marketing,  Business Development) on this date.
 | `[]` | `{}` |
    | `TOTAL_QUALIFIED_OPPORTUNITIES_PROSPECTS` | 12 | `NUMBER` | **Total Qualified Opportunity Prospects (Conversion Denominator)**
Total count of prospects that reached qualified opportunity status on this date,  used as the denominator for go-live conversion rate calculations. Differs from  pursuit-level counts by focusing on unique prospects rather than individual pursuits.
 | **Total Qualified Opportunity Prospects (Conversion Denominator)**
Total count of prospects that reached qualified opportunity status on this date,  used as the denominator for go-live conversion rate calculations. Differs from  pursuit-level counts by focusing on unique prospects rather than individual pursuits.
 | `[]` | `{}` |
    | `SALES_QUALIFIED_OPPORTUNITIES_PROSPECTS` | 13 | `NUMBER` | **Sales Qualified Opportunity Prospects (Conversion Denominator)**
Count of prospects with Sales-attributed qualified opportunities on this date,  used as denominator for Sales team go-live conversion rate calculations.
 | **Sales Qualified Opportunity Prospects (Conversion Denominator)**
Count of prospects with Sales-attributed qualified opportunities on this date,  used as denominator for Sales team go-live conversion rate calculations.
 | `[]` | `{}` |
    | `ALLE_QUALIFIED_OPPORTUNITIES_PROSPECTS` | 14 | `NUMBER` | **Alle Qualified Opportunity Prospects (Conversion Denominator)**
Count of prospects with Alle-attributed qualified opportunities on this date,  used as denominator for Alle partnership go-live conversion rate calculations.
 | **Alle Qualified Opportunity Prospects (Conversion Denominator)**
Count of prospects with Alle-attributed qualified opportunities on this date,  used as denominator for Alle partnership go-live conversion rate calculations.
 | `[]` | `{}` |
    | `SALES_DEVELOPMENT_QUALIFIED_OPPORTUNITIES_PROSPECTS` | 15 | `NUMBER` | **Sales Development Qualified Opportunity Prospects (Conversion Denominator)**
Count of prospects with Sales Development-attributed qualified opportunities on this date,  used as denominator for SDR/BDR team go-live conversion rate calculations.
 | **Sales Development Qualified Opportunity Prospects (Conversion Denominator)**
Count of prospects with Sales Development-attributed qualified opportunities on this date,  used as denominator for SDR/BDR team go-live conversion rate calculations.
 | `[]` | `{}` |
    | `MARKETING_QUALIFIED_OPPORTUNITIES_PROSPECTS` | 16 | `NUMBER` | **Marketing Qualified Opportunity Prospects (Conversion Denominator)**
Count of prospects with Marketing-attributed qualified opportunities on this date,  used as denominator for Marketing team go-live conversion rate calculations.
 | **Marketing Qualified Opportunity Prospects (Conversion Denominator)**
Count of prospects with Marketing-attributed qualified opportunities on this date,  used as denominator for Marketing team go-live conversion rate calculations.
 | `[]` | `{}` |
    | `BUSINESS_DEVELOPMENT_QUALIFIED_OPPORTUNITIES_PROSPECTS` | 17 | `NUMBER` | **Business Development Qualified Opportunity Prospects (Conversion Denominator)**
Count of prospects with Business Development-attributed qualified opportunities on this date,  used as denominator for BD team go-live conversion rate calculations.
 | **Business Development Qualified Opportunity Prospects (Conversion Denominator)**
Count of prospects with Business Development-attributed qualified opportunities on this date,  used as denominator for BD team go-live conversion rate calculations.
 | `[]` | `{}` |
    | `PRACTICE_DEVELOPMENT_QUALIFIED_OPPORTUNITIES_PROSPECTS` | 18 | `NUMBER` |  |  | `[]` | `{}` |
    | `OTHER_QUALIFIED_OPPORTUNITIES_PROSPECTS` | 19 | `NUMBER` | **Other Qualified Opportunity Prospects (Conversion Denominator)**
Count of prospects with Other-attributed qualified opportunities on this date,  used as denominator for miscellaneous source go-live conversion rate calculations.
 | **Other Qualified Opportunity Prospects (Conversion Denominator)**
Count of prospects with Other-attributed qualified opportunities on this date,  used as denominator for miscellaneous source go-live conversion rate calculations.
 | `[]` | `{}` |
    | `TOTAL_GO_LIVES_PROSPECTS_60_DAY` | 20 | `NUMBER` | **Total 60-Day Go-Live Conversions (Numerator)**
Count of prospects who achieved go-live status within 60 days of their qualified  opportunity date, where the qualified opportunity occurred on this date. Used as  numerator for 60-day conversion rate calculation (total_go_lives_prospects_60_day / total_qualified_opportunities_prospects).
 | **Total 60-Day Go-Live Conversions (Numerator)**
Count of prospects who achieved go-live status within 60 days of their qualified  opportunity date, where the qualified opportunity occurred on this date. Used as  numerator for 60-day conversion rate calculation (total_go_lives_prospects_60_day / total_qualified_opportunities_prospects).
 | `[]` | `{}` |
    | `SALES_GO_LIVES_PROSPECTS_60_DAY` | 21 | `NUMBER` | **Sales 60-Day Go-Live Conversions (Numerator)**
Count of Sales-attributed prospects who achieved go-live within 60 days of their  qualified opportunity date (this date). Enables Sales team conversion rate analysis.
 | **Sales 60-Day Go-Live Conversions (Numerator)**
Count of Sales-attributed prospects who achieved go-live within 60 days of their  qualified opportunity date (this date). Enables Sales team conversion rate analysis.
 | `[]` | `{}` |
    | `ALLE_GO_LIVES_PROSPECTS_60_DAY` | 22 | `NUMBER` | **Alle 60-Day Go-Live Conversions (Numerator)**
Count of Alle-attributed prospects who achieved go-live within 60 days of their  qualified opportunity date (this date). Enables Alle partnership conversion rate analysis.
 | **Alle 60-Day Go-Live Conversions (Numerator)**
Count of Alle-attributed prospects who achieved go-live within 60 days of their  qualified opportunity date (this date). Enables Alle partnership conversion rate analysis.
 | `[]` | `{}` |
    | `SALES_DEVELOPMENT_GO_LIVES_PROSPECTS_60_DAY` | 23 | `NUMBER` | **Sales Development 60-Day Go-Live Conversions (Numerator)**
Count of Sales Development-attributed prospects who achieved go-live within 60 days  of their qualified opportunity date (this date). Enables SDR/BDR conversion rate analysis.
 | **Sales Development 60-Day Go-Live Conversions (Numerator)**
Count of Sales Development-attributed prospects who achieved go-live within 60 days  of their qualified opportunity date (this date). Enables SDR/BDR conversion rate analysis.
 | `[]` | `{}` |
    | `MARKETING_GO_LIVES_PROSPECTS_60_DAY` | 24 | `NUMBER` | **Marketing 60-Day Go-Live Conversions (Numerator)**
Count of Marketing-attributed prospects who achieved go-live within 60 days of their  qualified opportunity date (this date). Enables Marketing conversion rate analysis.
 | **Marketing 60-Day Go-Live Conversions (Numerator)**
Count of Marketing-attributed prospects who achieved go-live within 60 days of their  qualified opportunity date (this date). Enables Marketing conversion rate analysis.
 | `[]` | `{}` |
    | `BUSINESS_DEVELOPMENT_GO_LIVES_PROSPECTS_60_DAY` | 25 | `NUMBER` | **Business Development 60-Day Go-Live Conversions (Numerator)**
Count of Business Development-attributed prospects who achieved go-live within 60 days  of their qualified opportunity date (this date). Enables BD conversion rate analysis.
 | **Business Development 60-Day Go-Live Conversions (Numerator)**
Count of Business Development-attributed prospects who achieved go-live within 60 days  of their qualified opportunity date (this date). Enables BD conversion rate analysis.
 | `[]` | `{}` |
    | `PRACTICE_DEVELOPMENT_GO_LIVES_PROSPECTS_60_DAY` | 26 | `NUMBER` |  |  | `[]` | `{}` |
    | `OTHER_GO_LIVES_PROSPECTS_60_DAY` | 27 | `NUMBER` | **Other 60-Day Go-Live Conversions (Numerator)**
Count of Other-attributed prospects who achieved go-live within 60 days of their  qualified opportunity date (this date). Enables miscellaneous source conversion rate analysis.
 | **Other 60-Day Go-Live Conversions (Numerator)**
Count of Other-attributed prospects who achieved go-live within 60 days of their  qualified opportunity date (this date). Enables miscellaneous source conversion rate analysis.
 | `[]` | `{}` |
    | `TOTAL_GO_LIVES` | 28 | `NUMBER` | **Total Daily Go-Lives**
Total count of prospects who achieved go-live status on this date, aggregated across  all attribution sources. Represents successful completion of the sales process and  key output metric for sales performance.
 | **Total Daily Go-Lives**
Total count of prospects who achieved go-live status on this date, aggregated across  all attribution sources. Represents successful completion of the sales process and  key output metric for sales performance.
 | `[]` | `{}` |
    | `SALES_GO_LIVES` | 29 | `NUMBER` | **Sales Team Daily Go-Lives**
Count of prospects with Sales attribution who achieved go-live status on this date.  Measures Sales team success in converting prospects to active customers.
 | **Sales Team Daily Go-Lives**
Count of prospects with Sales attribution who achieved go-live status on this date.  Measures Sales team success in converting prospects to active customers.
 | `[]` | `{}` |
    | `ALLE_GO_LIVES` | 30 | `NUMBER` | **Alle Partnership Daily Go-Lives**
Count of prospects with Alle attribution who achieved go-live status on this date.  Measures Alle partnership success in converting prospects to active customers.
 | **Alle Partnership Daily Go-Lives**
Count of prospects with Alle attribution who achieved go-live status on this date.  Measures Alle partnership success in converting prospects to active customers.
 | `[]` | `{}` |
    | `SALES_DEVELOPMENT_GO_LIVES` | 31 | `NUMBER` | **Sales Development Daily Go-Lives**
Count of prospects with Sales Development attribution who achieved go-live status on this date.  Measures SDR/BDR team success in converting prospects to active customers.
 | **Sales Development Daily Go-Lives**
Count of prospects with Sales Development attribution who achieved go-live status on this date.  Measures SDR/BDR team success in converting prospects to active customers.
 | `[]` | `{}` |
    | `MARKETING_GO_LIVES` | 32 | `NUMBER` | **Marketing Daily Go-Lives**
Count of prospects with Marketing attribution who achieved go-live status on this date.  Measures Marketing team success in converting prospects to active customers.
 | **Marketing Daily Go-Lives**
Count of prospects with Marketing attribution who achieved go-live status on this date.  Measures Marketing team success in converting prospects to active customers.
 | `[]` | `{}` |
    | `BUSINESS_DEVELOPMENT_GO_LIVES` | 33 | `NUMBER` | **Business Development Daily Go-Lives**
Count of prospects with Business Development attribution who achieved go-live status on this date.  Measures BD team success in converting prospects to active customers.
 | **Business Development Daily Go-Lives**
Count of prospects with Business Development attribution who achieved go-live status on this date.  Measures BD team success in converting prospects to active customers.
 | `[]` | `{}` |
    | `PRACTICE_DEVELOPMENT_GO_LIVES` | 34 | `NUMBER` |  |  | `[]` | `{}` |
    | `OTHER_GO_LIVES` | 35 | `NUMBER` | **Other Attribution Daily Go-Lives**
Count of prospects with Other attribution who achieved go-live status on this date.  Measures miscellaneous source success in converting prospects to active customers.
 | **Other Attribution Daily Go-Lives**
Count of prospects with Other attribution who achieved go-live status on this date.  Measures miscellaneous source success in converting prospects to active customers.
 | `[]` | `{}` |
    | `TOTAL_GO_LIVES_BY_GO_LIVE_SOURCE_60_DAY` | 36 | `NUMBER` | **Total 60-Day Fast Go-Lives**
Count of prospects who achieved go-live on this date AND went live within 60 days  of their qualified opportunity. Measures proportion of "fast" conversions among  total go-lives, indicating sales cycle efficiency.
 | **Total 60-Day Fast Go-Lives**
Count of prospects who achieved go-live on this date AND went live within 60 days  of their qualified opportunity. Measures proportion of "fast" conversions among  total go-lives, indicating sales cycle efficiency.
 | `[]` | `{}` |
    | `SALES_GO_LIVES_BY_GO_LIVE_SOURCE_60_DAY` | 37 | `NUMBER` | **Sales 60-Day Fast Go-Lives**
Count of Sales-attributed prospects who achieved go-live on this date within 60 days  of their qualified opportunity. Measures Sales team conversion speed efficiency.
 | **Sales 60-Day Fast Go-Lives**
Count of Sales-attributed prospects who achieved go-live on this date within 60 days  of their qualified opportunity. Measures Sales team conversion speed efficiency.
 | `[]` | `{}` |
    | `ALLE_GO_LIVES_BY_GO_LIVE_SOURCE_60_DAY` | 38 | `NUMBER` | **Alle 60-Day Fast Go-Lives**
Count of Alle-attributed prospects who achieved go-live on this date within 60 days  of their qualified opportunity. Measures Alle partnership conversion speed efficiency.
 | **Alle 60-Day Fast Go-Lives**
Count of Alle-attributed prospects who achieved go-live on this date within 60 days  of their qualified opportunity. Measures Alle partnership conversion speed efficiency.
 | `[]` | `{}` |
    | `SALES_DEVELOPMENT_GO_LIVES_BY_GO_LIVE_SOURCE_60_DAY` | 39 | `NUMBER` | **Sales Development 60-Day Fast Go-Lives**
Count of Sales Development-attributed prospects who achieved go-live on this date within  60 days of their qualified opportunity. Measures SDR/BDR conversion speed efficiency.
 | **Sales Development 60-Day Fast Go-Lives**
Count of Sales Development-attributed prospects who achieved go-live on this date within  60 days of their qualified opportunity. Measures SDR/BDR conversion speed efficiency.
 | `[]` | `{}` |
    | `MARKETING_GO_LIVES_BY_GO_LIVE_SOURCE_60_DAY` | 40 | `NUMBER` | **Marketing 60-Day Fast Go-Lives**
Count of Marketing-attributed prospects who achieved go-live on this date within 60 days  of their qualified opportunity. Measures Marketing conversion speed efficiency.
 | **Marketing 60-Day Fast Go-Lives**
Count of Marketing-attributed prospects who achieved go-live on this date within 60 days  of their qualified opportunity. Measures Marketing conversion speed efficiency.
 | `[]` | `{}` |
    | `BUSINESS_DEVELOPMENT_GO_LIVES_BY_GO_LIVE_SOURCE_60_DAY` | 41 | `NUMBER` | **Business Development 60-Day Fast Go-Lives**
Count of Business Development-attributed prospects who achieved go-live on this date within  60 days of their qualified opportunity. Measures BD conversion speed efficiency.
 | **Business Development 60-Day Fast Go-Lives**
Count of Business Development-attributed prospects who achieved go-live on this date within  60 days of their qualified opportunity. Measures BD conversion speed efficiency.
 | `[]` | `{}` |
    | `PRACTICE_DEVELOPMENT_GO_LIVES_BY_GO_LIVE_SOURCE_60_DAY` | 42 | `NUMBER` |  |  | `[]` | `{}` |
    | `OTHER_GO_LIVES_BY_GO_LIVE_SOURCE_60_DAY` | 43 | `NUMBER` | **Other 60-Day Fast Go-Lives**
Count of Other-attributed prospects who achieved go-live on this date within 60 days  of their qualified opportunity. Measures miscellaneous source conversion speed efficiency. | **Other 60-Day Fast Go-Lives**
Count of Other-attributed prospects who achieved go-live on this date within 60 days  of their qualified opportunity. Measures miscellaneous source conversion speed efficiency. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.prospect_attribution_summary`
    *   `model.cherry_data_model.pursuit_engagement_summary`
    *   `model.cherry_data_model.sf_user_history`
    *   `model.cherry_data_model.stg_sf_users`

---
