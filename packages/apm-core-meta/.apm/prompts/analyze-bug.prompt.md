---
description: Systematic approach to bug resolution and root cause investigation.
input:
  - issue: "The bug description, issue ID, or stack trace to analyze"
allowed-tools: [bash, read, grep]
---

# Analyze Bug

Your task is to systematically investigate and diagnose the bug described in: `${input:issue}`.

## Investigation Steps

1. **Understand the Report**: Analyze the provided issue description or stack trace to identify the core symptom.
2. **Reproduce (if possible)**: Look for existing tests related to the symptom. If a reproduction script or test is missing, propose one to empirically confirm the failure state.
3. **Trace the Execution**: Use grep, file search, and read tools to trace the code path related to the bug.
4. **Identify Root Cause**: Determine the underlying reason for the failure (e.g., logic error, race condition, missing validation, state mutation).
5. **Propose Fix**: Draft a minimal, surgical fix for the issue. Ensure the fix aligns with existing architectural patterns and does not introduce regressions.

## Output Format

Present your findings in a structured diagnostic report:

- **Symptom**: Brief summary of the observed behavior.
- **Root Cause**: The technical reason the bug occurs, including specific files and functions.
- **Proposed Fix**: A detailed explanation of the necessary code changes.
- **Verification Strategy**: How the fix should be tested to prevent regressions.
