# 2026-06-20 — RAG for Security Operations

Building RAG systems for security data is different from generic chatbots.

Challenges specific to this domain:

- High sensitivity: you cannot just send firewall logs or NAC data to a public LLM
- Need for precise citations (regulators want to see exactly which rule + log line drove a conclusion)
- Time sensitivity during incidents

Current architecture that seems promising:

- Private embedding model or hosted embeddings (never raw logs to OpenAI)
- Retrieval over structured data (not just vector search over text)
- Strong guardrails + human-in-the-loop before any automated action

The biggest win so far has been using RAG to correlate "why was this user allowed here?" across firewall, ISE, and BGP data.

Still early, but this direction feels much more powerful than pure agent loops for regulated environments.
