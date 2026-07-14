# Handoff: `omni-email-playbook` goals

Date: 2026-07-13
Status: aligned at goal/contract level; implementation design has not started

## Resume here

Recreate `omni-email-playbook` as a separately invocable skill whose output is a confirmed **email specification**, not final prose.

Start by reading:

- `docs/create_new_skill-process.md`
- `docs/project.md`
- `docs/handoff/omni-playbook-vault-goals-20260713.md`
- `~/notes/omni/AGENTS.md`
- `~/.agents/skills/omni-email-playbook/SKILL.md` as evidence, not authority
- `~/.agents/skills/email-voice/SKILL.md` to preserve the boundary
- `/tmp/handoff-omni-goals-20260712.md` if it still exists, for prehistory only

Do not rewrite `email-voice`. It is mature and intentionally separate.

## Intended outcome

Given either:

- a goal to send a message to a client; or
- an inbound client email/thread plus a response goal,

the skill retrieves relevant Omni playbook knowledge, works out what the response needs to accomplish, researches missing facts when appropriate, and produces a factual/structural specification that the user can hand to `email-voice`.

The playbook should support boilerplate and repeated support responses, but its deeper role is response strategy: route the request, surface uncertainty, avoid inventing client intent, and define the core content before prose styling begins.

## Confirmed lifecycle

```text
client message/thread + response goal
                │
                ▼
      omni-email-playbook
        ├── retrieve relevant playbook knowledge
        ├── classify the request or outbound goal
        ├── identify knowns, unknowns, and assumptions
        ├── research if necessary
        ├── clarify rather than infer missing client intent
        ├── define the purpose and desired action
        ├── define the core content
        ├── apply escalation/commitment boundaries
        └── produce an email specification
                │
                ▼
       user confirms specification is sufficient
                │
                ├──► user invokes email-voice with the specification
                │
                └──► playbook offers an optional knowledge review
                       ├── add a capture to inbox for later intake
                       ├── write directly to the vault playbook
                       └── do not store
```

The optional knowledge review happens only after the email specification has been accepted. It is not allowed to distract from getting the client response ready. It may happen alongside the user's separate `email-voice` pass.

## Ownership boundary

`omni-email-playbook` owns:

- the communication goal;
- request/outbound classification;
- retrieval from `~/notes/omni/playbook/`;
- factual orientation;
- knowns, unknowns, and assumptions;
- targeted research;
- clarification strategy;
- core content and response structure;
- reusable boilerplate selection;
- escalation, security, commercial, and promise boundaries;
- the final email specification.

`email-voice` owns:

- final prose;
- the user's established voice;
- register, warmth, rhythm, and formatting;
- rewriting the accepted specification into an email draft.

The user owns:

- confirming the specification;
- manually invoking `email-voice`;
- the final edit and sending;
- deciding whether crystallised knowledge should be stored and where.

## Strategic clarification principle

A major reason for recreating this skill is to correct a recurring failure mode: inferring a client's intent when the email does not provide enough information.

A clarification response such as "I'm not quite sure what you mean here; could you explain further?" is a valid strategic outcome. The playbook should prefer a precise clarifying question over completing a plausible but unsupported story.

This does not eliminate research. The skill should first distinguish:

- information the playbook or thread already establishes;
- facts the agent can research;
- intent or company-specific facts only the client, user, or colleague can supply.

## Research branch

If the core content cannot be specified from the thread and existing playbook knowledge, research before proposing the email specification. Research findings should be sourced and confidence-calibrated.

Research does not license guessing about:

- the client's unstated outcome;
- private company decisions;
- commercial commitments;
- platform/security facts not confirmed by an authoritative source.

## Completion criterion

The playbook phase is complete only when:

- the communication goal and desired client action are explicit;
- all required core content is accounted for;
- knowns, unknowns, and assumptions are separated;
- needed research has been completed or a deliberate clarification/escalation chosen;
- relevant playbook knowledge and boundaries have been applied;
- the response structure is explicit;
- the email specification is sufficient for `email-voice`;
- the user has confirmed that specification.

Only after this gate may the skill suggest preserving reusable knowledge.

## Memory and retrieval model

The Obsidian vault is canonical. `omni-email-playbook` is a procedure over the vault-local retrieval surface at `~/notes/omni/playbook/`.

The skill should contain stable procedural constraints. It should not accumulate the changing company corpus in `SKILL.md`.

Any reusable knowledge discovered during an email session must be offered after specification confirmation, with an explicit destination choice every time:

- inbox for later `intake` processing;
- direct playbook write when already crystallised;
- no storage.

## Revisions and rejected directions

- Rejected: treating the existing skill's contents as a finished specification. It was created in an unreliable session and is evidence only.
- Rejected: combining this skill with `email-voice`.
- Rejected: making this skill primarily a style/drafting guide.
- Rejected: storing reusable knowledge before the email work is complete.
- Rejected: automatically invoking or composing user-invoked skills. The user manually hands the accepted specification to `email-voice`.
- Revised: the playbook may produce a structured email specification rather than a polished draft.
- Revised: research is an explicit phase when existing information is insufficient.
- Added: clarification-over-inference is a first-class response strategy.
- Retained from the old draft as evidence to validate: request classification, granular-access teaching, conservative promises, and escalation boundaries. None should be copied uncritically; confirm them against the canonical vault/company evidence during implementation.

## Open decisions for the next session

1. **Email specification schema.** Define the smallest useful handoff shape for `email-voice` without turning it into a bureaucratic form.
2. **Invocation description.** Decide the concise user-facing description and whether arguments should accept a goal, pasted email, thread path, or any combination.
3. **Retrieval method.** Decide how the skill searches and selects atomic vault notes from the playbook directory.
4. **Classification vocabulary.** Re-evaluate the old request-shape table against real support emails rather than preserving it automatically.
5. **Research stopping rule.** Define when enough is known to specify the email, clarify, or escalate.
6. **Knowledge-review prompt.** Decide how to offer inbox/direct-playbook/no-storage without pulling attention away from `email-voice`.
7. **Boilerplate boundary.** Distinguish safe reusable phrasing from context-dependent claims and commitments.
8. **Examples and privacy.** Decide how full client-specific examples, sanitised examples, and distilled patterns participate in retrieval.
9. **Evaluation after observation.** Use several real email-specification runs first, then derive cases from observed failures; likely branches include underspecified client intent, researchable facts, colleague-only unknowns, routine boilerplate, outbound messages, and the post-confirmation storage gate.

## Evidence and source anchors

- Existing playbook draft: `~/.agents/skills/omni-email-playbook/SKILL.md`
- Existing style skill: `~/.agents/skills/email-voice/SKILL.md`
- Existing general work-context draft: `~/.agents/skills/omni-work-context/SKILL.md`
- Earlier goals/design handoff: `/tmp/handoff-omni-goals-20260712.md`
- Vault rules: `~/notes/omni/AGENTS.md`
- Related LibreChat/MCP technical reference: `~/.agents/skills/librechat-fluency/SKILL.md`

The earlier handoff says mining 5–10 strong sent replies was blocked on user action. That remains useful source work, but examples should feed the canonical vault playbook rather than become an ever-growing skill body.

## Suggested skills

- `align` — settle the specification schema, retrieval flow, and non-obvious research/storage gates.
- `email-voice` — inspect during design and use after a specification is confirmed; do not merge its responsibilities.
- `librechat-fluency` — use when an email requires LibreChat/OmniChat technical research.
- `blind-spot-pass` — invoke again only if real email examples reveal a different problem framing.
- `writing-great-skills` reference via `docs/create_new_skill-process.md` — design predictable stages and checkable completion criteria.

## First move next session

Collect two or three representative email cases: one routine/boilerplate, one underspecified request requiring a clarifying question, and one needing research or escalation. Use them to align on the email-specification shape before writing the skill.
