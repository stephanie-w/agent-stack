---
description: Decomposes PRDs into independent, end-to-end vertical slices.
input:
  - prd_path: "Path to the PRD file"
allowed-tools: [bash, read, grep]
---

# PRD to Issues

Use the `prd-to-issues` skill to decompose ${input:prd_path}.

1. LOAD the `prd-to-issues` skill.
2. Read the PRD at ${input:prd_path}.
3. Break the requirements into vertical slices (tracer bullets).
4. Propose actionable GitHub issues.
