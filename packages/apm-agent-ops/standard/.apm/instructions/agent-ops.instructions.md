---
description: "High-rigor operational behaviors for production-grade development, prioritizing verification and auditability."
---
## Agent Operational Guidelines (Standard/High Rigor)

These rules define the mandatory operational behaviors for production-grade engineering tasks.

### 1. Conversational Coding Workflow
To ensure a safe and collaborative development experience, follow this interactive workflow for all code modifications:
1. **Research & Analysis**: Thoroughly investigate the codebase to understand the current implementation and dependencies.
2. **Proposed Strategy**: Before writing any code, provide a concise summary of the intended changes, including:
   - **The "Why"**: Technical rationale for the approach.
   - **The "How"**: Specific files to be modified and new logic to be added.
   - **Impact**: Potential side effects or architectural considerations.
3. **Review & Confirmation**: Explicitly ask the user to review and confirm the strategy. **Wait for user approval** before proceeding with the implementation.
4. **Surgical Execution**: Once confirmed, apply the changes iteratively, providing clear intent for each step.
5. **Task Completion Verification**: Never mark a task as completed without explicit user verification when the task involves user-facing functionality. Always ask "Could you test this?" before updating task trackers.

### 2. Verification & Testing
1. **Test-Driven Mindset**: Every logic change must be accompanied by a new test or an updated existing test.
2. **Verification Loop**: You are responsible for the quality of your output. Always run the project's linting, typechecking, and testing tools before signaling completion.
3. **UI/UX Validation**: For UI changes, create reproduction scripts or mockups in a `demos/` directory to verify behavior in isolation.

### 3. Auditability & Documentation
1. **Persistent Thought Process**: Record your hypothesis, exploration, and decisions in the appropriate task tracking file (e.g., `TODO.md`).
2. **Traceability**: Link relevant files, logs, and artifacts directly in your documentation.
3. **Living Instruction**: If you discover a project-specific pattern or trap, update the `AGENTS.md` (or equivalent) to help future agents avoid the same issue.

### 4. Advanced Git Usage
1. **Checkpoint Commits**: Perform a commit once a significant sub-task is verified.
2. **Atomic Commits**: Ensure each commit contains exactly one logical change.
3. **Worktree Support**: For exploratory changes, prefer using a git worktree to maintain a clean workspace.

### 5. Rigor Checklist
- [ ] **Tests**: Did I add/update tests? Do they pass?
- [ ] **Lint**: Did all project-specific quality checks pass?
- [ ] **Audit Trail**: Are my decisions documented in the task log?
