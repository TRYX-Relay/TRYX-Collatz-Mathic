# Snowman / Collatz Mathic verification

The active September 5 infinite-addressing baseline restores the internal Number-and-Fold claim; it explicitly does not assert conventional universal finite-orbit termination. The later lyrics file is marked CANDIDATE. Source locks are not changed here.

The concrete all-address mechanism is retrieved from TRYX.COLLATZ.MICRO.ALL.NUMBER.ADDRESS.TO.ONE.VPA.FOLD.CLOSURE.THEOREM.260824.1351, sections 4–7. Source SHA-256: 56e234469b1e6c381dbf41bccfb2b8c480dd7c5ae32a864e0f805eb368935813

Formal targets:

1. Every positive integer has a finite factorization 2^p U with U positive and odd.
2. Every certified packet satisfying 2^p U=3H+1 has fold residual 2^p U-3H=1.
3. Every positive odd source H has such a packet with fold value 1. This is a universally quantified address statement, not a finite enumeration.
4. Different source identities give different packets even when their fold values agree.
5. The archived fixtures H=149,213,218453,611669 reconstruct exactly with (p,U)=(6,7),(7,5),(17,5),(18,7).

The packet retains its source, exponent, odd carrier, positivity/parity facts and reconstruction witness. This formalization does not identify that record with scalar 1, implement the complete AMM or C4 machinery, or claim a finite Collatz path from H to 1.

The source distinguishes direct number addresses from inverse-orbit addresses. The algebraic residual is 1; the odd successor U can be different from 1. Conventional termination would require a further proof relating the internal construction to a finite sequence of actual Collatz steps for every positive input. No such proof is supplied or assumed here.

The challenge states exactly these limited claims; the proof module supplies their derivations. Comparator/nanoda and axiom inspection use the existing pipeline. Initial status: awaiting hosted verification.
