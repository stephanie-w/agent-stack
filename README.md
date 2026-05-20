# Agent Package Manager (APM) Stacks

Welcome to the APM Monorepo. This repository contains a collection of composable agent primitives (skills, prompts, instructions, and agents) designed to be installed via the Agent Package Manager (`apm`).

Instead of monolithic, "do-everything" packages, these packages are segmented by **layer** and **flavor**. This allows developers to compose their exact agent environment based on the nature of their project and their current task while avoiding contradictory instructions.

## Project Structure

The monorepo is organized into five logic layers, each containing a core package and optional "flavor" sub-packages.

```text
packages/
├── apm-agent-ops/               # THE "BEHAVIOR" LAYER
│   ├── .apm/
│   │   ├── instructions/        # Base: Agent Safety & Integrity
│   │   ├── prompts/             # code-mentor
│   │   └── skills/              # ask-user, code-mentor
│   ├── standard/                # FLAVOR: High Rigor Ops
│   ├── rapid/                   # FLAVOR: High Velocity Ops
│   └── tones/                   # FLAVORS: Agent Communication Style
│       ├── caveman/             # Ultra-minimal token usage
│       └── standard/            # Balanced context and brevity

│
├── apm-core-meta/               # THE "HOW TO AGENT" LAYER
│   └── .apm/
│       ├── prompts/             # discover-standards, inject-standards, index-standards
│       └── skills/              # reflect, make-skill, improve-codebase-architecture, discover-standards, inject-standards, index-standards
│
├── apm-engineering-standards/   # THE "BASE" LAYER
│   ├── .apm/
│   │   ├── instructions/        # Base: Git Workflow
│   │   ├── prompts/             # commit, create-pr, review-pr, onboard-developer, analyze-bug
│   │   └── skills/              # Release Manager, task-management
│   ├── full/                    # FLAVOR: Stateful Task Tracking
│   └── basic/                   # FLAVOR: Checklist Task Tracking
│
├── apm-python-expert/           # THE "DOMAIN & STRUCTURE" LAYER
│   ├── .apm/
│   │   ├── agents/              # Personas: API Architect, Security Auditor, Backend Developer
│   │   ├── instructions/        # Python & Python Security standards
│   │   └── skills/              # Code Critic, Security Auditor
│   ├── fullstack/               # FLAVOR: Polyglot Monorepo
│   └── workspace/               # FLAVOR: uv Workspace
│
└── apm-product-discovery/       # THE "UPSTREAM" LAYER
    └── .apm/
        ├── agents/              # Persona: POC Architect
        ├── instructions/        # Base: Product Strategy Protocols
        ├── prompts/             # write-a-prd, grill-me, plan-product, shape-spec, prd-to-issues
        └── skills/              # write-a-prd, prd-to-issues, plan-product, shape-spec
```

## The Layered Architecture

To prevent "context bloat" and ensure agents only load the rules they need, the packages are divided into five distinct layers. Some layers offer **flavors**—mutually exclusive sub-packages for different development philosophies.

1. **`apm-agent-ops`**: The "Behavior" layer. Core operational rules, safety protocols, and conversational patterns.
   - *Flavors*: `standard` (High Rigor) vs `rapid` (High Velocity).
2. **`apm-core-meta`**: The "How to Agent" layer. Meta-skills for agents to index standards, self-improve, or critique architecture.
3. **`apm-engineering-standards`**: The "Base" layer. Universal rules for Git, releases, and task tracking.
   - *Flavors*: `full` (Stateful tracking) vs `basic` (Simple checklists).
4. **`apm-python-expert`**: The "Domain & Structure" layer. Language-specific depth (Security, FastAPI) and project layout rules.
   - *Flavors*: `fullstack` (Polyglot) vs `workspace` (Pure Python workspaces).
5. **`apm-product-discovery`**: The "Upstream" layer. Idea-to-code tools (PRD writing, Grill Me).

---

## Development & Authoring Standards

To maintain a high-quality, composable ecosystem, all contributors must follow these standards.

### 1. Package Organization
*   **Layering**: Place primitives in the most generic layer possible. Universal rules go in `engineering-standards`; meta-rules go in `core-meta`.
*   **Flavors**: If two rulesets are mutually exclusive (e.g., Fast vs. Rigorous), move them into `flavor/` sub-directories with their own `apm.yml`.
*   **Zero-Padding**: Use numeric prefixes for instruction files (e.g., `00-base.md`, `01-security.md`) to control concatenation order during `apm compile`.

### 2. Writing Instructions (`.instructions.md`)
*   **Composability**: Always start titles with `##` (H2). APM folds multiple files into one; H2 prevents broken header hierarchies in the final `AGENTS.md`.
*   **Frontmatter**: Must include a `description` (one-line summary) and `applyTo` (glob pattern or `"*"` for global).
*   **Scope**: Use instructions for **Policies** ("The Laws of the Repo"). Keep them concise to avoid context bloat.
*   **Mutual Exclusivity**: Never place contradictory instructions (e.g., two different tones or operational paces) in the same directory. Always use nested flavor packages to force the user to select exactly one via `apm.yml`.

### 3. Writing Agents (`.agent.md`)
*   **Persona-Driven**: Use agents for **Specializations** ("The Expert"). Define "Who" the agent is, what tools it has access to, and what model it should use.
*   **Hierarchy**: Use `##` (H2) for the agent title.
*   **Capability**: Use the `tools:` field to restrict or grant tool access (e.g., allowing `read` but denying `shell`).

### 4. Writing Prompts (`.prompt.md`)
*   **Hybrid Pattern**: Use prompts as "Entry Points" for complex skills. A prompt should be a thin wrapper that uses `LOAD <skill_name>` to trigger a multi-resource skill.
*   **Parameterization**: Use `${input:variable_name}` to make prompts executable via the CLI (`apm run ... --param variable_name="..."`).
*   **Intent**: A prompt should represent a single, actionable workflow (e.g., `write-a-prd`).

### 5. Writing Skills (`/skills/`)
*   **Encapsulation**: Put logic that requires scripts, templates, or heavy reference material into a skill folder.
*   **Structure**: A skill must have a `SKILL.md`. Optional directories include `scripts/`, `templates/`, `assets/`, and `references/`.
*   **Auto-Discovery**: Skills are auto-discovered by agents when the folder is in the context; keep the `SKILL.md` description high-signal.

---

## Common Agent Stacks (Use Cases)

Developers configure their `apm.yml` by selecting the layers and flavors that match their scenario.

### 1. The "Repo Initializer" (Day 0)
**Goal:** Scaffold a fresh repository and establish structural boundaries.

```yaml
# apm.yml
dependencies:
  apm:
    # Choose your repo structure flavor
    - stephanie/apm-python-expert/workspace
    
    # Discovery tools and high-rigor operational standards
    - stephanie/apm-core-meta
    - stephanie/apm-agent-ops/standard
```

### 2. The "Daily Driver" (Day N)
**Goal:** Always-on guardrails and style enforcement for production development.

```yaml
# apm.yml
dependencies:
  apm:
    # Base Git flow + Rich, stateful task tracking
    - stephanie/apm-engineering-standards
    - stephanie/apm-engineering-standards/full
    
    # Domain rules for Python
    - stephanie/apm-python-expert
    - stephanie/apm-agent-ops/standard
```

### 3. The "Junior / Onboarding" Stack
**Goal:** Maximum guidance and an interactive mentor.

```yaml
# apm.yml
dependencies:
  apm:
    - stephanie/apm-engineering-standards
    - stephanie/apm-engineering-standards/full
    - stephanie/apm-python-expert
    - stephanie/apm-agent-ops # Includes 'code-mentor' skill
```

### 4. The "Senior / Proof of Concept" Stack
**Goal:** Speed and minimal friction.

```yaml
# apm.yml
dependencies:
  apm:
    # Upstream planning tools (write-a-prd, grill-me)
    - stephanie/apm-product-discovery
    
    # High-velocity operational mode + simple task checklists
    - stephanie/apm-agent-ops/rapid
    - stephanie/apm-engineering-standards/basic
```

### 5. The "Code Surgeon / Security Audit" Stack
**Goal:** Deep debugging or compliance checking.

```yaml
# apm.yml
dependencies:
  apm:
    # Deep security scans
    - stephanie/apm-python-expert/.apm/skills/python-security-auditor/SKILL.md
    
    # Architectural critique skill
    - stephanie/apm-core-meta/.apm/skills/improve-codebase-architecture/SKILL.md
```

---

## Installation

To add a package or flavor to your project:

```bash
# Install a core layer
apm install stephanie/apm-engineering-standards

# Install a specific flavor (sub-package)
apm install stephanie/apm-engineering-standards/full

# Install a specific primitive
apm install stephanie/apm-python-expert/.apm/agents/api-architect.agent.md
```

For more details on APM, refer to the official documentation.