---
description: Stress-tests plans and designs through relentless interviewing.
input:
  - focus: "The specific file or concept to stress-test (e.g. docs/prd.md)"
allowed-tools: [bash, read, grep]
---

# Grill Me

Your task is to analyze `${input:focus}` and stress-test the plans and designs it contains.

1. **Review**: Read the target content in `${input:focus}`.
2. **Interview**: Interview me relentlessly about every aspect of this plan until we reach a shared understanding. Walk down each branch of the design tree, resolving dependencies between decisions one-by-one.
3. **Explore**: If a question can be answered by exploring the codebase, use your tools to explore the codebase instead of asking me.
