---
description: "Guidelines for managing polyglot fullstack monorepos with backend and frontend separation."
---
## Fullstack Monorepo Standard (Backend & Frontend)

This document defines the architecture and orchestration for fullstack monorepos that separate **backend** (typically Python) and **frontend** (typically TypeScript/React) logic. This structure is designed for independent development cycles within a unified repository.

### 1. Directory Structure

The repository must follow a clean separation of concerns at the root level.

```text
monorepo/
├── backend/               # Python (FastAPI/Flask) - Managed with uv
│   ├── src/
│   ├── pyproject.toml
│   └── justfile           # Backend-specific tasks
├── frontend/              # Node.js (React/Vue) - Managed with npm/yarn/pnpm
│   ├── src/
│   ├── package.json
│   └── justfile           # Frontend-specific tasks
├── shared/                # Shared resources (e.g., OpenAPI schemas)
├── justfile               # Root-level orchestration (The "Glue")
└── .env                   # Shared environment configuration
```

### 2. Root Orchestration (`justfile`)

The root `justfile` is mandatory. It acts as the unified entry point for agents to manage both stacks simultaneously.

```justfile
## [setup] Install all dependencies for both stacks
install:
    cd backend && uv sync
    cd frontend && npm install

## [run] Start the entire stack in development mode
dev:
    @just --is-background backend-dev
    @just --is-background frontend-dev

## [run] Backend only
backend-dev:
    cd backend && just run

## [run] Frontend only
frontend-dev:
    cd frontend && npm run dev

## [quality] Run all checks across the monorepo
check-all:
    cd backend && just check
    cd frontend && npm run lint
```

### 3. Communication Protocols

- **Schema-First**: Use shared OpenAPI or JSON Schema to ensure frontend and backend are in sync. The `shared/` directory should house these contracts.
- **Environment**: Use a single `.env` at the root for shared variables (e.g., `API_PORT`, `DB_URL`), then symlink or reference it in the sub-directories.

### 4. Agent Operational Rules

1.  **Independent Stacks**: Always change into the specific stack directory (`backend/` or `frontend/`) before executing tool-specific commands (e.g., `npm install` must be run in `frontend/`).
2.  **Verify Both**: Changes to the backend API MUST be followed by verification of the frontend to ensure no breaking changes were introduced (checking API client generation, types, etc.).
3.  **Root-First Access**: Agents should first look at the **root justfile** to understand how the project is orchestrated before diving into sub-folders.
4.  **No Leaky Dependencies**: Never import frontend assets into the backend or vice-versa. Use the `shared/` directory for any truly common data or schemas.
