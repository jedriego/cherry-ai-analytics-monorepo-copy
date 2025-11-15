## Model: `nice_support_conversion_rate_xf_archive`

`nice_support_conversion_rate_xf_archive`

*   **Unique ID:** `model.cherry_data_model.nice_support_conversion_rate_xf_archive`
*   **FQN:** `prod.archive.nice_support_conversion_rate_xf_archive`
*   **Description:** This model tracks conversion rates for NICE support interactions by measuring how many eligible  support contacts result in successful application submissions, approvals, or denials within  a defined attribution window. It focuses on inbound support contacts related to application assistance.

*   **Tags:** `['archive']`
*   **Meta:** `{'sources': [{'name': 'nice', 'tables': [{'name': 'inbounds', 'description': 'Raw inbound contact data from NICE'}], 'description': 'Source data from NICE contact center platform'}, {'name': 'cherry', 'tables': [{'name': 'applications', 'description': 'Raw applications data'}, {'name': 'application_status_timeline', 'description': 'Timeline tracking status changes for applications'}], 'description': 'Application system data source'}], 'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CONTACT_ID` | 1 | `NUMBER` | Unique identifier for the NICE contact | Unique identifier for the NICE contact | `[]` | `{}` |
    | `CONTACT_START_PT` | 2 | `TIMESTAMP_NTZ` | Timestamp in Pacific Time when the contact started | Timestamp in Pacific Time when the contact started | `[]` | `{}` |
    | `CONTACT_END_PT` | 3 | `TIMESTAMP_NTZ` | Timestamp in Pacific Time when the contact ended | Timestamp in Pacific Time when the contact ended | `[]` | `{}` |
    | `CONTACT_LENGTH` | 4 | `NUMBER` |  |  | `[]` | `{}` |
    | `DIRECTION` | 5 | `TEXT` | Direction of the contact (Inbound/Outbound) | Direction of the contact (Inbound/Outbound) | `[]` | `{}` |
    | `INITIAL_SKILL_NAME` | 6 | `TEXT` | Initial skill/queue the contact was routed to | Initial skill/queue the contact was routed to | `[]` | `{}` |
    | `MEDIA_TYPE_NAME` | 7 | `TEXT` | Channel of communication (Phone, SMS, Chat, Email) | Channel of communication (Phone, SMS, Chat, Email) | `[]` | `{}` |
    | `SERVICE_LEVEL_CATEGORY` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `OWNING_TEAM` | 9 | `TEXT` |  |  | `[]` | `{}` |
    | `T_HANDLE` | 10 | `NUMBER` |  |  | `[]` | `{}` |
    | `INITIAL_AGENT_NAME` | 11 | `TEXT` | Name of the first agent who handled the contact | Name of the first agent who handled the contact | `[]` | `{}` |
    | `INITIAL_TEAM_NAME` | 12 | `TEXT` |  |  | `[]` | `{}` |
    | `FINAL_SKILL_NAME` | 13 | `TEXT` | Final skill/queue that handled the contact | Final skill/queue that handled the contact | `[]` | `{}` |
    | `FINAL_AGENT_NAME` | 14 | `TEXT` | Name of the last agent who handled the contact | Name of the last agent who handled the contact | `[]` | `{}` |
    | `FINAL_TEAM_NAME` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `INTERACTION_PHONE_NUMBER` | 16 | `TEXT` | Phone number associated with the interaction | Phone number associated with the interaction | `[]` | `{}` |
    | `INTERACTION_EMAIL` | 17 | `TEXT` | Email address associated with the interaction | Email address associated with the interaction | `[]` | `{}` |
    | `INTERACTION_IP_ADDRESS` | 18 | `TEXT` |  |  | `[]` | `{}` |
    | `DISPOSITION_NAME` | 19 | `TEXT` | Disposition code for the support interaction | Disposition code for the support interaction | `[]` | `{}` |
    | `WAS_ABANDONED` | 20 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `WAS_REFUSED` | 21 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_RIGHT_PARTY_CONTACT` | 22 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_CONVERSION` | 23 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `IS_CONTACT` | 24 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `WAS_SHORT_ABANDON` | 25 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `BORROWER_KYC_STATUS` | 26 | `TEXT` | KYC (Know Your Customer) status of the borrower | KYC (Know Your Customer) status of the borrower | `[]` | `{}` |
    | `INTERACTION_BORROWER_ID` | 27 | `NUMBER` | Borrower ID associated with the support interaction | Borrower ID associated with the support interaction | `[]` | `{}` |
    | `INTERACTION_MERCHANT_ID` | 28 | `NUMBER` |  |  | `[]` | `{}` |
    | `INTERACTION_ORGANIZATION_ID` | 29 | `NUMBER` |  |  | `[]` | `{}` |
    | `INTERACTION_DAYS_AGO` | 30 | `NUMBER` |  |  | `[]` | `{}` |
    | `APPLICATION_ID` | 31 | `NUMBER` | ID of the application associated with the support interaction | ID of the application associated with the support interaction | `[]` | `{}` |
    | `INITIAL_STATUS` | 32 | `TEXT` | Initial status of the application in the application timeline | Initial status of the application in the application timeline | `[]` | `{}` |
    | `INITIAL_STATUS_PT` | 33 | `TIMESTAMP_NTZ` | Timestamp in Pacific Time of the initial application status | Timestamp in Pacific Time of the initial application status | `[]` | `{}` |
    | `STATUS_TWO` | 34 | `TEXT` | Second status of the application in the application timeline | Second status of the application in the application timeline | `[]` | `{}` |
    | `STATUS_TWO_PT` | 35 | `TIMESTAMP_NTZ` | Timestamp in Pacific Time of the second application status | Timestamp in Pacific Time of the second application status | `[]` | `{}` |
    | `STATUS_THREE` | 36 | `TEXT` | Third status of the application in the application timeline | Third status of the application in the application timeline | `[]` | `{}` |
    | `STATUS_THREE_PT` | 37 | `TIMESTAMP_NTZ` | Timestamp in Pacific Time of the third application status | Timestamp in Pacific Time of the third application status | `[]` | `{}` |
    | `STATUS_FOUR` | 38 | `TEXT` | Fourth status of the application in the application timeline | Fourth status of the application in the application timeline | `[]` | `{}` |
    | `STATUS_FOUR_PT` | 39 | `TIMESTAMP_NTZ` | Timestamp in Pacific Time of the fourth application status | Timestamp in Pacific Time of the fourth application status | `[]` | `{}` |
    | `FINAL_STATUS` | 40 | `TEXT` | Final status of the application (APPROVED, DENIED, etc.) | Final status of the application (APPROVED, DENIED, etc.) | `[]` | `{}` |
    | `FINAL_STATUS_PT` | 41 | `TIMESTAMP_NTZ` | Timestamp in Pacific Time of the final application status | Timestamp in Pacific Time of the final application status | `[]` | `{}` |
    | `INCOME_VERIFICATION_REQUIRED` | 42 | `NUMBER` |  |  | `[]` | `{}` |
    | `KYC_REQUIRED` | 43 | `NUMBER` |  |  | `[]` | `{}` |
    | `FROZEN_AT_SOME_POINT` | 44 | `NUMBER` |  |  | `[]` | `{}` |
    | `TIME_TO_COMPLETION_MINS` | 45 | `NUMBER` | Time in minutes from initial status to final status | Time in minutes from initial status to final status | `[]` | `{}` |
    | `TIME_TO_COMPLETION_DAYS` | 46 | `NUMBER` | Time in hours from initial status to final status | Time in hours from initial status to final status | `[]` | `{}` |
    | `ATTRIBUTION_WINDOW` | 47 | `NUMBER` | Number of hours (191) after a support interaction during which application status changes are attributed to the support contact | Number of hours (191) after a support interaction during which application status changes are attributed to the support contact | `[]` | `{}` |
    | `CONVERSION_ELIGIBLE` | 48 | `NUMBER` | Boolean (1/0) indicating if the support interaction is eligible for conversion tracking. Eligibility is based on disposition codes related to application assistance and excludes rescinded applications and blacklisted borrowers.
 | Boolean (1/0) indicating if the support interaction is eligible for conversion tracking. Eligibility is based on disposition codes related to application assistance and excludes rescinded applications and blacklisted borrowers.
 | `[]` | `{}` |
    | `CONVERTED` | 49 | `NUMBER` | Boolean (1/0) indicating if the eligible support interaction resulted in a conversion. Conversion occurs when an application status changes to APPROVED or DENIED within the attribution window after the support interaction.
 | Boolean (1/0) indicating if the eligible support interaction resulted in a conversion. Conversion occurs when an application status changes to APPROVED or DENIED within the attribution window after the support interaction.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.int_nice_inbounds_contact_information_joined`
    *   `model.cherry_data_model.src_cherry_applications`
    *   `model.cherry_data_model.stg_cherry_application_status_timeline`

---
