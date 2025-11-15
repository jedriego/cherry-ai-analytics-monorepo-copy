## Model: `ae_onboarding_conversion`

`ae_onboarding_conversion`

*   **Unique ID:** `model.cherry_data_model.ae_onboarding_conversion`
*   **FQN:** `prod.revenue_marts.ae_onboarding_conversion`
*   **Description:** This table consolidates the key metrics and dates related to the onboarding and conversion of accounts, and joins this information with data from the stg_merchants table.
*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `ACCOUNT_ID` | 1 | `TEXT` | The unique identifier for the account. | The unique identifier for the account. | `[]` | `{}` |
    | `SF_ACCOUNT_NAME` | 2 | `TEXT` | The name of the account as per the Salesforce records. | The name of the account as per the Salesforce records. | `[]` | `{}` |
    | `ACCOUNT_INDUSTRY_SEGMENT` | 3 | `TEXT` | The industry segment the account belongs to. | The industry segment the account belongs to. | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_TEAM` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_APPROVAL` | 6 | `DATE` | The date when the merchant was approved. | The date when the merchant was approved. | `[]` | `{}` |
    | `ONBOARDING_COMPLETED` | 7 | `DATE` | The date when the onboarding process was completed. | The date when the onboarding process was completed. | `[]` | `{}` |
    | `GO_LIVE_DATE` | 8 | `DATE` | The date when the merchant went live. | The date when the merchant went live. | `[]` | `{}` |
    | `COALESCED_DATE` | 9 | `DATE` | The coalesced date either from onboarding completion or the go-live date, prioritizing the onboarding completion date. | The coalesced date either from onboarding completion or the go-live date, prioritizing the onboarding completion date. | `[]` | `{}` |
    | `DAYS_IN_MERCHANT_APPROVAL_STAGE` | 10 | `NUMBER` | The number of days spent in the merchant approval stage, calculated as the difference between the merchant approval date and the coalesced date. | The number of days spent in the merchant approval stage, calculated as the difference between the merchant approval date and the coalesced date. | `[]` | `{}` |
    | `CONVERSION_WITHIN_15_DAYS` | 11 | `BOOLEAN` | A boolean flag indicating whether the account completed onboarding within 15 days of merchant approval. | A boolean flag indicating whether the account completed onboarding within 15 days of merchant approval. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.stg_account_milestones`
    *   `model.cherry_data_model.stg_merchants`

---
