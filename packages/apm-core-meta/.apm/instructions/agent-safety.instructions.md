---
description: "Mandatory safety and integrity protocols for AI agents, applicable across all development modes."
applyTo: "*"
---
## Agent Safety & Integrity Protocols

These are the foundational rules for AI agent behavior. They prioritize project integrity, security, and accuracy.

### 1. Core Safety Directives

#### 🛡️ Information Integrity
1.  **Read Before Write**: You MUST read relevant files (config, dependencies, existing source) before proposing or making changes. Never assume the state of the project.
2.  **No Hallucinations**: Do not use libraries, tools, or patterns that are not explicitly present or authorized in the workspace.
3.  **Secrets Management**: **NEVER** log, print, or commit secrets, API keys, or sensitive credentials. Protect `.env` files and system configuration folders rigorously.

#### 🧪 Structural Integrity
1.  **Atomic Changes**: Target specific lines or blocks for surgical edits. Avoid rewriting entire files unless necessary for a complete refactor.
2.  **No Silent Failures**: Errors must be explicitly handled, bubbled up, or reported. Never swallow exceptions silently.
3.  **Platform Neutrality**: Use platform-agnostic paths (relative paths) to ensure the project works across different environments.

### 2. Quality Checklist

Before completing any task, ensure:
- [ ] **Context**: I have verified the current project state.
- [ ] **Safety**: No secrets have been exposed.
- [ ] **Surgicality**: Changes are focused and minimal.
- [ ] **Error Handling**: Failures are transparent and handled.
