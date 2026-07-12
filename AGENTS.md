This file provides guidance to agents when working with code in this repository.

This repo was originally meant for Claude, but treat it as agent agnostic. Keep Claude/Anthropic guidance when it is useful source material; write new repo-facing guidance for agents generally.

## Purpose

This repository creates skills. Read `docs/project.md` for goals and workflow.

## Common Commands

```bash
./update-docs    # Fetch latest Anthropic skill documentation
./skills status  # List discovered skills and global install state
```

## Fresh Setup

Fresh users should follow `SETUP.md` before creating or installing skills.

## Repository Structure

See `docs/map.md` for complete structure and file descriptions.

## Creating skills

When the user asks to create a new skill, follow instructions in `docs/create_new_skill-process.md`. Do not invoke the skill-creator skill — this project has its own process that supersedes it.
