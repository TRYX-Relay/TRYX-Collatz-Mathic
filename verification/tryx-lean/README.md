# TRYX formula verification

This project installs the same pinned Lean, Mathlib, Comparator and independent nanoda checking pipeline used for the archived competitor review. It is an initial formalization project, not a replacement ENAID runtime or a new Mathic release.

## Initial claims

1. The v6 One-Tension identity: g + max(-(g-c-d),0) = c+d+max(g-c-d,0), for real channels.
2. The recorded decimal channels 820.87564089412, 134.87564089412 and 588 give positive remainder 98 exactly when interpreted as rationals embedded in the reals.
3. That atomic remainder is not zero. Accounting equality is therefore not confused with exhaustion.

The decimal inputs are recorded data, not an independently verified fluid quadrature. These proofs do not establish the 35-step corridor, atomic PNP implementation, temperature feedback, variable-viscosity closure, or universal Navier–Stokes regularity.

Source: locked Navier–Stokes Mathic v6, Atomic Score and Infinity Address sheets (retrieved v0.4 content). Retrieved v6 body SHA-256: 4752631cf5705669d51fae99ee0b3f025f8bdb70e9f7113926f3d389d65f562d. The locked release is unchanged.

## Run

Install elan, then from this directory:

```sh
lake exe cache get
lake build TryxProof
lake env lean TryxProof.lean
```

For independent verification, use a fresh checkout and the GitHub Actions workflow. It builds Comparator/lean4export plus pinned landrun and nanoda, then runs `lake exe comparator comparator.json` under Comparator's documented systemd/Landlock restrictions. The independent job does not compile the solution before invoking Comparator.

`TryxChallenge.lean` contains intentional reference placeholders. `TryxProof.lean` imports only Mathlib; its proof chain must not use those placeholders. Comparator checks the matching statements and permitted axioms.

## Add a formula

Write its precise mathematical statement and definitions, provide a Lean proof, and add a separately specified challenge and theorem entry. A formula alone is not a proof. Keep semantic translation review distinct from checker acceptance.

A successful build is Lean acceptance; a successful independent job adds statement/axiom comparison and nanoda checking. Infrastructure failures and timeouts are not mathematical disproofs. Save the commit, run URL and downloadable logs when reporting results. Initial status: awaiting hosted verification.
