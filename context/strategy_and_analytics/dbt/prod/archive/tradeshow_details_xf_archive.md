## Model: `tradeshow_details_xf_archive`

`tradeshow_details_xf_archive`

*   **Unique ID:** `model.cherry_data_model.tradeshow_details_xf_archive`
*   **FQN:** `prod.archive.tradeshow_details_xf_archive`
*   **Description:** This table combines tradeshow related campaign data, lead data, registration data, and loan volume data. It's useful for analyzing the effect of tradeshows on lead generation and business volume.
*   **Tags:** `['archive']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CAMPAIGN_ID` | 1 | `TEXT` | Unique identifier for the campaign | Unique identifier for the campaign | `[]` | `{}` |
    | `CAMPAIGN_NAME` | 2 | `TEXT` | Name of the campaign | Name of the campaign | `[]` | `{}` |
    | `PARENT_CAMPAIGN_ID` | 3 | `TEXT` | Unique identifier for the parent campaign | Unique identifier for the parent campaign | `[]` | `{}` |
    | `PARENT_CAMPAIGN_NAME` | 4 | `TEXT` | Name of the parent campaign | Name of the parent campaign | `[]` | `{}` |
    | `CAMPAIGN_START_DATE` | 5 | `DATE` | Start date of the campaign | Start date of the campaign | `[]` | `{}` |
    | `CAMPAIGN_END_DATE` | 6 | `DATE` | End date of the campaign | End date of the campaign | `[]` | `{}` |
    | `CAMPAIGN_COST` | 7 | `NUMBER` | Total cost associated with the campaign | Total cost associated with the campaign | `[]` | `{}` |
    | `CAMPAIGN_MEMBER_ID` | 8 | `TEXT` | Unique identifier for the campaign member | Unique identifier for the campaign member | `[]` | `{}` |
    | `ACCOUNT_ID` | 9 | `TEXT` | Unique identifier for the account associated with the lead | Unique identifier for the account associated with the lead | `[]` | `{}` |
    | `MERCHANT_ID` | 10 | `FLOAT` | Unique identifier for the merchant | Unique identifier for the merchant | `[]` | `{}` |
    | `LEAD_ID` | 11 | `TEXT` | Unique identifier for the lead | Unique identifier for the lead | `[]` | `{}` |
    | `CONTACT_ID` | 12 | `TEXT` | Unique identifier for the contact associated with the lead | Unique identifier for the contact associated with the lead | `[]` | `{}` |
    | `COMPANY_NAME` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `GO_LIVE_DATE` | 14 | `DATE` | Date when the lead went live | Date when the lead went live | `[]` | `{}` |
    | `REGISTRATION_DATE` | 15 | `TIMESTAMP_NTZ` | Date when the registration was made | Date when the registration was made | `[]` | `{}` |
    | `IS_TRADESHOW_REGISTRATION` | 16 | `BOOLEAN` | Indicates if the registration is associated with a tradeshow (TRUE if the registration date is within 90 days of the campaign start date) | Indicates if the registration is associated with a tradeshow (TRUE if the registration date is within 90 days of the campaign start date) | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 17 | `TEXT` | Industry segment of the lead | Industry segment of the lead | `[]` | `{}` |
    | `TOTAL_GROSS_AMOUNT` | 18 | `FLOAT` | Total gross loan amount for the merchant | Total gross loan amount for the merchant | `[]` | `{}` |
    | `FIRST_7_GROSS_AMOUNT` | 19 | `FLOAT` | Gross loan amount for the merchant in the first 7 days | Gross loan amount for the merchant in the first 7 days | `[]` | `{}` |
    | `FIRST_14_GROSS_AMOUNT` | 20 | `FLOAT` | Gross loan amount for the merchant in the first 14 days | Gross loan amount for the merchant in the first 14 days | `[]` | `{}` |
    | `FIRST_30_GROSS_AMOUNT` | 21 | `FLOAT` | Gross loan amount for the merchant in the first 30 days | Gross loan amount for the merchant in the first 30 days | `[]` | `{}` |
    | `FIRST_60_GROSS_AMOUNT` | 22 | `FLOAT` | Gross loan amount for the merchant in the first 60 days | Gross loan amount for the merchant in the first 60 days | `[]` | `{}` |
    | `FIRST_90_GROSS_AMOUNT` | 23 | `FLOAT` | Gross loan amount for the merchant in the first 90 days | Gross loan amount for the merchant in the first 90 days | `[]` | `{}` |
    | `FIRST_120_GROSS_AMOUNT` | 24 | `FLOAT` | Gross loan amount for the merchant in the first 120 days | Gross loan amount for the merchant in the first 120 days | `[]` | `{}` |
    | `FIRST_365_GROSS_AMOUNT` | 25 | `FLOAT` | Gross loan amount for the merchant in the first 365 days | Gross loan amount for the merchant in the first 365 days | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.merchant_loan_totals`
    *   `model.cherry_data_model.stg_campaigns_and_members`
    *   `model.cherry_data_model.stg_leads`
    *   `model.cherry_data_model.stg_registrations`

---
