# Learner State

## Purpose
Maintain continuity without pretending the learner mastered a topic because it appeared in a previous conversation.

## Recommended state schema

```yaml
learner:
  role_target: technical-business-analyst-foundation
  language: id
  pacing: normal        # compact | normal | slow
  active_module: programming-fundamentals
  active_concept: condition

competencies:
  sdlc:
    level: 3
    evidence: "Compared iterative vs sequential delivery in a new case"
  process_modeling:
    level: 3
    evidence: "Produced AS-IS flow with rejection path"
  requirements:
    level: 3
    evidence: "Found ambiguity in approval requirement"
  programming_condition:
    level: 2
    evidence: "Explained if/else; transfer not yet tested"

misconceptions:
  - concept: function-vs-variable
    observed: "Treats both as containers for values"
    next_probe: "Use payroll calculation: stored salary vs calculateNetSalary()"

review_queue:
  - requirements.acceptance-criteria
  - process-modeling.exception-path

last_transfer_case:
  name: purchasing-approval
  result: partial
  hints_used: 2

current_action:
  type: learner-question
  text: "Apa yang harus terjadi kalau nilai order berubah setelah approval?"
```

## Update rules
- Evidence text must describe an observable learner behavior.
- Scores change by demonstrated evidence, not time spent.
- A single lucky answer should not jump several levels.
- Repeated independent transfer can stabilize a level.
- Record misconceptions specifically enough to create a future probe.
- Remove a misconception only after a counter-case is handled correctly.

## State shown to learner
Do not dump YAML unless requested. Use a compact visible state:

```text
Module: Programming Fundamentals
Fokus: Condition / if-else
Level saat ini: 2/5 — bisa menjelaskan; transfer belum stabil
Sekarang: analisis 1 edge case approval
```

## Starting from unknown state
Do not administer a giant exam. Use micro-diagnostics inside the first real topic:
- one prerequisite question;
- one simple application;
- adjust pacing from evidence.
