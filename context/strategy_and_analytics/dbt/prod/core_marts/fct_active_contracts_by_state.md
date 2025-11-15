## Model: `fct_active_contracts_by_state`

`fct_active_contracts_by_state`

*   **Unique ID:** `model.cherry_data_model.fct_active_contracts_by_state`
*   **FQN:** `prod.core_marts.fct_active_contracts_by_state`
*   **Description:** Fact table that aggregates active loan contract metrics by borrower state, providing a geographic view of the active lending portfolio. This model combines funded contract information with borrower location data to create state-level summaries of contract counts and outstanding balances for active loans. Only includes contracts with loan status of 'OPEN' or 'LATE', representing the current active portfolio requiring servicing and collections attention. The model serves as a key reporting table for geographic analysis, compliance reporting, state-level performance tracking, and portfolio management. It enables analysis of lending concentration by geography, state-specific risk patterns, and regulatory compliance monitoring across different jurisdictions.

*   **Tags:** `['core']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `STATE_NAME` | 1 | `TEXT` | Name of the U.S. state where the borrower resides, derived from the borrower's address information. Serves as the primary dimension for geographic analysis and aggregation. Used for state-level compliance reporting, geographic risk assessment, and market analysis. This field enables tracking of lending concentration across different states and jurisdictions.
 | Name of the U.S. state where the borrower resides, derived from the borrower's address information. Serves as the primary dimension for geographic analysis and aggregation. Used for state-level compliance reporting, geographic risk assessment, and market analysis. This field enables tracking of lending concentration across different states and jurisdictions.
 | `[]` | `{}` |
    | `NUM_CONTRACTS` | 2 | `NUMBER` | Count of active loan contracts for borrowers residing in the specified state. Calculated as COUNT(*) of all funded contracts where the associated loan status is either 'OPEN' or 'LATE'. This metric represents the total number of active loan agreements requiring ongoing servicing, payment collection, or remediation activities. Used for portfolio size analysis, workload distribution planning, and state-level market penetration assessment.
 | Count of active loan contracts for borrowers residing in the specified state. Calculated as COUNT(*) of all funded contracts where the associated loan status is either 'OPEN' or 'LATE'. This metric represents the total number of active loan agreements requiring ongoing servicing, payment collection, or remediation activities. Used for portfolio size analysis, workload distribution planning, and state-level market penetration assessment.
 | `[]` | `{}` |
    | `OUTSTANDING_BALANCE` | 3 | `FLOAT` | Total outstanding loan balance for all active contracts in the specified state, calculated as the sum of loan_balance from the loan_plans table and rounded to 2 decimal places. This metric represents the total dollar amount of principal and accrued interest that borrowers in the state currently owe on their active loans. Used for portfolio valuation, risk assessment, geographic concentration analysis, and regulatory capital requirement calculations. Critical for understanding state-level exposure and managing geographic risk diversification. | Total outstanding loan balance for all active contracts in the specified state, calculated as the sum of loan_balance from the loan_plans table and rounded to 2 decimal places. This metric represents the total dollar amount of principal and accrued interest that borrowers in the state currently owe on their active loans. Used for portfolio valuation, risk assessment, geographic concentration analysis, and regulatory capital requirement calculations. Critical for understanding state-level exposure and managing geographic risk diversification. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.int_funded_information_pt`
    *   `model.cherry_data_model.src_borrowers`
    *   `model.cherry_data_model.stg_borrower_addresses_with_tz`
    *   `model.cherry_data_model.stg_loan_plans`

---
