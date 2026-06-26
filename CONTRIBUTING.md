# Contributing to AIBOS Enterprise

Thank you for your interest in improving the AI Business Operating System. This
repository is documentation-as-code: every contribution is treated as an
engineering artefact and must meet the AIBOS standards.

## Before You Start

1. Read [`00_ROOT/AIBOS_ROOT_SPECIFICATION.md`](00_ROOT/AIBOS_ROOT_SPECIFICATION.md) —
   it takes precedence over every other document.
2. Review the [`AIBOS_STYLE_GUIDE.md`](00_ROOT/AIBOS_STYLE_GUIDE.md),
   [`AIBOS_DOCUMENT_SCHEMA.md`](00_ROOT/AIBOS_DOCUMENT_SCHEMA.md) and
   [`AIBOS_NAMING_STANDARD.md`](00_ROOT/AIBOS_NAMING_STANDARD.md).
3. Use terminology defined in the
   [`AIBOS_ENTERPRISE_GLOSSARY.md`](00_ROOT/AIBOS_ENTERPRISE_GLOSSARY.md); do not
   redefine established terms.

## Standards Checklist

Every change MUST:

- Use British English and RFC 2119 keywords (MUST, SHOULD, MAY).
- Follow `UPPER_SNAKE_CASE.md` filenames and `kebab-case` directory names.
- Keep cross-references valid and avoid duplicating existing content.
- Apply [Semantic Versioning](https://semver.org) and update version history.
- Pass Markdown linting (`.markdownlint.json`) and link checks.

## Branching

Use the naming convention defined in `AIBOS_NAMING_STANDARD.md`:

```text
feature/<name>
bugfix/<name>
hotfix/<name>
release/<version>
docs/<topic>
```

## Commits

This repository follows [Conventional Commits](https://www.conventionalcommits.org/):

```text
<type>(<optional scope>): <description>

[optional body]

[optional footer]
```

Common types: `feat`, `fix`, `docs`, `refactor`, `chore`, `ci`, `test`.

Examples:

- `docs(root): clarify context loading order`
- `feat(phase-05): add data engineering skill prompt`

## Pull Requests

1. Fork the repository and create a topic branch.
2. Make focused, atomic changes.
3. Update `ROOT_INDEX.md` and `CHANGELOG.md` where applicable.
4. Ensure CI passes.
5. Complete the pull request template and request review.

## Validation

Refer to [`AIBOS_VALIDATION_STANDARD.md`](00_ROOT/AIBOS_VALIDATION_STANDARD.md).
Publication requires **no Critical issues and no Errors**, complete metadata,
valid cross-references and an updated version.

## Code of Conduct

By participating, you agree to uphold our
[Code of Conduct](CODE_OF_CONDUCT.md).
