# 2026-06-19 — Validating Micro-segmentation at Scale

One of the hardest parts of Zero Trust is proving that your segmentation actually works.

Common failure modes I've seen:

- Identity-aware ACLs that are bypassed by service accounts with broad privileges
- "Temporary" any/any rules for migrations that never get cleaned up
- East-west traffic that looks clean on paper but has dozens of exception paths in reality

Practical pattern that worked well:

1. Export current firewall + NAC (ISE) + routing data
2. Build a correlation layer (even simple pandas + graph) that flags allowed paths that should be blocked
3. Feed that into an LLM that produces human-readable investigation tickets

Result: time-to-answer for "is this properly segmented?" dropped from ~45 min to under 5 min.

Still working on making the validation deterministic and auditable for regulators.
