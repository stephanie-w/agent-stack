---
description: "Guidelines for managing Python monorepos using uv workspaces and namespace packages."
---
## Python Monorepo Standard (Namespaces)

This document defines the architecture and operational protocols for Python monorepos utilizing **uv workspaces** and **namespace packages**. This structure is preferred for large-scale engineering projects where multiple independent but related packages reside in a single repository.

### 1. Directory Structure

A Python monorepo must follow the `uv` workspace pattern with a central `pyproject.toml` at the root and individual packages in a `packages/` (or `libs/`, `services/`) directory.

```text
monorepo/
├── pyproject.toml         # Root workspace configuration
├── uv.lock                # Unified lockfile for the entire workspace
├── justfile               # Root-level orchestration
├── packages/
│   ├── core/              # Shared logic (e.g., myorg.core)
│   │   ├── pyproject.toml
│   │   └── src/myorg/core/
│   ├── api/               # API service (e.g., myorg.api)
│   │   ├── pyproject.toml
│   │   └── src/myorg/api/
└── tests/                 # Shared or package-specific tests
```

### 2. Workspace Configuration (`pyproject.toml`)

The root `pyproject.toml` must explicitly define the workspace members.

```toml
[tool.uv.workspace]
members = ["packages/*"]

[tool.uv.sources]
## Ensure packages can find each other locally
myorg-core = { workspace = true }
```

### 3. Namespace Packages

Use **native namespace packages** (PEP 420). 
- Do **NOT** include an `__init__.py` in the top-level namespace directory (e.g., `src/myorg/`).
- Include `__init__.py` only in the leaf package directory (e.g., `src/myorg/core/`).

### 4. Task Orchestration (`justfile`)

The root `justfile` should delegate commands to packages or run them workspace-wide.

```justfile
## Run checks across all workspace members
check-all:
    uv run ruff check .
    uv run mypy packages/

## Run a specific package
run package:
    uv run -p {{package}} start
```

### 5. Agent Operational Rules

1.  **Unified Lockfile**: Always run `uv sync` from the root to update the global `uv.lock`. Never create per-package lockfiles.
2.  **Cross-Package Changes**: When modifying a shared core package, the agent MUST verify downstream dependencies by running tests in the dependent packages.
3.  **Dependency Addition**: Add dependencies to specific packages using `uv add --package <name> <dep>`.
4.  **Imports**: Use absolute imports following the namespace (e.g., `from myorg.core.models import User`).
