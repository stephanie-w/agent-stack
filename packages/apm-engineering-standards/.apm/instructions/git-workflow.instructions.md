---
description: Standardized Git branching strategies, commit message formats, and collaboration protocols for version control.
applyTo: "*"
---
## Git Workflow Standards

This document defines the daily Git workflow, branching strategy, and commit standards for this project.

> **Note:** For release preparation, changelog generation, and hotfix processes, invoke the `release-manager` skill.

### Branch Strategy

#### Main Branches

- **`main`** - Production-ready code, always deployable
- **`develop`** - Integration branch for features, pre-release testing

#### Feature Branches

- **Naming Convention**: `feature/short-description` or `feature/issue-number-description`
- **Examples**: 
  - `feature/user-authentication`
  - `feature/123-payment-integration`
- **Lifecycle**: Created from `develop`, merged back to `develop`

#### Other Branch Types

- **Bugfix**: `bugfix/issue-description` - Non-critical bug fixes

### Commit Message Standards

#### Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

#### Types

- **feat**: New feature
- **fix**: Bug fix
- **docs**: Documentation changes
- **style**: Code style changes (formatting, no logic change)
- **refactor**: Code refactoring
- **test**: Adding or updating tests
- **chore**: Maintenance tasks, dependency updates

#### Examples

```bash
feat(auth): add JWT token validation

Implement JWT token validation middleware for API endpoints.
Includes token expiration and signature verification.

Closes #123
```

### Pull Request Requirements

#### Before Creating a PR

1. **Sync with target branch**: `git pull origin develop`
2. **Run quality checks**: `just lint && just test` (or `make ...`)
3. **Update dependencies**: `uv lock --upgrade` (if needed)
4. **Ensure clean commit history**: Consider squashing commits

#### PR Template Checklist

- [ ] Code follows project standards
- [ ] Tests pass (`just test`)
- [ ] Linting passes (`just lint`)
- [ ] Documentation updated (if applicable)
- [ ] Dependencies updated in `uv.lock`
- [ ] No merge conflicts with target branch

### Feature Development Workflow

1. **Create feature branch**:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/my-feature
   ```

2. **Development cycle**:
   ```bash
   # Make changes
   git add .
   git commit -m "feat(scope): description"
   
   # Push regularly
   git push origin feature/my-feature
   ```

3. **Before PR**:
   ```bash
   # Sync with develop
   git checkout develop
   git pull origin develop
   git checkout feature/my-feature
   git rebase develop
   
   # Quality checks
   just lint
   just test
   ```

4. **Create PR**: Target `develop` branch

### Git Configuration

#### Required Git Hooks

Add to Makefile or justfile:
```makefile
setup-hooks:
	@echo "Setting up Git hooks..."
	cp .githooks/pre-commit .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit
```

### Best Practices

#### Do's

- Write clear, descriptive commit messages
- Keep commits atomic (one logical change per commit)
- Rebase feature branches before merging
- Use `git pull --rebase` to avoid merge commits
- Delete merged branches promptly

#### Don'ts

- Don't commit directly to `main` or `develop`
- Don't force push to shared branches
- Don't commit large binary files
- Don't commit sensitive information (secrets, keys)
- Don't merge without code review

### Integration with Project Tools

#### Task Runner Integration (justfile/Makefile)

```makefile
git-setup:
	git config --local core.hooksPath .githooks
	
pre-commit:
	uv run ruff check .
	uv run pytest
```
