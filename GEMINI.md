# APM Stacks Monorepo: Instructional Context

Welcome to the Agent Package Manager (APM) Stacks repository. This project is a monorepo containing composable agent primitives (skills, prompts, instructions, and agents) designed to be managed and installed via `apm`.

## Project Overview

APM (Agent Package Manager) is a dependency manager for AI agents, similar to `npm` for software. It allows developers to declare the skills, prompts, and instructions their project needs in an `apm.yml` file, ensuring consistent agent behavior across different tools (GitHub Copilot, Gemini CLI, Cursor, etc.).

This monorepo is organized into **Layers** and **Flavors** to prevent context bloat and contradictory instructions.

### Architecture: Layers & Flavors

1.  **`apm-core-meta`**: The "How to Agent" layer. Contains meta-skills like Code Mentor, Architecture improvement, and Safety Protocols.
    *   *Flavors*: `standard` (High Rigor) vs `rapid` (High Velocity).
2.  **`apm-engineering-standards`**: The "Base" layer. Universal rules for Git workflows and releases.
    *   *Flavors*: `full` (Stateful tracking) vs `basic` (Checklist tracking).
3.  **`apm-python-expert`**: The "Domain & Structure" layer. Deep language-specific standards, security audits, and project layout principles.
    *   *Flavors*: `fullstack` (Polyglot) vs `workspace` (Pure Python workspaces).
4.  **`apm-product-discovery`**: The "Upstream" layer. Idea-to-code tools (PRD writing, Grill Me).

## Core Primitives

Primitives are located in `.apm/` subdirectories within each package:

*   **Instructions (`.instructions.md`)**: "Always-On" rules. Folded into `AGENTS.md` or `GEMINI.md` during compilation.
*   **Agents (`.agent.md`)**: Specialized "Personas" (e.g., `@api-architect`, `@backend-developer`).
*   **Skills (`/skills/`)**: Multi-resource folders containing a `SKILL.md`, scripts, templates, and references.
*   **Prompts (`.prompt.md`)**: Executable workflows triggered via `apm run`.

## Key Commands

### For Authors (Producers)
*   `apm compile --validate`: Validates all primitives in the package.
*   `apm compile`: Generates harness files (like `AGENTS.md`) for previewing.

### For Users (Consumers)
*   `apm install <package_path>`: Installs a package or flavor (e.g., `apm install stephanie/apm-core-meta/standard`).
*   `apm run <prompt_name> --param key="value"`: Executes a specific prompt workflow.

## Development Conventions

### 1. Instruction Files (`.instructions.md`)
*   **Frontmatter**: Must include `description` and `applyTo: "*"`.
*   **Headers**: Always start titles with `##` (H2). This ensures correct hierarchy when files are concatenated.
*   **Ordering**: Use numeric prefixes (e.g., `00-base.md`, `01-security.md`) to control the merge order.

### 2. Skill Folders
*   Each skill must have a `SKILL.md` file.
*   Optional subdirectories: `scripts/`, `templates/`, `assets/`, `references/`.

### 3. Prompt Files (`.prompt.md`)
*   Prompts should be "Entry Points" for complex skills.
*   Use `LOAD <skill_name>` within the prompt to trigger a skill.
*   Use `${input:variable_name}` for parameterization.

## Project Structure (Summary)

```text
packages/
├── apm-core-meta/               # Behavioral meta-skills, architecture, and standards discovery
├── apm-engineering-standards/   # Git workflows, release rules, and onboarding
├── apm-python-expert/           # Python deep-dives and repo structures
└── apm-product-discovery/       # Upstream planning tools (write-a-prd, grill-me, etc.)
```

## Reference
*   **docs/**: Local context on APM. For full and up-to-date documentation, visit the [official APM repository](https://github.com/microsoft/apm/tree/main/docs/src/content/docs).
*   **README.md**: Contains recommended "Agent Stacks" (package combinations).
*   **QUICKSTART.md**: High-level overview of APM mechanics.
*   **AGENTS.md**: Generated artifact (DO NOT EDIT MANUALLY).