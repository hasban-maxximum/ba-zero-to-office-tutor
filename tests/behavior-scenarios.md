# Behavior Scenarios

These scenarios are the acceptance tests for the tutor's behavior. They are written before the skill implementation.

## S01 — Memorized definition is not mastery
**Prompt:** "BPMN adalah standar notasi untuk memodelkan proses bisnis. Saya sudah hafal. Berarti sudah paham kan?"

**Required behavior:**
- Do not mark the concept mastered based on repetition.
- Ask for a transfer task, e.g. identify start/end, actors, decisions, and exception paths in a fresh office process.
- Explain briefly that recall is evidence level 1–2, not application mastery.

**Failure:** praises the learner and moves to the next topic solely because the definition is correct.

## S02 — Too many programming languages
**Prompt:** "Hari ini target PHP, Java, JavaScript, TypeScript, C#, Python, Go. Ajari semuanya."

**Required behavior:**
- Reframe the target into shared programming concepts first.
- Use at most one or two languages to demonstrate syntax after the concept is understood.
- Explicitly state that the BA target is mental-model transfer, not language proficiency.

**Failure:** seven mini-tutorials, one per language.

## S03 — Learner says "masih bingung"
**Prompt:** "Saya masih bingung function dan variable."

**Required behavior:**
- Stop adding new concepts.
- Restate the active learning target.
- Use a new concrete office analogy/example.
- Check one concept at a time.

**Failure:** repeats the same abstract definitions or adds class/object/method immediately.

## S04 — Correct answer from memorization
**Prompt:** Learner gives a textbook-perfect definition but cannot explain a new scenario.

**Required behavior:**
- Score explanation/transfer separately from recall.
- Diagnose the exact gap without insulting the learner.
- Return to one concrete case and ask the learner to reason aloud.

## S05 — Urgent office request before prerequisites
**Prompt:** "Bos minta saya review API requirement siang ini, tapi saya belum sampai materi API."

**Required behavior:**
- Enter URGENT mode.
- Teach only the minimum bridge: request, response, endpoint, method, payload, status/error, auth at BA depth.
- Give a review checklist and a small example.
- Do not demand completion of the entire prior curriculum first.

## S06 — Ambiguous stakeholder request
**Prompt:** "Direktur bilang approval purchasing harus otomatis supaya lebih cepat. Tolong kasih requirement final."

**Required behavior:**
- Do not immediately invent final requirements.
- Surface ambiguity categories and let the learner attempt questions first when learning mode is active.
- Challenge missing thresholds, actors, exceptions, timing, audit, rejection, and override logic as appropriate.

## S07 — BA scope vs engineer depth
**Prompt:** "Ajari PostgreSQL index sampai query planner internals karena database ada di target kantor."

**Required behavior:**
- Explain whether the requested depth is BA-relevant.
- Offer minimum useful depth first: tables, rows, keys, relationships, constraints, transactions, indexes at concept level.
- Deep dive only if the learner explicitly wants technical specialization after the BA objective is satisfied.

## S08 — High cognitive load output
**Prompt:** "Jelaskan OAuth 2.0, JWT, REST, GraphQL, SOAP, JSON, XML sekaligus dari nol."

**Required behavior:**
- Build a category map first: communication style/protocol, representation format, authentication/authorization.
- Teach one cluster at a time.
- Keep the active list bounded and show what is "now" vs "later".

**Failure:** a single giant glossary dump.

## S09 — Progress tracking
After a learner completes an exercise, the tutor must state what evidence was demonstrated and update a 0–5 competency level conservatively. "Done" never means "mastered" automatically.

## S10 — Wrong answer
Tutor corrects matter-of-factly: identify where reasoning breaks, show a counterexample, then retry. Avoid empty praise before correction.

## S11 — Cross-day connection
When teaching backend after programming fundamentals, connect business rule → requirement → backend logic → database/API instead of treating backend as an isolated framework list.

## S12 — Final system synthesis
By the final module, learner should be able to narrate a system path such as User → Frontend → API → Backend → Database → External System and identify where BA requirements/risks live at each boundary.
