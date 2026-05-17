---
name: release-manager
description: Executes release workflows, including changelog generation, version bumping, and hotfix deployments. Use when preparing a new release or patching production.
applyTo: "*"
---
# Release Manager Skill

Use this skill when the user asks to prepare a new software release, generate or update a changelog, or execute an emergency hotfix deployment.

## 1. Changelog Management

### Changelog Format

Follow [Keep a Changelog](https://keepachangelog.com/) format:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- New features

### Changed
- Changes in existing functionality

### Deprecated
- Soon-to-be removed features

### Removed
- Removed features

### Fixed
- Bug fixes

### Security
- Security improvements

## [1.2.0] - 2024-01-15

### Added
- User authentication system
- JWT token validation

### Fixed
- Database connection timeout issue
```

### Generating Changelog for Release

1. **Review commits since last release**:
   ```bash
   git log v1.1.0..develop --oneline --pretty=format:"%h %s"
   ```

2. **Categorize changes** based on commit types:
   - `feat:` → **Added**
   - `fix:` → **Fixed**
   - `refactor:`, `perf:` → **Changed**
   - `security:` → **Security**
   - Breaking changes → **Changed** (with migration notes)

3. **Update CHANGELOG.md**:
   - Move items from `[Unreleased]` to new version section
   - Add release date
   - Create new empty `[Unreleased]` section

### Automated Changelog Generation

If automated changelog generation tools are installed:

```bash
# Generate changelog
uv run auto-changelog --template keepachangelog
```

## 2. Release Process

Follow these steps to safely cut a new release.

1. **Create release branch**:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b release/vX.Y.Z
   ```

2. **Prepare release**:
   - Update version numbers in config files (e.g., `pyproject.toml`, `package.json`).
   - Generate and update `CHANGELOG.md`.
   - Run final testing (`just test`, `just lint`).
   - Commit the version bump and changelog update.

3. **Merge to main**:
   ```bash
   git checkout main
   git merge release/vX.Y.Z
   git tag vX.Y.Z
   git push origin main --tags
   ```

4. **Merge back to develop**:
   ```bash
   git checkout develop
   git merge release/vX.Y.Z
   ```

## 3. Hotfix Process

Use this process for emergency fixes directly to production (`main`).

1. **Create hotfix branch**:
   ```bash
   git checkout main
   git pull origin main
   git checkout -b hotfix/critical-fix-name
   ```

2. **Apply fix and test**:
   ```bash
   # Make fix
   just test
   git commit -m "fix: critical issue description"
   ```

3. **Merge to main and develop**:
   ```bash
   # To main
   git checkout main
   git merge hotfix/critical-fix-name
   # Bump patch version tag
   git tag vX.Y.Z+1 
   git push origin main --tags
   
   # To develop
   git checkout develop
   git merge hotfix/critical-fix-name
   ```
