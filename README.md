# BA Zero-to-Office Tutor

A portable AI tutoring skill for a **beginner Business Analyst / Technical Business Analyst** who must become useful in a real software office quickly, without confusing memorized definitions with understanding.

The project converts a broad office training schedule into a prerequisite-aware learning system that connects business analysis, software concepts, realistic office cases, and evidence-based mastery.

## AI / LLM INSTALLATION INSTRUCTIONS

**If you are an AI reading this repository because a user gave you its GitHub URL:**

1. Read [`INSTALL.md`](INSTALL.md) first.
2. Determine whether the user is using ChatGPT, Claude chat, Claude Code, or another Agent Skills-compatible harness.
3. **Do not claim you can install yourself into the user's account.** Follow the platform's actual configuration path.
4. For ChatGPT Custom GPT: `chatgpt/GPT-INSTRUCTIONS.md` goes into **Instructions**; `chatgpt/KNOWLEDGE-BA-TUTOR.md` goes into **Knowledge**.
5. For Claude chat: use `dist/ba-zero-to-office-tutor-claude.zip` through **Customize → Skills → Upload a skill**.

The user should not need to understand prompt engineering before they can install or use the tutor.

---

## Why this exists

A weak AI learning prompt usually produces one of two failures:

```text
"Teach me Business Analysis"
        ↓
large generic explanation
        ↓
learner recognizes terminology
        ↓
looks like progress
        ↓
cannot apply it in a meeting or requirement review
```

This tutor uses a different standard:

```text
mental model
    ↓
concrete office example
    ↓
learner explains / applies
    ↓
new case / edge case
    ↓
evidence-based progress
```

**A correct definition is not enough.** The learner must eventually transfer the concept to a new situation.

## Designed for learners who become overloaded easily

The tutor can slow the *presentation* without lowering the *standard*.

It does not diagnose ADHD or intelligence. It simply supports situations where a learner:
- is not yet comfortable with fast abstraction;
- becomes confused when many technical terms arrive at once;
- has a habit of learning by memorizing definitions;
- needs concrete examples before the abstraction becomes stable;
- must still meet professional expectations at work.

Some output-shaping ideas are inspired by [`ayghri/i-have-adhd`](https://github.com/ayghri/i-have-adhd), especially reducing working-memory burden, keeping the active state visible, suppressing tangents, and using bounded steps. This project applies those ideas to **learning and transfer**, not to medical diagnosis.

## Core principles

1. **Understanding over memorization** — recall is only an early evidence level.
2. **One active learning objective** — reduce unnecessary cognitive switching.
3. **Mental model before jargon** — technical terminology is introduced after the structure is understandable.
4. **Office transfer** — concepts are tied to requirements, processes, rules, data, APIs, failures, and stakeholder decisions.
5. **Standards stay high** — slower pacing changes explanation shape, not mastery criteria.

## Office curriculum

| Module | Office target | BA-oriented outcome |
|---|---|---|
| 1 | SDLC, Agile, Scrum, Waterfall | Understand how needs become released software changes |
| 2 | BPMN, Flowchart, AS-IS, TO-BE | Model current/future processes and exception paths |
| 3 | Requirement Gathering, User Story, BRD, FRD, Acceptance Criteria | Turn vague needs into testable requirements |
| 4 | Programming fundamentals | Read business rules as logic without learning seven languages |
| 5 | Backend development | Understand server-side validation, business logic, data/integration coordination |
| 6 | Frontend development | Understand user interaction, state, validation, and UI vs server responsibility |
| 7 | Database fundamentals | Reason about data, relationships, constraints, and consistency |
| 8 | API / system integration | Analyze contracts, mapping, auth, errors, retries, and ownership |
| 9 | Git / version control | Understand how changes are traced, reviewed, merged, and released |
| 10 | DevOps / cloud | Understand how code becomes a running production system |
| 11 | Documentation / system design | Connect process, requirement, UI, API, backend, database, integration, and delivery |

The detailed path is in [`skills/ba-zero-to-office-tutor/references/curriculum.md`](skills/ba-zero-to-office-tutor/references/curriculum.md).

### Schedule note
The supplied office spreadsheet labels `Senin, 23-08-2026`; 23 August 2026 is Sunday. The next Monday is 24 August 2026. The curriculum preserves the office label but explicitly flags the mismatch.

## What "mastery" means here

| Level | Evidence |
|---:|---|
| 0 | Not yet demonstrated |
| 1 | Recognizes term/example |
| 2 | Explains in own words |
| 3 | Transfers to a new straightforward case |
| 4 | Applies independently in realistic office work and catches important edge cases |
| 5 | Defends/synthesizes reasoning when assumptions change |

A schedule item marked `Done` means **covered**, not automatically mastered.

## Example

Instead of teaching seven programming languages separately:

```text
Stakeholder rule:
"Order >= Rp10,000,000 must be approved by a manager"

        ↓
Requirement / decision model

IF order.total >= 10,000,000
THEN require manager approval
ELSE continue normal flow

        ↓
BA questions

Exactly 10m included?
Can the order change after approval?
Who is manager if the manager is absent?
What is the reject/revise path?
```

Only after the logic is understood should syntax be shown in one representative language.

## Tutor modes

`LEARN`, `EXPLAIN`, `CASE`, `COACH`, `ASSESS`, `REVIEW`, and `URGENT` are defined in the skill. The learner does not need to use these exact keywords; the tutor selects the mode from context.

## Good first messages

```text
Lanjutkan target belajar kantor saya hari ini. Saya masih pemula.
```

```text
Saya sudah belajar BPMN kemarin. Tes apakah saya paham atau cuma hafal.
```

```text
Kasih saya case requirement kantor. Jangan berikan jawaban final sampai saya mencoba.
```

```text
Bos minta saya review API hari ini, tapi saya belum belajar API. Ajari minimum yang saya perlukan dulu.
```

## Repository structure

```text
skills/ba-zero-to-office-tutor/
├── SKILL.md
└── references/
    ├── curriculum.md
    ├── teaching-protocol.md
    ├── cognitive-load.md
    ├── assessment-rubric.md
    ├── learner-state.md
    ├── office-case-bank.md
    └── technical-mental-maps.md

chatgpt/
├── GPT-INSTRUCTIONS.md
├── BUILDER-PROMPT.md
└── KNOWLEDGE-BA-TUTOR.md

tests/
├── behavior-scenarios.md
└── test_repository.py

scripts/build.py
INSTALL.md
REFERENCES.md
```

## Build and verify

```bash
python3 scripts/build.py
python3 -m unittest tests/test_repository.py -v
```

Build outputs:
- `dist/ba-zero-to-office-tutor-claude.zip`
- `dist/ba-zero-to-office-tutor-repository.zip`
- `dist/SHA256SUMS.txt`

## Installation
See [`INSTALL.md`](INSTALL.md).

## Sources and acknowledgements
See [`REFERENCES.md`](REFERENCES.md).

## License
MIT. See [`LICENSE`](LICENSE).

## Publishing this repository
If the GitHub connector in your AI environment cannot create repositories, see [`PUBLISH-GITHUB.md`](PUBLISH-GITHUB.md). The package includes a guarded `scripts/publish-github.sh` for an authenticated GitHub CLI environment.
