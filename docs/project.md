# Skill Factory Project

## Overview

The Skill Factory is a repository designed to efficiently create and organize portable Agent Skills. It serves as both a knowledge base for skill creation and a structured output directory for completed skills.

## Goals

1. **Efficient Skill Creation**: Provide all necessary documentation and knowledge for AI agents to create high-quality skills
2. **Organization**: Maintain a clean, easy-to-navigate structure for all created skills
3. **Automation**: Support automated workflows for fetching documentation and generating skills

## Key Components

### Documentation (`docs/`)
Contains all instructional material needed to create skills:
- Official Anthropic documentation on skill creation
- Agent-agnostic project guidance
- Best practices and patterns
- Quick-start guides

### Output Directory (`output_skills/`)
Stores completed skills organized by category, each skill in its own folder.

## Workflow

1. Agent reads documentation from `docs/knowledge/`
2. Agent creates new skill following best practices
3. Skill is saved to `output_skills/[category]/[skill-name]/`
4. Process repeats for additional skills

## Fresh User Setup

New users should start with the root-level `SETUP.md` checklist before creating or installing skills.

## Future Enhancements

- Skill templates and generators
- Validation and testing workflows
