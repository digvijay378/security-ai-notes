# 2026-06-15 — Firewall Governance at Enterprise Scale

One of the most impactful projects I've worked on recently was building an AI-assisted firewall governance platform.

Key metrics from production:
- Policy review time reduced ~60%
- Legacy/unused rules removed: >30%
- Time to investigate segmentation issues: 45 min → <5 min

The secret wasn't magic AI. It was:
1. Good data plumbing (getting clean rule + hit + log + NAC data)
2. Clear risk models
3. Making the output actionable (Jira tickets, not just pretty dashboards)
4. Strong guardrails so the AI never auto-commits changes

This is the pattern I'm now packaging into the open source tools in this org.
