# Security Policy

The AIBOS Enterprise framework is built on **Security by Design**, **Privacy by
Design** and **Zero Trust** principles. See
[`00_ROOT/AIBOS_SECURITY_STANDARD.md`](00_ROOT/AIBOS_SECURITY_STANDARD.md) for the
full security baseline.

## Supported Versions

| Version | Supported |
|---------|:---------:|
| 2.0.x   | Yes       |
| < 2.0   | No        |

## Reporting a Vulnerability

Please **do not** open a public issue for security vulnerabilities.

Instead, report privately using GitHub's
[private vulnerability reporting](https://docs.github.com/en/code-security/security-advisories/guidance-on-reporting-and-writing-information-about-vulnerabilities/privately-reporting-a-security-vulnerability)
on this repository (Security → Report a vulnerability), or contact the
maintainers directly.

When reporting, please include:

- A description of the issue and its potential impact.
- Steps to reproduce or a proof of concept.
- Affected files, versions or configurations.
- Any suggested remediation.

## Response Targets

| Stage | Target |
|-------|--------|
| Acknowledgement | Within 3 business days |
| Initial assessment | Within 10 business days |
| Remediation plan | Communicated after triage |

## Disclosure

We follow coordinated disclosure. Please allow us reasonable time to remediate
before any public disclosure.

## Scope

As a documentation-and-prompts repository, the most relevant risks are:

- Accidental exposure of secrets or credentials in committed content.
- Prompt-injection or unsafe-automation guidance that contradicts the
  `AIBOS_AI_BEHAVIOUR_STANDARD.md`.
- Broken or misleading security guidance.

No secrets, credentials or personal data should ever be committed.
