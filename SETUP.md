# Setup

Use this checklist when opening this repository for the first time.

## 1. Install prerequisites

- Git
- Python 3.11+
- [`uv`](https://docs.astral.sh/uv/) for running the helper scripts

## 2. Clone the repository

```bash
git clone https://github.com/lexler/skill-factory.git
cd skill-factory
```

If you are working from a fork, replace the URL with your fork URL.

## 3. Read the local orientation files

```bash
cat AGENTS.md
cat docs/project.md
cat docs/map.md
```

`AGENTS.md` is the agent-agnostic project guide. Anthropic and Claude-specific documents remain in `docs/knowledge/` because they are useful source material, not because this repo requires Claude.

## 4. Check the skill registry

```bash
./skills status
```

The helper discovers skills under `output_skills/` and reports which ones are installed globally.

## 5. Install skills when you want them available

Global install symlinks selected skills into `~/.agents/skills/` by default:

```bash
./skills toggle
# or
./skills install tdd
```

Local install copies a selected skill into the current project's `.agents/skills/` directory:

```bash
./skills local install tdd
```

If your agent harness uses a different skill directory, set `AGENT_SKILLS_DIR` for global installs:

```bash
AGENT_SKILLS_DIR="$HOME/.claude/skills" ./skills install tdd
```

## 6. Create or edit skills

Ask your agent to follow `docs/create_new_skill-process.md`. New skills should be saved under:

```text
output_skills/<category>/<skill-name>/SKILL.md
```

## 7. Validate a skill before sharing

```bash
uv run --with pyyaml docs/knowledge/anthropic-skill-creator/scripts/quick_validate.py output_skills/<category>/<skill-name>
```

## 8. Refresh upstream reference docs when needed

```bash
./update-docs
```

This fetches Anthropic skill documentation into `docs/knowledge/anthropic-skill-docs/`. Review diffs after running it because those files are vendored reference material.
