# Testing

## Automated repository contract
Run:

```bash
python3 -m unittest tests/test_repository.py -v
```

This verifies structure, required references, key behavioral constraints, curriculum coverage, and packaging claims.

## Behavioral model tests
`behavior-scenarios.md` defines pressure/transfer scenarios that should be run against each target model after installing the skill/configuration.

A structural test cannot prove that a model will obey pedagogy under every conversation. For release validation, run at least S01, S02, S03, S05, S06, and S08 on the actual ChatGPT/Claude configuration and compare output to each scenario's Required behavior / Failure criteria.
