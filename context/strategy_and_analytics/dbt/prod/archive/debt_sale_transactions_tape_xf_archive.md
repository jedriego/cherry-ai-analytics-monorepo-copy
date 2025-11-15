## Model: `debt_sale_transactions_tape_xf_archive`

`debt_sale_transactions_tape_xf_archive`

*   **Unique ID:** `model.cherry_data_model.debt_sale_transactions_tape_xf_archive`
*   **FQN:** `prod.archive.debt_sale_transactions_tape_xf_archive`
*   **Description:** (No description provided)
*   **Tags:** `['archive']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `CUSTOMER_ID` | 1 | `TEXT` |  |  | `[]` | `{}` |
    | `LOAN_TRANSACTION_ID` | 2 | `NUMBER` |  |  | `[]` | `{}` |
    | `TRANSACTION_DATE` | 3 | `DATE` |  |  | `[]` | `{}` |
    | `REVERSE_DATE` | 4 | `DATE` |  |  | `[]` | `{}` |
    | `LOAN_TRANSACTION_TYPE` | 5 | `TEXT` |  |  | `[]` | `{}` |
    | `TRANSACTION_TITLE` | 6 | `TEXT` |  |  | `[]` | `{}` |
    | `PAYMENT_AMOUNT` | 7 | `NUMBER` |  |  | `[]` | `{}` |
    | `PAYMENT_PRINCIPAL` | 8 | `NUMBER` |  |  | `[]` | `{}` |
    | `PAYMENT_INTEREST` | 9 | `NUMBER` |  |  | `[]` | `{}` |
    | `PAYMENT_FEES` | 10 | `NUMBER` |  |  | `[]` | `{}` |
    | `RECOVERY_AMOUNT` | 11 | `NUMBER` |  |  | `[]` | `{}` |
    | `REVERSAL_AMOUNT` | 12 | `NUMBER` |  |  | `[]` | `{}` |
    | `CHARGE_AMOUNT` | 13 | `NUMBER` |  |  | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.loan_statuses_today_xf`
    *   `model.cherry_data_model.src_loan_tx`
    *   `model.cherry_data_model.src_loanpro_payments`

---
