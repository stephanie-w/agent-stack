# APM Quickstart Guide

This guide provides a high-level overview of how the Agent Package Manager (APM) works and how to manage this repository. Use this as a reference for future sessions to quickly regain context.

## 1. Core Primitives
APM manages four types of "primitives" located in `.apm/` subdirectories:

*   **Instructions (`.instructions.md`)**: "Always-On" rules. Folded into `AGENTS.md` (or `GEMINI.md`) during compilation.
*   **Agents (`.agent.md`)**: Specialized "Personas" that can be summoned (e.g., `@api-architect`).
*   **Skills (`/skills/<name>/SKILL.md`)**: Multi-resource guides (with scripts, templates, and references) that agents auto-discover.
*   **Prompts (`.prompt.md`)**: Executable workflows triggered via `apm run`.

## 2. The "Hybrid" Pattern
We use **Prompts as Entry Points** for complex **Skills**.
*   **The Skill**: Contains the deep logic, templates, and long-running process instructions.
*   **The Prompt**: A thin wrapper that accepts CLI parameters (e.g., `--param project_name="API"`) and uses `LOAD <skill_name>` to trigger the skill.
*   **Benefit**: Allows for "one-command" execution while keeping the agent focused.

## 3. Package Structure: Layers & Flavors
To prevent "Context Bloat" and contradictions, we use a layered architecture:

*   **Layers**: Logic segments (Meta, Standards, Architecture, Domain, Discovery).
*   **Flavors**: Mutually exclusive sub-packages within a layer (e.g., `standard` vs `rapid`).
*   **Conflict Rule**: Never install two flavors from the same layer in one project.

## 4. Key Commands

### For Producers (Authoring)
*   `apm compile --validate`: Validates all primitives in the package.
*   `apm compile`: Generates the harness files (like `AGENTS.md`) for previewing.

### For Consumers (Installing)
*   `apm install <owner>/<repo>/path/to/package`: Installs a package or flavor.
*   `apm run <prompt_name> --param key="value"`: Executes a prompt workflow.

## 5. Compilation & Harnesses
When `apm compile` or `apm install` runs:
1.  It scans all dependencies.
2.  It "folds" all global instructions (`applyTo: "*"`) into a single file (`AGENTS.md` or `GEMINI.md`).
3.  It deploys agents and skills to the appropriate IDE harness (e.g., `.github/agents/`).

## 6. Project Conventions
*   **Reference Syntax**: `#` is for git refs; `/` is for paths (e.g., `owner/repo/path`).
*   **README.md**: The primary source for "Agent Stacks" (recommended package combinations).
*   **AGENTS.md**: A generated artifact. **Do not edit manually.** Edit the source in `.apm/instructions/` instead.
