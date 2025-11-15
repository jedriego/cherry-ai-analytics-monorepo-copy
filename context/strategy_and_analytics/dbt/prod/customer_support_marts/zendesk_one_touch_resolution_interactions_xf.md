## Model: `zendesk_one_touch_resolution_interactions_xf`

`zendesk_one_touch_resolution_interactions_xf`

*   **Unique ID:** `model.cherry_data_model.zendesk_one_touch_resolution_interactions_xf`
*   **FQN:** `prod.customer_support_marts.zendesk_one_touch_resolution_interactions_xf`
*   **Description:** This model tracks one-touch resolution metrics for Zendesk support interactions by identifying eligible initial contacts and their subsequent interactions. It determines if issues were resolved in a single contact or if customers needed to reach out again within a defined timeframe.

*   **Tags:** `['customer_support', 'zendesk_refresh']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `INITIAL_CONTACT_ID` | 1 | `NUMBER` | Unique identifier for the first contact in the potential one-touch resolution pair | Unique identifier for the first contact in the potential one-touch resolution pair | `[]` | `{}` |
    | `NEXT_CONVERSATION_ID` | 2 | `NUMBER` | Unique identifier for the subsequent contact from the same customer | Unique identifier for the subsequent contact from the same customer | `[]` | `{}` |
    | `INITIAL_AGENT_NAME` | 3 | `TEXT` | Name of the agent who handled the initial contact | Name of the agent who handled the initial contact | `[]` | `{}` |
    | `INITIAL_AGENT_MANAGER` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `NEXT_AGENT_NAME` | 5 | `TEXT` | Name of the agent who handled the subsequent contact | Name of the agent who handled the subsequent contact | `[]` | `{}` |
    | `INITIAL_MEDIA_TYPE` | 6 | `TEXT` | Channel of communication for the initial contact (Phone, SMS, Chat, Email) | Channel of communication for the initial contact (Phone, SMS, Chat, Email) | `[]` | `{}` |
    | `NEXT_MEDIA_TYPE` | 7 | `TEXT` | Channel of communication for the subsequent contact | Channel of communication for the subsequent contact | `[]` | `{}` |
    | `INITIAL_DISPOSITION_NAME` | 8 | `TEXT` | Disposition code for the initial contact | Disposition code for the initial contact | `[]` | `{}` |
    | `NEXT_DISPOSITION_NAME` | 9 | `TEXT` | Disposition code for the subsequent contact | Disposition code for the subsequent contact | `[]` | `{}` |
    | `INITIAL_PHONE_NUMBER` | 10 | `TEXT` | Phone number associated with the initial contact | Phone number associated with the initial contact | `[]` | `{}` |
    | `INTIAL_EMAIL` | 11 | `TEXT` | Email address associated with the initial contact | Email address associated with the initial contact | `[]` | `{}` |
    | `INITIAL_MERCHANT_ID` | 12 | `TEXT` | Merchant ID associated with the initial contact | Merchant ID associated with the initial contact | `[]` | `{}` |
    | `INTIAL_BORROWER_ID` | 13 | `TEXT` | Borrower ID associated with the initial contact | Borrower ID associated with the initial contact | `[]` | `{}` |
    | `INTERACTION_MATCHING_KEY` | 14 | `TEXT` | Key used to match related interactions from the same customer, usually the borrower or merchant ID, if missing the email or phone number. | Key used to match related interactions from the same customer, usually the borrower or merchant ID, if missing the email or phone number. | `[]` | `{}` |
    | `INITIAL_INTERACTION_BEGIN` | 15 | `TIMESTAMP_NTZ` | Timestamp when the initial contact started | Timestamp when the initial contact started | `[]` | `{}` |
    | `NEXT_INTERACTION_BEGIN` | 16 | `TIMESTAMP_NTZ` | Timestamp when the subsequent contact started | Timestamp when the subsequent contact started | `[]` | `{}` |
    | `INITIAL_INTERACTION_NUMBER` | 17 | `NUMBER` | Sequence number of the initial interaction for the customer | Sequence number of the initial interaction for the customer | `[]` | `{}` |
    | `NEXT_INTERACTION_NUMBER` | 18 | `NUMBER` | Sequence number of the subsequent interaction for the customer | Sequence number of the subsequent interaction for the customer | `[]` | `{}` |
    | `IS_ONE_TOUCH_FOUR_ELIGIBLE` | 19 | `BOOLEAN` | Boolean indicating if the initial contact is eligible for one-touch resolution tracking | Boolean indicating if the initial contact is eligible for one-touch resolution tracking | `[]` | `{}` |
    | `TIME_DIFFERENCE` | 20 | `NUMBER` | Time difference in days between the initial and subsequent contacts | Time difference in days between the initial and subsequent contacts | `[]` | `{}` |
    | `OUTBOUND_IN_BETWEEN_IND` | 21 | `NUMBER` | Count of outbound contacts made to the customer between the initial and subsequent contacts | Count of outbound contacts made to the customer between the initial and subsequent contacts | `[]` | `{}` |
    | `SMS_IN_BETWEEN_IND` | 22 | `NUMBER` | Count of outbound SMS messages sent to the customer between the initial and subsequent contacts | Count of outbound SMS messages sent to the customer between the initial and subsequent contacts | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.src_borrowers`
    *   `model.cherry_data_model.stg_sms_notifications`
    *   `model.cherry_data_model.stg_zendesk_one_touch_eligible_contacts`
    *   `model.cherry_data_model.stg_zendesk_tickets`
    *   `seed.cherry_data_model.ops_user_teams`

---
