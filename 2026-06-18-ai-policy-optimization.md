# 2026-06-18 — AI for Firewall Policy Optimization

Today I shipped the first public version of the firewall policy optimizer.

Key lessons:

- Hit count data is gold. Rules with 0 hits for 90 days are almost always safe to remove or heavily scope down.
- Shadow detection is surprisingly effective even with naive "any" heuristics.
- Business context matters more than pure technical analysis. A "risky" rule that enables a critical trading app may be acceptable if properly logged and reviewed.

Next: integrate actual hit count exports from Panorama and add a simple RAG layer that can explain *why* a rule was created (from tickets).

Risk reduction so far in real environments: 30-60% reduction in rule count after cleanup passes.
