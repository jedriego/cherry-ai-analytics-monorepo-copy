## Model: `daily_contact_rate_xf_archive`

`daily_contact_rate_xf_archive`

*   **Unique ID:** `model.cherry_data_model.daily_contact_rate_xf_archive`
*   **FQN:** `prod.archive.daily_contact_rate_xf_archive`
*   **Description:** A model which calculates the daily contact rate for support and servicing from '2022-03-01' until one day before the current date. It only considers inbound volume via Genesys.
**Contact rate is defined as the proportion of an eligible population making contact in any manner with either the support or sevicing teams at Cherry.**
The contact rate is an important metric for the support and servicing teams because it can both help evaluate the effectiveness of experiences before support is contacted, and the changes each team makes in their practices of proactive education. Better education would lead to a lower contact rate.
**The model currently considers re-contacts within any time period in any channel as contacts.**
*   **Tags:** `['archive', 'genesys', 'contact_rate', 'key-metrics', 'support', 'servicing', 'core_operating_results']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `REFERENCE_DATE` | 1 | `DATE` |  | The date in question for the contact rate value. | `[]` | `{}` |
    | `EVAL_WEEK` | 2 | `DATE` |  | The week of the reference_date, obtained by using `DATE_TRUNC('WEEK',...)` in Snowflake on the reference_date. | `[]` | `{}` |
    | `EVAL_MONTH` | 3 | `DATE` |  | The month of the reference_date, obtained by using `DATE_TRUNC('MONTH',...)` in Snowflake on the reference_date. | `[]` | `{}` |
    | `IS_WEEKEND` | 4 | `BOOLEAN` |  | Whether or not the reference_date is a weekend. Calculated using `DAYNAME` from Snowflake | `[]` | `{}` |
    | `CUMULATIVE_LIVE_MERCHANTS` | 5 | `NUMBER` |  | The number of live merchants with Cherry on this date.
When tracking cumulative live merchants we make the following assumptions:

1. The merchant must be currently active on the Cherry platform and able to transact. *This means
that terminated merchants are not included even for the period of time they were active with Cherry.*

2. The merchant must not be in **demo mode**

3. Dental subverticals are currently grouped together into a single top level *Dental* industry.
This means that a practice which only offers *Orthodontics* would currently be counted as a
*Dental* practice. | `[]` | `{}` |
    | `NUMBER_SERVICING_ELIGIBLE_BORROWERS` | 6 | `NUMBER` |  | The number of contracts eligible for servicing each day. The key criteria for a contract to
be servicing eligible are:

  1. 0 days past due


  2. Have a principal balance > $2


  3. Not have any amount due. *This excludes contracts with a same day missed payment* | `[]` | `{}` |
    | `DENIED_APPLICANTS` | 7 | `NUMBER` |  | The number of **DISTINCT** applicants with an active denial | `[]` | `{}` |
    | `REVIEW_APPLICANTS` | 8 | `NUMBER` |  | The number of **DISTINCT** borrowers with an application in some review state, either for Know Your Customer or Income Verification reasons
 | `[]` | `{}` |
    | `INITIALIZED_APPLICANTS` | 9 | `NUMBER` |  | The number of **DISTINCT** applicants who have begun an application but not provided their information | `[]` | `{}` |
    | `APPROVED_APPLICANTS` | 10 | `NUMBER` |  | The number of **DISTINCT** applicants who have an approval that is not expired. It does not take into account if the approval has been used | `[]` | `{}` |
    | `APPROVED_NOT_FUNDED_APPLICANTS` | 11 | `NUMBER` |  | The number of **DISTINCT** applicants who have an approval that is not expired. It removes applicants who funded a contract after matching reference_date in the row
 | `[]` | `{}` |
    | `TOTAL_APPLICANTS` | 12 | `NUMBER` |  | The number of **DISTINCT** applicants with a non-expired application in any state | `[]` | `{}` |
    | `ATTRIBUTED_MERCH_CONTACTS` | 13 | `NUMBER` |  | The number of contacts which can be attributed to merchant related matters on the reference_date | `[]` | `{}` |
    | `IMPLIED_MERCH_CONTACTS` | 14 | `NUMBER` |  | The number of unanswered contacts which are implied to be merchant related based on the observed monthly wrap-up code frequency from handled interactions.
 | `[]` | `{}` |
    | `ATTRIBUTED_SERVICING_CONTACTS` | 15 | `NUMBER` |  | The number of contacts which can be attributed to servicing related matters on the reference_date | `[]` | `{}` |
    | `IMPLIED_SERVICING_CONTACTS` | 16 | `NUMBER` |  | The number of unanswered contacts which are implied to be servicing related based on the observed monthly wrap-up code frequency from handled interactions.
 | `[]` | `{}` |
    | `ATTRIBUTED_APPLICANT_CONTACTS` | 17 | `NUMBER` |  | The number of contacts which can be attributed to applicant related matters on the reference_date | `[]` | `{}` |
    | `IMPLIED_APPLICANT_CONTACTS` | 18 | `NUMBER` |  | The number of unanswered contacts which are implied to be applicant related based on the observed monthly wrap-up code frequency from handled interactions.
 | `[]` | `{}` |
    | `TOTAL_MERCH_CONTACTS` | 19 | `NUMBER` |  | The total number of merchant contacts. Sums both attributed and implied contacts | `[]` | `{}` |
    | `TOTAL_SERVICING_CONTACTS` | 20 | `NUMBER` |  | The total number of servicing contacts. Sums both attributed and implied contacts | `[]` | `{}` |
    | `TOTAL_APPLICANT_CONTACTS` | 21 | `NUMBER` |  | The total number of applicant contacts. Sums both attributed and implied contacts | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `model.cherry_data_model.int_answered_contact_splits`
    *   `model.cherry_data_model.pivot_inbound_genesys_xf_archive`
    *   `model.cherry_data_model.stg_daily_contact_rate_eligible`

---
