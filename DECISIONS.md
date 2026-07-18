# Decisions

- 2026-07-12: Make repo-facing docs and install defaults agent-agnostic while keeping Claude/Anthropic materials as vendored/reference guidance.
- 2026-07-12: Use `~/.agents/skills/` as the default global install target, with `AGENT_SKILLS_DIR` and `PROJECT_AGENT_SKILLS_DIR` overrides for harness-specific layouts.
- 2026-07-12: Create `blind-spot-pass` as a user-invoked practice that checks the direction of a rough goal before solutions, using context gathering, targeted territory research, and layered uncertainty mapping.
- 2026-07-12: Keep the pass diagnostic rather than solution-generating; the user decides whether to clarify, reframe, research further, or proceed.
- 2026-07-12: Treat the documented Claude Code frontmatter controls as valid extensions alongside the Agent Skills standard fields in the repository validator.
- 2026-07-13: Use the Omni Obsidian vault as the canonical store for changing company, client, and playbook knowledge; skills hold procedures and stable constraints, and any future context skill is a deliberate projection.
- 2026-07-13: Replace the proposed mutable `omni-work-context` rewrite with a generic, separately invoked `intake` skill whose first target is the Omni vault.
- 2026-07-13: Process intake oldest-first and one item per assistant message, writing only approved durable outcomes before moving the source capture to `archive/`.
- 2026-07-13: Keep intake interaction terse while allowing teaching artifacts to be as deep as their subjects require.
- 2026-07-13: Store reusable communication knowledge in a vault-local `playbook/` directory as atomic linked notes, including client-specific context under `playbook/clients/`.
- 2026-07-13: Define `omni-email-playbook` as a research-and-reasoning skill that produces a user-confirmed email specification; the user then invokes `email-voice` as a separate prose/style pass.
- 2026-07-13: Offer reusable-knowledge filing only after the email specification is confirmed, with Zack choosing inbox, direct playbook write, or no storage each time.
- 2026-07-13: Ground evals in observed failures after several real runs rather than inventing them before the first implementation.
- 2026-07-13: Build the intake skill, Omni vault playbook, and Omni email skill in parallel Herdr tabs, isolating the two skill builders in separate worktrees and leaving shared files and integration to the lead.
