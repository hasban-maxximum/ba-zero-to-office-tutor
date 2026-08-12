# Curriculum and Dependency Graph

## Purpose
This curriculum converts the office target list into an understanding-first Technical Business Analyst path. The dates preserve the office schedule as supplied; the depth is intentionally BA-oriented rather than engineer-proficiency oriented.

> Calendar note: the source spreadsheet labels **"Senin, 23-08-2026"**, but 23 August 2026 is Sunday. The next Monday is 24 August 2026. Preserve the office label if reporting against the spreadsheet, but flag the calendar mismatch when scheduling.

## Competency spine

```text
Business context
  ↓
Business process
  ↓
Requirement & business rule
  ↓
Programming logic
  ↓
Frontend ↔ API ↔ Backend ↔ Database
  ↓                    ↕
External systems   Infrastructure
  ↓                    ↓
Git / delivery → DevOps / Cloud
  ↓
System design + technical documentation
```

The learner should increasingly see one connected system, not eleven isolated subjects.

---

## Module 1 — SDLC and Development Methodologies
**Office date:** Friday, 7 Aug 2026  
**Office terms:** SDLC, Agile, Scrum, Waterfall

### Outcome
Explain how a need becomes a released and maintained software change, and why different delivery methods change BA activities.

### Must understand
- lifecycle: discovery/analysis → design → build → test → release → operate/change;
- iterative vs sequential delivery;
- Scrum as a framework inside an Agile way of working, not a synonym for all Agile;
- where BA work appears: discovery, refinement, acceptance, change analysis.

### Transfer evidence
Given a regulatory deadline with fixed scope vs a new product with uncertain user needs, explain which delivery characteristics matter and why.

---

## Module 2 — Business Process Analysis and Modeling
**Office date:** Monday, 10 Aug 2026  
**Office terms/tools:** BPMN, Flowchart, AS-IS, TO-BE; Draw.io, Bizagi, Visio

### Outcome
Turn messy descriptions of work into a readable current-state process, identify pain points, and propose a justified future-state process.

### Must understand
- process boundary: trigger/start, end outcome;
- actor/role and handoff;
- activity/task;
- decision/gateway and business rule;
- normal path vs exception path;
- AS-IS describes current reality; TO-BE describes intended future behavior;
- notation is subordinate to correctness of process reasoning.

### BPMN depth
Know event, task, gateway, sequence flow, pool/lane at working-reading level. Do not chase the entire BPMN specification before the learner can model a simple approval process correctly.

### Transfer evidence
Model employee reimbursement including rejection, missing receipt, and finance correction paths.

---

## Module 3 — Requirements Engineering / Business Analysis
**Office date:** Tuesday, 11 Aug 2026  
**Office terms/tools:** Requirement Gathering, User Story, BRD, FRD, Acceptance Criteria; Confluence

### Outcome
Transform stakeholder language into explicit, testable, traceable requirements without inventing missing business decisions.

### Must understand
- elicitation is not merely "asking what feature you want";
- problem vs symptom vs requested solution;
- business requirement, stakeholder/user need, functional requirement, non-functional requirement, business rule, constraint;
- user story as a collaboration format, not a replacement for all requirement detail;
- acceptance criteria as testable boundaries of expected behavior;
- BRD/FRD naming and contents vary by organization; purpose matters more than template worship;
- ambiguity: actor, trigger, condition, threshold, data, timing, exception, authority, audit, outcome.

### Transfer evidence
Given "approval purchasing harus otomatis supaya lebih cepat", identify unknowns before drafting final requirements.

---

## Module 4 — Programming Fundamentals for BA
**Office date:** Wednesday, 12 Aug 2026  
**Office examples:** PHP, Java, JavaScript, TypeScript, C#, Python, Go

### Outcome
Understand how written requirements become deterministic logic without needing proficiency in seven languages.

### Concept clusters
Teach one cluster at a time.

**A. Values and decisions**
- instruction;
- variable/value;
- basic data type;
- operator/comparison;
- boolean condition;
- if/else branching.

**B. Reuse and repetition**
- function: named reusable behavior with inputs/outputs;
- loop/iteration: apply logic repeatedly to a collection;
- collection/list concept.

**C. Structure and failure**
- object/class at conceptual level: data + behavior model;
- input/output;
- error/exception and why failure behavior must be specified.

**D. Later bridge**
- synchronous vs asynchronous only when API/integration needs it.

### Canonical example
Business rule: "Orders at or above Rp10,000,000 require manager approval."

```text
IF order.total >= 10,000,000
THEN approval_required = manager
ELSE continue normal process
```

Show syntax in one language only after the learner understands the rule as logic. A second language may demonstrate transfer; do not tour all seven languages.

### BA questions generated by programming thinking
- exactly equal to 10 million: included or not?
- currency and rounding?
- who counts as manager?
- what happens if manager is unavailable?
- can the order change after approval?
- what error state should the user see?

### Transfer evidence
Learner converts leave-policy rules into structured pseudologic and identifies unspecified edge cases without writing production code.

---

## Module 5 — Backend Development
**Office date:** Thursday, 13 Aug 2026  
**Office examples:** Laravel, Spring Boot, ASP.NET Core, Express.js, NestJS, Django

### Outcome
Understand where server-side business logic, authorization, persistence coordination, and integrations typically live.

### Mental model
```text
Request
  ↓
Authentication / authorization
  ↓
Validation
  ↓
Business logic
  ↓
Database / external service
  ↓
Response
```

### Product map
- PHP → Laravel
- Java → Spring Boot
- C# → ASP.NET Core
- JavaScript/TypeScript → Express.js / NestJS
- Python → Django

These frameworks differ substantially in implementation, but they occupy a comparable architectural category for BA orientation.

### Transfer evidence
Given "user can cancel an approved order", identify which rules likely belong in backend validation/business logic and what data/state changes must be considered.

---

## Module 6 — Frontend Development
**Office date:** Friday, 14 Aug 2026  
**Office examples:** HTML, CSS, JavaScript, React, Vue.js, Angular

### Outcome
Understand how users interact with system state and why UI behavior is not the same as enforcing a business rule.

### Must understand
- HTML: structure/content semantics;
- CSS: presentation/layout;
- JavaScript: browser behavior/logic;
- React/Vue/Angular: application UI frameworks/libraries at category level;
- form state, client validation, loading/error/empty/success states;
- frontend validation improves UX; critical rules must still be enforced server-side;
- accessibility and responsive behavior as requirement concerns.

### Transfer evidence
Review an approval form and identify happy path, invalid input, loading, unauthorized, server error, and successful submission states.

---

## Module 7 — Database Fundamentals
**Office date:** Tuesday, 18 Aug 2026  
**Office examples:** PostgreSQL, MySQL, SQL Server, Oracle Database, MongoDB, Redis

### Outcome
Reason about how business information is stored, related, constrained, queried, and changed.

### Relational core
- table, row, column;
- primary key and identity;
- foreign key and relationships;
- one-to-one, one-to-many, many-to-many;
- null/optional data;
- unique constraint;
- transaction concept;
- index concept: faster lookup with trade-offs, not query-planner internals.

### NoSQL orientation
- MongoDB: document-oriented category;
- Redis: key-value/in-memory category often used for cache, session, queue-like patterns depending on architecture;
- NoSQL is not "better" or "faster" by definition; data model and workload determine suitability.

### BA translation examples
"One national ID may belong to only one customer" → uniqueness/business rule + validation.  
"Order contains many products" → entity relationship.  
"Payment and balance update must succeed together" → transaction/consistency concern.

### Transfer evidence
Model Customer, Order, Order Item, Product at concept level and identify cardinality/business constraints.

---

## Module 8 — System Integration and API
**Office date:** Wednesday, 19 Aug 2026  
**Office terms:** REST API, GraphQL, SOAP, JSON, XML, OAuth 2.0, JWT

### Outcome
Understand system-to-system communication well enough to analyze contracts, data mapping, auth, failures, retries, and ownership.

### Category map
Do not teach this as seven unrelated definitions.

```text
System communication
├── Interface / interaction style
│   ├── REST
│   ├── GraphQL
│   └── SOAP
├── Data representation
│   ├── JSON
│   └── XML
└── Access / security concepts
    ├── OAuth 2.0
    └── JWT (token format often used in auth flows; not equivalent to OAuth)
```

### API mental model
request → endpoint/operation → method/action → headers/auth → payload/parameters → processing → status/error → response body.

### BA integration checklist
- system of record / data owner;
- trigger and direction;
- contract/schema and field mapping;
- authentication/authorization;
- timeout/retry/idempotency expectations;
- error ownership and user-visible outcome;
- rate/volume/frequency;
- audit/trace identifier.

### Transfer evidence
Review a payment-status integration and reason about duplicate callbacks, timeout, invalid signature, stale status, and retry.

---

## Module 9 — Version Control (Git)
**Office date:** Thursday, 20 Aug 2026  
**Office examples:** Git, GitHub, GitLab

### Outcome
Understand how software changes are isolated, reviewed, combined, traced, and released collaboratively.

### Must understand
- repository;
- commit as a traceable change snapshot;
- branch;
- diff;
- pull/merge request and review;
- merge conflict concept;
- tag/release concept;
- Git is version control; GitHub/GitLab are collaboration platforms around repositories and additional workflows.

### BA relevance
Trace a requirement/change request to implementation work, understand why "already coded" is not the same as "merged/deployed", and communicate about versions without pretending to be a developer.

### Transfer evidence
Explain the path from approved requirement → developer branch → review → merge → release and where BA validation may occur.

---

## Module 10 — DevOps and Cloud Infrastructure
**Office date:** Friday, 21 Aug 2026  
**Office terms:** Docker, Linux, Nginx, AWS, GCP, Azure, CI/CD

### Outcome
Understand how application code becomes a running service and where environment/configuration/deployment failures can alter business behavior.

### Mental model
```text
Code repository
  ↓
Build / test pipeline (CI)
  ↓
Artifact / container
  ↓
Deploy (CD)
  ↓
Runtime environment
  ├── application
  ├── database
  ├── network / reverse proxy
  ├── secrets / configuration
  └── monitoring/logging
```

### Product categories
- Docker: containerization;
- Linux: common server OS/runtime environment;
- Nginx: web server/reverse proxy category;
- AWS/GCP/Azure: cloud platforms with many services, not single technologies;
- CI/CD: automated integration/delivery/deployment workflow concepts.

### BA relevance
Environment-specific config, scheduled jobs, external connectivity, secrets, permissions, deployment sequence, rollback, maintenance windows, and observability can all affect acceptance and incident analysis.

### Transfer evidence
Explain why a feature can work in staging but fail in production without concluding "the code must be different".

---

## Module 11 — Technical Documentation and System Design
**Office label:** Monday, 23 Aug 2026 (calendar mismatch; Monday is 24 Aug 2026)  
**Office tools:** Jira, Confluence, Draw.io, Figma, Miro, Postman, Swagger/OpenAPI, DBeaver, pgAdmin

### Outcome
Synthesize business process, requirements, UI, API, backend, data, integration, and infrastructure into traceable technical communication.

### Tool-by-purpose map
- Jira: work/issues/change tracking;
- Confluence: collaborative documentation/knowledge;
- Draw.io/Miro: diagrams and collaborative modeling;
- Figma: UI/interaction design reference;
- Postman: API exploration/testing client;
- Swagger/OpenAPI: machine/human-readable HTTP API contract/documentation ecosystem;
- DBeaver/pgAdmin: database inspection/administration clients.

### System-design BA view
For each component/boundary, identify:
- responsibility;
- input/output;
- owner;
- business rules;
- data stored/changed;
- failure behavior;
- security/permission expectation;
- traceability to requirement and acceptance evidence.

### Final synthesis evidence
Learner narrates a flow such as:

```text
User
 ↓
Frontend
 ↓
API
 ↓
Backend
 ↓
Database
 ↕
External System
```

and can explain what happens at each boundary, what can fail, what remains ambiguous, and what a BA should verify.

---

# Suggested prerequisite behavior
The schedule is fast. Do not block a module because every earlier module is imperfect. Use just-in-time bridges, then revisit weak prerequisites during review.

# Review cadence
At the beginning of each new module:
1. retrieve one concept from the previous module;
2. retrieve one older foundational concept;
3. connect both to today's topic;
4. spend most of the session on today's target.

# Completion definition
A module may be marked **covered** when its concepts were taught. Mark individual competencies **applied** only when the learner demonstrates transfer on a new case. Never equate schedule completion with mastery.
