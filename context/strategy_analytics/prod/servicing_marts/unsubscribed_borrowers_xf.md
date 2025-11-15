## Model: `unsubscribed_borrowers_xf`

`unsubscribed_borrowers_xf`

*   **Unique ID:** `model.cherry_data_model.unsubscribed_borrowers_xf`
*   **FQN:** `prod.servicing_marts.unsubscribed_borrowers_xf`
*   **Description:** **Unified Borrower Communication Consent Management**
This model serves as the centralized source of truth for borrower communication consent and  unsubscribe status across all of Cherry's communication channels. It consolidates unsubscribe  and consent data from multiple platforms (Twilio, SendGrid, Genesys) with borrower information  to determine which borrowers have given consent for SMS and email communications. This unified  view is critical for TCPA compliance, CAN-SPAM compliance, and operational efficiency in  collections and customer service communications.
**Multi-Platform Integration:** - **Twilio SMS Unsubscribes**: Captures STOP messages and error codes (21610) indicating 
  unsubscribed phone numbers from SMS campaigns
- **SendGrid Email Unsubscribes**: Tracks unsubscribe and group_unsubscribe events from 
  email campaigns, specifically focusing on collections and recovery templates
- **Genesys SMS Consent**: Manages SMS acceptance preferences from the Genesys contact 
  center system for borrowers with external contact records

**Key Business Logic:** - **SMS Consent Calculation**: Returns TRUE when borrower is NOT in Twilio unsubscribes 
  AND either has Genesys SMS acceptance TRUE or NULL (default consent)
- **Email Consent Calculation**: Returns TRUE when borrower email is NOT in SendGrid 
  unsubscribes list (simple opt-out model)
- **Phone Number Validation**: Excludes invalid phone numbers ('9999999999', numbers 
  containing 'old' or 'conflict')
- **Flag Integration**: Includes borrower-level operational flags (do not call, cease 
  and desist) for comprehensive consent management

**Critical Staging Model Integration:** - **borrowers_merged_emails_xf**: Primary borrower data with intelligently merged email 
  addresses from multiple sources (borrower-provided and Plaid-sourced)
- **stg_unsubscribed_mobile_phones**: Twilio SMS unsubscribes derived from STOP messages 
  and delivery error codes (21610) indicating carrier-level blocks
- **stg_unsubscribed_borrower_emails**: SendGrid email unsubscribes from collections and 
  recovery email templates, tracking unsubscribe and group_unsubscribe events
- **src_genesys_external_contacts**: Genesys contact center SMS acceptance preferences 
  for borrowers with established external contact records
- **int_max_loan_flag_values**: Aggregated borrower-level operational flags including 
  do not call and cease and desist restrictions

**Compliance Framework:** - **TCPA (SMS)**: Ensures SMS communications only reach consenting borrowers by checking 
  both Twilio unsubscribes and Genesys consent preferences
- **CAN-SPAM (Email)**: Maintains email unsubscribe compliance through SendGrid tracking 
  and immediate opt-out enforcement
- **FDCPA (Collections)**: Integrates do not call and cease and desist flags for 
  collections compliance requirements

**Primary Use Cases:** - Real-time consent verification for collections and customer service communications - Compliance auditing and regulatory reporting for communication consent - Marketing campaign audience filtering and segmentation - Customer service workflow automation based on communication preferences - Data quality monitoring for communication consent accuracy
**Grain:** One record per borrower with current consent status across all communication channels

*   **Tags:** `['servicing_and_collections', 'genesys', 'trueaccord', 'debt-sale', 'sendgrid', 'twilio', 'collections_hourly']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `BORROWER_ID` | 1 | `NUMBER` | Unique borrower identifier from Cherry's system, serving as the primary key for this model.  Used for linking consent status to all borrower-related communications and operational  workflows across collections, customer service, and marketing systems.
 | Unique borrower identifier from Cherry's system, serving as the primary key for this model.  Used for linking consent status to all borrower-related communications and operational  workflows across collections, customer service, and marketing systems.
 | `[]` | `{}` |
    | `FIRST_NAME` | 2 | `TEXT` | First name of the borrower from the borrowers_merged_emails_xf source. Used for  personalized communications and account verification during consent-compliant  outreach efforts.
 | First name of the borrower from the borrowers_merged_emails_xf source. Used for  personalized communications and account verification during consent-compliant  outreach efforts.
 | `[]` | `{}` |
    | `LAST_NAME` | 3 | `TEXT` | Last name of the borrower from the borrowers_merged_emails_xf source. Used for  personalized communications and account verification during consent-compliant  outreach efforts.
 | Last name of the borrower from the borrowers_merged_emails_xf source. Used for  personalized communications and account verification during consent-compliant  outreach efforts.
 | `[]` | `{}` |
    | `BORROWER_SSN` | 4 | `TEXT` | Social Security Number of the borrower for identity verification purposes. Critical  for ensuring consent records are accurately attributed to the correct individual  and maintaining data integrity across communication systems.
 | Social Security Number of the borrower for identity verification purposes. Critical  for ensuring consent records are accurately attributed to the correct individual  and maintaining data integrity across communication systems.
 | `[]` | `{}` |
    | `DATE_OF_BIRTH` | 5 | `DATE` | Date of birth of the borrower for additional identity verification. Used to ensure  consent records are properly associated with the correct borrower and support  compliance verification processes.
 | Date of birth of the borrower for additional identity verification. Used to ensure  consent records are properly associated with the correct borrower and support  compliance verification processes.
 | `[]` | `{}` |
    | `BORROWER_ADDRESS_ID` | 6 | `NUMBER` | Foreign key reference to the borrower's address record. Used for linking geographic  information that may impact communication regulations and consent requirements  based on state and local laws.
 | Foreign key reference to the borrower's address record. Used for linking geographic  information that may impact communication regulations and consent requirements  based on state and local laws.
 | `[]` | `{}` |
    | `PHONE_NUMBER` | 7 | `TEXT` | Primary phone number from the borrower record after validation filtering. Excludes  invalid numbers ('9999999999', numbers containing 'old' or 'conflict'). Used as  the key for SMS consent verification and Twilio unsubscribe checking.
 | Primary phone number from the borrower record after validation filtering. Excludes  invalid numbers ('9999999999', numbers containing 'old' or 'conflict'). Used as  the key for SMS consent verification and Twilio unsubscribe checking.
 | `[]` | `{}` |
    | `CELL_NUMBER` | 8 | `TEXT` | Cell phone number from Genesys external contacts when available. Provides additional  contact information context and supports multi-number consent management for borrowers  with multiple phone numbers in different systems.
 | Cell phone number from Genesys external contacts when available. Provides additional  contact information context and supports multi-number consent management for borrowers  with multiple phone numbers in different systems.
 | `[]` | `{}` |
    | `UNSUBSCRIBED_NUMBER` | 9 | `TEXT` | Phone number found in Twilio unsubscribes list, indicating the borrower has sent  a STOP message or experienced carrier-level delivery failures (error code 21610).  When not null, indicates explicit SMS opt-out or delivery restriction.
 | Phone number found in Twilio unsubscribes list, indicating the borrower has sent  a STOP message or experienced carrier-level delivery failures (error code 21610).  When not null, indicates explicit SMS opt-out or delivery restriction.
 | `[]` | `{}` |
    | `PHONE_UNSUBSCRIBED_AT_PT` | 10 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `IS_ACCEPTING_SMS` | 11 | `BOOLEAN` | SMS acceptance preference from Genesys external contacts system. When FALSE, indicates  explicit SMS refusal in the contact center system. When TRUE or NULL, allows SMS  communications (NULL treated as default consent). Used in has_sms_consent calculation.
 | SMS acceptance preference from Genesys external contacts system. When FALSE, indicates  explicit SMS refusal in the contact center system. When TRUE or NULL, allows SMS  communications (NULL treated as default consent). Used in has_sms_consent calculation.
 | `[]` | `{}` |
    | `HAS_SMS_CONSENT` | 12 | `BOOLEAN` | **Primary SMS consent flag calculated through multi-platform logic.** Returns TRUE  when unsubscribed_number IS NULL (not in Twilio unsubscribes) AND is_accepting_sms  is TRUE or NULL (Genesys consent or default consent). This sophisticated logic ensures  SMS communications only reach borrowers who have not explicitly opted out and maintains  TCPA compliance across multiple consent tracking systems.
 | **Primary SMS consent flag calculated through multi-platform logic.** Returns TRUE  when unsubscribed_number IS NULL (not in Twilio unsubscribes) AND is_accepting_sms  is TRUE or NULL (Genesys consent or default consent). This sophisticated logic ensures  SMS communications only reach borrowers who have not explicitly opted out and maintains  TCPA compliance across multiple consent tracking systems.
 | `[]` | `{}` |
    | `EMAIL` | 13 | `TEXT` | Primary email address from borrowers_merged_emails_xf, intelligently combining  borrower-provided and Plaid-sourced emails. Used as the key for email consent  verification and SendGrid unsubscribe checking.
 | Primary email address from borrowers_merged_emails_xf, intelligently combining  borrower-provided and Plaid-sourced emails. Used as the key for email consent  verification and SendGrid unsubscribe checking.
 | `[]` | `{}` |
    | `UNSUBSCRIBED_EMAIL` | 14 | `TEXT` | Email address found in SendGrid unsubscribes list from collections and recovery  email campaigns. When not null, indicates explicit email opt-out through unsubscribe  or group_unsubscribe events. Used to prevent future email communications.
 | Email address found in SendGrid unsubscribes list from collections and recovery  email campaigns. When not null, indicates explicit email opt-out through unsubscribe  or group_unsubscribe events. Used to prevent future email communications.
 | `[]` | `{}` |
    | `EMAIL_UNSUBSCRIBED_AT_PT` | 15 | `TIMESTAMP_TZ` |  |  | `[]` | `{}` |
    | `HAS_EMAIL_CONSENT` | 16 | `BOOLEAN` | **Primary email consent flag using opt-out model.** Returns TRUE when unsubscribed_email  IS NULL, indicating the borrower has not unsubscribed from email communications. This  simple but effective approach ensures CAN-SPAM compliance by respecting all email  unsubscribe requests captured through SendGrid event tracking.
 | **Primary email consent flag using opt-out model.** Returns TRUE when unsubscribed_email  IS NULL, indicating the borrower has not unsubscribed from email communications. This  simple but effective approach ensures CAN-SPAM compliance by respecting all email  unsubscribe requests captured through SendGrid event tracking.
 | `[]` | `{}` |
    | `IS_DO_NOT_CALL` | 17 | `BOOLEAN` | Borrower-level do not call flag from int_max_loan_flag_values, with FALSE as default  when null. When TRUE, indicates legal or regulatory restriction preventing voice  contact regardless of SMS/email consent status. Critical for TCPA compliance and  FDCPA adherence in collections operations.
 | Borrower-level do not call flag from int_max_loan_flag_values, with FALSE as default  when null. When TRUE, indicates legal or regulatory restriction preventing voice  contact regardless of SMS/email consent status. Critical for TCPA compliance and  FDCPA adherence in collections operations.
 | `[]` | `{}` |
    | `IS_CEASE_AND_DESIST` | 18 | `BOOLEAN` | Borrower-level cease and desist flag from int_max_loan_flag_values, with FALSE as  default when null. When TRUE, indicates formal legal notice requiring cessation of  all collection communications. Overrides other consent preferences and requires  immediate communication suspension for FDCPA compliance. | Borrower-level cease and desist flag from int_max_loan_flag_values, with FALSE as  default when null. When TRUE, indicates formal legal notice requiring cessation of  all collection communications. Overrides other consent preferences and requires  immediate communication suspension for FDCPA compliance. | `[]` | `{}` |
    | `BORROWER_GENESYS_ID` | 19 | `TEXT` | Genesys system identifier for the borrower when an external contact record exists.  Links borrower records to Genesys contact center data for integrated consent management  and customer service workflow coordination.
 | Genesys system identifier for the borrower when an external contact record exists.  Links borrower records to Genesys contact center data for integrated consent management  and customer service workflow coordination.
 | `[]` | `{}` |
    | `GENESYS_CONTACT_ID` | 20 | `TEXT` | Specific Genesys external contact record identifier. Used for detailed contact center  integration and consent preference management within Genesys workflows and agent tools.
 | Specific Genesys external contact record identifier. Used for detailed contact center  integration and consent preference management within Genesys workflows and agent tools.
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.borrowers_merged_emails_xf`
    *   `model.cherry_data_model.int_max_loan_flag_values`
    *   `model.cherry_data_model.src_genesys_external_contacts`
    *   `model.cherry_data_model.stg_unsubscribed_borrower_emails`
    *   `model.cherry_data_model.stg_unsubscribed_mobile_phones`

---
