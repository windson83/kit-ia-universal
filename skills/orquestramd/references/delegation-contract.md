# Delegation Contract

Use this format when dispatching work to a dynamically selected execution capability.

```text
TASK_ID: WP-###
SELECTED_RESOURCE: <discovered resource name/id>
RESOURCE_TYPE: <agent|subagent|workflow|other executable capability>
CAPABILITY_MATCH: <why this discovered resource fits the required profile>
OBJECTIVE: <one measurable outcome>
CONTEXT: <only relevant project facts>
INPUTS:
- <file/output/decision>
DEPENDENCIES:
- <TASK_ID or NONE>
AUGMENTING_SKILLS:
- <discovered skill if relevant, otherwise NONE>
SCOPE_ALLOWED:
- <directories/files/subsystems>
DO_NOT_CHANGE:
- <protected scope>
EXPECTED_OUTPUT:
- <artifact/code/analysis>
ACCEPTANCE_CRITERIA:
- <criterion 1>
- <criterion 2>
VALIDATION_REQUIRED:
- <commands/checks/evidence>
RETURN_FORMAT:
1. Inspected
2. Changed/proposed
3. Files touched
4. Tests/checks
5. Evidence
6. Risks/assumptions
7. Blockers
8. Recommended next dependency
```

## Delegation quality test

Before dispatch, answer yes to all:

- Was the resource discovered in the current environment?
- Was its definition read deeply enough to understand its role and constraints?
- Does its declared capability match this work package?
- Can it identify success without guessing?
- Are upstream dependencies available?
- Is ownership/scope clear?
- Is the output consumable by downstream work?
- Is there a verification method?
- Is the task narrow enough to review?

## Skill augmentation

If one or more discovered skills improve execution, attach them conceptually to the work package, but only in the manner supported by the runtime.

Never claim a skill executed autonomously unless the host actually provides that behavior.
