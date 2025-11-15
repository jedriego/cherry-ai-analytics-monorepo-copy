## Model: `sf_merchant_objects_xf`

`sf_merchant_objects_xf`

*   **Unique ID:** `model.cherry_data_model.sf_merchant_objects_xf`
*   **FQN:** `prod.salesforce_marts.sf_merchant_objects_xf`
*   **Description:** **Allē-Cherry-Salesforce Data Consistency Monitor**
This model identifies data inconsistencies and mapping discrepancies between Allē merchant records,  Cherry merchant systems, and Salesforce account data, serving as a critical data quality monitoring  tool for the Allē partnership integration. The model focuses specifically on newly created Allē merchants  (post July 9, 2024) and detects cases where merchant identifiers stored in Salesforce accounts do not  match the actual Allē merchant IDs or corresponding Cherry merchant IDs in the source systems.
**Key Business Logic:** - **Allē Partnership Focus**: Filters to organization_id = 17450 (Allē organization) and specific 
  business_id = '3622d15d-87fd-497a-9f29-348f94f57d56' for targeted Allē partnership data
- **Post-Migration Scope**: Only includes Allē merchants created after July 9, 2024, focusing 
  on recent integration data that may have synchronization issues
- **Data Consistency Detection**: Identifies mismatches between Allē merchant IDs stored in 
  Salesforce vs actual Allē merchant IDs, and Cherry merchant ID misalignments
- **Account Mapping Strategy**: Attempts multiple join strategies (Cherry merchant ID match, 
  Allē location ID match) to establish correct Salesforce account relationships
- **Exception Filtering**: Final WHERE clause specifically filters for problematic records where 
  stored IDs don't match actual system IDs

**Critical Staging Model Context:** Based on research of staging models, this model integrates: - **src_merchants**: Cherry merchant data filtered to Allē organization (17450) for merchant creation tracking - **src_partner_practices**: Allē practice data linking Allē business entities to Cherry merchant IDs 
  through practice_id relationships for cross-system mapping
- **src_alle_practice_metadata**: Allē practice metadata containing corresponding Cherry merchant and 
  organization IDs, providing authoritative mapping between Allē and Cherry systems
- **src_sf_accounts**: Salesforce account data containing stored merchant_id and alle_id values 
  that may be inconsistent with source system data

**Data Quality Issues Detected:** - Allē merchant IDs in Salesforce not matching actual Allē merchant records - Cherry merchant IDs in Salesforce not matching corresponding Cherry merchant IDs from Allē metadata - Missing merchant ID mappings where relationships should exist - Account relationships that exist but have incorrect identifier mappings
**Primary Use Cases:** - Data synchronization monitoring between Allē and Salesforce systems - Identifying accounts requiring merchant ID updates or corrections - Partnership integration data quality assurance - Troubleshooting missing or incorrect account-merchant relationships - Supporting data remediation and cleanup processes
**Grain:** One record per Allē merchant with data consistency issues (filtered exceptions only)

*   **Tags:** `['salesforce']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `ALLE_MERCHANT_ID` | 1 | `NUMBER` | **Allē Merchant Identifier**
The actual Allē merchant ID from Cherry's merchant system (organization_id = 17450) created  after July 9, 2024. This represents the authoritative Allē merchant identifier that should  be correctly reflected in Salesforce account records but may be missing or incorrect.
 | **Allē Merchant Identifier**
The actual Allē merchant ID from Cherry's merchant system (organization_id = 17450) created  after July 9, 2024. This represents the authoritative Allē merchant identifier that should  be correctly reflected in Salesforce account records but may be missing or incorrect.
 | `[]` | `{}` |
    | `ALLE_MERCHANT_CREATION_DATE` | 2 | `TIMESTAMP_NTZ` | **Allē Merchant Creation Timestamp**
Timestamp when the Allē merchant record was originally created in Cherry's system. Used to  filter for post-integration merchants (after 2024-07-09) and provides context for when  potential data consistency issues may have been introduced.
 | **Allē Merchant Creation Timestamp**
Timestamp when the Allē merchant record was originally created in Cherry's system. Used to  filter for post-integration merchants (after 2024-07-09) and provides context for when  potential data consistency issues may have been introduced.
 | `[]` | `{}` |
    | `CHERRY_MERCHANT_ID` | 3 | `FLOAT` | **Corresponding Cherry Merchant ID**
The Cherry merchant ID that corresponds to this Allē merchant, derived from Allē practice  metadata's corresponding_merchant_id field. This represents the authoritative Cherry merchant  identifier that should be stored in Salesforce but may be missing or incorrect in the  account record.
**Data Source Priority:** 1. alle_practice_metadata.corresponding_merchant_id (primary source) 2. sf_accounts.merchant_id (if Cherry merchant ID match found) 3. NULL if no valid mapping exists
 | **Corresponding Cherry Merchant ID**
The Cherry merchant ID that corresponds to this Allē merchant, derived from Allē practice  metadata's corresponding_merchant_id field. This represents the authoritative Cherry merchant  identifier that should be stored in Salesforce but may be missing or incorrect in the  account record.
**Data Source Priority:** 1. alle_practice_metadata.corresponding_merchant_id (primary source) 2. sf_accounts.merchant_id (if Cherry merchant ID match found) 3. NULL if no valid mapping exists
 | `[]` | `{}` |
    | `ACCOUNT_ID` | 4 | `TEXT` | **Associated Salesforce Account ID**
Salesforce account ID that has been matched to this Allē merchant through various join strategies.  This account contains stored merchant identifier values that are inconsistent with the actual  Allē or Cherry merchant IDs, requiring data correction or synchronization.
**Join Strategy Priority:** 1. Cherry Merchant ID match (sf_accounts.merchant_id = corresponding_merchant_id) 2. Allē Location ID match (sf_accounts.alle_location_id = alle_practice_metadata.alle_location_id) 3. Only accounts with successful matches are included
 | **Associated Salesforce Account ID**
Salesforce account ID that has been matched to this Allē merchant through various join strategies.  This account contains stored merchant identifier values that are inconsistent with the actual  Allē or Cherry merchant IDs, requiring data correction or synchronization.
**Join Strategy Priority:** 1. Cherry Merchant ID match (sf_accounts.merchant_id = corresponding_merchant_id) 2. Allē Location ID match (sf_accounts.alle_location_id = alle_practice_metadata.alle_location_id) 3. Only accounts with successful matches are included
 | `[]` | `{}` |
    | `SALESFORCE_ACCOUNT_JOIN_TYPE` | 5 | `TEXT` | **Account Matching Method Indicator**
Describes the method used to successfully match the Allē merchant to a Salesforce account,  indicating which identifier enabled the relationship discovery:
**Join Types:** - **'Cherry Merchant Id'**: Account matched via sf_accounts.merchant_id = corresponding_merchant_id - **'Alle Merchant Id'**: Account matched via sf_accounts.alle_location_id = alle_location_id - **'No Salesforce Account Match'**: No account relationship found (excluded from final results)
This field helps prioritize remediation efforts by indicating which identifier type successfully  established the account relationship while others remain inconsistent.
 | **Account Matching Method Indicator**
Describes the method used to successfully match the Allē merchant to a Salesforce account,  indicating which identifier enabled the relationship discovery:
**Join Types:** - **'Cherry Merchant Id'**: Account matched via sf_accounts.merchant_id = corresponding_merchant_id - **'Alle Merchant Id'**: Account matched via sf_accounts.alle_location_id = alle_location_id - **'No Salesforce Account Match'**: No account relationship found (excluded from final results)
This field helps prioritize remediation efforts by indicating which identifier type successfully  established the account relationship while others remain inconsistent.
 | `[]` | `{}` |
    | `CHERRY_ORGANIZATION_ID` | 6 | `NUMBER` | **Corresponding Cherry Organization ID**
Cherry organization identifier that corresponds to this Allē merchant, sourced from  alle_practice_metadata.corresponding_organization_id. Provides organizational context  for the merchant and enables organization-level data consistency analysis.
**Use Cases:** - Organization-level data synchronization monitoring - Multi-merchant organization data consistency tracking - Supporting organizational hierarchy corrections in Salesforce - Enabling bulk data remediation at the organization level | **Corresponding Cherry Organization ID**
Cherry organization identifier that corresponds to this Allē merchant, sourced from  alle_practice_metadata.corresponding_organization_id. Provides organizational context  for the merchant and enables organization-level data consistency analysis.
**Use Cases:** - Organization-level data synchronization monitoring - Multi-merchant organization data consistency tracking - Supporting organizational hierarchy corrections in Salesforce - Enabling bulk data remediation at the organization level | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.src_alle_practice_metadata`
    *   `model.cherry_data_model.src_merchants`
    *   `model.cherry_data_model.src_partner_practices`
    *   `model.cherry_data_model.src_sf_accounts`

---
