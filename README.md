# Collatz / Snowman Conjecture Mathic

**Virgil Lee Gattenby** - TRYX / ENAID / MATHIC

Collatz conjecture (3n+1 problem, hailstone sequences) research: local continuity closure, retained address packets, and formally verified fold identities.

- [Research manuscript](publications/collatz-mathic/MANUSCRIPT.md)
- [Locked score](charts/snowman/TRYX.SNOWMAN.CONJECTURE.MATHIC.TRIAD.CHART.STANDARD.SUCCESSOR.260902.LOCKED.html)
- [Lean proofs](verification/tryx-lean/TryxProof.lean)
- [Fresh local benchmark](publications/collatz-mathic/replay-result.json)
- [Historical proof verification](publications/collatz-mathic/verification-evidence.json)

Run `python3 publications/collatz-mathic/check_package.py`.

Local closure here means the retained packet satisfies its reconstruction, fold, and typed continuity checks. It does not mean universal finite Collatz orbit termination. The fresh benchmark checks 100,000 odd source addresses and four archived fixtures.
