# Handoff: `intake` skill goals

Date: 2026-07-13
Status: aligned at goal/contract level; implementation design has not started

## Resume here

Design and create a separately invocable, general-purpose `intake` skill. Its first configured corpus is the Omni Obsidian vault, but the procedure should remain useful for other inboxes later.

Start by reading:

- `docs/create_new_skill-process.md`
- `docs/project.md`
- `~/notes/omni/AGENTS.md`
- `~/notes/omni/CONTEXT.md`
- `/tmp/handoff-omni-goals-20260712.md` if it still exists; it records the earlier intake proposal, but the decisions below supersede its skill boundary

The vault is currently the human-owned knowledge system. Do not modify it until the user approves an implementation plan and the relevant write.

## Intended outcome

Turn fleeting Markdown captures into durable understanding without making the agent an autonomous vault gardener.

The skill should take one open inbox item, help the user understand it, fill useful blind spots, and agree what it should become. Possible outcomes include:

- durable company context;
- a teaching/resource note whose depth fits the subject;
- a question or named blind spot;
- a task and later its result;
- an unresolved problem;
- reusable atomic knowledge;
- reusable email knowledge;
- a deferred capture that remains visibly unresolved.

The skill is general and should be named `intake`, not `omni-intake`. Its initial target is `~/notes/omni/inbox/`; Omni-specific destinations and rules should come from the vault's local instructions rather than being baked into the general procedure.

## Confirmed contract

```text
~/notes/omni/inbox/
  one open fleeting note
          │
          ▼
        intake
  ├── preserve what the capture actually says
  ├── explain what it appears to mean
  ├── teach missing background
  ├── research externally when useful
  ├── challenge assumptions
  ├── expose questions and blind spots
  └── propose a disposition
          │
          ▼
  user confirms destination/change
          │
          ▼
  file it, defer it, or record its durable result
```

Rules already aligned:

- Process the oldest open item first by default.
- Process exactly one item at a time and never more than one inbox item in a single assistant message.
- There is no autonomous scheduler. "Daily" is a possible human cadence, not a system behavior.
- Aim for inbox zero by repeatedly completing one item at a time.
- Teach before asking the user to gather evidence.
- Distinguish the capture's claims, agent inference, researched facts, colleague-only questions, and unresolved uncertainty.
- Research when a useful blind spot appears; preserve a source trail in any resulting teaching resource.
- Keep routine interaction terse, high-level, and atomic. Propose a teaching artifact only when it adds value; the artifact itself may be as deep as the subject requires.
- Begin with gentle challenge and become more Socratic only when needed.
- Propose a disposition and obtain confirmation before changing durable vault knowledge.
- Preserve the user's meaning and voice; do not polish rough captures into generic prose.
- Client-identifying details remain inside the vault. Any pattern promoted outside the private corpus must be anonymised and explicitly confirmed.
- The teaching behavior is expected to improve through use. The user's preferred learning style is not known yet, so the first version should make that an observable tuning point rather than pretending it is settled.

## Completion criterion for one item

One intake item is complete only when:

- its original meaning is accounted for;
- useful background or research has been supplied where needed;
- assumptions, questions, and blind spots are visible;
- a destination or deliberate deferral has been agreed;
- the agreed disposition has been applied;
- the processed source capture has moved from `inbox/` to `archive/`; if the subject is deferred, its unresolved obligation survives first as a durable question, task, or unresolved-problem note.

## Memory model

The Obsidian vault is canonical for changing knowledge. Skills contain procedures and stable constraints, not a growing copy of company facts.

```text
raw captures → intake → durable Obsidian knowledge
                            │
                            └── optional deliberate projections into skills
```

A future context skill may extract stable company principles, constraints, or language from the vault. It must remain a projection, not a competing source of truth.

## Revisions and rejected directions

- Rejected: a large `omni-work-context` skill that globally loads all company knowledge.
- Rejected: making an installed skill the primary mutable memory container.
- Revised: the earlier `omni-intake` concept is now a general `intake` procedure with the Omni vault as its first target.
- Retained from the earlier proposal: one-at-a-time processing, explicit disposition, teaching/research, confirmation before filing, and sensitivity-aware promotion.
- Not chosen: an autonomous daily job or bulk inbox processor.

## Open decisions for the next session

1. **Minimal state machine.** Decide the exact frontmatter written before a completed capture moves to `archive/`, and how the durable replacement points back to its source when useful.
2. **Disposition vocabulary.** Re-evaluate the earlier fold, promote, park, task, ask, and drop labels against the now-general skill rather than preserving them automatically.
3. **Argument/config interface.** Decide how the generic skill learns the inbox path and vault-local rules.
4. **Approval interaction.** Keep confirmation sufficient for safe writes without turning each item into a questionnaire.
5. **Evaluation after observation.** Run several real items first, then create tests from observed failures in meaning preservation, useful teaching, uncertainty separation, one-item discipline, and write confirmation.

## Evidence and source anchors

- Existing draft context skill: `~/.agents/skills/omni-work-context/SKILL.md`
- Earlier design handoff: `/tmp/handoff-omni-goals-20260712.md`
- Vault ownership and editing rules: `~/notes/omni/AGENTS.md`
- Vault capture model: `~/notes/omni/CONTEXT.md`
- Current inbox observation on 2026-07-13: `~/notes/omni/inbox/` existed and contained no files. The design has therefore not yet been tested against a real capture batch.

## Suggested skills

- `align` — confirm the unresolved lifecycle, state, and interaction decisions before implementation.
- `blind-spot-pass` — use only if new evidence changes the problem framing; the initial pass is complete.
- `writing-great-skills` reference via `docs/create_new_skill-process.md` — shape invocation, completion criteria, progressive disclosure, and evals.
- `extract-knowledge` — useful when testing whether a processed capture becomes standalone durable prose, but it should not replace the intake procedure.

## First move next session

Restate this handoff against the current vault rules, then align on the minimal state machine, disposition vocabulary, and argument/config interface before naming the skill description and designing its steps. Defer eval design until several real runs expose actual failure modes.
