# Dynamic Workflow Patterns

These are capability-role patterns, not agent-name mappings.

The orchestrator must resolve each role to resources discovered in the current environment.

## 1. New full-stack capability

```text
requirements/product capability
          ↓
architecture capability
   ┌──────┼───────────────┐
   ↓      ↓               ↓
UI/UX   backend/data   platform needs
   ↓      ↓               ↓
frontend implementation / integration
          ↓
 ┌────────┼─────────┬──────────┐
 ↓        ↓         ↓          ↓
review   QA     security    performance
 └────────┴─────────┴──────────┘
          ↓
     release gate
          ↓
     documentation
```

Only instantiate branches required by the task and supported by available capabilities.

## 2. Frontend redesign

```text
reconnaissance
   ├→ UX/information-architecture capability
   └→ visual/frontend-design capability
              ↓
        design synthesis
              ↓
     frontend implementer
              ↓
   ┌──────────┼──────────┐
   ↓          ↓          ↓
review       QA      accessibility/perf
   └──────────┴──────────┘
              ↓
            gate
```

A discovered design skill may augment the design or implementation capability rather than act as a separate worker.

## 3. Security hardening

```text
architecture/threat analysis
          ↓
security-specialized design guidance
          ↓
implementation owner(s)
          ↓
independent review
          ↓
security validation
          ↓
functional regression
          ↓
release gate
```

## 4. Database migration

```text
architecture/data contract
          ↓
data/database capability
   ├→ application adjustments
   └→ backup/rollback validation
          ↓
integration tests
          ↓
security validation if permissions/exposure changed
          ↓
release plan
```

## 5. Incident

```text
triage
  ↓
debug/root-cause capability + domain owner
  ↓
containment
  ↓
minimal correction
  ↓
focused regression + relevant security validation
  ↓
deploy/recovery
  ↓
postmortem/documentation
```

## 6. CI/CD or platform modernization

```text
platform/deployment capability
     ├→ container/runtime capability (if relevant)
     └→ pipeline/release capability
              ↓
security/infra validation
              ↓
smoke/regression validation
              ↓
release simulation
```

## 7. Capability not yet known

When a task requires a role not covered by these examples:

```text
work-package requirement
        ↓
search Capability Registry
        ↓
newly discovered specialized capability
        ↓
normal delegation + validation flow
```

This is intentional: OrquestraMD must expand naturally as new capabilities are added.
