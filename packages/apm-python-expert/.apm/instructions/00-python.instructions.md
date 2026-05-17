---
description: Technical specifications and best practices for Python development, including dependency management with uv, project structure, and code quality.
---
## Python Project Standards

This document defines the **technical specifications** for Python projects. For operational protocols and agent behaviors, refer to `AGENTS.md`.


### 1. Python Version Requirements

- **Minimum Version**: 3.13+
- **Compatibility**: Ensure compatibility with latest features (e.g., Type Parameter Syntax).

### 2. Dependency Management (uv)

- **Manager**: `uv` is the exclusive project manager.
- **Build Backend**: `hatchling` (configured in `pyproject.toml`).
- **Locking**: `uv.lock` is the source of truth for reproducible builds.

#### Standard Commands

```bash
uv init --lib                         # Initialize
uv add <pkg>                          # Add dependency
uv add --dev <pkg>                    # Add dev dependency
uv add --dev <pkg> --script <script>  # Add dependency to a script
uv sync                               # Sync environment
uv run <cmd>                          # Execute in venv
```

#### Dependency Organization (`pyproject.toml`)

- **Production**: Keep minimal.
- **Development**:
  - `ruff` (Linting)
  - `mypy` (Typing)
  - `pytest`, `pytest-cov` (Testing)

### 3. Project Organization

#### File Structure (src-layout)

```
project/
├── pyproject.toml         # Configuration
├── justfile               # Primary Task runner (preferred)
├── Makefile               # Legacy Task runner
├── src/
│   └── <package>/         # Source code
│       ├── __init__.py
│       ├── core           # Domain Logic (no external I/O if possible)
│       ├── utils
│       ├── __about__.py   # Versioning
│       └── main.py        # Entrypoint
├── tests/                 # Tests (mirrors src structure)
└── README.md
```

#### Standard Task Targets (justfile/Makefile)

All projects must implement these targets in their `justfile` (or `Makefile` for legacy):

- `install` - Install dependencies via `uv sync`.
- `install-dev`  - Install package and dev dependencies using `uv sync`
- `run` - Execute the application.
- `run-dry-run` - Execute the application in dry-run mode 
- `fix` - Fix formatting and linting issues.
- `check` - Run all quality checks (formatting, linting, types)
- `typecheck` - run `mypy`
- `test` - Run `pytest`.
- `test-fast` - Run fast tests only (skips slow markers)
- `clean` - Remove build artifacts and caches.

#### Application Entrypoint

Define in `pyproject.toml`:

```toml
[project.scripts]
app = "src.main:main"
```

Execution: `just run` or `uv run app`.

### 4. Code Quality Standards

#### Linting & Formatting (Ruff)

- **Line Length**: 88 chars.
- **Quotes**: Double quotes.
- **Imports**: Sorted automatically by Ruff.

#### Import Conventions

- **Third-party/stdlib**: Absolute imports (e.g., `from pydantic import BaseModel`).
- **Local imports**: Relative imports (e.g., `from . import foo` or `from ..core import X`).
- **Ordering**: stdlib → third-party → local (with blank lines between groups).
- **Type annotations**: Use `from __future__ import annotations` for forward references.
- **No wildcard imports**: Avoid `from module import *`.
- **Lazy imports**: Import heavy dependencies inside functions when not needed at module load time.
- **Explicit exports**: Use `__all__` to define the public API.

#### Type Checking (MyPy)

- **Strict Mode**: Mandatory.
- **No Implicit Optional**: True.
- **Disallow Untyped Defs**: True.

#### Testing (Pytest)

- **Coverage**: Minimum 72%.
- **Organization**: Functional grouping (e.g., `TestUserAuth`).
- **Markers**: `unit`, `integration`, `slow`.

### 5. Implementation Patterns

#### Module Structure

Use Google-style docstrings and complete type hints.

```python
def calculate_metric(data: list[float]) -> float:
    """Calculates the primary metric.

    Args:
        data: A list of input values.

    Returns:
        The calculated metric.

    Raises:
        ValueError: If data is empty.
    """
    if not data:
        raise ValueError("Data cannot be empty")
    return sum(data) / len(data)
```

#### Error Handling

- **Specific exceptions**: Catch specific exception types, not broad ones.
- **No bare except**: Never use `except Exception:` without logging or re-raising.
- **Log before re-raising**: Log the error before re-raising to preserve context.
- **Reraise correctly**: Use `raise` without arguments to preserve the original traceback.

```python
try:
    risky_operation()
except ValueError as e:
    logger.warning("Invalid value: %s", e)
    raise from e
```

#### Context Managers

Use `with` statements or `@contextmanager` for resource cleanup (files, connections, locks).

```python
with open("data.txt") as f:
    data = f.read()
## File automatically closed

## Or for custom resources:
from contextlib import contextmanager

@contextmanager
def managed_connection():
    conn = create_connection()
    try:
        yield conn
    finally:
        conn.close()
```

#### Configuration & Logging

- **Config**: Use `pydantic-settings` or `os.environ`.
- **Logging**: Use `logging` module. Levels: `DEBUG`, `INFO`, `WARNING`, `ERROR`.

#### Data Models (Pydantic)

Use Pydantic for all data models, input validation, and structured data exchange.

##### Core Principles

- **Strict Typing**: Always use `Field` with explicit constraints rather than relying on type coercion.
- **Validation**: Use `model_validator` for cross-field validation.
- **Serialization**: Leverage `model_dump` and `model_validate` for serialization/deserialization.

##### Basic Model

```python
from pydantic import BaseModel, ConfigDict, Field
from datetime import datetime


class User(BaseModel):
    id: int
    name: str = Field(min_length=1, max_length=100)
    email: str
    created_at: datetime
    is_active: bool = True

    model_config = ConfigDict(extra="ignore")
```

##### Nested Models

```python
from pydantic import BaseModel, Field


class Address(BaseModel):
    street: str
    city: str
    zip_code: str = Field(pattern=r"^\d{5}$")


class UserProfile(BaseModel):
    user: User
    address: Address
    bio: str | None = None
```

##### Configuration Models

```python
from pydantic import BaseModel, Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class DatabaseConfig(BaseModel):
    host: str = "localhost"
    port: int = Field(ge=1, le=65535)
    name: str


class AppSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="APP_", env_file=".env")

    database: DatabaseConfig
    debug: bool = False
    log_level: str = "INFO"
```

##### Strict Mode

Enable strict mode for security-sensitive models:

```python
from pydantic import BaseModel, ConfigDict


class SecureConfig(BaseModel):
    model_config = ConfigDict(strict=True)

    api_key: str
    secret: str
```

##### Validation Helpers

- Use `Field` for constraints: `min_length`, `max_length`, `ge`, `le`, `pattern`, `regex`
- Use `validator` (v1 style) or `model_validator` (v2) for complex validation
- Use `BeforeValidator` for preprocessing input data

### 6. Strict Anti-Patterns (The "Do Not Use" List)
Violating these rules will result in rejected code.

#### 🚫 Code Structure
- **No Mutable Defaults**: `def foo(items=[])` is forbidden. Use `items=None`.
- **No Broad Exceptions**: `except Exception:` without logging or re-raising is forbidden.
- **No Global State**: Do not rely on or modify global variables. Pass state explicitly.
- **No Magic Numbers**: Define constants with descriptive names (e.g., `MAX_RETRIES = 3` instead of just `3`).

#### 🚫 Typing (Modern Python 3.10+)
- **No `typing.List`, `typing.Dict`, etc.**: Use built-in generics (e.g., `list[str]`, `dict[str, int]`).
- **No `typing.Optional`**: Use the union operator `X | None`.
- **No `typing.Union`**: Use the `|` operator (e.g., `int | str`).

#### 🚫 Observability
- **No `print()` Statements**: Use the standard `logging` module or `structlog`. `print()` is for CLI output only, not debugging.
- **No Silent Failures**: Errors must be explicitly handled or bubbled up.

### 7. Tech Stack Summary
- **Minimum Version**: 3.13+
- **Manager**: `uv` (Command: `uv run ...`)
- **Task Runner**: `just` (Preferred) or `make` (Legacy)
- **Linter/Formatter**: `ruff`
- **Type Checker**: `mypy` (Strict mode)
- **Testing**: `pytest`

