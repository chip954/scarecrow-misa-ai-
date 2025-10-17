# Compact Triage Demo (MISA)

**Frame:** SEV-1 spike in UserDB-Auth 500s (~80% NA).  
**Plan (≤3):** (1) Stop change/declare; (2) isolate region vs. last deploy; (3) reversible mitigation.  
**Answer:** *Decision:* Roll back last deploy (NA), freeze changes. *Fallback:* shift NA traffic to EU; disable `beta_cache`.  
**Checks (1–2):** Root cause unconfirmed; rollback assumes deploy-correlation.  
**Next-Deed:** “Proceed” to execute mitigation (if tools allowed) or “LOOK-ONLY: logs/stacktrace sample”.
