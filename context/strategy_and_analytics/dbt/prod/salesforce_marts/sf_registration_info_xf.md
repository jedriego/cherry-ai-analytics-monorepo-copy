## Model: `sf_registration_info_xf`

`sf_registration_info_xf`

*   **Unique ID:** `model.cherry_data_model.sf_registration_info_xf`
*   **FQN:** `prod.salesforce_marts.sf_registration_info_xf`
*   **Description:** **Current Registration Information with Change Detection**
This model provides the most recent state of registration information for Application Lead and  Merchant Lead registrations by deduplicating snapshot records to ensure only the latest version  of each registration is returned. It serves as the primary source for current registration data  analysis, monitoring registration status changes, and tracking registration lifecycle events.
**Key Business Logic:** - **Current State Focus**: Uses row_number() over registration_id ordered by dbt_updated_at desc 
  to ensure only the most recent snapshot record per registration is returned
- **Registration Type Filtering**: Only includes 'Application Lead' and 'Merchant Lead' registration 
  types, excluding 'Partner Practice Lead' registrations for focused analysis
- **Change Detection Architecture**: Built on snapshot infrastructure that captures changes to key 
  registration fields including status updates, business information changes, and Salesforce linkages
- **Unified Registration View**: Combines application leads, merchant leads, and associated Salesforce 
  objects into a single registration record with complete business context

**Snapshot Change Detection:** The underlying snapshot tracks changes to critical fields: - Business information (business_name, dba, registration_type) - Status transitions and approval workflows - Salesforce object linkages (account_id, lead_id, opportunity_id) - Owner assignments and territory changes - Timestamp updates from source systems
**Critical Staging Model Context:** Based on research of staging models, this model integrates: - **sf_registration_info_snapshot**: Daily snapshots capturing registration changes with check strategy 
  on key business fields to detect meaningful updates
- **sf_registration_info**: Staging model that filters stg_registrations_new for Application Lead and 
  Merchant Lead types with deduplication by max_timestamp
- **stg_registrations_new**: Comprehensive registration model combining application leads, merchant leads, 
  and partner practice leads with complex business logic for unified registration records
- **stg_application_leads**: Application submission data with approval workflows and business details - **stg_merchant_leads**: Merchant request data including partner practice lead information - **Salesforce Integration**: Account, lead, and opportunity linkages with owner history tracking
**Primary Use Cases:** - Current registration status monitoring and reporting - Registration lifecycle analysis and conversion tracking - Salesforce-Cherry registration data synchronization monitoring - Business development pipeline analysis and owner performance tracking - Registration change detection and audit trail analysis
**Grain:** One record per registration with the most recent snapshot data

*   **Tags:** `['salesforce']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `REGISTRATION_ID` | 1 | `TEXT` | The unique identifier for each registration record, constructed through sophisticated business logic  that prioritizes application_lead_id, then concatenated organization and merchant lead identifiers,  then partner practice lead identifiers, with fallback to merchant-only records for comprehensive coverage
 | The unique identifier for each registration record, constructed through sophisticated business logic  that prioritizes application_lead_id, then concatenated organization and merchant lead identifiers,  then partner practice lead identifiers, with fallback to merchant-only records for comprehensive coverage
 | `[]` | `{}` |
    | `BUSINESS_NAME` | 2 | `TEXT` | The official business name for the registration, coalesced from merchant names, application lead  business names, and merchant lead names to provide the most accurate business identification  across different registration pathways
 | The official business name for the registration, coalesced from merchant names, application lead  business names, and merchant lead names to provide the most accurate business identification  across different registration pathways
 | `[]` | `{}` |
    | `DBA` | 3 | `TEXT` | The "Doing Business As" name from application lead data, representing the trade name or public-facing  business name that may differ from the official legal business name
 | The "Doing Business As" name from application lead data, representing the trade name or public-facing  business name that may differ from the official legal business name
 | `[]` | `{}` |
    | `REGISTRATION_TYPE` | 4 | `TEXT` | The type of registration indicating the pathway through which the practice engaged with Cherry.  Limited to 'Application Lead' (formal application submission) and 'Merchant Lead' (direct merchant  request) types, excluding partner practice leads for focused analysis
 | The type of registration indicating the pathway through which the practice engaged with Cherry.  Limited to 'Application Lead' (formal application submission) and 'Merchant Lead' (direct merchant  request) types, excluding partner practice leads for focused analysis
 | `[]` | `{}` |
    | `STATUS` | 5 | `TEXT` | The current status of the registration combining application lead status and merchant lead status  to indicate the approval workflow stage, such as SUBMITTED, IN_REVIEW, APPROVED, DENIED, or ACTIVE
 | The current status of the registration combining application lead status and merchant lead status  to indicate the approval workflow stage, such as SUBMITTED, IN_REVIEW, APPROVED, DENIED, or ACTIVE
 | `[]` | `{}` |
    | `TYPE` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `UNIQUE_PRACTICE_ID` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `UNIQUE_PRACTICE_TYPE` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_LEAD_ID` | 9 | `NUMBER` | The unique identifier for merchant lead records when the registration originated through the merchant  lead pathway rather than formal application submission, enabling tracking of direct merchant requests
 | The unique identifier for merchant lead records when the registration originated through the merchant  lead pathway rather than formal application submission, enabling tracking of direct merchant requests
 | `[]` | `{}` |
    | `PARTNER_ID` | 10 | `TEXT` |  |  | `[]` | `{}` |
    | `MERCHANT_ID` | 11 | `NUMBER` | The unique identifier for the Cherry merchant account associated with this registration, providing  the operational link between registration records and active merchant platform usage
 | The unique identifier for the Cherry merchant account associated with this registration, providing  the operational link between registration records and active merchant platform usage
 | `[]` | `{}` |
    | `ORGANIZATION_ID` | 12 | `NUMBER` |  |  | `[]` | `{}` |
    | `CHERRY_MERCHANT_ID` | 13 | `FLOAT` |  |  | `[]` | `{}` |
    | `PRIMARY_MERCHANT_ID` | 14 | `FLOAT` |  |  | `[]` | `{}` |
    | `CHERRY_ORGANIZATION_ID` | 15 | `NUMBER` |  |  | `[]` | `{}` |
    | `PRIMARY_ORGANIZATION_ID` | 16 | `NUMBER` |  |  | `[]` | `{}` |
    | `SF_ACCOUNT_ID` | 17 | `TEXT` | The Salesforce account identifier linked to this registration through sophisticated mapping logic  that prioritizes merchant account mappings, then application lead mappings, enabling CRM integration  and sales pipeline tracking
 | The Salesforce account identifier linked to this registration through sophisticated mapping logic  that prioritizes merchant account mappings, then application lead mappings, enabling CRM integration  and sales pipeline tracking
 | `[]` | `{}` |
    | `SF_ACCOUNT_NAME` | 18 | `TEXT` |  |  | `[]` | `{}` |
    | `SF_LEAD_ID` | 19 | `TEXT` | The Salesforce lead identifier associated with this registration when the registration originated  from or was linked to a Salesforce lead record, enabling marketing attribution and lead conversion analysis
 | The Salesforce lead identifier associated with this registration when the registration originated  from or was linked to a Salesforce lead record, enabling marketing attribution and lead conversion analysis
 | `[]` | `{}` |
    | `SF_OPPORTUNITY_ID` | 20 | `TEXT` | The Salesforce opportunity identifier for the sales opportunity associated with this registration,  filtered to exclude closed lost opportunities unless specifically related to merchant termination,  ensuring focus on active sales pipeline
 | The Salesforce opportunity identifier for the sales opportunity associated with this registration,  filtered to exclude closed lost opportunities unless specifically related to merchant termination,  ensuring focus on active sales pipeline
 | `[]` | `{}` |
    | `APPLICATION_CREATED_AT` | 21 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `APPLICATION_LEAD_REGISTERED_AT` | 22 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `MERCHANT_LEAD_REGISTERED_AT` | 23 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `REGISTERED_AT` | 24 | `TIMESTAMP_NTZ` | The calculated registration date representing the earliest significant interaction date for each  registration, using sophisticated business logic that considers application submission dates,  merchant creation dates, and merchant lead dates with priority rules for multi-merchant organizations
 | The calculated registration date representing the earliest significant interaction date for each  registration, using sophisticated business logic that considers application submission dates,  merchant creation dates, and merchant lead dates with priority rules for multi-merchant organizations
 | `[]` | `{}` |
    | `MERCHANT_CREATED_AT` | 25 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `INDUSTRY` | 26 | `TEXT` |  |  | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 27 | `TEXT` |  |  | `[]` | `{}` |
    | `ADDRESS_STREET` | 28 | `TEXT` |  |  | `[]` | `{}` |
    | `ADDRESS_UNIT` | 29 | `TEXT` |  |  | `[]` | `{}` |
    | `ADDRESS_CITY` | 30 | `TEXT` |  |  | `[]` | `{}` |
    | `ADDRESS_STATE` | 31 | `TEXT` |  |  | `[]` | `{}` |
    | `ADDRESS_ZIP` | 32 | `TEXT` |  |  | `[]` | `{}` |
    | `WEBSITE` | 33 | `TEXT` |  |  | `[]` | `{}` |
    | `PHONE` | 34 | `TEXT` |  |  | `[]` | `{}` |
    | `POC_FIRST_NAME` | 35 | `TEXT` |  |  | `[]` | `{}` |
    | `POC_LAST_NAME` | 36 | `TEXT` |  |  | `[]` | `{}` |
    | `POC_EMAIL` | 37 | `TEXT` |  |  | `[]` | `{}` |
    | `POC_PHONE` | 38 | `TEXT` |  |  | `[]` | `{}` |
    | `ADDITIONAL_MATERIALS_REQUESTED` | 39 | `TEXT` |  |  | `[]` | `{}` |
    | `FINANCING_OPTIONS` | 40 | `TEXT` |  |  | `[]` | `{}` |
    | `IS_FIRST_LOOK` | 41 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `FIRST_LOOK_DECLINE_EXPLANATION` | 42 | `TEXT` |  |  | `[]` | `{}` |
    | `PROMO_PERIOD` | 43 | `NUMBER` | The promotional period or special terms associated with this registration from application lead data,  indicating any special onboarding incentives or promotional pricing arrangements offered during registration
 | The promotional period or special terms associated with this registration from application lead data,  indicating any special onboarding incentives or promotional pricing arrangements offered during registration
 | `[]` | `{}` |
    | `ESTABLISHED_AT` | 44 | `DATE` |  |  | `[]` | `{}` |
    | `USER_ROLE` | 45 | `TEXT` |  |  | `[]` | `{}` |
    | `APPLICATION_LEAD_OWNER_ID` | 46 | `TEXT` |  |  | `[]` | `{}` |
    | `APPLICATION_LEAD_OWNER_DEPARTMENT` | 47 | `TEXT` |  |  | `[]` | `{}` |
    | `OWNER_ID` | 48 | `TEXT` | The identifier for the current owner of this registration, derived through complex logic that  prioritizes opportunity override owners, then opportunity owners, then account executives,  then application lead owners, ensuring proper sales attribution and responsibility tracking
 | The identifier for the current owner of this registration, derived through complex logic that  prioritizes opportunity override owners, then opportunity owners, then account executives,  then application lead owners, ensuring proper sales attribution and responsibility tracking
 | `[]` | `{}` |
    | `OWNER_DEPARTMENT` | 49 | `TEXT` |  |  | `[]` | `{}` |
    | `OWNER_TEAM` | 50 | `TEXT` |  |  | `[]` | `{}` |
    | `OWNER_SUBTEAM` | 51 | `TEXT` |  |  | `[]` | `{}` |
    | `OWNER_NAME` | 52 | `TEXT` |  |  | `[]` | `{}` |
    | `OWNER_TITLE` | 53 | `TEXT` |  |  | `[]` | `{}` |
    | `MAX_TIMESTAMP` | 54 | `TIMESTAMP_NTZ` | The most recent update timestamp across all source systems for this registration, calculated as  the greatest value among application lead updates and merchant lead updates, enabling change detection  and ensuring data freshness for snapshot comparison logic | The most recent update timestamp across all source systems for this registration, calculated as  the greatest value among application lead updates and merchant lead updates, enabling change detection  and ensuring data freshness for snapshot comparison logic | `[]` | `{}` |
    | `DBT_SCD_ID` | 55 | `TEXT` |  |  | `[]` | `{}` |
    | `DBT_UPDATED_AT` | 56 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `DBT_VALID_FROM` | 57 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `DBT_VALID_TO` | 58 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `snapshot.cherry_data_model.sf_registration_info_snapshot`

---
