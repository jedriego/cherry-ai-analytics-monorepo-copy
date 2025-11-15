## Model: `nice_collections_contacts_xf_archive`

`nice_collections_contacts_xf_archive`

*   **Unique ID:** `model.cherry_data_model.nice_collections_contacts_xf_archive`
*   **FQN:** `prod.archive.nice_collections_contacts_xf_archive`
*   **Description:** This model transforms and consolidates collections contact data from NICE inbound and outbound systems. It includes contact details, agent information, disposition data, and payment metrics for collections and recoveries teams.

*   **Tags:** `['archive']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CONTACT_ID` | 1 | `NUMBER` | Unique identifier for the contact interaction | Unique identifier for the contact interaction | `[]` | `{}` |
    | `CONTACT_START_PT` | 2 | `TIMESTAMP_NTZ` | Timestamp in Pacific Time when the contact interaction started | Timestamp in Pacific Time when the contact interaction started | `[]` | `{}` |
    | `MEDIA_TYPE_NAME` | 3 | `TEXT` | Channel of communication (Phone, SMS, Chat, Email) | Channel of communication (Phone, SMS, Chat, Email) | `[]` | `{}` |
    | `INITIAL_SKILL_NAME` | 4 | `TEXT` | Initial skill/queue the contact was routed to | Initial skill/queue the contact was routed to | `[]` | `{}` |
    | `FINAL_SKILL_NAME` | 5 | `TEXT` | Final skill/queue that handled the contact | Final skill/queue that handled the contact | `[]` | `{}` |
    | `DIRECTION` | 6 | `TEXT` | Direction of contact (Inbound/Outbound) | Direction of contact (Inbound/Outbound) | `[]` | `{}` |
    | `SPECIALIST` | 7 | `TEXT` | Name of the collections agent who handled the contact | Name of the collections agent who handled the contact | `[]` | `{}` |
    | `INTERACTION_PHONE_NUMBER` | 8 | `TEXT` | Phone number associated with the interaction | Phone number associated with the interaction | `[]` | `{}` |
    | `INTERACTION_EMAIL` | 9 | `TEXT` | Email address associated with the interaction | Email address associated with the interaction | `[]` | `{}` |
    | `INTERACTION_IP_ADDRESS` | 10 | `TEXT` | IP address associated with the interaction | IP address associated with the interaction | `[]` | `{}` |
    | `DISPOSITION_NAME` | 11 | `TEXT` | Agent-selected final disposition/outcome of the contact | Agent-selected final disposition/outcome of the contact | `[]` | `{}` |
    | `INTERACTION_BORROWER_ID` | 12 | `NUMBER` | Borrower ID associated with the interaction | Borrower ID associated with the interaction | `[]` | `{}` |
    | `IS_RIGHT_PARTY_CONTACT` | 13 | `BOOLEAN` | Boolean indicating if the contact reached the intended borrower | Boolean indicating if the contact reached the intended borrower | `[]` | `{}` |
    | `IS_CONVERSION` | 14 | `BOOLEAN` | Boolean indicating if the contact resulted in a conversion (payment, promise to pay, forbearance, etc.) | Boolean indicating if the contact resulted in a conversion (payment, promise to pay, forbearance, etc.) | `[]` | `{}` |
    | `HANDLE_TIME` | 15 | `NUMBER` | Total time spent handling the contact (including after-call work) | Total time spent handling the contact (including after-call work) | `[]` | `{}` |
    | `AFTER_CALL_WORK_TIME` | 16 | `NUMBER` | Time spent on after-call work | Time spent on after-call work | `[]` | `{}` |
    | `DPD_BUCKET_FINAL` | 17 | `TEXT` | Days past due bucket (Late 1, Late 30, Late 60, Late 90, Charged-Off) for the most delinquent loan | Days past due bucket (Late 1, Late 30, Late 60, Late 90, Charged-Off) for the most delinquent loan | `[]` | `{}` |
    | `DAYS_PAST_DUE` | 18 | `NUMBER` | Exact number of days past due for the most delinquent loan | Exact number of days past due for the most delinquent loan | `[]` | `{}` |
    | `IS_SAFE_SELECT_OUTBOUND` | 19 | `BOOLEAN` | Boolean indicating if the contact was a Safe Select outbound call | Boolean indicating if the contact was a Safe Select outbound call | `[]` | `{}` |
    | `Q1_2025_COLLECTIONS_GROUP` | 20 | `TEXT` | Test/control group assignment for Q1 2025 collections experiment | Test/control group assignment for Q1 2025 collections experiment | `[]` | `{}` |
    | `WAS_ABANDONED` | 21 | `BOOLEAN` | Boolean indicating if the contact was abandoned | Boolean indicating if the contact was abandoned | `[]` | `{}` |
    | `WAS_SHORT_ABANDON` | 22 | `BOOLEAN` | Boolean indicating if the contact was abandoned quickly (within 15 seconds), Collections excludes these in traditional abandon reporting. | Boolean indicating if the contact was abandoned quickly (within 15 seconds), Collections excludes these in traditional abandon reporting. | `[]` | `{}` |
    | `WAS_AGENT_COMMITMENT` | 23 | `BOOLEAN` | Boolean indicating if the agent secured a payment commitment (same-day payment or promise to pay or forbearance or loan modification) | Boolean indicating if the agent secured a payment commitment (same-day payment or promise to pay or forbearance or loan modification) | `[]` | `{}` |
    | `WAS_AGENT_COMMITMENT_PAYMENT` | 24 | `BOOLEAN` | Boolean indicating if the agent commitment resulted in a payment | Boolean indicating if the agent commitment resulted in a payment | `[]` | `{}` |
    | `SUM_AGENT_COMMITMENT_PAYMENT_AMT` | 25 | `NUMBER` | Total amount paid from agent-secured commitments | Total amount paid from agent-secured commitments | `[]` | `{}` |
    | `WAS_SAME_DAY_SELF_SERVE_PAYMENT` | 26 | `BOOLEAN` | Boolean indicating if a self-service payment was made the same day | Boolean indicating if a self-service payment was made the same day | `[]` | `{}` |
    | `SAME_DAY_SELF_SERVE_PAYMENT_AMT` | 27 | `FLOAT` | Amount of self-service payment made same day | Amount of self-service payment made same day | `[]` | `{}` |
    | `WAS_SELF_SERVE_OR_AGENT_COMMITTED_PAYMENT` | 28 | `BOOLEAN` | Boolean indicating if any payment was made (self-serve or agent-committed) | Boolean indicating if any payment was made (self-serve or agent-committed) | `[]` | `{}` |
    | `SELF_SERVE_OR_AGENT_COMMITTED_PAYMENT_AMT` | 29 | `FLOAT` | Total amount of payments (self-serve or agent-committed) | Total amount of payments (self-serve or agent-committed) | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.collections_test_control_population_q1_2025`
    *   `model.cherry_data_model.daily_loan_xf`
    *   `model.cherry_data_model.int_cherry_and_loanpro_payments`
    *   `model.cherry_data_model.int_nice_inbounds_contact_information_joined`
    *   `model.cherry_data_model.int_nice_outbounds_contact_information_joined`
    *   `model.cherry_data_model.nice_collections_dials_xf_archive`
    *   `model.cherry_data_model.servicing_rep_incentive_xf`
    *   `model.cherry_data_model.src_cherry_loans`
    *   `model.cherry_data_model.stg_nice_contacts`
    *   `seed.cherry_data_model.ops_user_teams`

---
