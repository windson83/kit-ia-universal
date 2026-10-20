# Dynamic Capability Discovery Protocol

OrquestraMD must discover capabilities at runtime instead of maintaining a permanent agent roster.

## Goal

Create an ephemeral, task-scoped understanding of the agents, subagents, skills and callable workflows currently available.

A newly added capability should become usable on the next discovery cycle without modifying OrquestraMD.

## Discovery process

### 1. Locate capability sources

Use the host environment first. If filesystem discovery is supported, inspect project and user/global locations that may contain agent or skill definitions.

Typical hints include directories named:

```text
agents/
skills/
.claude/agents/
.claude/skills/
```

These are examples, not an allowlist. Also inspect project instructions for custom locations.

### 2. Enumerate resources

Collect candidate definition files and registry entries.

For filesystem skills, a directory containing `SKILL.md` is usually a strong signal of a skill definition.

For filesystem agents, Markdown files in a configured agent directory are usually candidates.

Do not infer semantics solely from filenames.

### 3. Lightweight profile

Read metadata/frontmatter/description first when possible.

Extract:

- name;
- type;
- purpose;
- triggers;
- capability domains;
- technologies;
- tools;
- constraints;
- input/output expectations.

### 4. Shortlist

Compare the current work package's capability requirements against the lightweight profiles.

Only deeply load definitions likely to matter.

### 5. Deep read

For shortlisted resources, read enough of the full definition to understand:

- exact responsibilities;
- explicit exclusions;
- invocation method;
- expected evidence;
- operating workflow;
- compatibility requirements;
- dependencies or companion capabilities.

### 6. Register

Create an in-memory capability registry.

Suggested conceptual schema:

```text
id
name
type
source
description
capabilities[]
technologies[]
tools[]
can_implement
can_review
can_validate
constraints[]
inputs[]
outputs[]
confidence
```

## Selection behavior

Never select solely by name similarity.

Good match:

```text
Task requires:
- React implementation
- accessible menus
- state management

Candidate definition declares:
- frontend implementation
- React
- accessibility
- component/state architecture
```

Weak match:

```text
Filename contains "frontend" but definition is only a visual-design advisory skill.
```

## Agents and skills are not equivalent

An autonomous agent can often own a work package.

A skill usually augments reasoning/execution by adding instructions, standards or tool workflows.

The orchestrator must determine how the runtime expects each resource type to be used.

## Precedence and duplicates

When two capability definitions overlap:

1. obey explicit project/runtime precedence rules;
2. prefer project-specific resources when they encode local constraints;
3. compare declared specialization and exclusions;
4. avoid running redundant resources unless independent review adds value.

## Refresh behavior

Refresh discovery at least at the start of substantial orchestration.

Refresh again when:

- the user adds/removes a capability;
- the environment changes;
- selection fails because a referenced resource disappeared;
- the task changes to a materially different domain.

## Anti-patterns

Do not:

- maintain a static list of known agent filenames;
- require manual catalog updates for every new specialist;
- assume all `.md` files are agents;
- invoke all discovered agents "just in case";
- treat a passive skill as an autonomous worker;
- use filename matching as the only routing method;
- retain a stale capability snapshot across unrelated orchestration tasks.
