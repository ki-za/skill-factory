# Handoff: parallel Omni knowledge-loop build

Date: 2026-07-13
Status: goals aligned; implementation not started

## Objective

Use Herdr to run three coordinated workstreams in separate tabs:

1. build the general `intake` skill;
2. establish the vault-local Omni playbook corpus;
3. recreate `omni-email-playbook` as an email-specification skill.

This document is an orchestration index. The goals and constraints live in the referenced artifacts below; read them rather than copying their content into spawn prompts or new plans.

## Authoritative paths

Read in this order:

- Repo rules: `AGENTS.md`
- Skill-creation process: `docs/create_new_skill-process.md`
- Repo purpose and structure: `docs/project.md`, `docs/map.md`
- Shared sequence and current status: `PLAN.md`
- Durable architecture decisions: `DECISIONS.md`

Workstream contracts:

- Intake: `docs/handoff/intake-skill-goals-20260713.md`
- Omni vault playbook: `docs/handoff/omni-playbook-vault-goals-20260713.md`
- Omni email specification: `docs/handoff/omni-email-playbook-goals-20260713.md`

Live corpus and local constraints:

- Vault rules: `~/notes/omni/AGENTS.md`
- Vault context: `~/notes/omni/CONTEXT.md`
- Vault note template: `~/notes/omni/templates/standard.md`
- Existing style boundary: `~/.agents/skills/email-voice/SKILL.md`

Source evidence, not authority:

- `~/.agents/skills/omni-work-context/SKILL.md`
- `~/.agents/skills/omni-email-playbook/SKILL.md`
- `/tmp/handoff-omni-goals-20260712.md` if it still exists

## Lead responsibilities

The lead agent owns coordination and integration:

- run `./update-docs` once before skill authoring, then make the refreshed baseline available to both skill worktrees;
- present the three-tab ownership plan before spawning if the user has not already approved it;
- create isolated Git worktrees for the two skill-factory builders;
- keep `PLAN.md`, `DECISIONS.md`, `CHANGELOG.md`, and `docs/handoff/` lead-owned;
- collect category, invocation, name, and description proposals required by `docs/create_new_skill-process.md`;
- obtain user approval before any vault write;
- integrate worker outputs, run validation, and resolve cross-workstream contracts;
- do not design evals until several real runs have exposed actual failure modes.

The user has already approved parallel Herdr tabs and same-session approved writes. This does not authorize unreviewed vault edits.

## Workstream ownership

### Tab: `intake`

Owns an isolated skill-factory worktree and only the eventual `intake` skill directory plus description iterations in that worktree's `playground/`.

Read `docs/handoff/intake-skill-goals-20260713.md`. Design the generic skill and its interface with vault-local rules. Do not edit the live Omni vault; propose any required vault contract to the lead and playbook worker. Do not add imagined evals.

Done for the parallel build phase when the skill passes mechanical validation and its remaining live-run assumptions are named.

### Tab: `omni-playbook`

Owns `~/notes/omni/playbook/**` and any explicitly approved minimal `inbox/` or `archive/` substrate. It does not edit skill-factory output skills.

Read `docs/handoff/omni-playbook-vault-goals-20260713.md` and the vault's `AGENTS.md` before proposing changes. Start with the smallest useful linked structure; avoid a speculative taxonomy. Every live vault write requires explicit user approval.

Done for the parallel build phase when the approved corpus foundation supports one client context, one route/principle, and retrieval by the email skill without becoming an autonomous vault garden.

### Tab: `omni-email`

Owns a second isolated skill-factory worktree and only the eventual `omni-email-playbook` skill directory plus description iterations in that worktree's `playground/`.

Read `docs/handoff/omni-email-playbook-goals-20260713.md` and the existing `email-voice` skill. Build against the agreed path `~/notes/omni/playbook/`, but do not invent the playbook taxonomy or edit the vault. Preserve the confirmed-specification handoff and post-confirmation knowledge-review gate. Do not add imagined evals.

Done for the parallel build phase when the skill passes mechanical validation and can be integrated against the corpus worker's retrieval surface.

## Conflict controls

- Never run both skill builders in the same Git working tree.
- Workers do not commit shared planning, decision, changelog, map, or handoff files.
- Workers do not install skills globally or replace the current personal source skills.
- The vault worker is the only worker allowed to propose edits under `~/notes/omni/playbook/`.
- The intake worker may specify a vault interface but cannot implement it concurrently.
- The email worker consumes the playbook path contract but cannot choose its information architecture.
- The lead integrates; workers report paths changed, validation commands, assumptions, and blockers.

## Herdr launch shape

First confirm the session is Herdr-managed:

```bash
test "${HERDR_ENV:-}" = 1
herdr pane list
herdr workspace list
```

Use `git-worktrees` to create one isolated worktree for `intake` and another for `omni-email-playbook`. The vault tab may use the vault repository directly because it owns a separate repository and path surface.

Create three named tabs in the current workspace, parsing each returned root-pane ID rather than guessing IDs:

```bash
herdr tab create --workspace <workspace-id> --label intake
herdr tab create --workspace <workspace-id> --label omni-playbook
herdr tab create --workspace <workspace-id> --label omni-email
```

For each returned root pane, start the configured agent from its owned worktree or vault directory, then send a short prompt pointing to this handoff and the workstream-specific handoff. Fresh agents do not inherit the lead's conversation, so paths, ownership, done criteria, and write restrictions must be explicit.

Monitor with:

```bash
herdr pane list
herdr wait agent-status <pane-id> --status done --timeout <milliseconds>
herdr pane read <pane-id> --source recent-unwrapped --lines 100
```

Re-read pane IDs before control operations because Herdr IDs may compact. Keep the lead tab available for user approvals and integration.

## Integration gate

Do not call the parallel wave complete merely because three workers finish. The lead must verify:

- both skills follow the current repo authoring process and pass `quick_validate.py`;
- `intake` remains generic and reads target-local rules;
- the corpus remains canonical and human-owned;
- `omni-email-playbook` retrieves from the corpus and outputs a user-confirmed specification rather than final prose;
- `email-voice` remains unchanged;
- no worker performed an unapproved vault write or global installation;
- all assumptions requiring real use remain visible;
- `git diff --check` passes in every touched repository.

After integration, run several real intake and email cases before designing evals.

## Current external state

At handoff creation, the skill-factory working tree contains uncommitted alignment refinements to `PLAN.md`, `DECISIONS.md`, `CHANGELOG.md`, and the three workstream handoffs. Inspect `git status` and `git diff` before creating worktrees or refreshing docs. The parent nix-dots repository also has an approved edit to `home/.pi/agent/AGENTS.md` adding the recurring-process question: what would make this annoying enough that the user would stop using it after a week?

A concurrent commit already created the three workstream handoffs: `df784cd` (`Document Omni intake and email workflow handoffs`). Preserve it.

## Suggested skills

- `herdr` — create, monitor, and coordinate the separate tabs; check `HERDR_ENV=1` first.
- `git-worktrees` — isolate the two skill-factory builders so parallel edits and commits cannot collide.
- `launching-agent-teams` — apply its role decomposition, rich spawn-prompt, approval, and integration principles; use Herdr tabs rather than Claude's experimental team runtime.
- `align` — resolve each workstream's remaining non-obvious design decisions before implementation.
- `context-management` — checkpoint before spawning and compact completed worker investigations before integration.
- `extract-knowledge` — useful when turning approved intake or email discoveries into standalone atomic notes; it does not replace either target skill.
