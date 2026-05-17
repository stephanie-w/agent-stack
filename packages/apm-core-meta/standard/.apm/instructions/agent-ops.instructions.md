---
description: "High-rigor operational behaviors for production-grade development, prioritizing verification and auditability."
---
## Agent Operational Guidelines (Standard/High Rigor)

These rules define the mandatory operational behaviors for production-grade engineering tasks.

### 1. Verification & Testing
1. **Test-Driven Mindset**: Every logic change must be accompanied by a new test or an updated existing test.
2. **Verification Loop**: You are responsible for the quality of your output. Always run the project's linting, typechecking, and testing tools before signaling completion.
3. **UI/UX Validation**: For UI changes, create reproduction scripts or mockups in a `demos/` directory to verify behavior in isolation.

### 2. Auditability & Documentation
1. **Persistent Thought Process**: Record your hypothesis, exploration, and decisions in the appropriate task tracking file (e.g., `TODO.md`).
2. **Traceability**: Link relevant files, logs, and artifacts directly in your documentation.
3. **Living Instruction**: If you discover a project-specific pattern or trap, update the `AGENTS.md` (or equivalent) to help future agents avoid the same issue.

### 3. Advanced Git Usage
1. **Checkpoint Commits**: Perform a commit once a significant sub-task is verified.
2. **Atomic Commits**: Ensure each commit contains exactly one logical change.
3. **Worktree Support**: For exploratory changes, prefer using a git worktree to maintain a clean workspace.

### 4. Rigor Checklist
- [ ] **Tests**: Did I add/update tests? Do they pass?
- [ ] **Lint**: Did all project-specific quality checks pass?
- [ ] **Audit Trail**: Are my decisions documented in the task log?
