## Model: `unified_one_touch_resolution_xf`

`unified_one_touch_resolution_xf`

*   **Unique ID:** `model.cherry_data_model.unified_one_touch_resolution_xf`
*   **FQN:** `prod.customer_support_marts.unified_one_touch_resolution_xf`
*   **Description:** Unified model that combines NICE and Zendesk one-touch resolution metrics. This model tracks one-touch resolution by identifying eligible initial contacts and their subsequent interactions. It determines if issues were resolved in a single contact or if customers needed to reach out again within a defined timeframe. Provides a single source of truth for one-touch resolution metrics across both contact center platforms.

*   **Tags:** `['customer_support']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_SYSTEM` | 1 | `TEXT` | Source system for the record ('NICE' or 'ZENDESK') | Source system for the record ('NICE' or 'ZENDESK') | `[]` | `{}` |
    | `INITIAL_CONTACT_ID` | 2 | `NUMBER` | Unique identifier for the first contact in the potential one-touch resolution pair | Unique identifier for the first contact in the potential one-touch resolution pair | `[]` | `{}` |
    | `NEXT_CONVERSATION_ID` | 3 | `NUMBER` | Unique identifier for the subsequent contact from the same customer | Unique identifier for the subsequent contact from the same customer | `[]` | `{}` |
    | `INITIAL_SKILL` | 4 | `TEXT` | NICE-specific initial skill/queue the first contact was routed to (NULL for Zendesk) | NICE-specific initial skill/queue the first contact was routed to (NULL for Zendesk) | `[]` | `{}` |
    | `NEXT_SKILL` | 5 | `TEXT` | NICE-specific skill/queue the subsequent contact was routed to (NULL for Zendesk) | NICE-specific skill/queue the subsequent contact was routed to (NULL for Zendesk) | `[]` | `{}` |
    | `INITIAL_AGENT_NAME` | 6 | `TEXT` | Name of the agent who handled the initial contact | Name of the agent who handled the initial contact | `[]` | `{}` |
    | `NEXT_AGENT_NAME` | 7 | `TEXT` | Name of the agent who handled the subsequent contact | Name of the agent who handled the subsequent contact | `[]` | `{}` |
    | `INITIAL_MEDIA_TYPE` | 8 | `TEXT` | Channel of communication for the initial contact (Phone, SMS, Chat, Email) | Channel of communication for the initial contact (Phone, SMS, Chat, Email) | `[]` | `{}` |
    | `NEXT_MEDIA_TYPE` | 9 | `TEXT` | Channel of communication for the subsequent contact | Channel of communication for the subsequent contact | `[]` | `{}` |
    | `INITIAL_DISPOSITION_NAME` | 10 | `TEXT` | Disposition code for the initial contact | Disposition code for the initial contact | `[]` | `{}` |
    | `NEXT_DISPOSITION_NAME` | 11 | `TEXT` | Disposition code for the subsequent contact | Disposition code for the subsequent contact | `[]` | `{}` |
    | `INITIAL_PHONE_NUMBER` | 12 | `TEXT` | Phone number associated with the initial contact | Phone number associated with the initial contact | `[]` | `{}` |
    | `INTIAL_EMAIL` | 13 | `TEXT` | Email address associated with the initial contact | Email address associated with the initial contact | `[]` | `{}` |
    | `INITIAL_MERCHANT_ID` | 14 | `TEXT` | Merchant ID associated with the initial contact | Merchant ID associated with the initial contact | `[]` | `{}` |
    | `INTIAL_BORROWER_ID` | 15 | `TEXT` | Borrower ID associated with the initial contact | Borrower ID associated with the initial contact | `[]` | `{}` |
    | `INTERACTION_MATCHING_KEY` | 16 | `TEXT` | Key used to match related interactions from the same customer, usually the borrower or merchant ID, if missing the email or phone number | Key used to match related interactions from the same customer, usually the borrower or merchant ID, if missing the email or phone number | `[]` | `{}` |
    | `INITIAL_INTERACTION_BEGIN` | 17 | `TIMESTAMP_NTZ` | Timestamp when the initial contact started | Timestamp when the initial contact started | `[]` | `{}` |
    | `NEXT_INTERACTION_BEGIN` | 18 | `TIMESTAMP_NTZ` | Timestamp when the subsequent contact started | Timestamp when the subsequent contact started | `[]` | `{}` |
    | `INITIAL_INTERACTION_NUMBER` | 19 | `NUMBER` | Sequence number of the initial interaction for the customer | Sequence number of the initial interaction for the customer | `[]` | `{}` |
    | `NEXT_INTERACTION_NUMBER` | 20 | `NUMBER` | Sequence number of the subsequent interaction for the customer | Sequence number of the subsequent interaction for the customer | `[]` | `{}` |
    | `IS_ONE_TOUCH_FOUR_ELIGIBLE` | 21 | `BOOLEAN` | Boolean indicating if the initial contact is eligible for one-touch resolution tracking (4-day window) | Boolean indicating if the initial contact is eligible for one-touch resolution tracking (4-day window) | `[]` | `{}` |
    | `TIME_DIFFERENCE` | 22 | `NUMBER` | Time difference in days between the initial and subsequent contacts | Time difference in days between the initial and subsequent contacts | `[]` | `{}` |
    | `OUTBOUND_IN_BETWEEN_IND` | 23 | `NUMBER` | Count of outbound contacts made to the customer between the initial and subsequent contacts | Count of outbound contacts made to the customer between the initial and subsequent contacts | `[]` | `{}` |
    | `SMS_IN_BETWEEN_IND` | 24 | `NUMBER` | Count of outbound SMS messages sent to the customer between the initial and subsequent contacts | Count of outbound SMS messages sent to the customer between the initial and subsequent contacts | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.nice_one_touch_resolution_interactions_xf_archive`
    *   `model.cherry_data_model.zendesk_one_touch_resolution_interactions_xf`

---
