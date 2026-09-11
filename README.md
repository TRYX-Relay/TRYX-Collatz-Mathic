# Collatz conjecture research — Snowman Mathic and Lean 4 verification

[![Package replay](https://github.com/TRYX-Relay/TRYX-Collatz-Mathic/actions/workflows/verify-collatz-package.yml/badge.svg)](https://github.com/TRYX-Relay/TRYX-Collatz-Mathic/actions/workflows/verify-collatz-package.yml)
[![Lean and independent checker workflow](https://github.com/TRYX-Relay/TRYX-Collatz-Mathic/actions/workflows/verify-tryx-formulas.yml/badge.svg)](https://github.com/TRYX-Relay/TRYX-Collatz-Mathic/actions/workflows/verify-tryx-formulas.yml)

Badges show workflow status for the statements in this repository. The scope of each result is described below.


**Virgil Lee Gattenby** - TRYX / ENAID / MATHIC

Collatz conjecture (3n+1 problem, hailstone sequences) research: local continuity closure, retained address packets, and formally verified fold identities.

- [Research manuscript](publications/collatz-mathic/MANUSCRIPT.md)
- [Locked score](charts/snowman/TRYX.SNOWMAN.CONJECTURE.MATHIC.TRIAD.CHART.STANDARD.SUCCESSOR.260902.LOCKED.html)
- [Lean proofs](verification/tryx-lean/TryxProof.lean)
- [Fresh local benchmark](publications/collatz-mathic/replay-result.json)
- [Historical proof verification](publications/collatz-mathic/verification-evidence.json)

Run `python3 publications/collatz-mathic/check_package.py`.

Local closure here means the retained packet satisfies its reconstruction, fold, and typed continuity checks. It does not mean universal finite Collatz orbit termination. The fresh benchmark checks 100,000 odd source addresses and four archived fixtures.

## Reproduce and inspect

Requires Git and Python 3. From a terminal:

```sh
git clone https://github.com/TRYX-Relay/TRYX-Collatz-Mathic.git
cd TRYX-Collatz-Mathic
python3 publications/collatz-mathic/check_package.py
```

The Python command checks the archived package and replay. To build the formal statements, follow the [pinned Lean project instructions](verification/tryx-lean/README.md).

[Short demonstration walkthrough](DEMONSTRATION.md) · [Citation metadata](CITATION.cff)

## Research triad

These three research packages share the TRYX → ENAID → Laws → MATHIC construction order. Sheet Mathics presents the work through scores and lyrics, with accompanying executable checks and formal statements.

| Research | Demonstrated scope |
| --- | --- |
| [Navier–Stokes Mathic v6](https://github.com/TRYX-Relay/TRYX-Navier-Stokes-Mathic) | Signed Action accounting identities and recorded corridor replay |
| [Problem No Problem / P vs NP](https://github.com/TRYX-Relay/TRYX-PNP-MATHIC) | Existential Boolean folding semantics and finite benchmarks |
| [Snowman / Collatz conjecture](https://github.com/TRYX-Relay/TRYX-Collatz-Mathic) | Address reconstruction, fold identities, and local continuity checks |

## Independent review

Do the retained packets reconstruct correctly, fold to the stated identity, and reject the corrupted packet? Report the commit, command, input, and observed output in a [repository issue](https://github.com/TRYX-Relay/TRYX-Collatz-Mathic/issues). Please distinguish package integrity, replay results, and the exact Lean theorem statement when reporting findings.
