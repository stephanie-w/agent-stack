---
description: Collaborative workflow for crafting Product Requirements Documents.
input:
  - project_name: "The name of the project or feature"
allowed-tools: [bash, read, grep]
---

# Write a PRD

Use the `write-a-prd` skill to scaffold and draft a PRD for ${input:project_name}.

1. LOAD the `write-a-prd` skill.
2. Interview the user to gather requirements.
3. Explore the repo to understand current state.
4. Draft the PRD following the template.
