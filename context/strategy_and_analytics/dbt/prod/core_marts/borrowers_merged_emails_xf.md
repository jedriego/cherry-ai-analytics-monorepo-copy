## Model: `borrowers_merged_emails_xf`

`borrowers_merged_emails_xf`

*   **Unique ID:** `model.cherry_data_model.borrowers_merged_emails_xf`
*   **FQN:** `prod.core_marts.borrowers_merged_emails_xf`
*   **Description:** Enhanced borrower data that merges borrower email addresses with Plaid-sourced email addresses to provide the most complete email information available. This model combines core borrower  attributes with KYC status information and prioritizes borrower-provided email addresses  while falling back to Plaid email data when borrower emails are unavailable. The model  serves as a comprehensive borrower dimension table for analytics and operational use cases.

*   **Tags:** `['core']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `BORROWER_ID` | 1 | `NUMBER` | Unique identifier for each borrower in the system. Primary key for the borrower entity.
 | Unique identifier for each borrower in the system. Primary key for the borrower entity.
 | `[]` | `{}` |
    | `BORROWER_CREATED_AT` | 2 | `TIMESTAMP_NTZ` | UTC timestamp when the borrower record was first created in the system.
 | UTC timestamp when the borrower record was first created in the system.
 | `[]` | `{}` |
    | `DATE_OF_BIRTH` | 3 | `DATE` | Date of birth of the borrower, used for identity verification and age validation. | Date of birth of the borrower, used for identity verification and age validation. | `[]` | `{}` |
    | `FIRST_NAME` | 4 | `TEXT` | First name of the borrower as provided during registration. | First name of the borrower as provided during registration. | `[]` | `{}` |
    | `LAST_NAME` | 5 | `TEXT` | Last name of the borrower as provided during registration. | Last name of the borrower as provided during registration. | `[]` | `{}` |
    | `PHONE_NUMBER` | 6 | `TEXT` | Primary phone number associated with the borrower account. | Primary phone number associated with the borrower account. | `[]` | `{}` |
    | `BORROWER_STATUS` | 7 | `TEXT` | Current status of the borrower account (e.g., active, inactive, suspended, closed).
 | Current status of the borrower account (e.g., active, inactive, suspended, closed).
 | `[]` | `{}` |
    | `BORROWER_ADDRESS_ID` | 8 | `NUMBER` | Foreign key reference to the borrower's primary address record in the address dimension.
 | Foreign key reference to the borrower's primary address record in the address dimension.
 | `[]` | `{}` |
    | `PHONE_STATUS` | 9 | `TEXT` | Current status of the borrower's phone number (e.g., verified, unverified, invalid).
 | Current status of the borrower's phone number (e.g., verified, unverified, invalid).
 | `[]` | `{}` |
    | `TAX_NUMBER_TYPE` | 10 | `TEXT` | Type of tax identification number provided by the borrower (e.g., SSN, ITIN, EIN).
 | Type of tax identification number provided by the borrower (e.g., SSN, ITIN, EIN).
 | `[]` | `{}` |
    | `BORROWER_SSN` | 11 | `TEXT` | Social Security Number of the borrower, used for identity verification and credit checks. | Social Security Number of the borrower, used for identity verification and credit checks. | `[]` | `{}` |
    | `BORROWER_SSN_CHECKSUM` | 12 | `TEXT` | Checksum or hash of the borrower's SSN for data integrity verification without  exposing the actual SSN value.
 | Checksum or hash of the borrower's SSN for data integrity verification without  exposing the actual SSN value.
 | `[]` | `{}` |
    | `BORROWER_LANGUAGE` | 13 | `TEXT` | Preferred language for communication with the borrower (e.g., English, Spanish).
 | Preferred language for communication with the borrower (e.g., English, Spanish).
 | `[]` | `{}` |
    | `BORROWER_CREATED_BY` | 14 | `NUMBER` | Identifier of the user or system that created the borrower record, for audit purposes.
 | Identifier of the user or system that created the borrower record, for audit purposes.
 | `[]` | `{}` |
    | `BORROWER_UPDATED_BY` | 15 | `NUMBER` | Identifier of the user or system that last updated the borrower record, for audit purposes.
 | Identifier of the user or system that last updated the borrower record, for audit purposes.
 | `[]` | `{}` |
    | `BALANCE_USED` | 16 | `FLOAT` | Current outstanding balance or amount of credit utilized by the borrower.
 | Current outstanding balance or amount of credit utilized by the borrower.
 | `[]` | `{}` |
    | `BORROWER_GENESYS_ID` | 17 | `TEXT` | Identifier used to link the borrower record with Genesys contact center system  for customer service interactions.
 | Identifier used to link the borrower record with Genesys contact center system  for customer service interactions.
 | `[]` | `{}` |
    | `CREATED_AT_PT` | 18 | `TIMESTAMP_NTZ` | Pacific Time timestamp when the borrower record was first created in the system.
 | Pacific Time timestamp when the borrower record was first created in the system.
 | `[]` | `{}` |
    | `UPDATED_AT_PT` | 19 | `TIMESTAMP_NTZ` | Pacific Time timestamp when the borrower record was last updated. | Pacific Time timestamp when the borrower record was last updated. | `[]` | `{}` |
    | `EMAIL` | 20 | `TEXT` | Primary email address for the borrower, intelligently merged using COALESCE to prefer  the borrower's directly provided email but fall back to Plaid-sourced email when  the borrower email is unavailable.
 | Primary email address for the borrower, intelligently merged using COALESCE to prefer  the borrower's directly provided email but fall back to Plaid-sourced email when  the borrower email is unavailable.
 | `[]` | `{}` |
    | `BORROWER_KYC_STATUS` | 21 | `TEXT` | Know Your Customer (KYC) verification status indicating the outcome of identity  verification processes (renamed from kyc_outcome_status for clarity).
 | Know Your Customer (KYC) verification status indicating the outcome of identity  verification processes (renamed from kyc_outcome_status for clarity).
 | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.int_highest_priority_plaid_email`
    *   `model.cherry_data_model.stg_borrowers_with_kyc_status`

---
