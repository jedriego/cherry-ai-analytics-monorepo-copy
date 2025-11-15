## Model: `unified_support_conversion_rate_xf`

`unified_support_conversion_rate_xf`

*   **Unique ID:** `model.cherry_data_model.unified_support_conversion_rate_xf`
*   **FQN:** `prod.customer_support_marts.unified_support_conversion_rate_xf`
*   **Description:** Unified model that combines NICE and Zendesk support conversion rate data. This model tracks conversion rates for support interactions by measuring how many eligible support contacts result in successful application submissions, approvals, or denials within a defined attribution window. It provides a single source of truth for support conversion metrics across both contact center platforms.

*   **Tags:** `['customer_support']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SOURCE_SYSTEM` | 1 | `TEXT` | Source system for the record ('NICE' or 'ZENDESK') | Source system for the record ('NICE' or 'ZENDESK') | `[]` | `{}` |
    | `CONTACT_CREATED_PT` | 2 | `TIMESTAMP_NTZ` | Unified timestamp when the contact was created (Pacific Time). Maps from contact_start_pt (NICE) or ticket_created_at_pt (Zendesk) | Unified timestamp when the contact was created (Pacific Time). Maps from contact_start_pt (NICE) or ticket_created_at_pt (Zendesk) | `[]` | `{}` |
    | `AGENT_NAME` | 3 | `TEXT` | Unified agent name field. Maps from initial_agent_name (NICE) or agent_name (Zendesk) | Unified agent name field. Maps from initial_agent_name (NICE) or agent_name (Zendesk) | `[]` | `{}` |
    | `BORROWER_ID` | 4 | `NUMBER` | Unified borrower ID. Maps from interaction_borrower_id (NICE) or borrower_id (Zendesk) | Unified borrower ID. Maps from interaction_borrower_id (NICE) or borrower_id (Zendesk) | `[]` | `{}` |
    | `MERCHANT_ID` | 5 | `NUMBER` | Unified merchant ID. Maps from interaction_merchant_id (NICE) or merchant_id (Zendesk) | Unified merchant ID. Maps from interaction_merchant_id (NICE) or merchant_id (Zendesk) | `[]` | `{}` |
    | `DISPOSITION_NAME` | 6 | `TEXT` | Unified disposition/wrap-up code. Maps from disposition_name (NICE) or agent_disposition (Zendesk) | Unified disposition/wrap-up code. Maps from disposition_name (NICE) or agent_disposition (Zendesk) | `[]` | `{}` |
    | `FINAL_STATUS_PT` | 7 | `TIMESTAMP_NTZ` | Timestamp of the final application status (Pacific Time) | Timestamp of the final application status (Pacific Time) | `[]` | `{}` |
    | `CONVERSION_ELIGIBLE` | 8 | `NUMBER` | Flag indicating if the interaction is eligible for conversion attribution (0 or 1) | Flag indicating if the interaction is eligible for conversion attribution (0 or 1) | `[]` | `{}` |
    | `CONVERTED` | 9 | `NUMBER` | Flag indicating if the interaction resulted in a conversion (0 or 1) | Flag indicating if the interaction resulted in a conversion (0 or 1) | `[]` | `{}` |
    | `CONTACT_ID` | 10 | `NUMBER` | Unique identifier for the NICE contact (NULL for Zendesk records) | Unique identifier for the NICE contact (NULL for Zendesk records) | `[]` | `{}` |
    | `CONTACT_START_PT` | 11 | `TIMESTAMP_NTZ` | NICE-specific timestamp when contact started (NULL for Zendesk records) | NICE-specific timestamp when contact started (NULL for Zendesk records) | `[]` | `{}` |
    | `CONTACT_END_PT` | 12 | `TIMESTAMP_NTZ` | NICE-specific timestamp when contact ended (NULL for Zendesk records) | NICE-specific timestamp when contact ended (NULL for Zendesk records) | `[]` | `{}` |
    | `INITIAL_STATUS` | 13 | `TEXT` | Initial status of the application | Initial status of the application | `[]` | `{}` |
    | `INITIAL_STATUS_PT` | 14 | `TIMESTAMP_NTZ` | Timestamp of the initial application status (Pacific Time) | Timestamp of the initial application status (Pacific Time) | `[]` | `{}` |
    | `FINAL_STATUS` | 15 | `TEXT` | Final status of the application | Final status of the application | `[]` | `{}` |
    | `APPLICATION_ID` | 16 | `NUMBER` | ID of the application associated with the support interaction | ID of the application associated with the support interaction | `[]` | `{}` |
    | `TIME_TO_COMPLETION_MINS` | 17 | `NUMBER` | Time to completion in minutes (from initial to final status) | Time to completion in minutes (from initial to final status) | `[]` | `{}` |
    | `TIME_TO_COMPLETION_DAYS` | 18 | `NUMBER` | Time to completion in hours (from initial to final status) | Time to completion in hours (from initial to final status) | `[]` | `{}` |
    | `ATTRIBUTION_WINDOW` | 19 | `NUMBER` | Window in hours used for attribution (191 hours for both systems) | Window in hours used for attribution (191 hours for both systems) | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.nice_support_conversion_rate_xf_archive`
    *   `model.cherry_data_model.zendesk_support_conversion_rate_xf`

---
