---
description: Draft a commit message using the project's Git standards.
allowed-tools: [bash, read, grep]
---

# Draft Git Commit

Your task is to draft a high-quality Git commit message based on the current staged changes, strictly adhering to our project's commit message format (`<type>(<scope>): <subject>`).

## Steps:

1. **Analyze Changes**: Run `git diff HEAD` (and `git status` if necessary) to review all changes in the working directory that are ready to be committed.
2. **Review Standards**: Recall the commit message standards from the `git-workflow` instructions in your context. Pay special attention to the allowed types (feat, fix, docs, style, refactor, test, chore) and the structural format.
3. **Draft Message**: Propose a commit message.
   - The `<subject>` must be concise and descriptive.
   - Include a `<body>` explaining the "why" and "what" if the change is non-trivial.
   - Note any closed issues in the `<footer>` if applicable.
4. **Confirm**: Present the drafted commit message to the user and ask if they would like you to execute the commit or if they want to make modifications.
