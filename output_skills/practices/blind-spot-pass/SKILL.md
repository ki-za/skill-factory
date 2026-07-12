---
name: blind-spot-pass
disable-model-invocation: true
description: Run a blind-spot pass on a rough goal before brainstorming or implementation.
---

STARTER_CHARACTER = 🧭

# Blind-Spot Pass

Use this as an entrance guide into unfamiliar territory. The user has a real goal, but it is not shaped enough to safely brainstorm, prototype, plan, or build.

The pass answers: **Are we pointed at the right problem, and what must we understand before choosing a direction?** It reveals the landscape; it does not select a solution.

## 1. Gather the starting context

Treat a rambling voice transcript as useful raw material. Extract what is present and ask for what is missing. Interview one question at a time, prioritizing the answer most likely to change the direction.

Establish enough of:

- the goal as currently stated
- the problem or opportunity behind it
- intended users, stakeholders, or audience
- the user's experience with the domain and codebase
- constraints: time, technology, budget, policy, compatibility, or taste
- evidence already observed
- approaches, references, or assumptions already considered
- what success would look like

Do not turn this into exhaustive requirements gathering. Stop the interview when the context is sufficient to inspect the landscape and identify direction-changing uncertainty. This step is complete when every missing context item that could materially change the pass is either answered or explicitly marked unknown.

## 2. Inspect the landscape

Use available evidence before relying on generic advice.

For work in a repository, inspect the relevant code, documentation, tests, history, existing patterns, and nearby features. For unfamiliar domain work, do targeted research into established approaches, quality criteria, common pitfalls, historical context, and meaningful alternatives. Prefer primary sources, respected references, mature implementations, and user-provided examples.

Research only enough to give the user an entranceway into the territory. Report sources and observations. Label interpretations as inferences and unresolved claims as unknowns. A concern without evidence may be raised as a hypothesis, never as a fact.

Describe established approaches and their tradeoffs when they clarify the landscape. Keep the work diagnostic: do not generate a menu of new solutions or start brainstorming interventions. This step is complete when the relevant territory has been inspected broadly enough to expose its major concepts, quality bar, pitfalls, and forks.

## 3. Check the direction

Compare the current goal with the landscape:

- Is it addressing the underlying problem or only a visible symptom?
- Do the intended users and success criteria fit the problem?
- Which assumptions are carrying the most weight?
- What evidence supports the current direction, and what evidence is missing?
- What would make this the wrong landscape entirely?
- Which constraints or existing patterns make the goal substantially different from the generic case?

Surface plausible reframings as questions or alternatives in problem framing, not as solutions. Keep the user's decision-making authority. This step is complete when the report makes clear whether the goal is currently well-directed, under-shaped, or pointed at a potentially different problem.

## 4. Map the forks and blind spots

Start high-level, then become granular. Identify the choices and uncertainties that could change the problem framing, architecture, user experience, cost, feasibility, safety, or success measure. Prioritize by consequence, not by how easy a question is to ask.

For each important item, state:

- **Fork** — what could branch
- **Why it matters** — what changes downstream
- **Current signal** — evidence, assumption, or absence of evidence
- **Question** — what would resolve it
- **Status** — answered, deferred, or open

Include unknown unknowns that the user may not know to ask about: what good looks like, common failure modes, historical decisions, domain vocabulary, hidden stakeholders, and constraints that only appear in practice. Every item must either be grounded in inspected evidence or clearly marked as a hypothesis.

This step is complete when every surfaced uncertainty that could change the direction is answered, deliberately deferred, or visible to the user.

## 5. Return a layered report

Use this order so the user gets orientation before detail:

1. **What I heard** — the current goal, problem, users, and constraints.
2. **Landscape** — the concepts, established approaches, quality bar, and pitfalls the user should know before choosing.
3. **Direction check** — whether the current goal appears well-directed, under-shaped, or potentially misframed, with reasons.
4. **Major forks** — the high-consequence branches.
5. **Granular blind spots** — the lower-level questions and practical potholes.
6. **Evidence ledger** — observed facts, inferences, hypotheses, and sources.
7. **Bottom line** — what is clear now, what remains decision-blocking, and what the user may choose to do next.

The bottom line is a decision aid, not a forced recommendation. Invite the user to clarify, investigate a particular fork, provide a reference, reframe the goal, or proceed to brainstorming when they judge the entranceway sufficient. Continue the conversation if their answers expose new direction-changing uncertainty.

The pass is complete when the user can see the landscape, the important forks, and the remaining decision-making gaps without mistaking speculation for knowledge. Keep solutions, prototypes, implementation plans, and implementation work for the next phase.
