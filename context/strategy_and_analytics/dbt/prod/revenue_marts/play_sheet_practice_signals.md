## Model: `play_sheet_practice_signals`

`play_sheet_practice_signals`

*   **Unique ID:** `model.cherry_data_model.play_sheet_practice_signals`
*   **FQN:** `prod.revenue_marts.play_sheet_practice_signals`
*   **Description:** **Recent Account Signals for Retention**
Consolidates key 14-day practice/account activity signals (new users, applications, transactions, case alerts, large approvals, and pricing tier proximity) into a single feed joined to practice context and POC info. Filters signals to those occurring >30 days after go-live.

*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SF_ACCOUNT_ID` | 1 | `TEXT` | Salesforce Account ID for the practice tied to the signal. | Salesforce Account ID for the practice tied to the signal. | `[]` | `{}` |
    | `SF_ACCOUNT_URL` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `CHERRY_MERCHANT_ID` | 3 | `FLOAT` | Cherry merchant ID for the practice (if applicable). | Cherry merchant ID for the practice (if applicable). | `[]` | `{}` |
    | `SIGNAL_TYPE` | 4 | `TEXT` | Categorical signal label, such as new user added or first transaction in over 30 days.
 | Categorical signal label, such as new user added or first transaction in over 30 days.
 | `[]` | `{}` |
    | `SIGNAL_URL` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `SF_ACCOUNT_NAME` | 6 | `TEXT` | Salesforce Account Name for display and routing. | Salesforce Account Name for display and routing. | `[]` | `{}` |
    | `SIGNAL_DATE` | 7 | `DATE` | Date of the signal (PT), used for freshness windows and scheduling. | Date of the signal (PT), used for freshness windows and scheduling. | `[]` | `{}` |
    | `SIGNAL_DETAILS` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT` | 9 | `TEXT` | Department of the current retention owner at the practice. | Department of the current retention owner at the practice. | `[]` | `{}` |
    | `RETENTION_OWNER_TEAM` | 10 | `TEXT` | Team of the current retention owner at the practice. | Team of the current retention owner at the practice. | `[]` | `{}` |
    | `RETENTION_OWNER` | 11 | `TEXT` | Name of the current retention owner. | Name of the current retention owner. | `[]` | `{}` |
    | `RETENTION_OWNER_TITLE` | 12 | `TEXT` | Title of the current retention owner. | Title of the current retention owner. | `[]` | `{}` |
    | `GO_LIVE_DATE` | 13 | `DATE` | Practice go-live date (eligibility to transact). | Practice go-live date (eligibility to transact). | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `POC_NAME` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `POC_EMAIL` | 16 | `TEXT` | Email of the practice POC user from Cherry. | Email of the practice POC user from Cherry. | `[]` | `{}` |
    | `POC_PHONE` | 17 | `TEXT` | Phone of the practice POC user from Cherry. | Phone of the practice POC user from Cherry. | `[]` | `{}` |
    | `LAST_60_VOLUME` | 18 | `FLOAT` | Total funded gross amount in the last 60 days for the practice. | Total funded gross amount in the last 60 days for the practice. | `[]` | `{}` |
    | `LAST_60_APPLICATIONS` | 19 | `NUMBER` | Number of applications in the last 60 days for the practice. | Number of applications in the last 60 days for the practice. | `[]` | `{}` |
    | `LAST_3_EVENTS` | 20 | `TEXT` | Pipe-delimited summary of the three most recent SF events on the account: "YYYY-MM-DD: <Subject> (<Owner Name>)". | Pipe-delimited summary of the three most recent SF events on the account: "YYYY-MM-DD: <Subject> (<Owner Name>)". | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.applications_loans_xf`
    *   `model.cherry_data_model.loan_info_xf`
    *   `model.cherry_data_model.merchant_account_mapping`
    *   `model.cherry_data_model.practice_info_full_xf`
    *   `model.cherry_data_model.pricing_tier_information`
    *   `model.cherry_data_model.src_borrowers`
    *   `model.cherry_data_model.src_cherry_merchant_users`
    *   `model.cherry_data_model.src_cherry_users`
    *   `model.cherry_data_model.src_merchants`
    *   `model.cherry_data_model.src_sf_cases`
    *   `model.cherry_data_model.stg_events`
    *   `model.cherry_data_model.stg_sf_users`

---
