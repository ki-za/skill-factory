# Changelog

## 2026-07-12

- Made the repository-facing guidance agent-agnostic while retaining Claude/Anthropic docs as high-quality reference material.
- Added `SETUP.md` as a fresh-user setup checklist.
- Updated `./skills` to default global installs to `~/.agents/skills/` with environment-variable overrides.
- Added the draft `practices/blind-spot-pass` skill for evidence-backed orientation before brainstorming or implementation.
- Added three eval prompts and assertions covering repository work, unfamiliar-domain research, and missing-context interviewing.
- Updated `quick_validate.py` to accept the documented Claude Code frontmatter controls and added regression coverage.
