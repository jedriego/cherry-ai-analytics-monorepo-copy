## Model: `practice_lifetime_value_xf`

`practice_lifetime_value_xf`

*   **Unique ID:** `model.cherry_data_model.practice_lifetime_value_xf`
*   **FQN:** `prod.core_marts.practice_lifetime_value_xf`
*   **Description:** This model calculates the lifetime value of practices by aggregating merchant-level data. It combines data from multiple merchants that belong to the same practice and adjusts various metrics accordingly.

*   **Tags:** `['core', 'practice', 'lifetime_value', 'core_marts']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `PRIMARY_MERCHANT_ID` | 1 | `FLOAT` | The primary merchant ID that represents the practice | The primary merchant ID that represents the practice | `[]` | `{}` |
    | `ACCOUNT_INDUSTRY_SEGMENT` | 2 | `TEXT` | The industry segment of the account | The industry segment of the account | `[]` | `{}` |
    | `ACCOUNT_INDUSTRY_SEGMENT_ADJ` | 3 | `TEXT` | Adjusted industry segment, set to 'Alle' for new practices | Adjusted industry segment, set to 'Alle' for new practices | `[]` | `{}` |
    | `GO_LIVE_DATE_ADJ` | 4 | `DATE` | The adjusted go-live date for the practice | The adjusted go-live date for the practice | `[]` | `{}` |
    | `MONTHS_SINCE_GO_LIVE_ADJ` | 5 | `NUMBER` | Number of months since the practice went live | Number of months since the practice went live | `[]` | `{}` |
    | `EVALUATION_MONTHS_ADJ` | 6 | `NUMBER` | Total number of months for evaluation period | Total number of months for evaluation period | `[]` | `{}` |
    | `EVALUATION_MONTHS_REMAINING_ADJ` | 7 | `NUMBER` | Number of months remaining in the evaluation period | Number of months remaining in the evaluation period | `[]` | `{}` |
    | `MARKETING_COST_ADJ` | 8 | `FLOAT` | Adjusted marketing cost for the practice | Adjusted marketing cost for the practice | `[]` | `{}` |
    | `MARKETING_BOX_COST_ADJ` | 9 | `FLOAT` | Adjusted marketing box cost, set to 0 for new practices | Adjusted marketing box cost, set to 0 for new practices | `[]` | `{}` |
    | `HAS_SALES_DEVELOPMENT_ADJ` | 10 | `BOOLEAN` | Whether the practice has sales development | Whether the practice has sales development | `[]` | `{}` |
    | `SALES_DEVELOPMENT_COST_ADJ` | 11 | `NUMBER` | Combined sales development cost from all merchants in the practice | Combined sales development cost from all merchants in the practice | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_ROLE_ADJ` | 12 | `TEXT` | The adjusted account executive role for the practice | The adjusted account executive role for the practice | `[]` | `{}` |
    | `ACCOUNT_EXECUTIVE_COST_ADJ` | 13 | `NUMBER` | The adjusted account executive cost for the practice | The adjusted account executive cost for the practice | `[]` | `{}` |
    | `ONBOARDING_TYPE_ADJ` | 14 | `TEXT` | The adjusted onboarding type for the practice | The adjusted onboarding type for the practice | `[]` | `{}` |
    | `ONBOARDING_COST_ADJ` | 15 | `NUMBER` | Combined onboarding cost from all merchants in the practice | Combined onboarding cost from all merchants in the practice | `[]` | `{}` |
    | `WEBSITE_IMPLEMENTATION_COST_ADJ` | 16 | `FLOAT` | Combined website implementation cost from all merchants in the practice | Combined website implementation cost from all merchants in the practice | `[]` | `{}` |
    | `REFERRAL_PARTNER_COST_ADJ` | 17 | `FLOAT` | Combined referral partner cost from all merchants in the practice | Combined referral partner cost from all merchants in the practice | `[]` | `{}` |
    | `RETENTION_OWNER_DEPARTMENT_ADJ` | 18 | `TEXT` | The adjusted retention owner department for the practice | The adjusted retention owner department for the practice | `[]` | `{}` |
    | `RETENTION_OWNER_TEAM_ADJ` | 19 | `TEXT` | The adjusted retention owner team for the practice | The adjusted retention owner team for the practice | `[]` | `{}` |
    | `RETENTION_OWNER_ADJ` | 20 | `TEXT` | The adjusted retention owner for the practice | The adjusted retention owner for the practice | `[]` | `{}` |
    | `MONTHLY_RETENTION_COST_ADJ` | 21 | `NUMBER` | The adjusted monthly retention cost for the practice | The adjusted monthly retention cost for the practice | `[]` | `{}` |
    | `TOTAL_RETENTION_COST_ADJ` | 22 | `NUMBER` | The adjusted total retention cost for the practice | The adjusted total retention cost for the practice | `[]` | `{}` |
    | `TOTAL_ACQUISITION_COST_ADJ` | 23 | `FLOAT` | The total acquisition cost, calculated as the sum of marketing cost, marketing box cost, sales development cost, account executive cost, onboarding cost, referral partner cost, and website implementation cost
 | The total acquisition cost, calculated as the sum of marketing cost, marketing box cost, sales development cost, account executive cost, onboarding cost, referral partner cost, and website implementation cost
 | `[]` | `{}` |
    | `GROSS_AMOUNT_TOTAL_ADJ` | 24 | `FLOAT` | Combined gross amount total from all merchants in the practice | Combined gross amount total from all merchants in the practice | `[]` | `{}` |
    | `REVENUE_TOTAL_ADJ` | 25 | `FLOAT` | Combined revenue total from all merchants in the practice | Combined revenue total from all merchants in the practice | `[]` | `{}` |
    | `CONTRIBUTION_MARGIN_TOTAL_ADJ` | 26 | `FLOAT` | Combined contribution margin total from all merchants in the practice | Combined contribution margin total from all merchants in the practice | `[]` | `{}` |
    | `VOLUME_PER_MONTH_AVG_ADJ` | 27 | `FLOAT` | Average monthly volume, calculated as gross amount total divided by months since go-live | Average monthly volume, calculated as gross amount total divided by months since go-live | `[]` | `{}` |
    | `REVENUE_PER_MONTH_AVG_ADJ` | 28 | `FLOAT` | Average monthly revenue, calculated as revenue total divided by months since go-live | Average monthly revenue, calculated as revenue total divided by months since go-live | `[]` | `{}` |
    | `REMAINING_CONTRIBUTION_MARGIN_EXPECTED_ADJ` | 29 | `FLOAT` | Combined remaining expected contribution margin from all merchants in the practice | Combined remaining expected contribution margin from all merchants in the practice | `[]` | `{}` |
    | `TOTAL_CONTRIBUTION_MARGIN_EXPECTED_ADJ` | 30 | `FLOAT` | Total expected contribution margin, calculated as the sum of current contribution margin and expected remaining contribution margin
 | Total expected contribution margin, calculated as the sum of current contribution margin and expected remaining contribution margin
 | `[]` | `{}` |
    | `LIFETIME_VALUE_ADJ` | 31 | `FLOAT` | The adjusted lifetime value of the practice, calculated as total expected contribution margin minus remaining retention costs | The adjusted lifetime value of the practice, calculated as total expected contribution margin minus remaining retention costs | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.merchant_lifetime_value`
    *   `model.cherry_data_model.practice_info_xf`
    *   `model.cherry_data_model.stg_merchants`

---
