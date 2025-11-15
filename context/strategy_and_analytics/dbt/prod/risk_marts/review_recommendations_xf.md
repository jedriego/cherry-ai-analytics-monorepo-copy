## Model: `review_recommendations_xf`

`review_recommendations_xf`

*   **Unique ID:** `model.cherry_data_model.review_recommendations_xf`
*   **FQN:** `prod.risk_marts.review_recommendations_xf`
*   **Description:** **Automated Review Recommendations Engine**
This model transforms the comprehensive performance data from `review_stats_xf` into specific,  actionable recommendations for merchant recovery and retention. It applies business rules and  logic to generate tailored advice based on merchant-specific challenges identified in financing  adoption, term length configuration, subprime exposure, and web positioning.
**Key Business Logic:** - **Rule-Based Recommendations**: Applies predefined business rules to merchant statistics 
  to generate specific, actionable recovery strategies
- **Multi-Dimensional Analysis**: Evaluates financing volume, application conversion, policy types, 
  term lengths, subprime exposure, and web positioning
- **Targeted Interventions**: Provides customized recommendations based on industry segment 
  (currently focused on MedSpa segment)
- **Consolidated Guidance**: Combines multiple recommendation categories into unified notes 
  for review team execution

**Business Rules Applied:** - **Financing Volume**: Low estimated monthly financing volume triggers financing education recommendations - **Conversion Issues**: Low application-to-funding ratios trigger denial investigation guidance - **Policy Optimization**: Very competitive menu eligibility and geographic considerations - **Term Length**: Suboptimal promotional term settings trigger configuration recommendations - **Subprime Strategy**: High subprime exposure triggers fee sensitivity and approval rate discussions - **Web Positioning**: Poor web review scores trigger website optimization guidance
**Primary Use Cases:** - Automated generation of recovery action plans - Standardized intervention strategies for review teams - Consistent application of best practices across merchants - Scalable review process management and execution guidance
**Grain:** One record per merchant under review (filtered to MedSpa segment)

*   **Tags:** `['risk']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `SF_ACCOUNT_ID` | 1 | `TEXT` | Salesforce account identifier linking merchants to CRM data, customer interactions, and sales process tracking. Used for operational workflow integration. | Salesforce account identifier linking merchants to CRM data, customer interactions, and sales process tracking. Used for operational workflow integration. | `[]` | `{}` |
    | `PRIMARY_MERCHANT_ID` | 2 | `FLOAT` | Cherry's primary merchant identifier representing the main merchant location for the account, used for consolidating multi-location merchant data and primary relationship management. | Cherry's primary merchant identifier representing the main merchant location for the account, used for consolidating multi-location merchant data and primary relationship management. | `[]` | `{}` |
    | `REVIEW_START_DATE` | 3 | `TEXT` | Start date of the current review period for the merchant, marking the beginning  of the formal review and intervention process.
 | Start date of the current review period for the merchant, marking the beginning  of the formal review and intervention process.
 | `[]` | `{}` |
    | `REVIEW_END_DATE` | 4 | `DATE` | End date of the current review period, indicating when review decisions and  outcomes are expected to be finalized.
 | End date of the current review period, indicating when review decisions and  outcomes are expected to be finalized.
 | `[]` | `{}` |
    | `FINANCING` | 5 | `TEXT` | Automated recommendation for addressing financing-related challenges based on estimated  monthly financing volume, application conversion rates, and policy types. Provides specific  guidance for financing education, denial investigation, or competitive positioning strategies.
 | Automated recommendation for addressing financing-related challenges based on estimated  monthly financing volume, application conversion rates, and policy types. Provides specific  guidance for financing education, denial investigation, or competitive positioning strategies.
 | `[]` | `{}` |
    | `TERM_LENGTH` | 6 | `TEXT` | Automated recommendation for optimizing promotional term length configuration based on  the merchant's current maximum promotional term settings. Addresses potential customer  perception issues related to 0% APR availability periods.
 | Automated recommendation for optimizing promotional term length configuration based on  the merchant's current maximum promotional term settings. Addresses potential customer  perception issues related to 0% APR availability periods.
 | `[]` | `{}` |
    | `SUBPRIME` | 7 | `TEXT` | Automated recommendation for managing subprime exposure and fee sensitivity based on  the merchant's prime/subprime loan mix. Provides guidance on subprime approval strategy  and revenue optimization discussions.
 | Automated recommendation for managing subprime exposure and fee sensitivity based on  the merchant's prime/subprime loan mix. Provides guidance on subprime approval strategy  and revenue optimization discussions.
 | `[]` | `{}` |
    | `WEB_REVIEW` | 8 | `TEXT` | Automated recommendation for improving Cherry's web positioning based on the merchant's  web review score. Provides specific guidance for website optimization and competitive  positioning improvements.
 | Automated recommendation for improving Cherry's web positioning based on the merchant's  web review score. Provides specific guidance for website optimization and competitive  positioning improvements.
 | `[]` | `{}` |
    | `NOTES` | 9 | `TEXT` | Consolidated recommendation text combining all applicable recommendations (financing,  term length, subprime, web review) into a single formatted note for review team execution.  Each recommendation category is separated by double line breaks for readability. | Consolidated recommendation text combining all applicable recommendations (financing,  term length, subprime, web review) into a single formatted note for review team execution.  Each recommendation category is separated by double line breaks for readability. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.review_stats_xf`

---
