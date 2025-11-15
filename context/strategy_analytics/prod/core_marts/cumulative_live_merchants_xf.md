## Model: `cumulative_live_merchants_xf`

`cumulative_live_merchants_xf`

*   **Unique ID:** `model.cherry_data_model.cumulative_live_merchants_xf`
*   **FQN:** `prod.core_marts.cumulative_live_merchants_xf`
*   **Description:** This table shows the cumulative number of merchants that have gone live with Cherry over time.
### Warning for go live dates
Tracking of when merchants have gone live at Cherry has been a challenge until recently. For a long
period there was little tracking of when specifically a merchant became live. However, we now
automatically stamp the date that a merchant is ready to transact in Salesforce the first time
that we see a merchant is no longer in demo mode.

This is not true for all merchants, and not all live merchants have a record in salesforce so
we prefer values in the following order:

  1. **Commission eligibility start date from Salesforce:** This is set programatically when Salesforce
  first learns that the merchant is no longer in demo mode. This has been backfilled using data
  from when *started at* was set in the Cherry database.

  2. **Initial transactions date from Salesforce:** This is the field which was previously, and still
  is programatically set, in Salesforce. The logic for stamping it on the record is slightly less
  powerful so it is second in order of priority. This has been backfilled using data from when
  *started at* was set in the Cherry database.

  3. **Started At Date from Cherry Merchant Record:** This is the least reliable datapoint as it has
  never been programatically set. For a long time it was our best method of tracking of tracking the
  date that merchants started as before we began using Snowflake we had no way to join Cherry data
  to Salesforce data. It was updated with the newly active merchants each day to allow for sales rep
  commission reporting.
### Warning for Cumulative Live Merchants Count
When tracking cumulative live merchants we make the following assumptions:

1. The merchant must be currently active on the Cherry platform and able to transact. *This means
that terminated merchants are not included even for the period of time they were active with Cherry.*

2. The merchant must not be in **demo mode**

3. Dental subverticals are currently grouped together into a single top level *Dental* industry.
This means that a practice which only offers *Orthodontics* would currently be counted as a
*Dental* practice.
*   **Tags:** `['core', 'contact_rate', 'key-metrics']`
*   **Meta:** `{'monitoring': {'+tags': ['monitoring_metrics'], '+schema': 'monitoring'}}`
*   **Columns:**
    | Name | Index | Type | Comment | Description | Tags | Meta |
    |------|-------|------|---------|-------------|------|------|
    | `REFERENCE_DATE` | 1 | `DATE` | The date in question. One row for each day since September 1, 2020 excluding today | The date in question. One row for each day since September 1, 2020 excluding today | `[]` | `{}` |
    | `INDUSTRY` | 2 | `TEXT` | The industry of an organization, pulled from the Cherry database. There used to be some level of industry aggregation on this field, but that has been removed with the launch of more granular industries in the Cherry database.
 | The industry of an organization, pulled from the Cherry database. There used to be some level of industry aggregation on this field, but that has been removed with the launch of more granular industries in the Cherry database.
 | `[]` | `{}` |
    | `MERCHANT_TYPE` | 3 | `TEXT` |  |  | `[]` | `{}` |
    | `CUMULATIVE_MERCHANTS_ACTIVE` | 4 | `NUMBER` | The cumulative number of merchants active in the industry.
When tracking cumulative live merchants we make the following assumptions:

1. The merchant must be currently active on the Cherry platform and able to transact. *This means
that terminated merchants are not included even for the period of time they were active with Cherry.*

2. The merchant must not be in **demo mode**

3. Dental subverticals are currently grouped together into a single top level *Dental* industry.
This means that a practice which only offers *Orthodontics* would currently be counted as a
*Dental* practice. | The cumulative number of merchants active in the industry.
When tracking cumulative live merchants we make the following assumptions:

1. The merchant must be currently active on the Cherry platform and able to transact. *This means
that terminated merchants are not included even for the period of time they were active with Cherry.*

2. The merchant must not be in **demo mode**

3. Dental subverticals are currently grouped together into a single top level *Dental* industry.
This means that a practice which only offers *Orthodontics* would currently be counted as a
*Dental* practice. | `[]` | `{}` |
*   **Depends On (Parents):**
    *   `macro.cherry_data_model.convert_to_pt`
    *   `model.cherry_data_model.calendar_table_xf`
    *   `model.cherry_data_model.stg_merchants`

---
