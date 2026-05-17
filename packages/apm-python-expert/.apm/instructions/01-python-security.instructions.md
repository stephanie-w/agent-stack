---
description: "Guidelines and checklist for identifying and preventing security vulnerabilities in Python code."
---
## Python Security Standard

This document defines the **security requirements and audit checklists** for Python development.

### 🛡️ Core Security Principles

1.  **Least Privilege**: Processes should run with the minimum permissions necessary.
2.  **Defense in Depth**: Use multiple layers of security (e.g., input validation + parameterization).
3.  **Fail Securely**: Error messages should not leak sensitive information.
4.  **Trust Nothing**: Treat all external input (API calls, files, user input) as malicious.

### 🚫 Critical Anti-Patterns (Security Risks)

#### 1. Insecure Deserialization
- **NEVER** use `pickle.load()` on untrusted data. It can execute arbitrary code.
- **NEVER** use `yaml.load()` (use `yaml.safe_load()` instead).
- **NEVER** use `jsonpickle` on untrusted sources.

#### 2. Arbitrary Code Execution
- Avoid `eval()`, `exec()`, and `input()` (in Python 2, though we use 3.13+).
- Be extremely cautious with `getattr()` and `setattr()` on objects controlled by user input.

#### 3. Command Injection
- Use `subprocess.run(args, ...)` with a list of arguments, **NOT** a string with `shell=True`.
- If `shell=True` is absolutely necessary, use `shlex.quote()` to escape inputs.

#### 4. SQL Injection
- Always use parameterized queries (e.g., `cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))`).
- **NEVER** use string formatting (f-strings, `%`, `.format()`) to build queries.

#### 5. Insecure Cryptography
- Never use weak hashing algorithms like `md5` or `sha1` for security-sensitive data.
- Use `hashlib.sha256` or higher, or specialized libraries like `bcrypt` for passwords.
- Use `secrets` module instead of `random` for cryptographic purposes (tokens, salts).

### 🔍 Security Audit Checklist

#### Injection
- [ ] Is `shell=True` used in `subprocess`?
- [ ] Are SQL queries built using string concatenation/formatting?
- [ ] Is user input passed directly to OS commands?

#### Data Handling
- [ ] Is `pickle` or `yaml.load()` used?
- [ ] Are there hardcoded secrets, API keys, or passwords?
- [ ] Is sensitive data (PII, tokens) logged?
- [ ] Is Pydantic used with `strict=True` for security-critical inputs?

#### Web & API
- [ ] Is CORS configured too broadly (`*`)?
- [ ] Are there missing authentication/authorization checks on sensitive endpoints?
- [ ] Is `DEBUG = True` in production?

#### Filesystem
- [ ] Are temporary files created insecurely (e.g., `tempfile.mktemp()`)?
- [ ] Is there potential for Path Traversal (e.g., `open(user_provided_path)`)?

### 🛠️ Recommended Security Tools
- **Static Analysis**: `bandit` (specifically for security issues).
- **Vulnerability Scanning**: `pip-audit`, `safety`.
- **Linting**: `ruff` (with security-related rules enabled).
- **Secrets Detection**: `detect-secrets`, `gitleaks`.
