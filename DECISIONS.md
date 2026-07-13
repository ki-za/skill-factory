# Decisions

- 2026-07-12: Make repo-facing docs and install defaults agent-agnostic while keeping Claude/Anthropic materials as vendored/reference guidance.
- 2026-07-12: Use `~/.agents/skills/` as the default global install target, with `AGENT_SKILLS_DIR` and `PROJECT_AGENT_SKILLS_DIR` overrides for harness-specific layouts.
- 2026-07-12: Create `blind-spot-pass` as a user-invoked practice that checks the direction of a rough goal before solutions, using context gathering, targeted territory research, and layered uncertainty mapping.
- 2026-07-12: Keep the pass diagnostic rather than solution-generating; the user decides whether to clarify, reframe, research further, or proceed.
- 2026-07-12: Treat the documented Claude Code frontmatter controls as valid extensions alongside the Agent Skills standard fields in the repository validator.
- 2026-07-13: Use the Omni Obsidian vault as the canonical changing knowledge store; skills contain procedures and stable constraints, while any future context skill is a deliberate projection.
- 2026-07-13: Replace the proposed mutable `omni-work-context` skill with a general, separately invoked `intake` skill whose first target is the Omni vault inbox.
- 2026-07-13: Keep `omni-email-playbook` separate from `email-voice`: the playbook produces a user-confirmed email specification, then the user manually invokes the voice pass.
- 2026-07-13: Store reusable communication knowledge in a vault-local `playbook/` directory as atomic linked notes, and consider promotion only after the email specification is confirmed.
