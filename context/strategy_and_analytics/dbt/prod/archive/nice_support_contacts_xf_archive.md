## Model: `nice_support_contacts_xf_archive`

`nice_support_contacts_xf_archive`

*   **Unique ID:** `model.cherry_data_model.nice_support_contacts_xf_archive`
*   **FQN:** `prod.archive.nice_support_contacts_xf_archive`
*   **Description:** This model transforms and consolidates support contact data from NICE inbound and outbound systems. It includes contact details, agent information, disposition data, and metrics for support team interactions. The model is tagged for archive.

*   **Tags:** `['archive']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CONTACT_ID` | 1 | `NUMBER` | Unique identifier for the contact interaction | Unique identifier for the contact interaction | `[]` | `{}` |
    | `CAMPAIGN_ID` | 2 | `NUMBER` | ID of the campaign associated with the contact | ID of the campaign associated with the contact | `[]` | `{}` |
    | `MASTER_CONTACT_ID` | 3 | `NUMBER` | Master ID that links related contacts together | Master ID that links related contacts together | `[]` | `{}` |
    | `POINT_OF_CONTACT_ID` | 4 | `NUMBER` | ID for the specific point of contact | ID for the specific point of contact | `[]` | `{}` |
    | `INTERACTION_BORROWER_ID` | 5 | `NUMBER` | Borrower ID associated with the interaction | Borrower ID associated with the interaction | `[]` | `{}` |
    | `CONTACT_INTERACTION_MERCHANT_ID` | 6 | `NUMBER` | Merchant ID associated with the interaction | Merchant ID associated with the interaction | `[]` | `{}` |
    | `CONTACT_INTERACTION_ORGANIZATION_ID` | 7 | `NUMBER` | Organization ID associated with the interaction | Organization ID associated with the interaction | `[]` | `{}` |
    | `INTERACTION_PRIMARY_MERCHANT_ID` | 8 | `FLOAT` | Primary merchant ID mapped from the interaction merchant | Primary merchant ID mapped from the interaction merchant | `[]` | `{}` |
    | `INTERACTION_PRIMARY_ORGANIZATION_ID` | 9 | `NUMBER` | Primary organization ID mapped from the interaction organization | Primary organization ID mapped from the interaction organization | `[]` | `{}` |
    | `CONTACT_START_PT` | 10 | `TIMESTAMP_NTZ` | Timestamp in Pacific Time when the contact interaction started | Timestamp in Pacific Time when the contact interaction started | `[]` | `{}` |
    | `CONTACT_END_PT` | 11 | `TIMESTAMP_NTZ` | Timestamp in Pacific Time when the contact interaction ended | Timestamp in Pacific Time when the contact interaction ended | `[]` | `{}` |
    | `LAST_UPDATED_PT` | 12 | `TIMESTAMP_NTZ` | Timestamp in Pacific Time when the contact was last updated | Timestamp in Pacific Time when the contact was last updated | `[]` | `{}` |
    | `FINAL_STATUS_PT` | 13 | `TIMESTAMP_NTZ` | Timestamp in Pacific Time of the final status update | Timestamp in Pacific Time of the final status update | `[]` | `{}` |
    | `CONTACT_LENGTH` | 14 | `NUMBER` | Duration of the contact in seconds | Duration of the contact in seconds | `[]` | `{}` |
    | `DIRECTION` | 15 | `TEXT` | Direction of contact (Inbound/Outbound) | Direction of contact (Inbound/Outbound) | `[]` | `{}` |
    | `MEDIA_TYPE_NAME` | 16 | `TEXT` | Channel of communication (Phone, SMS, Chat, Email) | Channel of communication (Phone, SMS, Chat, Email) | `[]` | `{}` |
    | `INITIAL_AGENT_NAME` | 17 | `TEXT` | Name of the first agent who handled the contact | Name of the first agent who handled the contact | `[]` | `{}` |
    | `INITIAL_SKILL_NAME` | 18 | `TEXT` | Initial skill/queue the contact was routed to | Initial skill/queue the contact was routed to | `[]` | `{}` |
    | `INITIAL_TEAM_NAME` | 19 | `TEXT` | Initial team the contact was routed to | Initial team the contact was routed to | `[]` | `{}` |
    | `FINAL_AGENT_NAME` | 20 | `TEXT` | Name of the last agent who handled the contact | Name of the last agent who handled the contact | `[]` | `{}` |
    | `FINAL_SKILL_NAME` | 21 | `TEXT` | Final skill/queue that handled the contact | Final skill/queue that handled the contact | `[]` | `{}` |
    | `FINAL_TEAM_NAME` | 22 | `TEXT` | Final team that handled the contact | Final team that handled the contact | `[]` | `{}` |
    | `SUPPORT_AGENTS` | 23 | `TEXT` | Comma-separated list of all support agents who handled the contact | Comma-separated list of all support agents who handled the contact | `[]` | `{}` |
    | `NUM_SEGMENTS` | 24 | `NUMBER` | Number of segments in the contact interaction | Number of segments in the contact interaction | `[]` | `{}` |
    | `END_REASON` | 25 | `TEXT` | Reason the contact ended | Reason the contact ended | `[]` | `{}` |
    | `DISPOSITION_NAME` | 26 | `TEXT` | Final disposition/outcome of the contact | Final disposition/outcome of the contact | `[]` | `{}` |
    | `SERVICE_LEVEL` | 27 | `TEXT` | Service level categorization (Patient, Practice, Other) | Service level categorization (Patient, Practice, Other) | `[]` | `{}` |
    | `PATIENT_CATEGORIZATION` | 28 | `TEXT` | Categorization of patient contacts (Pre-checkout/Application, Post-Checkout) | Categorization of patient contacts (Pre-checkout/Application, Post-Checkout) | `[]` | `{}` |
    | `SECONDARY_DISPOSITION_NAME` | 29 | `TEXT` | Secondary disposition for the contact | Secondary disposition for the contact | `[]` | `{}` |
    | `DISPOSITION_NOTES` | 30 | `TEXT` | Notes added to the disposition | Notes added to the disposition | `[]` | `{}` |
    | `TAG_NAME` | 31 | `TEXT` | Tags applied to the contact | Tags applied to the contact | `[]` | `{}` |
    | `SERVICE_LEVEL_CATEGORY` | 32 | `TEXT` | Service level category classification | Service level category classification | `[]` | `{}` |
    | `OWNING_TEAM` | 33 | `TEXT` | Team that owns the contact | Team that owns the contact | `[]` | `{}` |
    | `INITIAL_AGENT_PHONE` | 34 | `TEXT` | Phone number of the initial agent | Phone number of the initial agent | `[]` | `{}` |
    | `FINAL_AGENT_PHONE` | 35 | `TEXT` | Phone number of the final agent | Phone number of the final agent | `[]` | `{}` |
    | `FROM_ADDRESS` | 36 | `TEXT` | Address the contact came from (email, phone) | Address the contact came from (email, phone) | `[]` | `{}` |
    | `TO_ADDRESS` | 37 | `TEXT` | Address the contact was directed to (email, phone) | Address the contact was directed to (email, phone) | `[]` | `{}` |
    | `INTERACTION_PHONE_NUMBER` | 38 | `TEXT` | Phone number associated with the interaction | Phone number associated with the interaction | `[]` | `{}` |
    | `INTERACTION_IP_ADDRESS` | 39 | `TEXT` | IP address associated with the interaction | IP address associated with the interaction | `[]` | `{}` |
    | `INTERACTION_EMAIL` | 40 | `TEXT` | Email address associated with the interaction | Email address associated with the interaction | `[]` | `{}` |
    | `POINT_OF_CONTACT_NAME` | 41 | `TEXT` | Name of the point of contact | Name of the point of contact | `[]` | `{}` |
    | `SERVICE_LEVEL_FLAG` | 42 | `NUMBER` | Flag indicating service level status | Flag indicating service level status | `[]` | `{}` |
    | `TRANSFER_INDICATOR_NAME` | 43 | `TEXT` | Indicator for transferred contacts | Indicator for transferred contacts | `[]` | `{}` |
    | `CONTACT_TYPE` | 44 | `TEXT` | Type of contact from transcript data | Type of contact from transcript data | `[]` | `{}` |
    | `SUMMARIZATION` | 45 | `TEXT` | AI-generated summary of the interaction | AI-generated summary of the interaction | `[]` | `{}` |
    | `ORIGINAL_DISPOSITION` | 46 | `TEXT` | Original disposition from transcript data | Original disposition from transcript data | `[]` | `{}` |
    | `SUBDISPOSITION` | 47 | `TEXT` | Subdisposition from transcript data | Subdisposition from transcript data | `[]` | `{}` |
    | `IS_SERVICE_HOURS` | 48 | `BOOLEAN` | Boolean indicating if the contact occurred during service hours (Eastern Time) | Boolean indicating if the contact occurred during service hours (Eastern Time) | `[]` | `{}` |
    | `IS_INITIAL_AGENT_SUPPORT` | 49 | `BOOLEAN` | Boolean indicating if the initial agent was from the support team | Boolean indicating if the initial agent was from the support team | `[]` | `{}` |
    | `IS_FINAL_AGENT_SUPPORT` | 50 | `BOOLEAN` | Boolean indicating if the final agent was from the support team | Boolean indicating if the final agent was from the support team | `[]` | `{}` |
    | `IS_RIGHT_PARTY_CONTACT` | 51 | `BOOLEAN` | Boolean indicating if the contact reached the intended person | Boolean indicating if the contact reached the intended person | `[]` | `{}` |
    | `IS_CONVERSION` | 52 | `BOOLEAN` | Boolean indicating if the contact resulted in a conversion | Boolean indicating if the contact resulted in a conversion | `[]` | `{}` |
    | `IS_CONTACT` | 53 | `BOOLEAN` | Boolean indicating if this was a valid contact | Boolean indicating if this was a valid contact | `[]` | `{}` |
    | `ELIGIBLE_FOR_CSAT_SURVEY` | 54 | `BOOLEAN` | Boolean indicating if the contact is eligible for CSAT survey | Boolean indicating if the contact is eligible for CSAT survey | `[]` | `{}` |
    | `WAS_REFUSED` | 55 | `BOOLEAN` | Boolean indicating if the contact was refused | Boolean indicating if the contact was refused | `[]` | `{}` |
    | `WAS_ABANDONED` | 56 | `BOOLEAN` | Boolean indicating if the contact was abandoned | Boolean indicating if the contact was abandoned | `[]` | `{}` |
    | `WAS_SHORT_ABANDON` | 57 | `BOOLEAN` | Boolean indicating if the contact was abandoned quickly | Boolean indicating if the contact was abandoned quickly | `[]` | `{}` |
    | `WAS_TAKEOVER` | 58 | `BOOLEAN` | Boolean indicating if the contact was taken over by another agent | Boolean indicating if the contact was taken over by another agent | `[]` | `{}` |
    | `IS_ONE_TOUCH_RESOLUTION_ELIGIBLE` | 59 | `BOOLEAN` | Boolean indicating if the contact is eligible for one-touch resolution tracking | Boolean indicating if the contact is eligible for one-touch resolution tracking | `[]` | `{}` |
    | `INITIAL_ONE_TOUCH_RESOLUTION_INTERACTION_BEGIN` | 60 | `TIMESTAMP_NTZ` | Timestamp of the initial interaction for one-touch resolution tracking | Timestamp of the initial interaction for one-touch resolution tracking | `[]` | `{}` |
    | `IS_ONE_TOUCH_RESOLUTION_SUCCESS` | 61 | `BOOLEAN` | Boolean indicating if the contact was successfully resolved in one touch | Boolean indicating if the contact was successfully resolved in one touch | `[]` | `{}` |
    | `IS_CONVERSION_ELIGIBLE` | 62 | `NUMBER` | Boolean indicating if the contact is eligible for conversion tracking | Boolean indicating if the contact is eligible for conversion tracking | `[]` | `{}` |
    | `IS_CONVERSION_SUCCESSFUL` | 63 | `NUMBER` | Boolean indicating if the contact resulted in a successful conversion | Boolean indicating if the contact resulted in a successful conversion | `[]` | `{}` |
    | `IS_CHATBOT_CAPTURE` | 64 | `BOOLEAN` | Boolean indicating if the contact was handled by a chatbot | Boolean indicating if the contact was handled by a chatbot | `[]` | `{}` |
    | `IS_IVR_CAPTURE` | 65 | `BOOLEAN` | Boolean indicating if the contact was handled by IVR | Boolean indicating if the contact was handled by IVR | `[]` | `{}` |
    | `T_ABANDON` | 66 | `NUMBER` | Time in seconds before the contact was abandoned | Time in seconds before the contact was abandoned | `[]` | `{}` |
    | `T_ACW` | 67 | `NUMBER` | Time in seconds spent on after-call work | Time in seconds spent on after-call work | `[]` | `{}` |
    | `T_HANDLE` | 68 | `NUMBER` | Time in seconds spent handling the contact | Time in seconds spent handling the contact | `[]` | `{}` |
    | `TOTAL_HANDLE_TIME` | 69 | `NUMBER` | Total time in seconds spent handling the contact (handle + ACW) | Total time in seconds spent handling the contact (handle + ACW) | `[]` | `{}` |
    | `ADJUSTED_TOTAL_HANDLE_TIME` | 70 | `NUMBER` | Adjusted handle time based on media type (calls at 100%, chat/email/SMS at 20%) | Adjusted handle time based on media type (calls at 100%, chat/email/SMS at 20%) | `[]` | `{}` |
    | `ADJ_TOTAL_HANDLE_TIME_5TH_PCTILE` | 71 | `NUMBER` | 5th percentile of adjusted handle time for the media type | 5th percentile of adjusted handle time for the media type | `[]` | `{}` |
    | `ADJ_TOTAL_HANDLE_TIME_95TH_PCTILE` | 72 | `NUMBER` | 95th percentile of adjusted handle time for the media type | 95th percentile of adjusted handle time for the media type | `[]` | `{}` |
    | `IS_ADJ_TOTAL_HANDLE_TIME_OUTLIER` | 73 | `BOOLEAN` | Boolean indicating if the adjusted handle time is an outlier | Boolean indicating if the adjusted handle time is an outlier | `[]` | `{}` |
    | `T_WAITING_FOR_CALLBACK` | 74 | `NUMBER` | Time in seconds spent waiting for callback | Time in seconds spent waiting for callback | `[]` | `{}` |
    | `T_CONFERENCE` | 75 | `NUMBER` | Time in seconds spent in conference | Time in seconds spent in conference | `[]` | `{}` |
    | `T_HOLD` | 76 | `NUMBER` | Time in seconds the customer was on hold | Time in seconds the customer was on hold | `[]` | `{}` |
    | `T_PRE_QUEUE` | 77 | `NUMBER` | Time in seconds spent in pre-queue | Time in seconds spent in pre-queue | `[]` | `{}` |
    | `T_IN_QUEUE` | 78 | `NUMBER` | Time in seconds spent in queue | Time in seconds spent in queue | `[]` | `{}` |
    | `T_POST_QUEUE` | 79 | `NUMBER` | Time in seconds spent in post-queue | Time in seconds spent in post-queue | `[]` | `{}` |
    | `T_RELEASE` | 80 | `NUMBER` | Time in seconds spent in release state | Time in seconds spent in release state | `[]` | `{}` |
    | `T_ROUTING` | 81 | `NUMBER` | Time in seconds spent routing the contact | Time in seconds spent routing the contact | `[]` | `{}` |
    | `HOLD_COUNT` | 82 | `NUMBER` | Number of times the customer was placed on hold | Number of times the customer was placed on hold | `[]` | `{}` |
    | `IS_PEAK_CONTACT` | 83 | `BOOLEAN` | Boolean indicating if the contact occurred during peak hours | Boolean indicating if the contact occurred during peak hours | `[]` | `{}` |
    | `IS_ALLE_CONTACT` | 84 | `BOOLEAN` | Boolean indicating if the contact is related to Alle | Boolean indicating if the contact is related to Alle | `[]` | `{}` |
    | `IS_YELLOW_CONTACT` | 85 | `BOOLEAN` | Boolean indicating if the contact came through Yellow.ai | Boolean indicating if the contact came through Yellow.ai | `[]` | `{}` |
    | `CSAT_SCORE` | 86 | `NUMBER` | Customer satisfaction score for the interaction | Customer satisfaction score for the interaction | `[]` | `{}` |
    | `CSAT_NOTES` | 87 | `TEXT` | Customer notes from the satisfaction survey | Customer notes from the satisfaction survey | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.cherry_data_model.is_support_service_hours`
    *   `model.cherry_data_model.int_nice_alle_contacts`
    *   `model.cherry_data_model.int_nice_automation_segments_and_volumes`
    *   `model.cherry_data_model.int_nice_automation_segments_and_volumes_peak_hourly_volumes`
    *   `model.cherry_data_model.int_nice_inbounds_contact_information_joined`
    *   `model.cherry_data_model.int_nice_outbounds_contact_information_joined`
    *   `model.cherry_data_model.merchant_account_mapping`
    *   `model.cherry_data_model.nice_one_touch_resolution_interactions_xf_archive`
    *   `model.cherry_data_model.nice_support_conversion_rate_xf_archive`
    *   `model.cherry_data_model.src_nice_sms_chat_phone_numbers`
    *   `model.cherry_data_model.src_nice_yellow_custom_data`
    *   `model.cherry_data_model.stg_nice_contacts`
    *   `model.cherry_data_model.stg_nice_transcripts`
    *   `model.cherry_data_model.tagged_customer_satisfaction_responses_xf`
    *   `seed.cherry_data_model.ops_user_teams`

---
