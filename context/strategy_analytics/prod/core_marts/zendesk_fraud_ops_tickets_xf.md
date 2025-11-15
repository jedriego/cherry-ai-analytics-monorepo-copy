## Model: `zendesk_fraud_ops_tickets_xf`

`zendesk_fraud_ops_tickets_xf`

*   **Unique ID:** `model.cherry_data_model.zendesk_fraud_ops_tickets_xf`
*   **FQN:** `prod.core_marts.zendesk_fraud_ops_tickets_xf`
*   **Description:** Filtered Zendesk tickets view specifically for Fraud Operations team activities, enhanced with combined transcript data. This model selects only tickets assigned to the 'Fraud Operations' team from the staging Zendesk tickets data and joins them with conversation transcripts aggregated chronologically. The model combines multiple transcript entries per ticket into a single consolidated transcript field, ordered by day to maintain conversation flow. This is essential for fraud investigation workflows, providing fraud operations analysts with complete ticket information alongside full conversation context in a single record for efficient case review and analysis.

*   **Tags:** `['core', 'zendesk_refresh']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `TICKET_ID` | 1 | `NUMBER` | Unique identifier for the Zendesk ticket. Inherited from stg_zendesk_tickets and serves as the primary key for this model. Only includes tickets assigned to the 'Fraud Operations' team, making this a filtered subset of all tickets.
 | Unique identifier for the Zendesk ticket. Inherited from stg_zendesk_tickets and serves as the primary key for this model. Only includes tickets assigned to the 'Fraud Operations' team, making this a filtered subset of all tickets.
 | `[]` | `{}` |
    | `URL` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `AGENT_NAME` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `AGENT_USER_ID` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `REQUESTER_NAME` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `REQUESTER_USER_ID` | 6 | `NUMBER` |  |  | `[]` | `{}` |
    | `SUBMITTER_NAME` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `SUBMITTER_USER_ID` | 8 | `NUMBER` |  |  | `[]` | `{}` |
    | `DIRECTION` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_TCN_OUTBOUND` | 10 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `BORROWER_ID` | 11 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_ID` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `ORGANIZATION_ID` | 13 | `TEXT` |  |  | `[]` | `{}` |
    | `GROUP_NAME` | 14 | `TEXT` |  |  | `[]` | `{}` |
    | `TEAM` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `MANAGER` | 16 | `TEXT` |  |  | `[]` | `{}` |
    | `TICKET_CURRENT_STATUS` | 17 | `TEXT` |  |  | `[]` | `{}` |
    | `MEDIA_TYPE_NAME` | 18 | `TEXT` |  |  | `[]` | `{}` |
    | `WAS_CALLBACK` | 19 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `CUSTOMER_TYPE` | 20 | `TEXT` |  |  | `[]` | `{}` |
    | `PATIENT_PRACTICE_SEGMENTATION` | 21 | `TEXT` |  |  | `[]` | `{}` |
    | `TIER` | 22 | `TEXT` |  |  | `[]` | `{}` |
    | `TICKET_CREATED_AT_PT` | 23 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `TICKET_FIRST_TOUCHED_PT` | 24 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `CHAT_SMS_FIRST_AGENT_RESPONSE_PT` | 25 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `CHAT_SMS_FIRST_CUSTOMER_RESPONSE_TO_AGENT_PT` | 26 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `TICKET_RESOLVED_PT` | 27 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `TIME_IN_QUEUE` | 28 | `NUMBER` |  |  | `[]` | `{}` |
    | `WAS_ABANDONED` | 29 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `WAS_SHORT_ABANDON` | 30 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `SERVICE_LEVEL_SECONDS` | 31 | `NUMBER` |  |  | `[]` | `{}` |
    | `SERVICE_LEVEL_THRESHOLD` | 32 | `NUMBER` |  |  | `[]` | `{}` |
    | `MET_SERVICE_LEVEL` | 33 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `HANDLE_TIME` | 34 | `NUMBER` |  |  | `[]` | `{}` |
    | `HOLD_TIME` | 35 | `NUMBER` |  |  | `[]` | `{}` |
    | `JEENIE_TRANSFER_FLAG` | 36 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `COLLECTIONS_TRANSFERS_FLAG` | 37 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ALLE_TRANSFER_FLAG` | 38 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `AFTER_CALL_WORK_TIME` | 39 | `NUMBER` |  |  | `[]` | `{}` |
    | `INTERACTION_PHONE_NUMBER` | 40 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERACTION_EMAIL_ADDRESS` | 41 | `TEXT` |  |  | `[]` | `{}` |
    | `EMAIL` | 42 | `TEXT` |  |  | `[]` | `{}` |
    | `YELLOW_CONVERSATION_ID` | 43 | `TEXT` |  |  | `[]` | `{}` |
    | `YELLOW_SESSION_ID` | 44 | `TEXT` |  |  | `[]` | `{}` |
    | `LOAN_ID` | 45 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_PAST_DUE` | 46 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_CHARGED_OFF` | 47 | `TEXT` |  |  | `[]` | `{}` |
    | `MERGED_TICKET_IDS` | 48 | `VARIANT` |  |  | `[]` | `{}` |
    | `YELLOW_SUMMARIZATION` | 49 | `TEXT` |  |  | `[]` | `{}` |
    | `EMAIL_SUBJECT` | 50 | `TEXT` |  |  | `[]` | `{}` |
    | `EMAIL_DESCRIPTION` | 51 | `TEXT` |  |  | `[]` | `{}` |
    | `SCHEDULED_TIME` | 52 | `DATE` |  |  | `[]` | `{}` |
    | `EARLY_CALLBACK` | 53 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `CALLBACK_TIME` | 54 | `TEXT` |  |  | `[]` | `{}` |
    | `COLLECTIONS_BORROWER_FLAG` | 55 | `TEXT` |  |  | `[]` | `{}` |
    | `WAS_COMPLAINT` | 56 | `TEXT` |  |  | `[]` | `{}` |
    | `WAS_COLLECTIONS_CONTACT_ROUTED_TO_SUPPORT` | 57 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `AGENT_DISPOSITION` | 58 | `TEXT` |  |  | `[]` | `{}` |
    | `PATIENT_DISPOSITION` | 59 | `TEXT` |  |  | `[]` | `{}` |
    | `PRACTICE_DISPOSITION` | 60 | `TEXT` |  |  | `[]` | `{}` |
    | `ALLE_DISPOSITION` | 61 | `TEXT` |  |  | `[]` | `{}` |
    | `COLLECTIONS_DISPOSITION` | 62 | `TEXT` |  |  | `[]` | `{}` |
    | `COLLECTIONS_TIER` | 63 | `TEXT` |  |  | `[]` | `{}` |
    | `RECOVERIES_DISPOSITION` | 64 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_RIGHT_PARTY_CONTACT` | 65 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_COLLECTIONS_CONVERSION` | 66 | `TEXT` |  |  | `[]` | `{}` |
    | `CSAT_SCORE` | 67 | `NUMBER` |  |  | `[]` | `{}` |
    | `MAX_DAYS_PAST_DUE` | 68 | `NUMBER` |  |  | `[]` | `{}` |
    | `IS_FORBEARANCE` | 69 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `PRIORITY` | 70 | `TEXT` |  |  | `[]` | `{}` |
    | `HAS_INCIDENTS` | 71 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_PUBLIC` | 72 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `VIA_FOLLOWUP_SOURCE_ID` | 73 | `NUMBER` |  |  | `[]` | `{}` |
    | `FOLLOWUP_IDS` | 74 | `VARIANT` |  |  | `[]` | `{}` |
    | `TICKET_FORM_ID` | 75 | `NUMBER` |  |  | `[]` | `{}` |
    | `ALLOW_CHANNELBACK` | 76 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ALLOW_ATTACHMENTS` | 77 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `FROM_MESSAGING_CHANNEL` | 78 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `USER_AUTHENTICATION` | 79 | `TEXT` |  |  | `[]` | `{}` |
    | `TIER_STRING` | 80 | `TEXT` |  |  | `[]` | `{}` |
    | `LANGUAGE_CONFIDENCE` | 81 | `TEXT` |  |  | `[]` | `{}` |
    | `TIME_SPENT_LAST_UPDATE_SEC` | 82 | `NUMBER` |  |  | `[]` | `{}` |
    | `LANGUAGE` | 83 | `TEXT` |  |  | `[]` | `{}` |
    | `SUPPORTCODE` | 84 | `TEXT` |  |  | `[]` | `{}` |
    | `SENTIMENT_CONFIDENCE` | 85 | `TEXT` |  |  | `[]` | `{}` |
    | `SENTIMENT` | 86 | `TEXT` |  |  | `[]` | `{}` |
    | `CALLBACK_STATUS` | 87 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `SYSTEM_LOCATION` | 88 | `TEXT` |  |  | `[]` | `{}` |
    | `SYSTEM_RAW_EMAIL_IDENTIFIER` | 89 | `TEXT` |  |  | `[]` | `{}` |
    | `SYSTEM_JSON_EMAIL_IDENTIFIER` | 90 | `TEXT` |  |  | `[]` | `{}` |
    | `SYSTEM_IP_ADDRESS` | 91 | `TEXT` |  |  | `[]` | `{}` |
    | `SYSTEM_EML_REDACTED` | 92 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `SYSTEM_EMAIL_ID` | 93 | `TEXT` |  |  | `[]` | `{}` |
    | `SYSTEM_LATITUDE` | 94 | `FLOAT` |  |  | `[]` | `{}` |
    | `SYSTEM_LONGITUDE` | 95 | `FLOAT` |  |  | `[]` | `{}` |
    | `SYSTEM_MESSAGE_ID` | 96 | `TEXT` |  |  | `[]` | `{}` |
    | `VIA_SOURCE_FROM_NAME` | 97 | `TEXT` |  |  | `[]` | `{}` |
    | `SYSTEM_CLIENT` | 98 | `TEXT` |  |  | `[]` | `{}` |
    | `VIA_SOURCE_TO_PHONE` | 99 | `TEXT` |  |  | `[]` | `{}` |
    | `VIA_SOURCE_FROM_PHONE` | 100 | `TEXT` |  |  | `[]` | `{}` |
    | `VIA_SOURCE_TO_FORMATTED_PHONE` | 101 | `TEXT` |  |  | `[]` | `{}` |
    | `VIA_SOURCE_FROM_FORMATTED_PHONE` | 102 | `TEXT` |  |  | `[]` | `{}` |
    | `VIA_SOURCE_TO_BRAND_ID` | 103 | `NUMBER` |  |  | `[]` | `{}` |
    | `VIA_SOURCE_FROM_SUBJECT` | 104 | `TEXT` |  |  | `[]` | `{}` |
    | `VIA_SOURCE_FROM_CHANNEL` | 105 | `TEXT` |  |  | `[]` | `{}` |
    | `VIA_SOURCE_FROM_BRAND_ID` | 106 | `NUMBER` |  |  | `[]` | `{}` |
    | `TOPIC` | 107 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_ARRAY` | 108 | `TEXT` |  |  | `[]` | `{}` |
    | `URL_VISITATION` | 109 | `TEXT` |  |  | `[]` | `{}` |
    | `PROBLEM_ID` | 110 | `NUMBER` |  |  | `[]` | `{}` |
    | `BRAND_ID` | 111 | `NUMBER` |  |  | `[]` | `{}` |
    | `FORUM_TOPIC_ID` | 112 | `NUMBER` |  |  | `[]` | `{}` |
    | `SYSTEM_MACHINE_GENERATED` | 113 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `SUN_CO_CONVERSATION_ID` | 114 | `TEXT` |  |  | `[]` | `{}` |
    | `TCN_DIALED_FROM` | 115 | `TEXT` |  |  | `[]` | `{}` |
    | `LOAN_DAYS_PAST_DUE` | 116 | `TEXT` |  |  | `[]` | `{}` |
    | `MONTHS_SINCE_CHARGED_OFF` | 117 | `NUMBER` |  |  | `[]` | `{}` |
    | `SKILL` | 118 | `TEXT` |  |  | `[]` | `{}` |
    | `PRACTICE_RECOVERIES` | 119 | `TEXT` |  |  | `[]` | `{}` |
    | `MANUAL_FUNDING_RULE` | 120 | `TEXT` |  |  | `[]` | `{}` |
    | `FOLLOW_UP_DATE` | 121 | `DATE` |  |  | `[]` | `{}` |
    | `CALLER_ID` | 122 | `TEXT` |  |  | `[]` | `{}` |
    | `CLEAR_TIE_BETWEEN_PROVIDED_PII_AND_BORROWER_PII` | 123 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `CALLED_OUT_TO_BORROWER` | 124 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `CONFIRMED_BORROWER_IN_CALL` | 125 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_ON_SSN` | 126 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NO_CLEAR_TIE_BETWEEN_PROVIDED_PII_AND_BORROWER_PII` | 127 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_MULTIPLE_MATCHING_IDENTITY_CONCERNS` | 128 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CLUSTERED_APPLICATIONS_CONCERNS_ON_SENTILINK_INSIGHTS_APPLICATION_INFORMATION` | 129 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_ON_THE_ID_DRIVER_S_LICENSE_FAIL_IF_IT_IS_A_SUSPICIOUS_FABRICATED_DOCUMENT` | 130 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_ON_THE_EMAIL_ADDRESS_REPORT_TO_THE_BORROWER` | 131 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_ON_THE_PHONE_NUMBER_REPORTING_TO_THE_BORROWER` | 132 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_ON_THE_ADDRESS_REPORTING_TO_THE_BORROWER` | 133 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_ON_WHETHER_THE_DOCUMENTS_ARE_LIVE_PHOTOS` | 134 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_THE_DOCUMENT_EXPIRED` | 135 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_ON_SELFIE_PHOTO_MATCHING_THE_ID_PHOTO` | 136 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_ON_DRIVER_S_LICENSE_MATCHING_THE_APPLICATION_REPORT_TO_THE_BORROWER` | 137 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_ON_ID_THEFT_SCORE_REVIEW_IF_ABOVE_750` | 138 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_THERE_ANY_SUSPICIOUS_ACTIVITY_WITH_THIS_BORROWER_AND_PRACTICE_OTHER_CHERRY_PRACTICES_REFER_TO_PURE_CELEBRITEA` | 139 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `HAS_THE_BORROWER_APPLIED_TO_ANY_SUSPICIOUS_CONFIRMED_FRAUD_PRACTICE` | 140 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_THE_BORROWER_CONNECTED_TO_A_CHERRY_MERCHANT_PRACTICE_OF_THEIR_OWN` | 141 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ARE_THERE_ANY_CONCERNS_WITH_THE_SENTILINK_APP_FRAUD_SCORES` | 142 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ARE_THERE_ANY_CONCERNS_WITH_THE_UTILIZATION` | 143 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_WITH_AVG_PRACTICE_SENTILINK_SCORES_PERCENTILE` | 144 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_WITH_FPD_RATE_LIFETIME` | 145 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_PREVIOUS_WEBHOOKS_FIRED_ON_PRACTICE` | 146 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_BORROWER_LINKS_TO_OTHER_BORROWERS_USERS_MERCHANTS` | 147 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ARE_THERE_A_LARGE_OF_BORROWERS_FROM_ANOTHER_STATE` | 148 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_OTHER_NOTES_ON_FRAUD_ID_REPORTING_DATABASE_REVIEW` | 149 | `TEXT` |  |  | `[]` | `{}` |
    | `ARE_THERE_ANY_CONCERNS_AFTER_REVIEWING_THE_WEBSITE_SERVICES_REVIEW_AVG_TICKET_SIZE_COMPARED_TO_EXPECTED_BASED_ON_SERVICES` | 150 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ARE_THERE_ANY_CONCERNS_WHEN_REVIEWING_THE_EMAILS_STATES_FOR_PAST_10_BORROWERS` | 151 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ARE_THERE_ANY_CONCERNS_FROM_REVIEWING_AT_LEAST_THREE_BORROWERS_TO_ASCERTAIN_WHETHER_ID_THEFT_IS_OCCURRING` | 152 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `CONDUCTED_PRACTICE_EXPERIENCE_CALL` | 153 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `VOIDED_CONTRACT` | 154 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_WITH_FRAUD_ID_REPORTING_DATABASES` | 155 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_WITH_PREVIOUS_BORROWER_PREVIOUS_APPLICATIONS_CONTRACTS` | 156 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_WITH_PERSONA_RESULTS_IF_BORROWER_COMPLETED` | 157 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_FROM_REVIEWING_THE_BASIC_PRACTICE_RISK_DATA` | 158 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `SEND_EMAIL_TO_PRACTICE` | 159 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `MANUAL_FUNDING_CATEGORY` | 160 | `TEXT` |  |  | `[]` | `{}` |
    | `INTENT_CONFIDENCE` | 161 | `TEXT` |  |  | `[]` | `{}` |
    | `INTENT` | 162 | `TEXT` |  |  | `[]` | `{}` |
    | `SUSPECTED_FRAUD` | 163 | `TEXT` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_ON_THE_PHONE_NUMBER_EMAIL_ADDRESS_REPORTING_TO_THE_BORROWER` | 164 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_PRACTICE_ABUSE_FRAUD_RISK_SIGNALS` | 165 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `FUNDED_CONTRACT` | 166 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `SENT_EMAIL_TO_PRACTICE` | 167 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ARE_THERE_CONCERNS_ON_PRACTICE_ABUSE_FRAUD_RISK_SIGNALS` | 168 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_FROM_REVIEWING_THE_PRACTICE_ABUSE_FRAUD_RISK_SIGNALS` | 169 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_FROM_REVIEWING_PRACTICE_ABUSE_FRAUD_RISK_SIGNALS` | 170 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_WITH_BASIC_PRACTICE_RISK_SIGNALS` | 171 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `ANY_CONCERNS_WITH_PRACTICE_ABUSE_FRAUD_RISK_SIGNALS` | 172 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `REVIEW_CATEGORY` | 173 | `TEXT` |  |  | `[]` | `{}` |
    | `DO_NOT_DISCLOSE` | 174 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `FRAUD_OPS_TICKET_TYPE` | 175 | `TEXT` |  |  | `[]` | `{}` |
    | `SLACK_CHANNEL_ID` | 176 | `TEXT` |  |  | `[]` | `{}` |
    | `NOTES_FROM_FRAUD_ID_REPORTING_DATABASES` | 177 | `TEXT` |  |  | `[]` | `{}` |
    | `WEBHOOK_RULE` | 178 | `TEXT` |  |  | `[]` | `{}` |
    | `MORE_INFORMATION_REQUIRED` | 179 | `TEXT` |  |  | `[]` | `{}` |
    | `RATIONALE_FOR_FINAL_RESOLUTION` | 180 | `TEXT` |  |  | `[]` | `{}` |
    | `FINAL_RESOLUTION` | 181 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_COMPLAINTS_INBOX_SUPPORT` | 182 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_EXECUTIVE_ESCALATION_SUPPORT` | 183 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_SUPPORT_FAQ` | 184 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `NOTES_TOPIC` | 185 | `TEXT` |  |  | `[]` | `{}` |
    | `NOTES_OUTCOME` | 186 | `TEXT` |  |  | `[]` | `{}` |
    | `NOTES_SUMMARY` | 187 | `TEXT` |  |  | `[]` | `{}` |
    | `UPDATED_AT_PT` | 188 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `FIVETRAN_SYNCED_PT` | 189 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `TRANSCRIPT` | 190 | `TEXT` | Complete conversation transcript for the ticket, created by combining all individual transcript entries using LISTAGG function. Multiple transcript records per ticket are concatenated with spaces and ordered chronologically by day to maintain proper conversation flow. This provides fraud operations analysts with the full conversation context in a single field for efficient case review, investigation, and decision-making. Empty when no transcript data exists for the ticket. | Complete conversation transcript for the ticket, created by combining all individual transcript entries using LISTAGG function. Multiple transcript records per ticket are concatenated with spaces and ordered chronologically by day to maintain proper conversation flow. This provides fraud operations analysts with the full conversation context in a single field for efficient case review, investigation, and decision-making. Empty when no transcript data exists for the ticket. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.stg_zendesk_tickets`
    *   `model.cherry_data_model.stg_zendesk_transcripts`

---
