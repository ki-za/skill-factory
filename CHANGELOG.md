# Changelog

## 2026-07-13

- Added separate continuation handoffs for the general `intake` skill, the recreated `omni-email-playbook`, and the vault-local Omni playbook knowledge directory.
- Recorded the aligned memory, skill-boundary, email-specification, research, and post-handoff knowledge-promotion decisions.
- Documented the complete Omni knowledge-loop design and grounded evals in observed real-world runs.
- Added a single orchestration handoff for building the intake skill, vault-local playbook, and Omni email specification skill in parallel isolated Herdr tabs.

## 2026-07-12

- Made the repository-facing guidance agent-agnostic while retaining Claude/Anthropic docs as high-quality reference material.
- Added `SETUP.md` as a fresh-user setup checklist.
- Updated `./skills` to default global installs to `~/.agents/skills/` with environment-variable overrides.
- Added the draft `practices/blind-spot-pass` skill for evidence-backed orientation before brainstorming or implementation.
- Added three eval prompts and assertions covering repository work, unfamiliar-domain research, and missing-context interviewing.
- Updated `quick_validate.py` to accept the documented Claude Code frontmatter controls and added regression coverage.
