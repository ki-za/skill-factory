---
name: omni-email-playbook
description: Plans Omni client replies and outbound emails as confirmed specifications for handoff to email-voice.
disable-model-invocation: true
argument-hint: "[goal, email, or thread]"
---

STARTER_CHARACTER = 📨

# Omni email playbook

Turn an inbound client thread or outbound communication goal into a confirmed factual and structural specification. Keep final prose, voice, warmth, register, and formatting for the separately invoked `email-voice` skill.

Treat `~/notes/omni/playbook/` as the changing knowledge source and this skill as the procedure over it. Treat the vault as read-only until the post-confirmation storage choice explicitly authorises a write.

## 1. Frame the communication

Extract from the invocation and conversation:

- the thread or outbound context;
- the communication goal;
- the client or audience;
- any outcome or next action already requested by the user.

When a material input is missing, ask the single highest-leverage question. A request for clarification from the client can itself be the right response strategy; it is not a failure to complete the answer.

Complete this step when the communication goal and available source material are explicit, and any absent material is named.

## 2. Retrieve the playbook

Read `~/notes/omni/AGENTS.md` and any `AGENTS.md` under `~/notes/omni/playbook/` before using the corpus.

Resolve `~/notes/omni/playbook/`, then search every Markdown file beneath it recursively. Do not assume folders, filenames, `type:` values, or a fixed taxonomy. Build search terms from the client, product or tool, request route, desired outcome, and distinctive thread language. Search:

- filenames;
- body text;
- frontmatter;
- wikilinks.

Read the strongest hits, then follow a relevant wikilink or `parent:`, `resource:`, or `application:` relationship one hop when it could change the response. Inspect only task-relevant notes. Preserve note provenance, uncertainty, and client boundaries.

If the directory is missing, empty, or has no relevant hit, report that plainly and continue from the thread and authoritative research. Record the paths of notes actually used.

Complete this step when every strong retrieval hit has been checked and there is either a source list or an explicit no-corpus/no-hit result.

## 3. Route the work

Classify lightly; these labels guide reasoning rather than define a vault schema.

**Direction**

- inbound reply
- outbound message
- follow-up or holding reply

**Work route**

- MCP or integration
- troubleshooting or broken behaviour
- platform how-to or training
- Word template or export
- security or data
- scope or commercial
- discovery or proposal
- admin or relationship
- other or unclear

For each material claim or gap, assign an information posture:

- established by the thread or playbook;
- externally researchable;
- needs client clarification;
- needs user or colleague input;
- needs escalation or explicit deferral.

Separate knowns, unknowns, and assumptions. Treat granular-access guidance, conservative promises, and escalation routes from earlier skills as leads only unless the canonical playbook or another authoritative source confirms them.

Complete this step when the direction, route, knowns, unknowns, assumptions, and owner of every material gap are visible.

## 4. Resolve material gaps

Research a gap when a public, current, authoritative source can resolve it. Cite the source and calibrate confidence. Research cannot establish unstated client intent, private company decisions, commercial commitments, or unconfirmed security and platform facts.

Use this gate for every proposed inference:

1. Is it directly supported by the thread, playbook, or an authoritative source?
2. Would being wrong alter the advice, commitment, security posture, or client's next action?
3. Can the client, user, or named colleague answer it more reliably?

Infer only when support is direct and the cost of error is low. Otherwise choose a precise clarification, escalation, holding response, or explicit deferral. Apply the same standard to boilerplate: reuse stable explanations, not context-dependent claims or promises.

Stop researching when every material gap is one of:

- answered with a source;
- confirmed as non-blocking;
- assigned a clarification question;
- assigned to a named person or escalation route;
- deliberately deferred in the response.

Complete this step when no unresolved material gap is being covered by a plausible story.

## 5. Produce the email specification

Output semantic content and structure, not email prose. Use this compact shape:

```text
Email specification

Situation / goal:
Classification:
Desired client action or outcome:
Facts to state:
Unknowns, assumptions, and disposition:
Boundaries / escalations:
Core content:
Suggested structure:
Sources used:
```

Keep the specification proportional to the email. Omit an irrelevant empty field, but retain every material unknown, boundary, and source. `Core content` accounts for each point the response must communicate; `Suggested structure` gives ordering rather than drafted paragraphs. A clarification or holding response still uses the same specification.

Complete this step when the goal and desired action are explicit, every required content point is represented, every material gap has a disposition, applicable boundaries are visible, and `email-voice` could draft without inventing substance.

## 6. Confirm the handoff

Ask the user whether the specification is sufficient for `email-voice` or needs correction. Revise the complete specification after corrections so the user can inspect the whole handoff.

The playbook phase completes only after the user explicitly confirms the specification. Then direct the user to invoke `email-voice` with the accepted specification; leave that invocation and final drafting to the user.

## 7. Offer knowledge review after confirmation

Only after confirmation, check whether the session produced genuinely reusable knowledge. Skip this step when it did not.

When it did, keep the prompt subordinate to email completion:

```text
Spec accepted. One reusable item surfaced: <one-line summary>.
Store it where?

1. Inbox capture for later intake
2. Direct playbook note proposal
3. Nowhere
```

For inbox or direct-playbook storage, first prepare the proposed content and destination. Apply the vault's current `AGENTS.md` and template rules, preserve confidentiality, provenance, and uncertainty, and ask for explicit approval before writing. Make a direct playbook proposal atomic and linked without inventing a taxonomy. Treat no response as no storage.

Complete this step when the user has chosen a destination and any write made was explicitly approved in the current session.
