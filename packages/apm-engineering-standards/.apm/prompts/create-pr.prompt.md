---
description: Generate a comprehensive Pull Request description based on recent commits and the PR checklist.
allowed-tools: [bash, read, grep]
---

# Create Pull Request Description

Your task is to draft a rich, informative Pull Request description that follows our project's PR Template Checklist and accurately summarizes the recent work.

## Steps:

1. **Gather Context**:
   - Identify the current branch and the target branch (usually `develop`).
   - Run `git log develop..HEAD --oneline` to see the commits that make up this feature/fix.
   - Run `git diff develop...HEAD` if you need more context on the actual code changes.
2. **Review Standards**: Recall the "Pull Request Requirements" and "PR Template Checklist" from the `git-workflow` instructions in your context.
3. **Draft Description**: Create the markdown for the PR body. It must include:
   - A high-level summary of the purpose of the PR.
   - A bulleted list of the key changes.
   - The mandatory PR Template Checklist (with boxes checked `[x]` where you have verified they are met, and `[ ]` for the user to review).
4. **Present**: Output the markdown for the user to copy/paste, or offer to use the GitHub CLI (`gh pr create`) if it is available in the environment.
