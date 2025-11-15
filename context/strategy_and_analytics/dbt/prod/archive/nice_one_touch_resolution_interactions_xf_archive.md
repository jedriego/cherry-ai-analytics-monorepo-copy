## Model: `nice_one_touch_resolution_interactions_xf_archive`

`nice_one_touch_resolution_interactions_xf_archive`

*   **Unique ID:** `model.cherry_data_model.nice_one_touch_resolution_interactions_xf_archive`
*   **FQN:** `prod.archive.nice_one_touch_resolution_interactions_xf_archive`
*   **Description:** This model tracks one-touch resolution metrics for NICE support interactions by identifying eligible initial contacts and their subsequent interactions. It determines if issues were resolved in a single contact or if customers needed to reach out again within a defined timeframe.

*   **Tags:** `['archive']`
*   **Meta:** `{'sources': [{'name': 'nice', 'tables': [{'name': 'one_touch_eligible_contacts', 'description': 'Contacts eligible for one-touch resolution tracking'}, {'name': 'outbounds', 'description': 'Outbound contacts from NICE'}], 'description': 'Source data from NICE contact center platform'}, {'name': 'sms', 'tables': [{'name': 'notifications', 'description': 'SMS notifications sent to customers'}], 'description': 'SMS notification system'}], 'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `INITIAL_CONTACT_ID` | 1 | `NUMBER` | Unique identifier for the first contact in the potential one-touch resolution pair | Unique identifier for the first contact in the potential one-touch resolution pair | `[]` | `{}` |
    | `NEXT_CONVERSATION_ID` | 2 | `NUMBER` | Unique identifier for the subsequent contact from the same customer | Unique identifier for the subsequent contact from the same customer | `[]` | `{}` |
    | `INITIAL_SKILL` | 3 | `TEXT` | Initial skill/queue the first contact was routed to | Initial skill/queue the first contact was routed to | `[]` | `{}` |
    | `NEXT_SKILL` | 4 | `TEXT` | Skill/queue the subsequent contact was routed to | Skill/queue the subsequent contact was routed to | `[]` | `{}` |
    | `INITIAL_AGENT_NAME` | 5 | `TEXT` | Name of the agent who handled the initial contact | Name of the agent who handled the initial contact | `[]` | `{}` |
    | `NEXT_AGENT_NAME` | 6 | `TEXT` | Name of the agent who handled the subsequent contact | Name of the agent who handled the subsequent contact | `[]` | `{}` |
    | `INITIAL_MEDIA_TYPE` | 7 | `TEXT` | Channel of communication for the initial contact (Phone, SMS, Chat, Email) | Channel of communication for the initial contact (Phone, SMS, Chat, Email) | `[]` | `{}` |
    | `NEXT_MEDIA_TYPE` | 8 | `TEXT` | Channel of communication for the subsequent contact | Channel of communication for the subsequent contact | `[]` | `{}` |
    | `INITIAL_DISPOSITION_NAME` | 9 | `TEXT` | Disposition code for the initial contact | Disposition code for the initial contact | `[]` | `{}` |
    | `NEXT_DISPOSITION_NAME` | 10 | `TEXT` | Disposition code for the subsequent contact | Disposition code for the subsequent contact | `[]` | `{}` |
    | `INITIAL_PHONE_NUMBER` | 11 | `TEXT` | Phone number associated with the initial contact | Phone number associated with the initial contact | `[]` | `{}` |
    | `INTIAL_EMAIL` | 12 | `TEXT` | Email address associated with the initial contact | Email address associated with the initial contact | `[]` | `{}` |
    | `INITIAL_MERCHANT_ID` | 13 | `NUMBER` | Merchant ID associated with the initial contact | Merchant ID associated with the initial contact | `[]` | `{}` |
    | `INTIAL_BORROWER_ID` | 14 | `NUMBER` | Borrower ID associated with the initial contact | Borrower ID associated with the initial contact | `[]` | `{}` |
    | `INTERACTION_MATCHING_KEY` | 15 | `TEXT` | Key used to match related interactions from the same customer, usually the borrower or merchant ID, if missing the email or phone number | Key used to match related interactions from the same customer, usually the borrower or merchant ID, if missing the email or phone number | `[]` | `{}` |
    | `INITIAL_INTERACTION_BEGIN` | 16 | `TIMESTAMP_NTZ` | Timestamp when the initial contact started | Timestamp when the initial contact started | `[]` | `{}` |
    | `NEXT_INTERACTION_BEGIN` | 17 | `TIMESTAMP_NTZ` | Timestamp when the subsequent contact started | Timestamp when the subsequent contact started | `[]` | `{}` |
    | `INITIAL_INTERACTION_NUMBER` | 18 | `NUMBER` | Sequence number of the initial interaction for the customer | Sequence number of the initial interaction for the customer | `[]` | `{}` |
    | `NEXT_INTERACTION_NUMBER` | 19 | `NUMBER` | Sequence number of the subsequent interaction for the customer | Sequence number of the subsequent interaction for the customer | `[]` | `{}` |
    | `IS_ONE_TOUCH_FOUR_ELIGIBLE` | 20 | `BOOLEAN` | Boolean indicating if the initial contact is eligible for one-touch resolution tracking | Boolean indicating if the initial contact is eligible for one-touch resolution tracking | `[]` | `{}` |
    | `TIME_DIFFERENCE` | 21 | `NUMBER` | Time difference in days between the initial and subsequent contacts | Time difference in days between the initial and subsequent contacts | `[]` | `{}` |
    | `OUTBOUND_IN_BETWEEN_IND` | 22 | `NUMBER` | Count of outbound contacts made to the customer between the initial and subsequent contacts | Count of outbound contacts made to the customer between the initial and subsequent contacts | `[]` | `{}` |
    | `SMS_IN_BETWEEN_IND` | 23 | `NUMBER` | Count of outbound SMS messages sent to the customer between the initial and subsequent contacts | Count of outbound SMS messages sent to the customer between the initial and subsequent contacts | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.int_nice_outbounds_contact_information_joined`
    *   `model.cherry_data_model.src_borrowers`
    *   `model.cherry_data_model.stg_nice_one_touch_eligible_contacts`
    *   `model.cherry_data_model.stg_sms_notifications`

---
