## Model: `sf_account_merchant_info_xf`

`sf_account_merchant_info_xf`

*   **Unique ID:** `model.cherry_data_model.sf_account_merchant_info_xf`
*   **FQN:** `prod.salesforce_marts.sf_account_merchant_info_xf`
*   **Description:** **Salesforce Account with Enriched Merchant Information**
This model provides a unified view of Salesforce accounts enriched with Cherry merchant and  organization information, serving as the primary integration point between Salesforce CRM  data and Cherry's operational systems. The model performs sophisticated business logic to  derive merchant dashboard status based on actual merchant/organization states and compares  it with stored Salesforce values to detect discrepancies requiring attention.
**Key Business Logic:** - **Status Derivation**: Calculates merchant dashboard status based on merchant/organization active states and demo flags - **Status Comparison**: Compares derived status with stored Salesforce status to trigger updates when mismatched - **Address Enrichment**: Joins latest merchant address information for complete contact details - **Change Detection**: Tracks timestamp updates from account history to detect Salesforce field changes - **Deduplication**: Uses qualify clause to ensure one record per account_id based on latest timestamp
**Status Hierarchy Logic:** 1. **'Inactive'**: When either merchant or organization is_active = false 2. **'Demo'**: When organization is_demo = true (regardless of active status) 3. **'Production'**: When both merchant and organization are active and not demo
**Critical Staging Model Context:** Based on research of staging models, this model integrates: - **src_sf_accounts**: Salesforce account master data including stored merchant_dashboard_status and Cherry merchant_id mappings - **src_merchants**: Cherry merchant operational data including is_active status and organization relationships   - **src_organizations**: Cherry organization data including is_active, is_demo flags, and industry classifications - **stg_merchant_addresses**: Latest merchant address information with timezone and geographic details - **src_sf_account_history**: Salesforce field change tracking for detecting when Org_System_ID__c updates occur
**Grain:** One record per account_id (deduplicated by latest max_timestamp)

*   **Tags:** `['salesforce']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `ACCOUNT_ID` | 1 | `TEXT` | **Salesforce Account Primary Key**
Unique identifier for each Salesforce account. Serves as the primary key for this model  and the main integration point between Salesforce CRM and Cherry's operational systems.
 | **Salesforce Account Primary Key**
Unique identifier for each Salesforce account. Serves as the primary key for this model  and the main integration point between Salesforce CRM and Cherry's operational systems.
 | `[]` | `{}` |
    | `MERCHANT_ID` | 2 | `FLOAT` | **Cherry Merchant Identifier**
Cherry's unique identifier for the merchant location associated with this Salesforce account.  Links to Cherry's merchant system for operational data including transaction processing,  address management, and organizational hierarchy. Sourced from the Org_System_ID__c field  in Salesforce accounts.
 | **Cherry Merchant Identifier**
Cherry's unique identifier for the merchant location associated with this Salesforce account.  Links to Cherry's merchant system for operational data including transaction processing,  address management, and organizational hierarchy. Sourced from the Org_System_ID__c field  in Salesforce accounts.
 | `[]` | `{}` |
    | `ORGANIZATION_ID` | 3 | `NUMBER` | **Cherry Organization Identifier**
Unique identifier for the Cherry organization that owns this merchant. Organizations are  parent entities that can contain multiple merchant locations, enabling multi-location  practice management and consolidated organizational settings.
 | **Cherry Organization Identifier**
Unique identifier for the Cherry organization that owns this merchant. Organizations are  parent entities that can contain multiple merchant locations, enabling multi-location  practice management and consolidated organizational settings.
 | `[]` | `{}` |
    | `MERCHANT_DASHBOARD_STATUS` | 4 | `TEXT` | **Derived Merchant Dashboard Status**
Business-rule derived status indicating the merchant's operational state based on actual  Cherry system data. Calculated using sophisticated hierarchy logic: - **'Inactive'**: Either merchant.is_active = false OR organization.is_active = false - **'Demo'**: organization.is_demo = true (overrides active status) - **'Production'**: Both merchant and organization are active AND not demo - **NULL**: When merchant or organization data is missing
This derived value is compared against the stored Salesforce status to detect discrepancies.
 | **Derived Merchant Dashboard Status**
Business-rule derived status indicating the merchant's operational state based on actual  Cherry system data. Calculated using sophisticated hierarchy logic: - **'Inactive'**: Either merchant.is_active = false OR organization.is_active = false - **'Demo'**: organization.is_demo = true (overrides active status) - **'Production'**: Both merchant and organization are active AND not demo - **NULL**: When merchant or organization data is missing
This derived value is compared against the stored Salesforce status to detect discrepancies.
 | `[]` | `{}` |
    | `INDUSTRY` | 5 | `TEXT` | **Practice Industry Classification**
Industry vertical classification for the practice, used for specialized service delivery,  risk assessment, and business intelligence. Sourced from the Cherry organization's industry  field, which provides standardized industry categorization for operational workflows.
 | **Practice Industry Classification**
Industry vertical classification for the practice, used for specialized service delivery,  risk assessment, and business intelligence. Sourced from the Cherry organization's industry  field, which provides standardized industry categorization for operational workflows.
 | `[]` | `{}` |
    | `ADDRESS_LINE_ONE` | 6 | `TEXT` | **Primary Street Address**
First line of the merchant's physical address sourced from the latest merchant address  record in Cherry's system. Represents the primary business location where the practice  operates and provides services to patients/customers.
 | **Primary Street Address**
First line of the merchant's physical address sourced from the latest merchant address  record in Cherry's system. Represents the primary business location where the practice  operates and provides services to patients/customers.
 | `[]` | `{}` |
    | `CITY_NAME` | 7 | `TEXT` | **City Name**
City where the merchant's business is located, sourced from the latest merchant address  record. Used for geographic analysis, territory assignment, and local market insights.
 | **City Name**
City where the merchant's business is located, sourced from the latest merchant address  record. Used for geographic analysis, territory assignment, and local market insights.
 | `[]` | `{}` |
    | `STATE_ABBREVIATION` | 8 | `TEXT` | **State Abbreviation**
Two-letter state abbreviation for the merchant's business location, sourced from the  latest merchant address record. Enables state-level regulatory compliance, territory  management, and geographic reporting.
 | **State Abbreviation**
Two-letter state abbreviation for the merchant's business location, sourced from the  latest merchant address record. Enables state-level regulatory compliance, territory  management, and geographic reporting.
 | `[]` | `{}` |
    | `ZIPCODE` | 9 | `TEXT` | **ZIP/Postal Code**
ZIP or postal code for the merchant's business address, sourced from the latest merchant  address record. Used for precise geographic analysis, demographic overlays, and local  market segmentation.
 | **ZIP/Postal Code**
ZIP or postal code for the merchant's business address, sourced from the latest merchant  address record. Used for precise geographic analysis, demographic overlays, and local  market segmentation.
 | `[]` | `{}` |
    | `MAX_TIMESTAMP` | 10 | `TIMESTAMP_NTZ` | **Record Freshness Timestamp**
Timestamp indicating when this account record was last updated, calculated as the greatest  (most recent) timestamp across all contributing data sources: - Salesforce account created_date_pt - Cherry merchant updated_at_pt   - Cherry organization updated_at_pt - Salesforce account history latest_update_datetime (for Org_System_ID__c changes)
**Special Logic**: If the derived merchant_dashboard_status differs from the stored  account_merchant_dashboard_status, this timestamp is set to current_timestamp to  trigger immediate processing and ensure real-time status synchronization.
Used by the qualify clause to ensure only the most recent record per account_id is returned. | **Record Freshness Timestamp**
Timestamp indicating when this account record was last updated, calculated as the greatest  (most recent) timestamp across all contributing data sources: - Salesforce account created_date_pt - Cherry merchant updated_at_pt   - Cherry organization updated_at_pt - Salesforce account history latest_update_datetime (for Org_System_ID__c changes)
**Special Logic**: If the derived merchant_dashboard_status differs from the stored  account_merchant_dashboard_status, this timestamp is set to current_timestamp to  trigger immediate processing and ensure real-time status synchronization.
Used by the qualify clause to ensure only the most recent record per account_id is returned. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.src_merchants`
    *   `model.cherry_data_model.src_organizations`
    *   `model.cherry_data_model.src_sf_account_history`
    *   `model.cherry_data_model.src_sf_accounts`
    *   `model.cherry_data_model.stg_merchant_addresses`

---
