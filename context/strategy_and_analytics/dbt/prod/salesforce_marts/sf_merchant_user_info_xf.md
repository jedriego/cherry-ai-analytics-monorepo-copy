## Model: `sf_merchant_user_info_xf`

`sf_merchant_user_info_xf`

*   **Unique ID:** `model.cherry_data_model.sf_merchant_user_info_xf`
*   **FQN:** `prod.salesforce_marts.sf_merchant_user_info_xf`
*   **Description:** A comprehensive view of merchant user information, including details from Salesforce, application roles, and Point of Contact (POC) status.
*   **Tags:** `['salesforce']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `USER_TYPE` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_USER_ID` | 2 | `NUMBER` | The unique identifier for the merchant user. | The unique identifier for the merchant user. | `[]` | `{}` |
    | `MERCHANT_USER_ID_SF` | 3 | `TEXT` | The merchant user's identifier in Salesforce. | The merchant user's identifier in Salesforce. | `[]` | `{}` |
    | `MERCHANT_ID` | 4 | `NUMBER` | The unique identifier for the merchant. | The unique identifier for the merchant. | `[]` | `{}` |
    | `MERCHANT_NAME` | 5 | `TEXT` | The name of the merchant. | The name of the merchant. | `[]` | `{}` |
    | `ACCOUNT_ID` | 6 | `TEXT` | The unique identifier for the Salesforce account associated with the merchant. | The unique identifier for the Salesforce account associated with the merchant. | `[]` | `{}` |
    | `ACCOUNT_NAME` | 7 | `TEXT` | The name of the Salesforce account associated with the merchant. | The name of the Salesforce account associated with the merchant. | `[]` | `{}` |
    | `USER_ID` | 8 | `NUMBER` | The unique identifier for the user in the cherry platform. | The unique identifier for the user in the cherry platform. | `[]` | `{}` |
    | `FIRST_NAME` | 9 | `TEXT` | The first name of the cherry platform user. | The first name of the cherry platform user. | `[]` | `{}` |
    | `LAST_NAME` | 10 | `TEXT` | The last name of the cherry platform user. | The last name of the cherry platform user. | `[]` | `{}` |
    | `EMAIL` | 11 | `TEXT` | The email address of the cherry platform user. | The email address of the cherry platform user. | `[]` | `{}` |
    | `PHONE` | 12 | `TEXT` | The phone number of the cherry platform user. | The phone number of the cherry platform user. | `[]` | `{}` |
    | `APPLICATION_USER_ROLE` | 13 | `TEXT` | The user's role within the application platform. | The user's role within the application platform. | `[]` | `{}` |
    | `MERCHANT_USER_ROLE` | 14 | `TEXT` | The user's role within the merchant's platform. | The user's role within the merchant's platform. | `[]` | `{}` |
    | `IS_POC` | 15 | `BOOLEAN` | Boolean indicating if the user is a Point of Contact (POC) for the merchant. | Boolean indicating if the user is a Point of Contact (POC) for the merchant. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.src_application_leads`
    *   `model.cherry_data_model.src_cherry_merchant_users`
    *   `model.cherry_data_model.src_cherry_users`
    *   `model.cherry_data_model.src_merchants`
    *   `model.cherry_data_model.src_sf_accounts`
    *   `model.cherry_data_model.src_sf_merchant_user_information`

---
