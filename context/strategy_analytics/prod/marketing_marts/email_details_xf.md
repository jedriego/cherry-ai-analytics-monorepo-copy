## Model: `email_details_xf`

`email_details_xf`

*   **Unique ID:** `model.cherry_data_model.email_details_xf`
*   **FQN:** `prod.marketing_marts.email_details_xf`
*   **Description:** **Comprehensive Email Marketing Performance Analytics**
This model serves as Cherry's definitive source for email marketing performance analysis, combining  SendGrid email delivery and engagement data with sophisticated lead attribution and prospect engagement  tracking. It provides complete visibility into email campaign effectiveness, lead conversion impact,  and engagement patterns across both batch campaigns and transactional emails.
**Key Business Logic:** - **Email Filtering**: Includes only delivered emails that are marketing-relevant (Single Send campaigns 
  or marketing-classified transactional emails)
- **Lead Matching**: Advanced email-to-lead matching using multiple data sources and prioritization logic - **Attribution Integration**: Incorporates fractional channel attribution with viewthrough credit to 
  measure email's role in lead generation
- **Engagement Tracking**: Tracks prospect engagement patterns before and after email delivery with 
  sophisticated timing analysis (3-day impact windows)
- **Campaign Correlation**: Links email campaigns to lead forms and demo bookings through UTM tracking
**Email Type Coverage:** - Single Send batch campaigns with audience targeting and scheduling - Marketing-relevant transactional emails (welcome, nurture, alerts) - Excludes non-marketing transactional emails and undelivered messages
**Primary Use Cases:** - Email campaign performance analysis and optimization - Lead attribution and conversion impact measurement - Prospect engagement pattern analysis and segmentation - Email marketing ROI calculation and channel contribution analysis - Campaign timing and frequency optimization

*   **Tags:** `['marketing_analytics', 'marketing', 'email', 'lead', 'demo', 'prospect', 'engagement']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `MESSAGE_ID` | 1 | `TEXT` | **SendGrid Message Identifier** - Unique SendGrid ID for each specific email sent to each recipient.  Primary key combining email campaign and individual recipient. Used for email event tracking and  performance analysis. Never NULL for delivered emails. Sourced from stg_sendgrid_emails.
 | **SendGrid Message Identifier** - Unique SendGrid ID for each specific email sent to each recipient.  Primary key combining email campaign and individual recipient. Used for email event tracking and  performance analysis. Never NULL for delivered emails. Sourced from stg_sendgrid_emails.
 | `[]` | `{}` |
    | `SINGLESEND_ID` | 2 | `TEXT` | **SendGrid Single Send Campaign ID** - SendGrid identifier for batch email campaigns. Present for  scheduled marketing campaigns but NULL for transactional emails. Used for campaign-level analysis  and performance tracking. Sourced from stg_sendgrid_emails.
 | **SendGrid Single Send Campaign ID** - SendGrid identifier for batch email campaigns. Present for  scheduled marketing campaigns but NULL for transactional emails. Used for campaign-level analysis  and performance tracking. Sourced from stg_sendgrid_emails.
 | `[]` | `{}` |
    | `TEMPLATE_ID` | 3 | `TEXT` | **SendGrid Template Identifier** - SendGrid template ID used for email design and content. Present  for transactional emails and some campaign emails. Used for template performance analysis and A/B  testing. Sourced from stg_sendgrid_emails.
 | **SendGrid Template Identifier** - SendGrid template ID used for email design and content. Present  for transactional emails and some campaign emails. Used for template performance analysis and A/B  testing. Sourced from stg_sendgrid_emails.
 | `[]` | `{}` |
    | `MAILING_ID` | 4 | `TEXT` | **Unified Mailing Identifier** - Surrogate key created from singlesend_id and template_id to enable  consistent joins across both Single Send campaigns and transactional emails. Simplifies cross-email-type  analysis and reporting. Used for unified email performance tracking. Sourced from stg_sendgrid_emails.
 | **Unified Mailing Identifier** - Surrogate key created from singlesend_id and template_id to enable  consistent joins across both Single Send campaigns and transactional emails. Simplifies cross-email-type  analysis and reporting. Used for unified email performance tracking. Sourced from stg_sendgrid_emails.
 | `[]` | `{}` |
    | `EMAIL_TYPE` | 5 | `TEXT` | **Email Send Type** - Classification of email based on SendGrid fields: 'Single Send' for batch  campaigns with audience targeting, 'Transactional' for automated trigger-based emails. Used for  email type analysis and performance segmentation. Sourced from stg_sendgrid_emails.
 | **Email Send Type** - Classification of email based on SendGrid fields: 'Single Send' for batch  campaigns with audience targeting, 'Transactional' for automated trigger-based emails. Used for  email type analysis and performance segmentation. Sourced from stg_sendgrid_emails.
 | `[]` | `{}` |
    | `IS_MARKETING_TRANSACTIONAL_EMAIL` | 6 | `BOOLEAN` | **Marketing Transactional Flag** - Boolean indicating whether a transactional email is classified  as marketing-relevant (vs. purely operational). Used to filter transactional emails for marketing  analysis. FALSE for Single Send emails, varies for transactional. Sourced from stg_sendgrid_emails.
 | **Marketing Transactional Flag** - Boolean indicating whether a transactional email is classified  as marketing-relevant (vs. purely operational). Used to filter transactional emails for marketing  analysis. FALSE for Single Send emails, varies for transactional. Sourced from stg_sendgrid_emails.
 | `[]` | `{}` |
    | `MESSAGE_NAME` | 7 | `TEXT` | **Campaign Name** - Human-readable name assigned to the email campaign by the sender in SendGrid.  Used for campaign identification and performance tracking across similar campaign types. Sourced  from stg_sendgrid_emails.
 | **Campaign Name** - Human-readable name assigned to the email campaign by the sender in SendGrid.  Used for campaign identification and performance tracking across similar campaign types. Sourced  from stg_sendgrid_emails.
 | `[]` | `{}` |
    | `MESSAGE_TYPE` | 8 | `TEXT` | **Message Type Classification** - Detailed categorization of email content based on message name  keyword analysis (e.g., 'welcome', 'newsletter', 'nurture'). Used for content type performance  analysis and messaging strategy optimization. Derived from message name logic in stg_sendgrid_emails.
 | **Message Type Classification** - Detailed categorization of email content based on message name  keyword analysis (e.g., 'welcome', 'newsletter', 'nurture'). Used for content type performance  analysis and messaging strategy optimization. Derived from message name logic in stg_sendgrid_emails.
 | `[]` | `{}` |
    | `MESSAGE_SEND_DATETIME_PT` | 9 | `TIMESTAMP_TZ` | **Campaign Send Time (Pacific)** - Pacific Time timestamp when the email campaign was initiated.  Represents batch send time, not individual delivery time. Used for send timing analysis and  campaign scheduling optimization. Sourced from stg_sendgrid_emails.
 | **Campaign Send Time (Pacific)** - Pacific Time timestamp when the email campaign was initiated.  Represents batch send time, not individual delivery time. Used for send timing analysis and  campaign scheduling optimization. Sourced from stg_sendgrid_emails.
 | `[]` | `{}` |
    | `UTM_CAMPAIGN` | 10 | `TEXT` | **UTM Campaign Code** - Primary campaign tracking code extracted from URLs clicked in the email.  Used for campaign attribution and cross-channel campaign tracking. NULL when no clicks or UTM  parameters present. Sourced from stg_sendgrid_emails click tracking.
 | **UTM Campaign Code** - Primary campaign tracking code extracted from URLs clicked in the email.  Used for campaign attribution and cross-channel campaign tracking. NULL when no clicks or UTM  parameters present. Sourced from stg_sendgrid_emails click tracking.
 | `[]` | `{}` |
    | `EMAIL` | 11 | `TEXT` | **Recipient Email Address** - Email address of the message recipient. Used for recipient identification,  lead matching, and delivery analysis. Critical for linking emails to lead and prospect data.  Sourced from stg_sendgrid_emails.
 | **Recipient Email Address** - Email address of the message recipient. Used for recipient identification,  lead matching, and delivery analysis. Critical for linking emails to lead and prospect data.  Sourced from stg_sendgrid_emails.
 | `[]` | `{}` |
    | `SUBJECT` | 12 | `TEXT` | **Email Subject Line** - Subject line text seen by recipients in their inbox. Used for subject  line performance analysis, A/B testing, and open rate optimization. Sourced from stg_sendgrid_emails.
 | **Email Subject Line** - Subject line text seen by recipients in their inbox. Used for subject  line performance analysis, A/B testing, and open rate optimization. Sourced from stg_sendgrid_emails.
 | `[]` | `{}` |
    | `LAST_PRIOR_OPEN_DATETIME_PT` | 13 | `TIMESTAMP_TZ` | **Previous Open Time (Pacific)** - Pacific Time timestamp of the recipient's last email open  prior to this specific email delivery. Used for engagement recency segmentation and email frequency  analysis. NULL for first-time recipients. Sourced from stg_sendgrid_emails engagement history.
 | **Previous Open Time (Pacific)** - Pacific Time timestamp of the recipient's last email open  prior to this specific email delivery. Used for engagement recency segmentation and email frequency  analysis. NULL for first-time recipients. Sourced from stg_sendgrid_emails engagement history.
 | `[]` | `{}` |
    | `DAYS_SINCE_LAST_OPEN` | 14 | `NUMBER` | **Days Since Last Email Open** - Number of days between the recipient's last prior email open  and this email's delivery. Used for engagement recency analysis and re-engagement campaign targeting.  NULL for first-time recipients. Calculated from date difference logic.
 | **Days Since Last Email Open** - Number of days between the recipient's last prior email open  and this email's delivery. Used for engagement recency analysis and re-engagement campaign targeting.  NULL for first-time recipients. Calculated from date difference logic.
 | `[]` | `{}` |
    | `PROCESSED_DATETIME_PT` | 15 | `TIMESTAMP_TZ` | **Processing Time (Pacific)** - Pacific Time when SendGrid processed the email for delivery.  First stage in email delivery pipeline before actual sending. Used for processing performance  analysis and delivery timeline tracking. Sourced from stg_sendgrid_emails.
 | **Processing Time (Pacific)** - Pacific Time when SendGrid processed the email for delivery.  First stage in email delivery pipeline before actual sending. Used for processing performance  analysis and delivery timeline tracking. Sourced from stg_sendgrid_emails.
 | `[]` | `{}` |
    | `DROPPED_DATETIME_PT` | 16 | `TIMESTAMP_TZ` | **Drop Time (Pacific)** - Pacific Time when email was dropped by SendGrid due to policy violations,  unsubscribe status, or other blocking factors. NULL for successfully processed emails. Used for  delivery issue analysis and list hygiene. Sourced from stg_sendgrid_emails.
 | **Drop Time (Pacific)** - Pacific Time when email was dropped by SendGrid due to policy violations,  unsubscribe status, or other blocking factors. NULL for successfully processed emails. Used for  delivery issue analysis and list hygiene. Sourced from stg_sendgrid_emails.
 | `[]` | `{}` |
    | `BOUNCED_DATETIME_PT` | 17 | `TIMESTAMP_TZ` | **Bounce Time (Pacific)** - Pacific Time when email bounced due to invalid address or delivery  failure. NULL for successful deliveries. Used for list quality analysis and deliverability tracking.  Sourced from stg_sendgrid_emails.
 | **Bounce Time (Pacific)** - Pacific Time when email bounced due to invalid address or delivery  failure. NULL for successful deliveries. Used for list quality analysis and deliverability tracking.  Sourced from stg_sendgrid_emails.
 | `[]` | `{}` |
    | `REASON_NOT_DELIVERED` | 18 | `TEXT` | **Non-Delivery Reason** - Text explanation for why email was not delivered (bounce reason, drop  reason, policy violation). Used for deliverability issue analysis and list cleanup. NULL for  successfully delivered emails. Sourced from stg_sendgrid_emails.
 | **Non-Delivery Reason** - Text explanation for why email was not delivered (bounce reason, drop  reason, policy violation). Used for deliverability issue analysis and list cleanup. NULL for  successfully delivered emails. Sourced from stg_sendgrid_emails.
 | `[]` | `{}` |
    | `DELIVERED_DATETIME_PT` | 19 | `TIMESTAMP_TZ` | **Delivery Time (Pacific)** - Pacific Time when email was successfully delivered to recipient's  inbox. Critical timestamp for engagement analysis and impact measurement. Only delivered emails  are included in this model. Used for all timing-based analysis. Sourced from stg_sendgrid_emails.
 | **Delivery Time (Pacific)** - Pacific Time when email was successfully delivered to recipient's  inbox. Critical timestamp for engagement analysis and impact measurement. Only delivered emails  are included in this model. Used for all timing-based analysis. Sourced from stg_sendgrid_emails.
 | `[]` | `{}` |
    | `OPENED_DATETIME_PT` | 20 | `TIMESTAMP_TZ` | **First Open Time (Pacific)** - Pacific Time when recipient first opened the email. Excludes  opens within 20 seconds of delivery (considered automatic/not genuine engagement). NULL if never  opened. Used for open rate analysis and engagement timing. Sourced from stg_sendgrid_emails.
 | **First Open Time (Pacific)** - Pacific Time when recipient first opened the email. Excludes  opens within 20 seconds of delivery (considered automatic/not genuine engagement). NULL if never  opened. Used for open rate analysis and engagement timing. Sourced from stg_sendgrid_emails.
 | `[]` | `{}` |
    | `CLICKED_DATETIME_PT` | 21 | `TIMESTAMP_TZ` | **First Click Time (Pacific)** - Pacific Time when recipient first clicked any link in the email.  Indicates strong engagement and intent. NULL if never clicked. Used for click-through analysis  and conversion tracking. Sourced from stg_sendgrid_emails.
 | **First Click Time (Pacific)** - Pacific Time when recipient first clicked any link in the email.  Indicates strong engagement and intent. NULL if never clicked. Used for click-through analysis  and conversion tracking. Sourced from stg_sendgrid_emails.
 | `[]` | `{}` |
    | `UNSUBSCRIBED_DATETIME_PT` | 22 | `TIMESTAMP_TZ` | **Unsubscribe Time (Pacific)** - Pacific Time when recipient first unsubscribed from emails  through this message. Used for unsubscribe analysis and list management. NULL if no unsubscribe  action. Sourced from stg_sendgrid_emails.
 | **Unsubscribe Time (Pacific)** - Pacific Time when recipient first unsubscribed from emails  through this message. Used for unsubscribe analysis and list management. NULL if no unsubscribe  action. Sourced from stg_sendgrid_emails.
 | `[]` | `{}` |
    | `EMAIL_MAILING_DELIVERED_ORDER` | 23 | `NUMBER` | **Email Delivery Order** - Sequential number indicating which delivery this is for this email  address receiving this specific mailing (1 = first time, 2 = second time, etc.). Used for frequency  analysis and repeated send tracking. Sourced from stg_sendgrid_emails ranking logic.
 | **Email Delivery Order** - Sequential number indicating which delivery this is for this email  address receiving this specific mailing (1 = first time, 2 = second time, etc.). Used for frequency  analysis and repeated send tracking. Sourced from stg_sendgrid_emails ranking logic.
 | `[]` | `{}` |
    | `EMAIL_MAILING_DELIVERED_RECENCY` | 24 | `NUMBER` | **Email Delivery Recency Rank** - Reverse sequential ranking where most recent delivery of this  mailing to this email is 1, second most recent is 2, etc. Used for recent delivery analysis and  frequency impact assessment. Sourced from stg_sendgrid_emails recency ranking.
 | **Email Delivery Recency Rank** - Reverse sequential ranking where most recent delivery of this  mailing to this email is 1, second most recent is 2, etc. Used for recent delivery analysis and  frequency impact assessment. Sourced from stg_sendgrid_emails recency ranking.
 | `[]` | `{}` |
    | `LEAD_ID` | 25 | `TEXT` | **Salesforce Lead Identifier** - Salesforce lead ID matched to the email recipient through sophisticated  email mapping logic across multiple data sources. NULL when no lead match found. Critical for lead  attribution and conversion analysis. Sourced from stg_sendgrid_emails lead matching.
 | **Salesforce Lead Identifier** - Salesforce lead ID matched to the email recipient through sophisticated  email mapping logic across multiple data sources. NULL when no lead match found. Critical for lead  attribution and conversion analysis. Sourced from stg_sendgrid_emails lead matching.
 | `[]` | `{}` |
    | `ACCOUNT_ID` | 26 | `TEXT` | **Salesforce Account Identifier** - Salesforce account ID linked to the email recipient when lead  converts to account or direct account match exists. Used for account-level email analysis and  customer journey tracking. Sourced from stg_sendgrid_emails account mapping.
 | **Salesforce Account Identifier** - Salesforce account ID linked to the email recipient when lead  converts to account or direct account match exists. Used for account-level email analysis and  customer journey tracking. Sourced from stg_sendgrid_emails account mapping.
 | `[]` | `{}` |
    | `PRACTICE_NAME` | 27 | `TEXT` |  |  | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 28 | `TEXT` |  |  | `[]` | `{}` |
    | `LEAD_CREATED_DATE` | 29 | `TIMESTAMP_NTZ` | **Lead Creation Date (Pacific)** - Date when the matched Salesforce lead was created. Used for  lead lifecycle analysis and email impact on lead generation timing. NULL when no lead match.  Sourced from stg_sendgrid_emails lead data integration.
 | **Lead Creation Date (Pacific)** - Date when the matched Salesforce lead was created. Used for  lead lifecycle analysis and email impact on lead generation timing. NULL when no lead match.  Sourced from stg_sendgrid_emails lead data integration.
 | `[]` | `{}` |
    | `EMAIL_DELIVERED_AFTER_LEAD_CREATED` | 30 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `HAS_LEAD_ID` | 31 | `BOOLEAN` | **Lead Match Flag** - Boolean indicating whether the email recipient was successfully matched to  a Salesforce lead. Used for match rate analysis and lead coverage assessment. Critical filter  for lead-focused email analysis. Sourced from stg_sendgrid_emails matching logic.
 | **Lead Match Flag** - Boolean indicating whether the email recipient was successfully matched to  a Salesforce lead. Used for match rate analysis and lead coverage assessment. Critical filter  for lead-focused email analysis. Sourced from stg_sendgrid_emails matching logic.
 | `[]` | `{}` |
    | `WAS_PROSPECT` | 32 | `BOOLEAN` | **Prospect Status Flag** - Boolean indicating whether the email recipient was ever identified as  a prospect (engaged lead before first demo). Used for prospect analysis and targeting effectiveness.  Sourced from stg_sendgrid_emails prospect classification.
 | **Prospect Status Flag** - Boolean indicating whether the email recipient was ever identified as  a prospect (engaged lead before first demo). Used for prospect analysis and targeting effectiveness.  Sourced from stg_sendgrid_emails prospect classification.
 | `[]` | `{}` |
    | `EMAIL_CAMPAIGN_MATCHES_LEAD_FORM` | 33 | `BOOLEAN` | **Lead Form Campaign Match** - Boolean indicating whether the matched lead submitted their lead  form from a URL containing the same UTM campaign as this email. Used for direct email attribution  to lead generation. Sourced from stg_sendgrid_emails campaign correlation logic.
 | **Lead Form Campaign Match** - Boolean indicating whether the matched lead submitted their lead  form from a URL containing the same UTM campaign as this email. Used for direct email attribution  to lead generation. Sourced from stg_sendgrid_emails campaign correlation logic.
 | `[]` | `{}` |
    | `FIRST_DEMO_SCHEDULE_DATETIME_PT` | 34 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `LEAD_CREATED_WITHIN_3_DAYS` | 35 | `BOOLEAN` | **3-Day Lead Creation Flag** - Boolean indicating whether the matched lead was created within 3  days of email delivery. Used for measuring email's direct impact on lead generation and conversion  timing analysis. Sourced from stg_sendgrid_emails timing logic.
 | **3-Day Lead Creation Flag** - Boolean indicating whether the matched lead was created within 3  days of email delivery. Used for measuring email's direct impact on lead generation and conversion  timing analysis. Sourced from stg_sendgrid_emails timing logic.
 | `[]` | `{}` |
    | `DEMO_SCHEDULED_WITHIN_3_DAYS` | 36 | `BOOLEAN` | **3-Day Demo Scheduling Flag** - Boolean indicating whether the matched lead's first demo was  scheduled within 3 days of email delivery. Used for measuring email's direct impact on demo  conversion and sales funnel acceleration. Sourced from stg_sendgrid_emails timing logic.
 | **3-Day Demo Scheduling Flag** - Boolean indicating whether the matched lead's first demo was  scheduled within 3 days of email delivery. Used for measuring email's direct impact on demo  conversion and sales funnel acceleration. Sourced from stg_sendgrid_emails timing logic.
 | `[]` | `{}` |
    | `IS_TO_EMPLOYEE` | 37 | `BOOLEAN` | **Employee Email Flag** - Boolean indicating whether the email was sent to a Cherry employee  (detected by @withcherry.com domain). Used to exclude internal emails from marketing performance  analysis. Sourced from stg_sendgrid_emails email domain analysis.
 | **Employee Email Flag** - Boolean indicating whether the email was sent to a Cherry employee  (detected by @withcherry.com domain). Used to exclude internal emails from marketing performance  analysis. Sourced from stg_sendgrid_emails email domain analysis.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.base_sendgrid_unified`
    *   `model.cherry_data_model.lead_demos_summary`
    *   `model.cherry_data_model.map_emails_to_prospects`
    *   `model.cherry_data_model.practice_prospects`
    *   `model.cherry_data_model.sendgrid_event_details`
    *   `model.cherry_data_model.sendgrid_transactional_emails`
    *   `model.cherry_data_model.stg_leads`

---
