## Model: `sf_lead_account_audit_xf`

`sf_lead_account_audit_xf`

*   **Unique ID:** `model.cherry_data_model.sf_lead_account_audit_xf`
*   **FQN:** `prod.salesforce_marts.sf_lead_account_audit_xf`
*   **Description:** The Salesforce account lead audit table can be used to identify any lead or account with duplicate or missing contact information. 

*   **Tags:** `['salesforce', 'accounts', 'leads', 'audit']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `UNIQUE_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `TYPE` | 2 | `TEXT` | The type of Salesforce object, either a lead or account | The type of Salesforce object, either a lead or account | `[]` | `{}` |
    | `ID` | 3 | `TEXT` | The Salesforce account or lead object ID | The Salesforce account or lead object ID | `[]` | `{}` |
    | `CONTACT_ID` | 4 | `TEXT` | The contact id associated with the given account, null if lead. | The contact id associated with the given account, null if lead. | `[]` | `{}` |
    | `EMAIL` | 5 | `TEXT` | The email of the associated contact or lead | The email of the associated contact or lead | `[]` | `{}` |
    | `PHONE` | 6 | `TEXT` | The phone number of the associated contact or lead | The phone number of the associated contact or lead | `[]` | `{}` |
    | `ADDITIONAL_LOCATION` | 7 | `BOOLEAN` | Binary field for when the account source is 'additional location', defaults to false if lead | Binary field for when the account source is 'additional location', defaults to false if lead | `[]` | `{}` |
    | `MISSING_EMAIL` | 8 | `NUMBER` | Binary field for when the email is null | Binary field for when the email is null | `[]` | `{}` |
    | `MISSING_PHONE` | 9 | `NUMBER` | Binary field for when the phone number is null | Binary field for when the phone number is null | `[]` | `{}` |
    | `DUPLICATE_EMAIL` | 10 | `NUMBER` | Identifies if another record (contact or lead) uses the same email | Identifies if another record (contact or lead) uses the same email | `[]` | `{}` |
    | `DUPLICATE_PHONE` | 11 | `NUMBER` | Identifies if another record (contact or lead) uses the same phone number | Identifies if another record (contact or lead) uses the same phone number | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.dbt_utils.generate_surrogate_key`
    *   `model.cherry_data_model.src_sf_accounts`
    *   `model.cherry_data_model.src_sf_contacts`
    *   `model.cherry_data_model.src_sf_leads`

---
