---
name: ask-user
description: Reusable pattern for presenting the user with explicit choices and gating execution until they respond. Used by other skills when a decision point requires human input before proceeding.
---

# Ask User — Choice Gate Pattern

Use this skill whenever a task reaches a fork where multiple valid paths exist, or where a wrong default would result in significant rework.

## 1. The Gating Contract

- **Prioritize the Tool**: If the `ask_user` (or `AskUserQuestion`) tool is available, use it to present structured choices.
- **2-4 Options Max**: Never present more than 4 options to avoid decision paralysis.
- **Stop the Turn**: **CRITICAL.** After presenting choices, you MUST stop execution. Do not make follow-up tool calls or "start" on a default path.
- **Escape Hatch**: Always include a "Skip", "Cancel", or "None of these" option.
- **Labels**: Use "Action + Qualifier" labels (e.g., "Merge Changes") rather than cryptic ones (e.g., "Option 1").

## 2. When to Gate

- **Destructive/Risky**: Bulk deletes, overwrites, or force-pushes.
- **Ambiguity**: Multiple interpretations of a user's request.
- **Forks**: Choosing between different architectural patterns or file locations.
- **Triage**: When multiple tasks are identified and you need to know which to do first.

## 3. Presentation Pattern (Text Fallback)

If the structured tool is unavailable, use this format:

🔀 **How should I handle this?**
[Brief 1-line context]

1. **Option A** — description
2. **Option B** — description
3. **Cancel** — stop here

## 4. Examples

### Example: File Conflict
"I found an existing `TODO.md` in the target directory. Should I:
1. **Overwrite** — Replace the old file with the new structured version.
2. **Merge** — Append new tasks to the bottom of the existing file.
3. **Cancel** — Do not modify the file."

### Example: Implementation Choice
"I can implement the API client using either `httpx` or `requests`. Both are available.
1. **Use httpx** — Supports async (recommended for this FastAPI project).
2. **Use requests** — Simpler, synchronous-only.
3. **Skip for now** — I'll decide later."

## 5. Anti-Patterns

- **Preemptive Action**: "While you decide, I'll go ahead and..." (❌ Never do this).
- **Silent Defaults**: Picking a path and only mentioning it after the work is done.
- **Stacking Questions**: Asking three different choice questions in one message.
