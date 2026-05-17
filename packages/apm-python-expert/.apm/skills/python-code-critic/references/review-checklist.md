# Code Review Checklist

This checklist provides a structured approach to reviewing code, ensuring common issues are addressed and best practices are followed.

## General

- [ ] Code style and formatting adheres to project conventions.
- [ ] Code is readable and understandable.
- [ ] Appropriate comments are present for complex logic, but not excessive for self-explanatory code.
- [ ] Variable, function, and class names are clear, descriptive, and follow naming conventions.
- [ ] No commented-out code or dead code.
- [ ] No sensitive information (API keys, passwords, etc.) is hardcoded.

## Functionality & Logic

- [ ] Does the code meet the requirements?
- [ ] Are edge cases and error conditions handled?
- [ ] Is input validated?
- [ ] Are there potential race conditions or concurrency issues?
- [ ] Is the logic sound and efficient?

## Performance

- [ ] Are there any obvious performance bottlenecks (e.g., N+1 queries, inefficient loops)?
- [ ] Is resource usage (memory, CPU) optimized?

## Security

- [ ] Are there any known vulnerabilities (e.g., SQL injection, XSS, insecure deserialization)?
- [ ] Are proper authentication and authorization checks in place?
- [ ] Is data encrypted where necessary (in transit, at rest)?

## Testing

- [ ] Unit tests cover critical paths and edge cases.
- [ ] Integration tests are sufficient.
- [ ] Tests are clear, maintainable, and run quickly.

## Documentation

- [ ] API endpoints are documented (if applicable).
- [ ] Important design decisions are explained.
- [ ] README is updated if necessary.
