# Technical Mental Maps for Business Analysts

## 1. Requirement to running behavior

```text
Stakeholder need
    ↓
Business rule / requirement
    ↓
Acceptance criteria
    ↓
Software change
    ↓
Frontend / Backend / Data / Integration
    ↓
Test evidence
    ↓
Deployment
    ↓
Observed business outcome
```

Use this when a learner treats a requirement document as the end product rather than a contract for behavior.

---

## 2. User request path

```text
User
 ↓
Frontend
 ↓ request
API boundary
 ↓
Backend
 ├── authorization
 ├── validation
 ├── business logic
 ├── database
 └── external integration
 ↓ response
Frontend state
 ↓
User sees outcome
```

BA questions at each boundary:
- Who is allowed?
- What inputs are valid?
- What rule decides the result?
- What data changes?
- What if dependency fails?
- What does the user see?

---

## 3. Business rule → programming logic

```text
Policy:
"Order >= 10m requires manager approval"

        ↓ structured requirement

Condition:
order.total >= 10m

        ↓ software logic

TRUE  → manager approval state/path
FALSE → normal state/path
```

The syntax can vary by language; the decision model remains recognizable.

---

## 4. Frontend vs backend

```text
Frontend
- presentation
- interaction
- local form state
- convenience validation

Backend
- trusted authorization
- authoritative validation
- business rules
- orchestration
- persistence/integration
```

This is a mental model, not an absolute architecture law. The BA takeaway: hiding or disabling a UI control does not by itself enforce a business/security rule.

---

## 5. Database relationships

```text
Customer 1 ─── * Order
Order    1 ─── * OrderItem
Product  1 ─── * OrderItem
```

Translate nouns and business cardinality before worrying about database-engine syntax.

---

## 6. Integration

```text
System A
   │ request / event
   ▼
Interface contract
   │
   ▼
System B

Cross-boundary concerns:
identity • schema • timing • retries • duplicate handling • errors • ownership • audit
```

---

## 7. Git and delivery

```text
Requirement
  ↓
Work item
  ↓
Branch/change
  ↓
Review
  ↓
Merge
  ↓
Build/test
  ↓
Deploy
  ↓
Release validation
```

"Developer finished coding" may only mean one intermediate state.

---

## 8. DevOps/cloud

```text
Source code
 ↓
CI build + tests
 ↓
Artifact/container
 ↓
Deployment
 ↓
Runtime environment
 ├── app
 ├── database
 ├── proxy/network
 ├── secrets/config
 └── logs/metrics
```

A production incident may originate from any layer; do not assume code is the only variable.

---

## 9. BA ambiguity lens

```text
WHO      actor / authority
WHEN     trigger / timing / order
WHAT     data / action / outcome
RULE     condition / threshold / calculation
EXCEPT   rejection / failure / override / cancellation
PROOF    acceptance / audit / traceability
```

Use the lens to inspect vague stakeholder statements, but do not force every category into every requirement.
