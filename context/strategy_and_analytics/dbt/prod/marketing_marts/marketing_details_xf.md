## Model: `marketing_details_xf`

`marketing_details_xf`

*   **Unique ID:** `model.cherry_data_model.marketing_details_xf`
*   **FQN:** `prod.marketing_marts.marketing_details_xf`
*   **Description:** Comprehensive marketing engagement summary combining email, direct mail, paid search, 
social media, referrals, and form submissions. This is a critical model for marketing 
reporting and attribution analysis.

*   **Tags:** `['marketing_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `PROSPECT_ID` | 1 | `TEXT` | Unique identifier for the prospect (can appear multiple times due to multiple pursuits and multi-touch attribution) | Unique identifier for the prospect (can appear multiple times due to multiple pursuits and multi-touch attribution) | `[]` | `{}` |
    | `PROSPECT_TYPE` | 2 | `TEXT` | Type of prospect (Lead or Account) | Type of prospect (Lead or Account) | `[]` | `{}` |
    | `PRACTICE_NAME` | 3 | `TEXT` | Name of the practice | Name of the practice | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 4 | `TEXT` | Industry segment classification | Industry segment classification | `[]` | `{}` |
    | `INDUSTRY` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `PHONE` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `EMAIL` | 7 | `TEXT` | Primary email address | Primary email address | `[]` | `{}` |
    | `WEBSITE` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `PURSUIT_ID` | 9 | `TEXT` | Unique identifier for the pursuit/opportunity | Unique identifier for the pursuit/opportunity | `[]` | `{}` |
    | `PURSUIT_TYPE` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `PURSUIT_OWNER_NAME` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `PURSUIT_OWNER_TEAM` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `PURSUIT_OWNER_DEPARTMENT` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `PURSUIT_START_DATE` | 14 | `DATE` | Start date of the pursuit | Start date of the pursuit | `[]` | `{}` |
    | `QUALIFIED_OPPORTUNITY_DATETIME_PT` | 15 | `TIMESTAMP_NTZ` | When the prospect became a qualified opportunity | When the prospect became a qualified opportunity | `[]` | `{}` |
    | `FIRST_SCHEDULED_DEMO_DATETIME_PT` | 16 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `PRIMARY_DEMO_DATETIME_PT` | 17 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `GO_LIVE_DATE` | 18 | `DATE` |  |  | `[]` | `{}` |
    | `CURRENT_MILESTONE` | 19 | `TEXT` | Current stage in the sales process | Current stage in the sales process | `[]` | `{}` |
    | `QUALIFIED_OPPORTUNITY_SOURCE` | 20 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_MARKETING_ASSISTED_QUALIFIED_OPPORTUNITY` | 21 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `QUALIFIED_OPPORTUNITY_TYPE` | 22 | `TEXT` |  |  | `[]` | `{}` |
    | `TOTAL_EMAILS_DELIVERED` | 23 | `NUMBER` | Total count of emails delivered | Total count of emails delivered | `[]` | `{}` |
    | `TOTAL_EMAILS_OPENED` | 24 | `NUMBER` | Total count of emails opened | Total count of emails opened | `[]` | `{}` |
    | `TOTAL_EMAILS_CLICKED` | 25 | `NUMBER` | Total count of emails clicked | Total count of emails clicked | `[]` | `{}` |
    | `FIRST_EMAIL_DELIVERED_DATETIME_PT` | 26 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `LAST_EMAIL_DELIVERED_DATETIME_PT` | 27 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `FIRST_EMAIL_OPENED_DATETIME_PT` | 28 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `LAST_EMAIL_OPENED_DATETIME_PT` | 29 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `EMAIL_OPEN_RATE` | 30 | `NUMBER` | Percentage of delivered emails that were opened | Percentage of delivered emails that were opened | `[]` | `{}` |
    | `EMAIL_CLICK_RATE` | 31 | `NUMBER` | Percentage of delivered emails that were clicked | Percentage of delivered emails that were clicked | `[]` | `{}` |
    | `PROSPECT_NEWSLETTER_COUNT` | 32 | `NUMBER` |  |  | `[]` | `{}` |
    | `PROSPECT_NEWSLETTER_OPENS` | 33 | `NUMBER` |  |  | `[]` | `{}` |
    | `EMAILS_DELIVERED_LAST_30_DAYS` | 34 | `NUMBER` | Emails delivered in last 30 days | Emails delivered in last 30 days | `[]` | `{}` |
    | `EMAILS_OPENED_LAST_30_DAYS` | 35 | `NUMBER` | Emails opened in last 30 days | Emails opened in last 30 days | `[]` | `{}` |
    | `EMAILS_DELIVERED_LAST_90_DAYS` | 36 | `NUMBER` | Emails delivered in last 90 days | Emails delivered in last 90 days | `[]` | `{}` |
    | `TOTAL_DIRECT_MAIL_SENT` | 37 | `NUMBER` | Total direct mail pieces sent | Total direct mail pieces sent | `[]` | `{}` |
    | `FIRST_DIRECT_MAIL_DATE` | 38 | `DATE` |  |  | `[]` | `{}` |
    | `LAST_DIRECT_MAIL_DATE` | 39 | `DATE` |  |  | `[]` | `{}` |
    | `DIRECT_MAIL_SENT_LAST_90_DAYS` | 40 | `NUMBER` | Direct mail sent in last 90 days | Direct mail sent in last 90 days | `[]` | `{}` |
    | `REFERRAL_SUBMISSION_DATETIME_PT` | 41 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `REFERRER_NAME` | 42 | `TEXT` | Name of the person who made the referral | Name of the person who made the referral | `[]` | `{}` |
    | `REFERRER_EMAIL` | 43 | `TEXT` |  |  | `[]` | `{}` |
    | `REFERRER_TYPE` | 44 | `TEXT` |  |  | `[]` | `{}` |
    | `REFERRAL_QUALIFICATION_STATUS` | 45 | `TEXT` | Status of referral qualification | Status of referral qualification | `[]` | `{}` |
    | `REFERRAL_PAYMENT_STATUS` | 46 | `TEXT` | Status of referral payment | Status of referral payment | `[]` | `{}` |
    | `REFERRAL_PAYOUT_AMOUNT` | 47 | `NUMBER` | Amount paid for referral | Amount paid for referral | `[]` | `{}` |
    | `TOTAL_FORM_SUBMISSIONS` | 48 | `NUMBER` | Total form submissions | Total form submissions | `[]` | `{}` |
    | `FIRST_FORM_SUBMISSION_DATETIME_PT` | 49 | `TIMESTAMP_NTZ` | Timestamp of first form submission | Timestamp of first form submission | `[]` | `{}` |
    | `LAST_FORM_SUBMISSION_DATETIME_PT` | 50 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `FIRST_FORM_UTM_SOURCE` | 51 | `TEXT` |  |  | `[]` | `{}` |
    | `FIRST_FORM_UTM_MEDIUM` | 52 | `TEXT` |  |  | `[]` | `{}` |
    | `FIRST_FORM_UTM_CAMPAIGN` | 53 | `TEXT` |  |  | `[]` | `{}` |
    | `PAID_SEARCH_CLICKS` | 54 | `NUMBER` | Total paid search clicks | Total paid search clicks | `[]` | `{}` |
    | `FIRST_PAID_SEARCH_CLICK_DATETIME_PT` | 55 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `LAST_PAID_SEARCH_CLICK_DATETIME_PT` | 56 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `PAID_SEARCH_CLICKS_LAST_30_DAYS` | 57 | `NUMBER` | Paid search clicks in last 30 days | Paid search clicks in last 30 days | `[]` | `{}` |
    | `GOOGLE_ADS_CLICKS` | 58 | `NUMBER` | Clicks from Google Ads specifically | Clicks from Google Ads specifically | `[]` | `{}` |
    | `SOCIAL_MEDIA_CLICKS` | 59 | `NUMBER` | Total social media clicks | Total social media clicks | `[]` | `{}` |
    | `FIRST_SOCIAL_CLICK_DATETIME_PT` | 60 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `LAST_SOCIAL_CLICK_DATETIME_PT` | 61 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `SOCIAL_CLICKS_LAST_30_DAYS` | 62 | `NUMBER` | Social clicks in last 30 days | Social clicks in last 30 days | `[]` | `{}` |
    | `QUALIFIED_OPPORTUNITY_ENGAGEMENT_SCORE` | 63 | `NUMBER` | Marketing engagement score at qualified opportunity stage | Marketing engagement score at qualified opportunity stage | `[]` | `{}` |
    | `QUALIFIED_OPPORTUNITY_TOP_SOURCE` | 64 | `TEXT` | Primary engagement source that contributed to qualified opportunity (enables multi-touch attribution) | Primary engagement source that contributed to qualified opportunity (enables multi-touch attribution) | `[]` | `{}` |
    | `HAS_MARKETING_ENGAGEMENT` | 65 | `BOOLEAN` | Flag indicating any marketing engagement | Flag indicating any marketing engagement | `[]` | `{}` |
    | `HAS_RECENT_MARKETING_ENGAGEMENT` | 66 | `BOOLEAN` | Flag indicating marketing engagement in last 30 days | Flag indicating marketing engagement in last 30 days | `[]` | `{}` |
    | `IS_INBOUND_QUALIFIED_OPPORTUNITY` | 67 | `BOOLEAN` | Flag indicating qualified opportunity came from inbound source | Flag indicating qualified opportunity came from inbound source | `[]` | `{}` |
    | `ENGAGED_CHANNELS` | 68 | `TEXT` | Comma-separated list of channels where prospect engaged | Comma-separated list of channels where prospect engaged | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.direct_mail_automated_incremental`
    *   `model.cherry_data_model.email_details_xf`
    *   `model.cherry_data_model.practice_prospects`
    *   `model.cherry_data_model.pursuit_engagement_score_summary`
    *   `model.cherry_data_model.pursuit_engagement_summary`
    *   `model.cherry_data_model.src_sf_inbound_forms`
    *   `model.cherry_data_model.stg_paid_search_attribution_engagement`
    *   `model.cherry_data_model.stg_referral_info`
    *   `model.cherry_data_model.stg_social_search_attribution_engagements`

---
