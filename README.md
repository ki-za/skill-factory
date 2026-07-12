# Skill Factory

Creates portable Agent Skills with built-in best practices from Anthropic's official documentation and other skill-authoring references.

## Why Skills?

Agents cannot hold everything in mind at once. Skills solve that by releasing task-specific information gradually:

1. **Startup**: only name + description are loaded
2. **When triggered**: full `SKILL.md` instructions are loaded
3. **As needed**: references load only when the task requires them

This keeps context lean while making rich knowledge available on demand.

**Skills vs slash commands**:
- Skills are usually model-invoked: the agent applies them when relevant based on frontmatter and linked instructions.
- Slash commands are user-invoked prompts (`/command`).

## Quick Start

Fresh users should run through [SETUP.md](SETUP.md) first.

1. Open this folder in your agent harness
2. Ask it to create a new skill
3. Answer a few questions — point to references or ask the agent to search online
4. Find your skill in `output_skills/[category]/[skill-name]/`

## Using Your Skill

This repo includes a `./skills` helper script for installation.

**Global** (all projects) — symlink selected skills into `~/.agents/skills/` by default:

```bash
./skills toggle    # interactive picker
./skills status    # check what's installed
```

Set `AGENT_SKILLS_DIR` if your harness uses another directory, for example `~/.claude/skills`.

Edits to `output_skills/` apply immediately when the installed skill is a symlink.

**Local** (single project) — copy the skill folder to the current project's `.agents/skills/` directory:

```bash
./skills local install tdd
./skills local status
```

Set `PROJECT_AGENT_SKILLS_DIR` if your project-level skill directory differs.

## Claude and Anthropic Material

This repository is agent-agnostic, but it keeps high-quality Claude Code and Anthropic guidance as reference material:

- `docs/knowledge/anthropic-skill-docs/` contains fetched Anthropic docs.
- `docs/knowledge/anthropic-skill-creator/` contains Anthropic's skill-creator/eval infrastructure.
- Claude-specific notes remain where they describe Claude-only behavior.

When writing portable skills, prefer `AGENTS.md`, `.agents/skills/`, and neutral wording such as “agent” unless the behavior is Claude-specific.

## STARTER_CHARACTER

Some skills define `STARTER_CHARACTER = [emoji]` near the top. This is a visual indicator that an agent has loaded the skill and is following its instructions. For example, the nullables skill uses ⭕️ and TDD uses 🔴/🌱/🌀.

If your harness supports global behavioral instructions, you can add a rule like:

```text
Always start replies with STARTER_CHARACTER + space (default: 🍀). Stack emojis when requested, don't replace.
```

Claude Code users can put that rule in global `~/.claude/CLAUDE.md`; other harnesses should use their equivalent global instruction file.

## Updating Best Practices

```bash
./update-docs
```

Pulls latest skill patterns from Anthropic.

## Structure

```text
docs/           — Skill creation knowledge and patterns
output_skills/  — Generated skills organized by category
SETUP.md        — Fresh-user setup checklist
```
