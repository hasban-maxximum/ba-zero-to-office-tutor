# Assessment Rubric

## Principle
**A definition is not mastery.** Familiarity can create false confidence, especially when a learner has been trained to memorize. Score only demonstrated evidence.

Use a **0–5** scale for each concept/competency.

| Level | Evidence | What learner can do | What is still missing |
|---|---|---|---|
| 0 | Unseen | No demonstrated knowledge | Everything |
| 1 | Recognition | Recognize the term/example when prompted | Independent explanation |
| 2 | Explanation | Explain in own words and reproduce a simple known example | Reliable transfer |
| 3 | Classification / transfer | Recognize and apply the concept in a new, straightforward case | Complex/ambiguous use |
| 4 | Application | Use it independently in a realistic office case and identify important edge cases | Robust defense under challenge |
| 5 | Defense / synthesis | Defend reasoning when assumptions change, compare alternatives, and connect impacts across system/process boundaries | Experience may still deepen judgment |

## Hard scoring rules
1. Textbook definition alone: maximum **Level 1** if copied/repeated, **Level 2** if genuinely explained in own words with a correct simple example.
2. "I understand" is not evidence.
3. Seeing the tutor solve a case is not evidence the learner can solve it.
4. A correct answer produced only after heavy hints does not receive the same score as independent reasoning.
5. Schedule status "Done" means the topic was covered; it does not automatically change competency score.

## Five evidence types
Use these progressively rather than every turn.

### A. Recall
"Apa tujuan acceptance criteria?"

### B. Teach-back
"Jelaskan dengan kata-kata Anda sendiri. Jangan pakai definisi yang tadi saya berikan."

### C. Discrimination
"Mana yang business rule dan mana yang functional requirement? Jelaskan kenapa."

### D. Transfer
Give a new domain/case with different nouns and ask the learner to apply the same concept.

### E. Challenge defense
Change an assumption or add an exception:
"Bagaimana jawaban Anda berubah kalau transaksi boleh diedit setelah approval?"

## Scoring example — programming condition
Learner says:
> "if/else itu percabangan berdasarkan kondisi."

Score: 1–2 depending on whether it is their own explanation.

Learner can map:
> "Jika order >= 10 juta harus manager approval; kalau kurang, langsung proses."

Score: potentially 3.

Learner additionally asks whether exactly 10 million is included, what happens if total changes after approval, and whether manager delegation exists:
Score: potentially 4.

Learner compares multiple policy designs and explains downstream UI/backend/data/audit impacts under changed assumptions:
Score: potentially 5.

## Correction protocol
When wrong:
1. identify the first incorrect inference;
2. show one counterexample;
3. ask learner to revise;
4. score the revised reasoning, noting hints used.

## Passing target
For a fast office foundation, aim for:
- Level 3 on most concepts;
- Level 4 on core BA competencies: process analysis, ambiguity detection, requirements, acceptance criteria, stakeholder reasoning;
- Level 2–3 may be sufficient for product-specific technologies not central to current work.
