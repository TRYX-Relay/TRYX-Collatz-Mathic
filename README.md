# Collatz Snowman Conjecture

**Virgil Lee Gattenby — Publication 9.24**

## Public document source

| Part | File |
| --- | --- |
| Collatz Snowman Conjecture Paper | [Read the paper](Collatz_Snowman_Conjecture_Paper.pdf) |
| Collatz MATHIC | [Open or download the MATHIC](Collatz_MATHIC.html) |
| ReadMe | [This reading guide](README.md) |
| Lean | [Complete Lean project](Lean/) · [Proof source](Lean/TryxProof.lean) |

Download the HTML MATHIC and open it in a browser to view the chart. GitHub displays its source code. The paper, MATHIC and Lean project are supplied directly in this public repository.

## Reading and verification

The paper presents Number-and-Fold closure at Templex One. The MATHIC is the byte-identical public copy of the sole active locked September 2 Snowman standard successor, not a new score version. The Lean project contains the proof, challenge template, comparator configuration, dependency manifest and pinned toolchain. `TryxProof.lean` supplies the proofs; the `sorry` placeholders in `TryxChallenge.lean` define the comparison targets.

With the pinned Lean toolchain and dependencies installed, run from `Lean/`:

```sh
lake build TryxProof
lake env lean TryxProof.lean
```

[Saved Lean and nanoda acceptance](publications/collatz-paper/publication-9.24/verification-evidence.json) · [Publication waypoint](publications/collatz-paper/publication-9.24/WAYPOINT.json) · [Four-part source manifest](publications/collatz-paper/public-source-261107-v1/WAYPOINT.json)

The five Snowman declarations establish positive dyadic factorization, packet fold value one, coverage of every positive odd source address, distinct source packets, and four archived reconstructions. Retain the paper's hypotheses and scope: these results do not establish universal finite Collatz orbit termination. This packaging update performs no new Lean run.

## Edition history

Publication 9.24 corrects the cover label and publication-status wording on page 23 of the 35-page paper. Other pages and the Lean source remain unchanged. [Predecessor 9.23](publications/collatz-paper/draft-9.23/COLLATZ_REVIEW.pdf) and [earlier release v1.0.0](https://github.com/TRYX-Relay/TRYX-Collatz-Mathic/releases/tag/v1.0.0) remain preserved.
