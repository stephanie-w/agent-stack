---
name: python-security-auditor
description: Specialized skill for conducting deep security audits of Python codebases, identifying vulnerabilities like injection, insecure deserialization, and secrets exposure.
---

# Python Security Auditor Skill

This skill enables you to perform systematic security audits of Python code. You will act as a senior security researcher, identifying risks and providing actionable remediation guidance based on the `Python Security Standard`.

## Core Capabilities

1.  **Vulnerability Scanning:** Identify high-risk patterns (Injection, Insecure Deserialization, etc.).
2.  **Data Flow Analysis:** Trace untrusted input from sources to sensitive sinks.
3.  **Secrets Detection:** Locate hardcoded credentials, tokens, and API keys.
4.  **Remediation Planning:** Generate structured security reports with fix recommendations.
5.  **Compliance Check:** Validate code against `40_Resources/standards/security/python-security.md`.

## Workflow

### 1. Initiation & Scope
The audit begins when a user asks to "audit", "check security", or "find vulnerabilities" in specific files or a directory.

### 2. Automated/Pattern-Based Scanning
Use `grep_search` to find immediate "red flags" defined in the `Python Security Standard`:
- `shell=True`
- `pickle.load`
- `yaml.load` (without SafeLoader)
- `eval(`, `exec(`
- Hardcoded strings that look like keys (e.g., `API_KEY = "..."`)

### 3. Detailed Manual Review
For identified high-risk files:
1.  **Read the code:** Use `read_file` to understand the context.
2.  **Trace Inputs:** Identify where external data (API params, file reads, user input) enters the system.
3.  **Verify Sinks:** Check if that data reaches a "sink" (database query, shell command, file system) without proper sanitization or parameterization.

### 4. Reporting Findings
Create a security report (either in the chat or as a new file `SECURITY-AUDIT.md`) using the following structure:

- **Vulnerability**: (e.g., SQL Injection)
- **Severity**: (Low | Medium | High | Critical)
- **Location**: (File and Line Number)
- **Description**: Technical explanation of the risk.
- **Remediation**: Specific code example of how to fix it.

### 5. Verification
If the user applies a fix, re-run the audit on the modified section to ensure the vulnerability is resolved and no new issues were introduced.

## Security Guidelines
- **Confidentiality**: Never log or repeat actual secrets found during the audit. Refer to them by their variable name or location only.
- **Precision**: Avoid false positives by verifying if a "dangerous" function is actually reachable by untrusted input.
- **Standards-Based**: Always ground findings in the `40_Resources/standards/security/python-security.md`.
