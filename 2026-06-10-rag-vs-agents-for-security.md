# 2026-06-10 — RAG vs Agents for Security Workflows

I've been experimenting with both.

**RAG strengths in security**:
- Grounded answers with citations back to specific rules/logs
- Easier to audit for compliance
- Less hallucination on factual questions ("which rule allowed this?")

**Agent strengths**:
- Can take multi-step actions (query logs → analyze → propose remediation)
- Good for exploratory work

For regulated finance environments, I'm currently leaning heavily toward RAG + strong human review loops rather than fully autonomous agents.

The combination (agent that uses RAG tools) seems most promising.
