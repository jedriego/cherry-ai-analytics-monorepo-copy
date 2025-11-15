## Model: `sf_organization_user_info_xf`

`sf_organization_user_info_xf`

*   **Unique ID:** `model.cherry_data_model.sf_organization_user_info_xf`
*   **FQN:** `prod.salesforce_marts.sf_organization_user_info_xf`
*   **Description:** **Salesforce Organization User Information with Cherry Integration**
This model provides a unified view of organization-level users by integrating Cherry's organization  user management system with Salesforce's merchant user information objects. Unlike the merchant-level  user model, this focuses specifically on users who have organization-wide access and responsibilities  rather than individual merchant/location-specific roles.
**Key Business Logic:** - **Organization-Level Focus**: Specifically targets users with organization-wide access rather than 
  individual merchant access, representing administrators and key stakeholders
- **Salesforce Integration**: Links Cherry organization users with Salesforce merchant user information 
  objects filtered for user_type = 'Organization'
- **Practice Account Mapping**: Uses sophisticated deduplication logic through the practices model to 
  ensure consistent account mapping when organizations have multiple Salesforce accounts
- **Role Enrichment**: Combines organization user roles with application user roles to provide complete 
  context about user permissions and responsibilities

**Data Integration Sources:** - Cherry organization user relationships from organization service - Salesforce merchant user information (organization type only) - Cherry user profile and contact information - Organization details and metadata - Application lead user roles for business context - Practice/account information for Salesforce linking
**Primary Use Cases:** - Organization-level user management and access control - Salesforce-Cherry user synchronization and data consistency monitoring - Organization administrator identification and contact management - Multi-location organization user oversight and reporting
**Grain:** One record per organization user with enriched profile and account information

*   **Tags:** `['salesforce']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `USER_TYPE` | 1 | `TEXT` | Hardcoded identifier set to 'Organization' to distinguish these records from merchant-level  user records, enabling consistent filtering and categorization across user management systems
 | Hardcoded identifier set to 'Organization' to distinguish these records from merchant-level  user records, enabling consistent filtering and categorization across user management systems
 | `[]` | `{}` |
    | `ORGANIZATION_USER_ID` | 2 | `NUMBER` | The unique identifier for the organization user relationship record from Cherry's organization  service, representing the primary key for the user-organization association
 | The unique identifier for the organization user relationship record from Cherry's organization  service, representing the primary key for the user-organization association
 | `[]` | `{}` |
    | `MERCHANT_USER_ID_SF` | 3 | `TEXT` | The Salesforce record ID from the merchant_user_information object that corresponds to this  organization user. Named consistently with merchant user models for alignment, though it  represents organization-type users in Salesforce rather than merchant-type users
 | The Salesforce record ID from the merchant_user_information object that corresponds to this  organization user. Named consistently with merchant user models for alignment, though it  represents organization-type users in Salesforce rather than merchant-type users
 | `[]` | `{}` |
    | `ORGANIZATION_ID` | 4 | `NUMBER` | The unique identifier for the Cherry organization that the user has access to, enabling  organization-level permissions and data filtering across the platform
 | The unique identifier for the Cherry organization that the user has access to, enabling  organization-level permissions and data filtering across the platform
 | `[]` | `{}` |
    | `ORGANIZATION_NAME` | 5 | `TEXT` | The business name of the organization as stored in Cherry's system, providing human-readable  identification for the organization the user is associated with
 | The business name of the organization as stored in Cherry's system, providing human-readable  identification for the organization the user is associated with
 | `[]` | `{}` |
    | `SF_ACCOUNT_ID` | 6 | `TEXT` | The Salesforce account ID that corresponds to this organization, derived through practice  mapping logic that prioritizes Allē-integrated accounts and earlier-created accounts when  multiple Salesforce accounts exist for the same organization
 | The Salesforce account ID that corresponds to this organization, derived through practice  mapping logic that prioritizes Allē-integrated accounts and earlier-created accounts when  multiple Salesforce accounts exist for the same organization
 | `[]` | `{}` |
    | `SF_ACCOUNT_NAME` | 7 | `TEXT` | The name of the Salesforce account as stored in Salesforce, providing the CRM-side identifier  for the organization and enabling cross-system reconciliation
 | The name of the Salesforce account as stored in Salesforce, providing the CRM-side identifier  for the organization and enabling cross-system reconciliation
 | `[]` | `{}` |
    | `USER_ID` | 8 | `NUMBER` | The unique identifier for the user from Cherry's user service, serving as the foreign key  to link organization user relationships with detailed user profile information
 | The unique identifier for the user from Cherry's user service, serving as the foreign key  to link organization user relationships with detailed user profile information
 | `[]` | `{}` |
    | `FIRST_NAME` | 9 | `TEXT` | The user's first name from Cherry's user profile system, providing personal identification  and enabling personalized communications and user interfaces
 | The user's first name from Cherry's user profile system, providing personal identification  and enabling personalized communications and user interfaces
 | `[]` | `{}` |
    | `LAST_NAME` | 10 | `TEXT` | The user's last name from Cherry's user profile system, completing personal identification  and supporting full name construction for display and communication purposes
 | The user's last name from Cherry's user profile system, completing personal identification  and supporting full name construction for display and communication purposes
 | `[]` | `{}` |
    | `EMAIL` | 11 | `TEXT` | The user's email address from Cherry's user profile system, serving as the primary contact  method and unique identifier for user communications and authentication
 | The user's email address from Cherry's user profile system, serving as the primary contact  method and unique identifier for user communications and authentication
 | `[]` | `{}` |
    | `PHONE` | 12 | `TEXT` | The user's phone number from Cherry's user profile system, providing an alternative contact  method and supporting multi-channel communication strategies
 | The user's phone number from Cherry's user profile system, providing an alternative contact  method and supporting multi-channel communication strategies
 | `[]` | `{}` |
    | `APPLICATION_USER_ROLE` | 13 | `TEXT` | The role assigned to the user during the application process, derived from application leads  and deduplicated to show the most recent role assignment. Provides context about the user's  initial business relationship and responsibilities during onboarding
 | The role assigned to the user during the application process, derived from application leads  and deduplicated to show the most recent role assignment. Provides context about the user's  initial business relationship and responsibilities during onboarding
 | `[]` | `{}` |
    | `ORGANIZATION_USER_ROLE` | 14 | `TEXT` | The current role assigned to the user within the organization as defined in Cherry's organization  service, indicating their level of access and responsibilities within the organization's  Cherry platform usage | The current role assigned to the user within the organization as defined in Cherry's organization  service, indicating their level of access and responsibilities within the organization's  Cherry platform usage | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.src_application_leads`
    *   `model.cherry_data_model.src_cherry_organization_users`
    *   `model.cherry_data_model.src_cherry_users`
    *   `model.cherry_data_model.src_organizations`
    *   `model.cherry_data_model.src_sf_merchant_user_information`
    *   `model.cherry_data_model.stg_practices`

---
