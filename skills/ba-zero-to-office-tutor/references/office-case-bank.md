# Office Case Bank

## How to use
Cases are for transfer and coaching. Do not present the full reference analysis before the learner attempts the task. Reveal details progressively when simulating stakeholder elicitation.

---

## Case 1 — Purchasing approval
**Useful for:** requirements, programming conditions, backend, audit, BPMN.

Stakeholder statement:
> "Pembelian besar harus approval manager supaya aman."

Hidden questions to probe:
- definition of "besar" and threshold equality;
- currency/tax basis;
- manager selection and delegation;
- edit-after-approval behavior;
- reject/revise/cancel paths;
- audit history;
- emergency override.

Transfer challenge: threshold differs by department.

---

## Case 2 — Employee leave
**Useful for:** process modeling, conditions, loops/batch, calendar integration.

Rules supplied:
- annual allowance 12 days;
- >3 consecutive working days requires manager approval;
- insufficient balance rejects the request;
- weekends do not consume balance.

Missing by design:
- public holidays;
- half-day leave;
- overlapping requests;
- balance reservation timing;
- cancellation after approval.

---

## Case 3 — Customer identity uniqueness
**Useful for:** database, validation, backend/frontend distinction.

Statement:
> "Satu NIK hanya boleh satu akun."

Probe:
- formatting/normalization;
- old/migrated duplicate data;
- NIK corrections;
- merged accounts;
- concurrency: two registrations at nearly the same time.

Key concept: frontend duplicate check is not sufficient enforcement; backend/database constraint may be needed depending on architecture.

---

## Case 4 — Payment callback
**Useful for:** API, integration, idempotency, security, status modeling.

External gateway sends payment status to the application.

Probe:
- duplicate callback;
- callback arrives out of order;
- invalid signature/auth;
- timeout;
- gateway says success while local update fails;
- transaction/reference identifier;
- retry responsibility.

---

## Case 5 — Payroll batch
**Useful for:** loop, function, exception handling, batch behavior.

Statement:
> "Setiap akhir bulan sistem hitung payroll seluruh karyawan."

Probe:
- one employee fails calculation;
- calculation version changes mid-run;
- employee terminated during period;
- rerun behavior;
- duplicate payment prevention.

---

## Case 6 — Stock reservation
**Useful for:** database consistency, API, race conditions at conceptual level.

Two customers attempt to buy the last item.

Ask learner:
- when stock becomes reserved;
- what "available" means;
- timeout/expiry;
- payment failure behavior;
- which system owns stock truth.

---

## Case 7 — Login and authorization
**Useful for:** frontend/backend, auth, API, error states.

Roles: staff, manager, finance.

Challenge:
A staff user manually calls a manager-only endpoint although the UI hides the button.

Expected insight:
UI visibility is not sufficient authorization enforcement.

---

## Case 8 — Vendor master synchronization
**Useful for:** system integration, data ownership, mapping.

ERP is system of record; procurement app keeps a local copy.

Probe:
- sync trigger and frequency;
- deleted/deactivated vendor;
- field mapping;
- failed partial sync;
- conflicting edits;
- audit/last-sync marker.

---

## Case 9 — Order status
**Useful for:** state transitions, requirements, backend, acceptance criteria.

States: draft, submitted, approved, rejected, fulfilled, cancelled.

Ask learner to define allowed transitions and unauthorized/impossible transitions.

Challenge: cancellation after fulfillment.

---

## Case 10 — Report export
**Useful for:** requirement detail, frontend/backend, performance awareness.

Request:
> "Tambahkan export Excel untuk semua transaksi."

Probe:
- selected filters vs truly all rows;
- date/time zone;
- column definition;
- data visibility/permissions;
- maximum volume;
- synchronous download vs background generation;
- sensitive fields.

---

## Case 11 — Staging vs production mismatch
**Useful for:** DevOps/cloud, configuration, debugging mindset.

Feature passes UAT in staging but production cannot reach an external API.

Ask learner to generate categories of hypotheses rather than blaming code immediately:
- environment configuration;
- credentials/secrets;
- network/firewall/DNS;
- endpoint differences;
- permissions;
- deployment/version;
- external allowlisting.

---

## Case 12 — Requirement change after development started
**Useful for:** Git, SDLC, change impact, traceability.

Stakeholder changes approval threshold from 10m to department-specific thresholds after a branch is already in review.

Ask learner to trace impact across requirement, acceptance criteria, code/change review, test evidence, documentation, and release communication.

---

## Capstone — Procurement system
Use after Module 11.

Learner receives:
- employee raises purchase request;
- manager approves depending on amount;
- finance checks budget;
- approved purchase is sent to ERP;
- vendor and item masters come from ERP;
- requester tracks status;
- audit history is required.

Learner must produce, at BA depth:
1. AS-IS/TO-BE outline;
2. key requirements and business rules;
3. user/API/system boundaries;
4. conceptual data entities/relationships;
5. failure/exception list;
6. acceptance strategy and traceability;
7. simple system context/flow diagram.

Do not require production code.
