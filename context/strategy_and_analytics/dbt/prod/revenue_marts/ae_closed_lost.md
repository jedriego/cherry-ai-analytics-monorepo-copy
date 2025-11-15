## Model: `ae_closed_lost`

`ae_closed_lost`

*   **Unique ID:** `model.cherry_data_model.ae_closed_lost`
*   **FQN:** `prod.revenue_marts.ae_closed_lost`
*   **Description:** This model provides insights into pursuits that were marked as "Closed Lost".  It includes details like opportunity name, date the opportunity was closed/lost,  the primary and secondary reasons for the loss, the opportunity owner's details, and related merchant industry segment.

*   **Tags:** `['revenue_analytics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `PURSUIT_ID` | 1 | `TEXT` | The unique identifier for the pursuit. | The unique identifier for the pursuit. | `[]` | `{}` |
    | `PROSPECT_ID` | 2 | `TEXT` |  |  | `[]` | `{}` |
    | `PURSUIT_OWNER_ID` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `QUALIFIED_OPPORTUNITY_SOURCE` | 4 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_ID` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_NAME` | 6 | `TEXT` | The name of the opportunity. | The name of the opportunity. | `[]` | `{}` |
    | `CLOSED_LOST_DATE` | 7 | `TIMESTAMP_TZ` | The date when the opportunity was marked as "Closed Lost". | The date when the opportunity was marked as "Closed Lost". | `[]` | `{}` |
    | `LOSS_REASON` | 8 | `TEXT` | The reason why the opportunity was marked as "Closed Lost". | The reason why the opportunity was marked as "Closed Lost". | `[]` | `{}` |
    | `REASON_EXISTS` | 9 | `BOOLEAN` | Boolean flag indicating if a loss reason exists for the opportunity. | Boolean flag indicating if a loss reason exists for the opportunity. | `[]` | `{}` |
    | `LOSS_REASON_WEIGHT` | 10 | `NUMBER` | The weight of the loss reason for the opportunity. | The weight of the loss reason for the opportunity. | `[]` | `{}` |
    | `PRIMARY_LOSS_REASON` | 11 | `TEXT` | The primary reason for the opportunity being closed/lost. | The primary reason for the opportunity being closed/lost. | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_ID` | 12 | `TEXT` | The unique identifier for the owner of the opportunity. | The unique identifier for the owner of the opportunity. | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_NAME` | 13 | `TEXT` | The name of the opportunity owner. | The name of the opportunity owner. | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_TEAM` | 14 | `TEXT` | The team to which the opportunity owner belongs. | The team to which the opportunity owner belongs. | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_SUBTEAM` | 15 | `TEXT` |  |  | `[]` | `{}` |
    | `OPPORTUNITY_OWNER_DEPARTMENT` | 16 | `TEXT` | The department to which the opportunity owner belongs. | The department to which the opportunity owner belongs. | `[]` | `{}` |
    | `BOOKED_BY_DEPARTMENT` | 17 | `TEXT` |  |  | `[]` | `{}` |
    | `BOOKED_BY_TEAM` | 18 | `TEXT` |  |  | `[]` | `{}` |
    | `BOOKED_BY_NAME` | 19 | `TEXT` |  |  | `[]` | `{}` |
    | `INDUSTRY_SEGMENT` | 20 | `TEXT` | The coalesced industry segment of the account/lead associated with the opportunity. | The coalesced industry segment of the account/lead associated with the opportunity. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.demo_details_xf`
    *   `model.cherry_data_model.pursuit_engagement_summary`
    *   `model.cherry_data_model.src_sf_lead_history`
    *   `model.cherry_data_model.src_sf_leads`
    *   `model.cherry_data_model.src_sf_opportunities`
    *   `model.cherry_data_model.stg_sf_users`
    *   `seed.cherry_data_model.seed_lead_primary_loss_reason_mapping`

---
