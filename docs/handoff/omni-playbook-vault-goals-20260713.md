# Handoff: Omni Obsidian playbook directory

Date: 2026-07-13
Status: directory role aligned; information architecture and implementation have not started

## Resume here

Design a vault-local communication playbook at:

```text
~/notes/omni/playbook/
```

This is not a new repository and not a giant context skill. It is part of the existing Omni Obsidian vault and should be usable as an agent working directory with local instructions.

Start by reading:

- `~/notes/omni/AGENTS.md`
- `~/notes/omni/CONTEXT.md`
- `~/notes/omni/templates/standard.md`
- `docs/handoff/omni-email-playbook-goals-20260713.md`
- `docs/handoff/intake-skill-goals-20260713.md`
- `/tmp/handoff-omni-goals-20260712.md` if it still exists, for the previous context only

Do not create or reorganise vault notes until the user approves the design and relevant changes.

## Intended outcome

Create a human-owned, durable retrieval surface for Omni client communication knowledge. It should hold and link the material that makes repeated support work easier:

- routing knowledge;
- boilerplate responses;
- response strategies;
- confirmed company principles and constraints;
- client relationship/context notes;
- reusable atomic knowledge;
- support examples and annotations;
- screenshots and product references;
- requirements and opportunities discovered through client requests.

The directory should be useful both to the user in Obsidian and to an agent launched from that directory.

## Canonical-memory decision

The Obsidian vault is the single source of truth for changing company knowledge used by these workflows.

```text
Omni vault
├── inbox/       raw/fleeting captures awaiting intake
├── playbook/    curated communication retrieval surface
└── wider notes  company, technical, client, project, and learning context
```

Skills are procedures. They may contain stable constraints necessary to perform their jobs, but the knowledge accumulated over time belongs in the vault.

A future extracted company-context skill may contain selected stable principles, constraints, or language. Such a skill is a deliberate projection from the vault, not an independent authority.

## Confirmed relationship to the skills

```text
inbox/ ──► intake ──► durable/atomic vault knowledge
                          │
                          └──► playbook entries when appropriate

client goal/thread ──► omni-email-playbook
                          │
                          ├── retrieves from playbook/
                          └── produces confirmed email specification
                                      │
                                      ├──► email-voice
                                      └──► optional knowledge promotion
```

- `intake` may route processed knowledge into the playbook when confirmed.
- `omni-email-playbook` reads the playbook while producing an email specification.
- After specification confirmation, `omni-email-playbook` may ask whether newly crystallised knowledge goes to the inbox, directly to the playbook, or nowhere.
- `email-voice` does not own this corpus; it only turns an accepted specification into prose.

## Information-shape decision

Start **route-first**, but do not impose a rigid database-like record schema on every note.

The vault is Zettelkasten-oriented. Playbook entries should usually be atomic ideas connected with Obsidian wikilinks. Useful note shapes may include:

- a request or support route;
- a response principle;
- a reusable explanation;
- a boilerplate fragment;
- a client-specific relationship/context note;
- a platform fact;
- an escalation boundary;
- an annotated example;
- a newly discovered requirement or service opportunity.

A client email often reveals more than a response pattern: it may expose a platform requirement, a new offer, an unresolved product problem, or important relationship context. The playbook should permit links to those wider vault notes rather than forcing everything into an email-entry template.

The earlier proposal that every entry must carry situation, goal, facts, structure, boilerplate, caveats, source, and anonymisation metadata was rejected as too rigid. Provenance and sensitivity still matter, but the note shape should fit the atomic idea.

## Provisional directory shape

The following is an orientation aid, not a confirmed folder taxonomy:

```text
~/notes/omni/playbook/
├── AGENTS.md
├── routes/
├── patterns/
├── examples/
├── principles/
└── references/
```

The user accepted the directory contract but prefers atomic linked notes. Before creating subdirectories, test whether a flatter structure with wikilinks and parent relationships better matches the vault's existing conventions.

## Local agent contract

A playbook-local `AGENTS.md` should extend, not replace, `~/notes/omni/AGENTS.md`.

The intended local behavior is:

- inspect, retrieve, compare, and propose freely within the task;
- preserve client confidentiality;
- distinguish client-specific context from reusable general knowledge;
- prefer anonymised reusable patterns when promoting beyond a client note;
- preserve provenance and uncertainty;
- ask before creating or changing playbook entries;
- avoid treating every drafted email as reusable knowledge;
- use vault frontmatter, wikilinks, and human-readable note names;
- keep the playbook useful to the human rather than optimising it solely for agents.

The local directory can be opened as an agent workspace. That does not make it an autonomous publisher or vault gardener.

## Revisions and rejected directions

- Rejected: a separate company-context repository.
- Rejected: an `omni-work-context` skill as the main mutable memory container.
- Rejected: a separate email-playbook repository.
- Chosen: the existing Omni Obsidian vault is the corpus, with `playbook/` inside it.
- Chosen: playbook knowledge is retrieved when needed instead of globally loaded across unrelated sessions.
- Chosen: atomic linked notes over a mandatory all-fields entry schema.
- Chosen: client-specific notes are legitimate because relationship context matters; reusable knowledge should be extracted and linked where appropriate.
- Chosen: client requests may generate product requirements, service opportunities, and broader knowledge, not only email boilerplate.
- Deferred: extracting mature, stable design principles or company constraints into a future skill.

## Open decisions for the next session

1. **Flat versus foldered structure.** Test the provisional folders against the vault's preference for links and `parent:` relationships.
2. **Playbook root note.** Decide whether a human-facing map/entry note is useful or would violate the vault's "no autonomous index notes" posture without explicit approval.
3. **Local `AGENTS.md`.** Align exact read/write permissions and whether same-session explicit approval is sufficient for edits.
4. **Client material boundary.** Decide what may live as client-specific notes, what requires sanitisation, and what should never enter `playbook/`.
5. **Screenshots/assets.** Define storage, naming, sensitivity, and linking conventions.
6. **Provenance.** Find the lightest way to retain source/confidence without imposing one large template on every atomic note.
7. **Staleness.** Decide how uncertain, superseded, or review-needed knowledge is marked.
8. **Routing.** Determine whether routes are notes, metadata, links, or a mix, and whether request type, response goal, or both drive retrieval.
9. **Versioning.** Confirm whether ordinary vault Git history is sufficient; no separate repository is currently intended.
10. **Initial migration.** Identify what, if anything, should be extracted from the existing `omni-work-context` and `omni-email-playbook` drafts into canonical vault notes.

## Evidence and source anchors

- Vault rules: `~/notes/omni/AGENTS.md`
- Vault context and capture philosophy: `~/notes/omni/CONTEXT.md`
- Vault template: `~/notes/omni/templates/standard.md`
- Existing context draft: `~/.agents/skills/omni-work-context/SKILL.md`
- Existing email playbook draft: `~/.agents/skills/omni-email-playbook/SKILL.md`
- Existing style skill: `~/.agents/skills/email-voice/SKILL.md`
- Earlier design handoff: `/tmp/handoff-omni-goals-20260712.md`

The existing vault already contains Omni orientation, communication, MCP, onboarding, project, and client-adjacent notes. Inspect only relevant notes before proposing a structure; do not bulk reorganise them.

## Suggested skills

- `align` — decide flat versus foldered structure, local permissions, provenance, and privacy boundaries.
- `blind-spot-pass` — use again only if inspecting real vault notes exposes a different corpus boundary.
- `extract-knowledge` — useful for turning a confirmed email-session insight into standalone atomic prose before filing.
- `omni-email-playbook` — once recreated, use it to test retrieval against representative communication cases.
- `intake` — once created, use it to test promotion from a fleeting capture into linked playbook knowledge.

## First move next session

Inspect a small representative sample of existing Omni notes and the standard template. Then propose the smallest playbook structure that supports one real support route, one client-specific context note, one reusable principle, and one example without introducing a premature taxonomy.
