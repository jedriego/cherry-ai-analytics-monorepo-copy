## Model: `zendesk_support_team_tickets_xf`

`zendesk_support_team_tickets_xf`

*   **Unique ID:** `model.cherry_data_model.zendesk_support_team_tickets_xf`
*   **FQN:** `prod.customer_support_marts.zendesk_support_team_tickets_xf`
*   **Description:** This model contains all Zendesk tickets actually handled by Support/Concierge teams, including  overflow from other teams. Used for agent performance metrics and team capacity analysis.

*   **Tags:** `['customer_support', 'zendesk_refresh']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `TICKET_ID` | 1 | `NUMBER` | Unique identifier for the Zendesk ticket | Unique identifier for the Zendesk ticket | `[]` | `{}` |
    | `URL` | 2 | `TEXT` | URL link to the Zendesk ticket's underlying JSON data | URL link to the Zendesk ticket's underlying JSON data | `[]` | `{}` |
    | `AGENT_NAME` | 3 | `TEXT` | Name of the agent who handled the ticket | Name of the agent who handled the ticket | `[]` | `{}` |
    | `REQUESTER_NAME` | 4 | `TEXT` | Name of the person who requested the ticket | Name of the person who requested the ticket | `[]` | `{}` |
    | `SUBMITTER_NAME` | 5 | `TEXT` | Name of the person who submitted the ticket | Name of the person who submitted the ticket | `[]` | `{}` |
    | `DIRECTION` | 6 | `TEXT` | Direction of contact (Inbound/Outbound) | Direction of contact (Inbound/Outbound) | `[]` | `{}` |
    | `IS_TCN_OUTBOUND` | 7 | `BOOLEAN` | Boolean indicating if the ticket was created from a TCN outbound call | Boolean indicating if the ticket was created from a TCN outbound call | `[]` | `{}` |
    | `GROUP_NAME` | 8 | `TEXT` | Zendesk group name assigned to the ticket | Zendesk group name assigned to the ticket | `[]` | `{}` |
    | `TEAM` | 9 | `TEXT` | Team assigned to the ticket (Support/Concierge) | Team assigned to the ticket (Support/Concierge) | `[]` | `{}` |
    | `MANAGER` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `TICKET_CURRENT_STATUS` | 11 | `TEXT` | Current status of the ticket (Open, Pending, Solved, Closed) | Current status of the ticket (Open, Pending, Solved, Closed) | `[]` | `{}` |
    | `MEDIA_TYPE_NAME` | 12 | `TEXT` | Channel of communication (Phone, SMS, Chat, Email) | Channel of communication (Phone, SMS, Chat, Email) | `[]` | `{}` |
    | `WAS_CALLBACK` | 13 | `BOOLEAN` | Boolean indicating if the ticket was a callback | Boolean indicating if the ticket was a callback | `[]` | `{}` |
    | `CUSTOMER_TYPE` | 14 | `TEXT` | Type of customer (Patient, Practice, Alle) | Type of customer (Patient, Practice, Alle) | `[]` | `{}` |
    | `PATIENT_PRACTICE_SEGMENTATION` | 15 | `TEXT` | Patient or practice segmentation information | Patient or practice segmentation information | `[]` | `{}` |
    | `TIER` | 16 | `TEXT` | Customer tier classification | Customer tier classification | `[]` | `{}` |
    | `TICKET_CREATED_AT_PT` | 17 | `TIMESTAMP_NTZ` | Timestamp in Pacific Time when the ticket was created | Timestamp in Pacific Time when the ticket was created | `[]` | `{}` |
    | `TICKET_FIRST_TOUCHED_PT` | 18 | `TIMESTAMP_NTZ` | Timestamp in Pacific Time when the ticket was first touched by an agent | Timestamp in Pacific Time when the ticket was first touched by an agent | `[]` | `{}` |
    | `CHAT_SMS_FIRST_AGENT_RESPONSE_PT` | 19 | `TIMESTAMP_NTZ` | Timestamp in Pacific Time of first agent response for chat/SMS tickets | Timestamp in Pacific Time of first agent response for chat/SMS tickets | `[]` | `{}` |
    | `CHAT_SMS_FIRST_CUSTOMER_RESPONSE_TO_AGENT_PT` | 20 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `TICKET_RESOLVED_PT` | 21 | `TIMESTAMP_NTZ` | Timestamp in Pacific Time when the ticket was resolved | Timestamp in Pacific Time when the ticket was resolved | `[]` | `{}` |
    | `WAS_ABANDONED` | 22 | `BOOLEAN` | Boolean indicating if the ticket was abandoned | Boolean indicating if the ticket was abandoned | `[]` | `{}` |
    | `TIME_IN_QUEUE` | 23 | `NUMBER` | Time in seconds the ticket spent in queue before being handled | Time in seconds the ticket spent in queue before being handled | `[]` | `{}` |
    | `SERVICE_LEVEL_SECONDS` | 24 | `NUMBER` | Service level measurement in seconds | Service level measurement in seconds | `[]` | `{}` |
    | `SERVICE_LEVEL_THRESHOLD` | 25 | `NUMBER` | Threshold in seconds for meeting service level | Threshold in seconds for meeting service level | `[]` | `{}` |
    | `MET_SERVICE_LEVEL` | 26 | `BOOLEAN` | Boolean indicating if the service level was met | Boolean indicating if the service level was met | `[]` | `{}` |
    | `HANDLE_TIME` | 27 | `NUMBER` | Total time spent handling the ticket | Total time spent handling the ticket | `[]` | `{}` |
    | `HOLD_TIME` | 28 | `NUMBER` | Time the customer was on hold during the interaction | Time the customer was on hold during the interaction | `[]` | `{}` |
    | `AFTER_CALL_WORK_TIME` | 29 | `NUMBER` | Time spent on after-call work | Time spent on after-call work | `[]` | `{}` |
    | `INTERACTION_PHONE_NUMBER` | 30 | `TEXT` | Phone number associated with the interaction | Phone number associated with the interaction | `[]` | `{}` |
    | `INTERACTION_EMAIL_ADDRESS` | 31 | `TEXT` | Email address associated with the interaction | Email address associated with the interaction | `[]` | `{}` |
    | `YELLOW_CONVERSATION_ID` | 32 | `TEXT` | Yellow.ai conversation identifier | Yellow.ai conversation identifier | `[]` | `{}` |
    | `YELLOW_SESSION_ID` | 33 | `TEXT` | Yellow.ai session identifier | Yellow.ai session identifier | `[]` | `{}` |
    | `MERGED_TICKET_IDS` | 34 | `VARIANT` | IDs of tickets that were merged into this ticket | IDs of tickets that were merged into this ticket | `[]` | `{}` |
    | `YELLOW_SUMMARIZATION` | 35 | `TEXT` | AI-generated summary from Yellow.ai | AI-generated summary from Yellow.ai | `[]` | `{}` |
    | `EMAIL_SUBJECT` | 36 | `TEXT` | Subject line for email tickets | Subject line for email tickets | `[]` | `{}` |
    | `EMAIL_DESCRIPTION` | 37 | `TEXT` | Description content for email tickets | Description content for email tickets | `[]` | `{}` |
    | `SCHEDULED_TIME` | 38 | `DATE` | Scheduled time for callbacks or planned interactions | Scheduled time for callbacks or planned interactions | `[]` | `{}` |
    | `EARLY_CALLBACK` | 39 | `BOOLEAN` | Boolean indicating if the callback occurred earlier than scheduled | Boolean indicating if the callback occurred earlier than scheduled | `[]` | `{}` |
    | `CALLBACK_TIME` | 40 | `TEXT` | Time when the callback was scheduled | Time when the callback was scheduled | `[]` | `{}` |
    | `COLLECTIONS_BORROWER_FLAG` | 41 | `TEXT` | Flag indicating if the borrower is in collections | Flag indicating if the borrower is in collections | `[]` | `{}` |
    | `WAS_COMPLAINT` | 42 | `TEXT` | Boolean indicating if the ticket was a complaint | Boolean indicating if the ticket was a complaint | `[]` | `{}` |
    | `AGENT_DISPOSITION` | 43 | `TEXT` | Agent-selected disposition for the ticket | Agent-selected disposition for the ticket | `[]` | `{}` |
    | `PATIENT_DISPOSITION` | 44 | `TEXT` | Patient-specific disposition | Patient-specific disposition | `[]` | `{}` |
    | `PRACTICE_DISPOSITION` | 45 | `TEXT` | Practice-specific disposition | Practice-specific disposition | `[]` | `{}` |
    | `ALLE_DISPOSITION` | 46 | `TEXT` | Alle-specific disposition | Alle-specific disposition | `[]` | `{}` |
    | `COLLECTIONS_DISPOSITION` | 47 | `TEXT` | Collections-specific disposition | Collections-specific disposition | `[]` | `{}` |
    | `RECOVERIES_DISPOSITION` | 48 | `TEXT` | Recoveries-specific disposition | Recoveries-specific disposition | `[]` | `{}` |
    | `IS_COLLECTIONS_CONTACT` | 49 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_RIGHT_PARTY_CONTACT` | 50 | `TEXT` | Boolean indicating if the contact reached the intended person | Boolean indicating if the contact reached the intended person | `[]` | `{}` |
    | `IS_COLLECTIONS_CONVERSION_ELIGIBLE` | 51 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_COLLECTIONS_CONVERSION` | 52 | `TEXT` | Boolean indicating if the contact resulted in a collections conversion | Boolean indicating if the contact resulted in a collections conversion | `[]` | `{}` |
    | `CSAT_SCORE` | 53 | `NUMBER` | Customer satisfaction score for the interaction | Customer satisfaction score for the interaction | `[]` | `{}` |
    | `IS_FORBEARANCE` | 54 | `BOOLEAN` | Boolean indicating if the borrower is in forbearance | Boolean indicating if the borrower is in forbearance | `[]` | `{}` |
    | `PRIORITY` | 55 | `TEXT` | Priority level assigned to the ticket | Priority level assigned to the ticket | `[]` | `{}` |
    | `HAS_INCIDENTS` | 56 | `BOOLEAN` | Boolean indicating if the ticket has associated incidents | Boolean indicating if the ticket has associated incidents | `[]` | `{}` |
    | `IS_PUBLIC` | 57 | `BOOLEAN` | Boolean indicating if the ticket is publicly visible | Boolean indicating if the ticket is publicly visible | `[]` | `{}` |
    | `VIA_FOLLOWUP_SOURCE_ID` | 58 | `NUMBER` | Source ID for follow-up communications | Source ID for follow-up communications | `[]` | `{}` |
    | `FOLLOWUP_IDS` | 59 | `VARIANT` | IDs of follow-up tickets | IDs of follow-up tickets | `[]` | `{}` |
    | `TICKET_FORM_ID` | 60 | `NUMBER` | ID of the form used to create the ticket | ID of the form used to create the ticket | `[]` | `{}` |
    | `ALLOW_CHANNELBACK` | 61 | `BOOLEAN` | Boolean indicating if channelback is allowed | Boolean indicating if channelback is allowed | `[]` | `{}` |
    | `ALLOW_ATTACHMENTS` | 62 | `BOOLEAN` | Boolean indicating if attachments are allowed | Boolean indicating if attachments are allowed | `[]` | `{}` |
    | `FROM_MESSAGING_CHANNEL` | 63 | `BOOLEAN` | Boolean indicating if the ticket came from a messaging channel | Boolean indicating if the ticket came from a messaging channel | `[]` | `{}` |
    | `USER_AUTHENTICATION` | 64 | `TEXT` | Method or status of user authentication | Method or status of user authentication | `[]` | `{}` |
    | `TIER_STRING` | 65 | `TEXT` | String representation of customer tier | String representation of customer tier | `[]` | `{}` |
    | `LANGUAGE_CONFIDENCE` | 66 | `TEXT` | Confidence score for language detection | Confidence score for language detection | `[]` | `{}` |
    | `TIME_SPENT_LAST_UPDATE_SEC` | 67 | `NUMBER` | Time in seconds spent on the last update | Time in seconds spent on the last update | `[]` | `{}` |
    | `LANGUAGE` | 68 | `TEXT` | Detected language of the ticket | Detected language of the ticket | `[]` | `{}` |
    | `SUPPORTCODE` | 69 | `TEXT` | Support code assigned to the ticket | Support code assigned to the ticket | `[]` | `{}` |
    | `SENTIMENT_CONFIDENCE` | 70 | `TEXT` | Confidence score for sentiment analysis | Confidence score for sentiment analysis | `[]` | `{}` |
    | `SENTIMENT` | 71 | `TEXT` | Detected sentiment of the ticket | Detected sentiment of the ticket | `[]` | `{}` |
    | `TCN_DIALED_FROM` | 72 | `TEXT` | Phone number used for TCN outbound calls | Phone number used for TCN outbound calls | `[]` | `{}` |
    | `LOAN_DAYS_PAST_DUE` | 73 | `TEXT` | Days past due for the loan | Days past due for the loan | `[]` | `{}` |
    | `MONTHS_SINCE_CHARGED_OFF` | 74 | `NUMBER` | Months since the loan was charged off | Months since the loan was charged off | `[]` | `{}` |
    | `MERCHANT_ID` | 75 | `TEXT` | Merchant ID associated with the ticket | Merchant ID associated with the ticket | `[]` | `{}` |
    | `ORGANIZATION_ID` | 76 | `TEXT` | Organization ID associated with the ticket | Organization ID associated with the ticket | `[]` | `{}` |
    | `EMAIL` | 77 | `TEXT` | Email address for the ticket | Email address for the ticket | `[]` | `{}` |
    | `JEENIE_TRANSFER_FLAG` | 78 | `BOOLEAN` | Boolean indicating if the ticket was transferred to Jeenie | Boolean indicating if the ticket was transferred to Jeenie | `[]` | `{}` |
    | `ALLE_TRANSFER_FLAG` | 79 | `BOOLEAN` | Boolean indicating if the ticket was transferred to Alle | Boolean indicating if the ticket was transferred to Alle | `[]` | `{}` |
    | `COLLECTIONS_TRANSFERS_FLAG` | 80 | `BOOLEAN` | Boolean indicating if the ticket was transferred to Collections | Boolean indicating if the ticket was transferred to Collections | `[]` | `{}` |
    | `SYSTEM_LOCATION` | 81 | `TEXT` | System location information | System location information | `[]` | `{}` |
    | `SYSTEM_RAW_EMAIL_IDENTIFIER` | 82 | `TEXT` | Raw email identifier from the system | Raw email identifier from the system | `[]` | `{}` |
    | `SYSTEM_JSON_EMAIL_IDENTIFIER` | 83 | `TEXT` | JSON email identifier from the system | JSON email identifier from the system | `[]` | `{}` |
    | `SYSTEM_IP_ADDRESS` | 84 | `TEXT` | IP address from the system | IP address from the system | `[]` | `{}` |
    | `SYSTEM_EML_REDACTED` | 85 | `BOOLEAN` | Boolean indicating if the email was redacted | Boolean indicating if the email was redacted | `[]` | `{}` |
    | `SYSTEM_EMAIL_ID` | 86 | `TEXT` | Email ID from the system | Email ID from the system | `[]` | `{}` |
    | `SYSTEM_LATITUDE` | 87 | `FLOAT` | Latitude from the system | Latitude from the system | `[]` | `{}` |
    | `SYSTEM_LONGITUDE` | 88 | `FLOAT` | Longitude from the system | Longitude from the system | `[]` | `{}` |
    | `SYSTEM_MESSAGE_ID` | 89 | `TEXT` | Message ID from the system | Message ID from the system | `[]` | `{}` |
    | `VIA_SOURCE_FROM_NAME` | 90 | `TEXT` | Source name for the ticket | Source name for the ticket | `[]` | `{}` |
    | `SYSTEM_CLIENT` | 91 | `TEXT` | Client information from the system | Client information from the system | `[]` | `{}` |
    | `VIA_SOURCE_TO_PHONE` | 92 | `TEXT` | Destination phone number | Destination phone number | `[]` | `{}` |
    | `VIA_SOURCE_FROM_PHONE` | 93 | `TEXT` | Source phone number | Source phone number | `[]` | `{}` |
    | `VIA_SOURCE_TO_FORMATTED_PHONE` | 94 | `TEXT` | Formatted destination phone number | Formatted destination phone number | `[]` | `{}` |
    | `VIA_SOURCE_FROM_FORMATTED_PHONE` | 95 | `TEXT` | Formatted source phone number | Formatted source phone number | `[]` | `{}` |
    | `VIA_SOURCE_TO_BRAND_ID` | 96 | `NUMBER` | Destination brand ID | Destination brand ID | `[]` | `{}` |
    | `VIA_SOURCE_FROM_SUBJECT` | 97 | `TEXT` | Subject from the source | Subject from the source | `[]` | `{}` |
    | `VIA_SOURCE_FROM_CHANNEL` | 98 | `TEXT` | Channel from the source | Channel from the source | `[]` | `{}` |
    | `VIA_SOURCE_FROM_BRAND_ID` | 99 | `NUMBER` | Brand ID from the source | Brand ID from the source | `[]` | `{}` |
    | `TOPIC` | 100 | `TEXT` | Topic of the ticket | Topic of the ticket | `[]` | `{}` |
    | `MERCHANT_ARRAY` | 101 | `TEXT` | Array of merchant information | Array of merchant information | `[]` | `{}` |
    | `URL_VISITATION` | 102 | `TEXT` | URL visitation information | URL visitation information | `[]` | `{}` |
    | `PROBLEM_ID` | 103 | `NUMBER` | ID of the problem associated with the ticket | ID of the problem associated with the ticket | `[]` | `{}` |
    | `BRAND_ID` | 104 | `NUMBER` | Brand ID associated with the ticket | Brand ID associated with the ticket | `[]` | `{}` |
    | `FORUM_TOPIC_ID` | 105 | `NUMBER` | Forum topic ID associated with the ticket | Forum topic ID associated with the ticket | `[]` | `{}` |
    | `SYSTEM_MACHINE_GENERATED` | 106 | `BOOLEAN` | Boolean indicating if the ticket was machine-generated | Boolean indicating if the ticket was machine-generated | `[]` | `{}` |
    | `SUN_CO_CONVERSATION_ID` | 107 | `TEXT` | SunCo conversation ID | SunCo conversation ID | `[]` | `{}` |
    | `SUPPORT_CONVERSION_ELIGIBLE` | 108 | `NUMBER` | Inbound Support ticket with application-related disposition (how_to_apply, manual_id_review, income_verification, denial, reapply) | Inbound Support ticket with application-related disposition (how_to_apply, manual_id_review, income_verification, denial, reapply) | `[]` | `{}` |
    | `SUPPORT_CONVERTED` | 109 | `NUMBER` | Eligible ticket resulting in app approval/denial within 191 hours (7 days 23 hours) | Eligible ticket resulting in app approval/denial within 191 hours (7 days 23 hours) | `[]` | `{}` |
    | `SUPPORT_TIME_TO_COMPLETION_MINS` | 110 | `NUMBER` | Minutes from initial to final application status for converted tickets | Minutes from initial to final application status for converted tickets | `[]` | `{}` |
    | `SUPPORT_TIME_TO_COMPLETION_DAYS` | 111 | `NUMBER` | Days from initial to final application status for converted tickets | Days from initial to final application status for converted tickets | `[]` | `{}` |
    | `IS_ONE_TOUCH_ELIGIBLE` | 112 | `BOOLEAN` | Boolean indicating if the ticket is included in the one touch resolution tracking model | Boolean indicating if the ticket is included in the one touch resolution tracking model | `[]` | `{}` |
    | `ONE_TOUCH_NEXT_CONTACT_ID` | 113 | `NUMBER` | ID of the next contact if there was a follow-up interaction | ID of the next contact if there was a follow-up interaction | `[]` | `{}` |
    | `ONE_TOUCH_NEXT_AGENT` | 114 | `TEXT` | Name of the agent who handled the next interaction | Name of the agent who handled the next interaction | `[]` | `{}` |
    | `ONE_TOUCH_NEXT_MEDIA_TYPE` | 115 | `TEXT` | Media type/channel of the next interaction | Media type/channel of the next interaction | `[]` | `{}` |
    | `ONE_TOUCH_NEXT_INTERACTION_BEGIN` | 116 | `TIMESTAMP_NTZ` | Timestamp when the next interaction began | Timestamp when the next interaction began | `[]` | `{}` |
    | `ONE_TOUCH_TIME_DIFFERENCE_DAYS` | 117 | `NUMBER` | Time difference in days between initial contact and next contact | Time difference in days between initial contact and next contact | `[]` | `{}` |
    | `IS_ONE_TOUCH_RESOLUTION` | 118 | `BOOLEAN` | Boolean indicating if the ticket was resolved without follow-up within 4 days (or qualifies for exceptions like disjointed SMS/email interactions or outbound calls in between) | Boolean indicating if the ticket was resolved without follow-up within 4 days (or qualifies for exceptions like disjointed SMS/email interactions or outbound calls in between) | `[]` | `{}` |
    | `CALLBACK_STATUS` | 119 | `BOOLEAN` | Status of the callback (Scheduled, Completed, Missed) | Status of the callback (Scheduled, Completed, Missed) | `[]` | `{}` |
    | `PRACTICE_RECOVERIES` | 120 | `TEXT` |  |  | `[]` | `{}` |
    | `FOLLOW_UP_DATE` | 121 | `DATE` |  |  | `[]` | `{}` |
    | `SKILL` | 122 | `TEXT` | Skill/queue associated with the ticket | Skill/queue associated with the ticket | `[]` | `{}` |
    | `WAS_SHORT_ABANDON` | 123 | `BOOLEAN` | Boolean indicating if the ticket was abandoned quickly (within 15 seconds) | Boolean indicating if the ticket was abandoned quickly (within 15 seconds) | `[]` | `{}` |
    | `TRANSCRIPT` | 124 | `TEXT` | Combined transcript of the interaction | Combined transcript of the interaction | `[]` | `{}` |
    | `NOTE_TOPIC` | 125 | `TEXT` | Topic of the AI-generated note | Topic of the AI-generated note | `[]` | `{}` |
    | `NOTE_OUTCOME` | 126 | `TEXT` | Outcome described in the AI-generated note | Outcome described in the AI-generated note | `[]` | `{}` |
    | `NOTE_SUMMARY` | 127 | `TEXT` | AI-generated summary of the interaction | AI-generated summary of the interaction | `[]` | `{}` |
    | `Q1_2025_COLLECTIONS_GROUP` | 128 | `TEXT` | Test/control group assignment for Q1 2025 collections experiment | Test/control group assignment for Q1 2025 collections experiment | `[]` | `{}` |
    | `BORROWER_ID` | 129 | `TEXT` | Borrower ID associated with the ticket | Borrower ID associated with the ticket | `[]` | `{}` |
    | `TRUE_LOAN_ID` | 130 | `NUMBER` | Determined loan ID associated with the ticket, derived from multiple sources | Determined loan ID associated with the ticket, derived from multiple sources | `[]` | `{}` |
    | `TRUE_MAX_DAYS_PAST_DUE` | 131 | `NUMBER` | Maximum days past due for the borrower's loans, derived from multiple sources | Maximum days past due for the borrower's loans, derived from multiple sources | `[]` | `{}` |
    | `TRUE_IS_CHARGED_OFF` | 132 | `BOOLEAN` | Boolean indicating if the loan is charged off (DPD >= 120) | Boolean indicating if the loan is charged off (DPD >= 120) | `[]` | `{}` |
    | `TRUE_IS_PAST_DUE` | 133 | `BOOLEAN` | Boolean indicating if the loan is past due but not charged off (DPD < 120) | Boolean indicating if the loan is past due but not charged off (DPD < 120) | `[]` | `{}` |
    | `DPD_BUCKET_FINAL` | 134 | `TEXT` | Days past due bucket (Current, Late 1, Late 15, Late 30, Late 60, Late 90, Charged-Off) | Days past due bucket (Current, Late 1, Late 15, Late 30, Late 60, Late 90, Charged-Off) | `[]` | `{}` |
    | `WAS_COLLECTIONS_CONTACT_ROUTED_TO_SUPPORT` | 135 | `BOOLEAN` | Boolean indicating if a collections contact was routed to support | Boolean indicating if a collections contact was routed to support | `[]` | `{}` |
    | `WAS_AGENT_COMMITMENT` | 136 | `BOOLEAN` | Boolean indicating if the agent secured a payment commitment (same-day payment or promise to pay or forbearance or loan modification) | Boolean indicating if the agent secured a payment commitment (same-day payment or promise to pay or forbearance or loan modification) | `[]` | `{}` |
    | `WAS_AGENT_COMMITMENT_PAYMENT` | 137 | `BOOLEAN` | Boolean indicating if the agent commitment resulted in a payment | Boolean indicating if the agent commitment resulted in a payment | `[]` | `{}` |
    | `SUM_AGENT_COMMITMENT_PAYMENT_AMT` | 138 | `NUMBER` | Total amount paid from agent-secured commitments | Total amount paid from agent-secured commitments | `[]` | `{}` |
    | `WAS_SAME_DAY_SELF_SERVE_PAYMENT` | 139 | `BOOLEAN` | Boolean indicating if a self-service payment was made the same day | Boolean indicating if a self-service payment was made the same day | `[]` | `{}` |
    | `SAME_DAY_SELF_SERVE_PAYMENT_AMT` | 140 | `FLOAT` | Amount of self-service payment made same day | Amount of self-service payment made same day | `[]` | `{}` |
    | `WAS_SELF_SERVE_OR_AGENT_COMMITTED_PAYMENT` | 141 | `BOOLEAN` | Boolean indicating if any payment was made (self-serve or agent-committed) | Boolean indicating if any payment was made (self-serve or agent-committed) | `[]` | `{}` |
    | `SELF_SERVE_OR_AGENT_COMMITTED_PAYMENT_AMT` | 142 | `FLOAT` | Total amount of payments (self-serve or agent-committed) | Total amount of payments (self-serve or agent-committed) | `[]` | `{}` |
    | `IS_SUPPORT_ELIGIBLE` | 143 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_SUPPORT_TEAM` | 144 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_COLLECTIONS_ELIGIBLE` | 145 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_COLLECTIONS_TEAM` | 146 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `UPDATED_AT_PT` | 147 | `TIMESTAMP_NTZ` | Timestamp in Pacific Time when the ticket was last updated | Timestamp in Pacific Time when the ticket was last updated | `[]` | `{}` |
    | `FIVETRAN_SYNCED_PT` | 148 | `TIMESTAMP_NTZ` | Timestamp in Pacific Time when the data was synced by Fivetran | Timestamp in Pacific Time when the data was synced by Fivetran | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.int_zendesk_tickets_enriched`

---
