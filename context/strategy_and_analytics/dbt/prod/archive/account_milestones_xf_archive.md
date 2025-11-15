## Model: `account_milestones_xf_archive`

`account_milestones_xf_archive`

*   **Unique ID:** `model.cherry_data_model.account_milestones_xf_archive`
*   **FQN:** `prod.archive.account_milestones_xf_archive`
*   **Description:** This model combines the account milestones (melted) and account details to provide a comprehensive view of  each account's progression through various stages along with details about the account.

*   **Tags:** `['archive']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `ACCOUNT_ID` | 1 | `TEXT` | Unique identifier for the account. | Unique identifier for the account. | `[]` | `{}` |
    | `MERCHANT_ID` | 2 | `NUMBER` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_ID` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `COMPANY_NAME` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_STAGE` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `HAS_PRIMARY_DEMO` | 6 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `PRIMARY_DEMO_BOOKED_BY_NAME` | 7 | `TEXT` |  |  | `[]` | `{}` |
    | `PRIMARY_DEMO_BOOKED_BY_TEAM` | 8 | `TEXT` |  |  | `[]` | `{}` |
    | `ACCOUNT_CREATED_DATE` | 9 | `DATE` |  |  | `[]` | `{}` |
    | `DEMO_SCHEDULED_DATE` | 10 | `DATE` |  |  | `[]` | `{}` |
    | `DEMO_COMPLETED_DATE` | 11 | `DATE` |  |  | `[]` | `{}` |
    | `REGISTRATION_DATE` | 12 | `DATE` |  |  | `[]` | `{}` |
    | `GO_LIVE_DATE` | 13 | `DATE` |  |  | `[]` | `{}` |
    | `PRIMARY_DEMO_DATE` | 14 | `DATE` |  |  | `[]` | `{}` |
    | `PRIMARY_DEMO_DATE_30_DAYS` | 15 | `TIMESTAMP_NTZ` |  |  | `[]` | `{}` |
    | `STAGE_WITHIN_DEMO_DATE_30_DAYS` | 16 | `BOOLEAN` |  |  | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 17 | `TEXT` | Industry segment of the account. | Industry segment of the account. | `[]` | `{}` |
    | `INDUSTRY` | 18 | `TEXT` | Industry to which the account belongs. | Industry to which the account belongs. | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_NAME` | 19 | `TEXT` | Name of the person or entity that owns or manages the opportunity associated with the account. | Name of the person or entity that owns or manages the opportunity associated with the account. | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_TEAM` | 20 | `TEXT` | Team of the person or entity that owns or manages the opportunity associated with the account. | Team of the person or entity that owns or manages the opportunity associated with the account. | `[]` | `{}` |
    | `RETENTION_OWNER_NAME` | 21 | `TEXT` | Name of the person or entity that owns or manages the retention associated with the account. | Name of the person or entity that owns or manages the retention associated with the account. | `[]` | `{}` |
    | `RETENTION_OWNER_TEAM` | 22 | `TEXT` | Team of the person or entity that owns or manages the retention associated with the account. | Team of the person or entity that owns or manages the retention associated with the account. | `[]` | `{}` |
    | `ACCOUNT_TERRITORY` | 23 | `TEXT` |  |  | `[]` | `{}` |
    | `SOURCE_STAGE_ORDER` | 24 | `NUMBER` |  |  | `[]` | `{}` |
    | `SOURCE_STAGE` | 25 | `TEXT` | The name of the source milestone/stage. | The name of the source milestone/stage. | `[]` | `{}` |
    | `SOURCE_DATE` | 26 | `DATE` | The date that the source milestone/stage occured. | The date that the source milestone/stage occured. | `[]` | `{}` |
    | `TARGET_STAGE_ORDER` | 27 | `NUMBER` |  |  | `[]` | `{}` |
    | `TARGET_STAGE` | 28 | `TEXT` | The name of the target milestone/stage. | The name of the target milestone/stage. | `[]` | `{}` |
    | `TARGET_DATE` | 29 | `DATE` | The date that the target milestone/stage occured. | The date that the target milestone/stage occured. | `[]` | `{}` |
    | `DAYS_IN_STAGE` | 30 | `NUMBER` | The number of days between the source and target dates | The number of days between the source and target dates | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.account_milestones_melted`
    *   `model.cherry_data_model.demo_details_xf`
    *   `model.cherry_data_model.src_sf_accounts`
    *   `model.cherry_data_model.src_sf_opportunities`
    *   `model.cherry_data_model.stg_leads`
    *   `model.cherry_data_model.stg_merchants`
    *   `model.cherry_data_model.stg_sf_users`

---
