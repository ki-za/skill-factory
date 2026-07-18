---
name: intake
description: Processes one inbox capture at a time into an approved durable outcome while preserving source meaning, uncertainty, and target-local rules.
disable-model-invocation: true
argument-hint: [target-root | inbox | capture]
---

STARTER_CHARACTER = 📥

# Intake

Process one fleeting capture through a human-owned knowledge system. Keep exactly one source capture in the working set until it is completed, skipped, or the user stops. A response may discuss only that item; begin another item only through a new invocation or explicit user request after completion.

## 1. Resolve the target

Interpret the invocation argument, when present, as one of:

- a capture file: process only that file;
- an inbox directory: select its oldest open capture;
- a target root: use the inbox path declared by its local rules, otherwise `<target-root>/inbox/`.

With no argument, infer the target only when the current workspace or its local instructions identify one unambiguously. Otherwise ask for the target path in one short question.

Read the applicable instruction files from the target root through the capture's directory, plus a root `CONTEXT.md` when present. Follow any local context, templates, privacy rules, link conventions, destination rules, or ordering rules they point to. Determine the archive path from those rules; absent a rule, propose the sibling `archive/` beside the inbox. A missing destination directory belongs in the later approval bundle rather than being created now.

For oldest-first selection, use the target's declared capture timestamp. Without one, use the earliest filesystem modification time and break ties by filename. Ignore directories, hidden system files, and items local rules mark closed. State which capture was selected and why. This step is complete when one source capture, its governing rules, its inbox, and its proposed archive path are identified.

## 2. Account for the capture

Read the complete capture without changing it. Preserve its wording as evidence even when it is rough, incomplete, or already partly processed.

Build an internal ledger that separates:

- what the capture says or requests;
- facts established by the capture or target corpus;
- agent inference;
- externally researched facts and their sources;
- questions only a named person or private source can answer;
- unresolved uncertainty and assumptions.

Inspect nearby target material only where it bears directly on the capture. Teach missing background before asking the user to gather evidence. Research when a consequential blind spot can be reduced, using public non-identifying terms unless the user explicitly authorizes disclosure of private context. Preserve a source trail in any proposed teaching resource.

Challenge gently where evidence and assumptions diverge. Keep routine analysis terse; propose a deeper teaching artifact only when it would remain useful after this intake run. This step is complete when the capture's original meaning is accounted for and every consequential claim is classified in the ledger.

## 3. Propose one disposition

Choose one primary disposition and combine secondary ones only when the capture genuinely has several durable outcomes:

- **merge** — add the useful material to an existing durable note;
- **create** — create one or more durable notes or resources;
- **task** — create or update an actionable task and, later, its result;
- **question** — preserve a named question or blind spot, including who or what may answer it;
- **defer** — preserve the unresolved obligation in a durable task, question, or problem note before archiving the source;
- **archive-only** — preserve the reviewed source in the archive without creating durable knowledge.

Skipping is not a disposition: it leaves the source untouched in the inbox and ends this run incomplete. Defer never means hiding the obligation in the archive.

Present one compact proposal:

```text
Intake proposal
Source: <path>
Meaning: <faithful restatement>
Useful context: <teaching or research, only if needed>
Uncertainty: <inference, questions, and blind spots>
Disposition: <primary [+ secondary]>
Write bundle:
- Create: <paths and concise content previews, or none>
- Update: <paths and exact intended changes, or none>
- Archive: <source path> -> <archive path>
```

Use the target's standard template and linking style in proposed durable notes. Preserve the capture's voice rather than polishing it into generic prose. Client-identifying or otherwise private material stays within its permitted corpus; any anonymized promotion beyond that boundary must be separately visible in the bundle.

Ask only the highest-leverage question when a missing answer would materially change the proposal. Otherwise end with: `Approve, revise, or skip?` This step is complete when the user can see every durable mutation and its intended content before deciding.

## 4. Obtain exact approval

Treat an unambiguous approval as authorization only for the displayed write bundle. A revision, new destination, filename collision, changed source, broadened scope, or additional write invalidates that approval: show the revised bundle and obtain approval again.

Do not combine approval for multiple captures. Discussion, answers to questions, and approval of the general workflow are not approval of a write bundle. This step is complete only when the current bundle is explicitly approved, or the user chooses revise or skip.

## 5. Apply the approved bundle

Immediately before writing, re-read the source and verify that it still matches the version analyzed. If it changed, return to the proposal step.

Apply durable outputs first. Create only approved directories and files, and never overwrite a collision. Follow target-local templates and relationships. When useful, link a durable output back to its archived source using the target's link conventions.

Before moving the source, preserve its body and add or update this default namespaced frontmatter unless local rules define another archive record:

```yaml
intake:
  status: archived
  processed_at: YYYY-MM-DD
  disposition: create
  outputs:
    - path-or-link
  unresolved:
    - path-or-link
```

Use the local calendar date, the primary disposition, and `[]` for empty lists. Merge this mapping without overwriting unrelated frontmatter. The archived capture remains source evidence; archive-only means preservation, not deletion.

Move the source only after every approved durable output succeeds. Verify each resulting path and confirm the source no longer exists in the inbox. If any operation fails, stop, report the exact partial state, and obtain approval before corrective writes. This step is complete when every approved output exists and the annotated source is present only at the approved archive path.

## 6. Close the item

Report:

- the disposition applied;
- files created, updated, and moved;
- unresolved questions or obligations and where they survived;
- research sources retained;
- any partial failure or deliberate deviation from the proposal.

Do not start the next capture automatically. One item is complete only when its meaning is accounted for, useful context was supplied, consequential uncertainty is visible, the user approved the disposition, every approved write succeeded, and the processed source moved from inbox to archive.
