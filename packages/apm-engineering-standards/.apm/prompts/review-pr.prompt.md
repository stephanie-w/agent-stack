---
description: Review a pull request against our coding standards and Git workflow rules.
input:
  - pr_url: "URL of the PR to review (optional if running inside the checked-out PR branch)"
allowed-tools: [bash, read, grep]
---

# Review Pull Request

Your task is to review the code changes for a specific Pull Request, evaluating them against our project's engineering standards.

## Steps:

1. **Fetch Changes**:
   - If `${input:pr_url}` is provided, use the GitHub CLI (`gh pr diff ${input:pr_url}`) or a web fetch tool to retrieve the diff.
   - If no URL is provided, assume we are on the PR branch and run `git diff develop...HEAD` to see the proposed changes.
2. **Review Against Standards**: Analyze the diff carefully. Keep the following in mind based on our `git-workflow` and general engineering context:
   - Is the code modular and clean?
   - Are there missing tests for new logic?
   - Does it violate any established architectural rules?
3. **Draft Feedback**: Provide a structured review summary containing:
   - **High-Level Assessment**: Overall thoughts on the approach.
   - **Blockers**: Critical issues or standard violations that must be fixed.
   - **Suggestions**: Architectural or stylistic improvements.
   - **Nits**: Minor formatting or naming details.
