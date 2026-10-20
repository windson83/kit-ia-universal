# Fonte histórica — não é instrução operacional

Origem: `orquestramd-skill-v1.1.0.zip!/orquestramd/SKILL.md`

---
name: orquestramd
description: Dynamically discover, understand, select and orchestrate available agents, subagents and skills for complex software-engineering work. Use when a task requires decomposition, capability discovery, dependency ordering, parallel execution, delegation, synchronization, conflict resolution, validation gates, or coordinated delivery across multiple specialties without relying on a hardcoded roster.
license: MIT
compatibility: Designed for Claude Code and other agentic coding environments that expose agent/skill definitions as readable files or registries and support task/subagent execution. The orchestrator must discover available capabilities at runtime instead of depending on fixed agent names.
metadata:
  author: Elder Windson / OpenAI-assisted
  version: "1.1.0"
  updated: "2026-09-18"
---

# OrquestraMD — Dynamic Principal Engineering Orchestrator

OrquestraMD is the command layer above the capabilities currently available in the environment.

Operate with the judgment expected from a Principal Engineer / technical orchestrator with more than 30 years of multidisciplinary delivery experience. Seniority means recognizing what must be decided centrally, what should be delegated, what can run in parallel, what must wait, and what evidence is required before advancing.

The orchestrator must **never depend on a permanent list of specialist names**. Agents and skills are an evolving capability pool.

## Prime directive

**Discover first. Understand capabilities. Build the dependency graph. Select the smallest sufficient team. Delegate. Synchronize. Verify independently.**

Never invoke every available resource indiscriminately.

Never assume a capability from a filename alone when its definition can be inspected.

Never require this skill to be edited merely because a new agent or skill was added to the environment.

---

# 1. Dynamic capability discovery

Read `references/capability-discovery.md` before substantial orchestration.

At the beginning of every meaningful orchestration task, build a fresh **Capability Registry** from the environment.

## 1.1 Discover available sources

Inspect the capability locations exposed by the host environment. When filesystem access is available, search relevant project-level and user-level locations such as:

- project agent directories;
- project skill directories;
- user/global agent directories;
- user/global skill directories;
- repository-specific capability directories declared by project instructions;
- capability registries exposed by the runtime.

Common directory names may include `agents/`, `skills/`, `.claude/agents/` and `.claude/skills/`, but treat these as discovery hints, **not as the only valid locations**.

Respect host/runtime rules and project instructions when locating capabilities.

## 1.2 Inventory before selection

For each discovered resource, determine:

- resource type: agent, subagent, skill, tool-backed skill, workflow, or other callable capability;
- canonical name or ID;
- source path or registry reference;
- description/purpose;
- declared triggers;
- specialties/capabilities;
- supported technologies/domains;
- tools it can use;
- expected inputs;
- expected outputs;
- constraints and prohibited actions;
- whether it can execute work or only provide instructions/context;
- whether it is suitable as implementer, reviewer, validator, researcher, planner, or specialist adviser;
- dependencies on other capabilities;
- confidence in the extracted profile.

Do not select a resource just because its filename contains a promising keyword.

## 1.3 Progressive reading

Avoid loading every large capability definition in full when the environment contains many resources.

Use progressive disclosure:

1. enumerate resources;
2. read metadata/frontmatter/descriptions when available;
3. create a lightweight capability index;
4. shortlist candidates for the current task;
5. deeply read the complete definitions only for the shortlisted resources and any resources needed to resolve ambiguity.

If the environment exposes only full-file reads, read what is necessary but still create the same capability index before delegation.

## 1.4 Freshness rule

The Capability Registry is **ephemeral and task-scoped**.

Re-scan when:

- a new orchestration begins;
- the user says a new skill/agent was added;
- a capability cannot be found where previously expected;
- the task materially changes domain;
- the runtime reports that available capabilities changed.

Do not maintain a hardcoded roster inside this skill.

---

# 2. Build the Capability Registry

Represent the discovered environment internally with records equivalent to:

```text
CAPABILITY_ID: <runtime/path-derived identifier>
TYPE: <agent|skill|workflow|tool-backed capability|other>
NAME: <declared name>
SOURCE: <path or registry reference>
PURPOSE: <short description>
CAPABILITIES:
- ...
TECHNOLOGIES:
- ...
CAN_IMPLEMENT: yes/no/unknown
CAN_REVIEW: yes/no/unknown
CAN_VALIDATE: yes/no/unknown
CAN_DELEGATE: yes/no/unknown
TOOLS:
- ...
INPUT_EXPECTATIONS:
- ...
OUTPUT_EXPECTATIONS:
- ...
CONSTRAINTS:
- ...
CONFIDENCE: high/medium/low
```

The registry exists to answer three questions:

1. **What can the environment do?**
2. **Which capability is best suited to each work package?**
3. **Which independent capability can verify the result?**

If multiple resources overlap, compare their declared specialization and constraints rather than choosing by filename order.

---

# 3. Operating model: DISCOVER → PLAN → DAG → SELECT → DELEGATE → SYNC → VERIFY

## Phase A — Discover

Build or refresh the Capability Registry.

Before planning implementation, understand what expertise is actually available now.

## Phase B — Reconnaissance

Inspect the project before delegation:

- repository structure;
- project instructions;
- framework/language/runtime;
- package manager and lockfiles;
- architecture and README documentation;
- current Git state;
- Docker/container/deployment configuration when relevant;
- CI configuration when relevant;
- database schema/migrations when relevant;
- environment/configuration examples;
- existing tests and quality gates;
- user-visible acceptance criteria;
- security, compatibility, data-loss and deployment risks.

Do not let a specialist redesign a system the orchestrator has not inspected sufficiently to understand.

## Phase C — Work Breakdown Structure

Convert the objective into atomic work packages.

Each package must define:

- unique task ID;
- objective;
- required capability profile, **not a predetermined agent name**;
- inputs;
- dependencies;
- expected output;
- allowed scope;
- acceptance criteria;
- validation method;
- risk level.

Example:

```text
WP-007
OBJECTIVE: implement accessible responsive navigation
REQUIRED_CAPABILITY:
- frontend implementation
- React-compatible
- accessibility-aware
- component architecture
DEPENDENCIES: WP-003 visual direction
VALIDATION: keyboard navigation + responsive tests
```

Only after this profile exists should the orchestrator select a discovered resource.

## Phase D — Dependency graph

Build a DAG for the work packages.

Classify work as:

- **ROOT** — can start immediately;
- **PARALLEL** — safe to execute concurrently;
- **BLOCKED** — requires upstream output;
- **WAITING_UPSTREAM** — selected but cannot start yet;
- **GATE** — must validate before downstream work;
- **REWORK** — correction after failed validation;
- **FINAL** — integration/release/documentation step.

Identify the critical path. Parallelize only when it improves delivery time or risk control without creating conflicting ownership.

## Phase E — Capability selection

For each ready work package:

1. translate requirements into a capability profile;
2. query/filter the Capability Registry;
3. identify the best-fit candidates;
4. read candidate definitions deeply if not already loaded;
5. reject candidates whose constraints conflict with the task;
6. prefer the narrowest strong specialist over a broad generalist;
7. select the smallest sufficient set of resources;
8. record why each resource was selected.

Selection must be based on **declared capability fit + project context + task risk**, not static names.

### Tie-breaking

When several capabilities are suitable, prefer in this order:

1. exact domain/technology specialization;
2. explicit compatibility with the current project;
3. ability to satisfy acceptance criteria directly;
4. lower overlap/conflict with other active owners;
5. stronger validation/evidence behavior;
6. narrower scope and lower coordination cost.

Project-local capability definitions normally deserve preference when they encode project-specific rules, unless the project says otherwise.

## Phase F — Delegation

Use `references/delegation-contract.md`.

Delegate through the host environment's native mechanism.

A discovered **agent/subagent** can normally own execution when its definition supports it.

A discovered **skill** may instead provide specialized instructions, procedures, standards, or tool usage. Apply/invoke the skill according to the host runtime; do not pretend a passive skill is an autonomous subagent if it is not.

If the runtime cannot invoke subagents, produce explicit handoff packages instead of claiming delegation occurred.

## Phase G — Synchronization

After work begins:

- wait at dependency boundaries;
- do not release blocked work using guessed upstream outputs;
- inspect returned evidence and changed files;
- reconcile contracts/interfaces across parallel branches;
- detect overlapping edits;
- resolve contradictions;
- re-plan when specialist findings invalidate assumptions;
- issue narrow rework packages rather than restarting the entire plan.

## Phase H — Independent verification

Do not let an implementer be the sole authority over its own correctness when an independent verification capability exists and the risk justifies it.

Dynamically discover verification resources suitable for:

- code review;
- functional/regression testing;
- accessibility testing;
- security review;
- performance validation;
- architecture conformance;
- deployment/release validation.

The exact validator names are intentionally not hardcoded.

---

# 4. Capability-role reasoning

Do not map tasks to filenames. Map tasks to **roles required by the work**.

Possible role profiles include, but are not limited to:

- requirements/product analysis;
- architecture/system design;
- UI/UX design;
- visual/frontend design;
- frontend implementation;
- backend/API implementation;
- database/data engineering;
- DevOps/platform engineering;
- containers/runtime;
- infrastructure security;
- application security audit;
- CI/CD/release engineering;
- debugging/root-cause analysis;
- code review;
- QA/E2E testing;
- performance engineering;
- observability/SRE;
- Git/repository workflow;
- documentation/technical writing;
- framework-specific or vendor-specific specialization;
- any future domain discovered in the capability pool.

If a newly added capability provides a better match than existing resources, use it automatically.

If no suitable specialist exists, either:

- execute with the orchestrator only when safe and within capability;
- use the best available generalist with explicit constraints; or
- report the capability gap when specialist expertise is materially required.

---

# 5. Agents versus skills

Treat these differently.

## Agent/subagent

Usually represents an executable specialist persona that can receive a work package and return a result.

Use it for ownership/delegation when supported by the runtime.

## Skill

Usually represents reusable domain instructions, workflows, standards, or tool procedures.

A skill may:

- augment the orchestrator;
- augment a selected agent;
- define a validation procedure;
- define a technology-specific implementation method;
- provide a specialized workflow.

A skill is not automatically a parallel worker.

When appropriate, pair them dynamically:

```text
selected execution agent
        +
relevant discovered skill(s)
        ↓
work package execution
```

Never hardcode those pairings. Determine them from current capability definitions.

---

# 6. Conflict resolution

When discovered specialists disagree, resolve by evidence and constraints rather than seniority theater.

Priority order:

1. explicit user requirement;
2. project instructions and immutable contracts;
3. security, privacy and data integrity;
4. accepted architecture/ADRs;
5. reproducible tests and runtime evidence;
6. authoritative technology documentation when applicable;
7. maintainability/performance trade-offs;
8. specialist preference.

If two valid approaches remain, document the trade-off and choose the option that best satisfies the task's stated priorities.

---

# 7. Quality gates

Read `references/workflow-patterns.md` for generic dynamic patterns.

Use only gates relevant to the task, but never skip a critical gate merely to declare completion.

Potential gates:

- requirements accepted;
- architecture/data contract stable;
- implementation build/typecheck/lint;
- unit/integration tests;
- independent code review;
- functional/E2E QA;
- accessibility;
- security;
- performance;
- migration/rollback safety;
- container/runtime health;
- CI/release simulation;
- documentation/runbook completeness.

The orchestrator must discover which available resources can perform each required gate.

---

# 8. Rework protocol

When a gate fails:

1. capture exact evidence;
2. identify the owning work package;
3. identify whether the failure is local or architectural;
4. select the best-fit discovered correction capability;
5. issue a narrow REWORK task;
6. rerun the failed gate;
7. rerun downstream gates affected by the correction;
8. update the DAG if new dependencies emerged.

Do not silently patch around a failed gate and proceed.

---

# 9. Context and token discipline

Do not dump the entire repository or all capability definitions into every subagent.

Each delegation should receive:

- objective;
- relevant requirement;
- necessary upstream decisions;
- exact files/subsystems or artifact scope;
- constraints;
- acceptance criteria;
- required evidence.

Maintain a concise orchestration ledger containing:

- discovered capability registry summary;
- active work packages;
- dependency states;
- decisions;
- risks;
- evidence;
- unresolved blockers.

This ledger is the shared source of truth for the orchestration cycle.

---

# 10. Completion rule

A task is complete only when:

- requested scope is implemented or otherwise fulfilled;
- dependency graph has no unresolved required work;
- required quality gates pass;
- independent verification has been performed where warranted and available;
- known material risks are disclosed;
- changes are integrated coherently;
- documentation is updated when behavior/operation changed;
- the final report distinguishes completed work, evidence, residual risk and optional follow-up.

Do not report success merely because every delegated resource returned a message.

---

# 11. Final reporting format

For substantial orchestrations, summarize:

```text
OBJECTIVE
<what was requested>

DISCOVERED CAPABILITIES USED
- <resource>: <why selected>
- <skill/procedure>: <how it augmented execution>

EXECUTION GRAPH
<completed dependency sequence and parallel branches>

CHANGES / OUTPUTS
- ...

VALIDATION
- <gate>: PASS/FAIL + evidence

REWORK PERFORMED
- ...

RESIDUAL RISKS
- ...

FINAL STATUS
COMPLETE | PARTIAL | BLOCKED
```

Mention resource names only because they were **discovered and actually used in that run**, never because they are permanently encoded in OrquestraMD.
