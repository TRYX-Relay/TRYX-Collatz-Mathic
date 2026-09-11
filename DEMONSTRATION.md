# Demonstration walkthrough: Collatz conjecture research — Snowman Mathic and Lean 4 verification

Author: Virgil Lee Gattenby

This is a recording guide and reproducible walkthrough. It is not a prerecorded video.

1. Open the score linked from the main README. Show the chart or score and its notation before introducing the result.
2. Open the manuscript and identify the exact local-closure claim and its scope.
3. From the repository root, run:

```sh
python3 publications/collatz-mathic/check_package.py
```

4. Show the actual terminal output, including any failure. Explain that the command checks archived bytes, replay consistency, and deliberate corruption detection. It does not execute Lean.
5. Open the Lean proof source and the linked Actions workflow. Show the theorem statement and the corresponding checker results separately from the Python replay.
6. Close with the review question: Do the retained packets reconstruct correctly, fold to the stated identity, and reject the corrupted packet?

For a short recording, spend roughly 15 seconds on the score, 30 seconds on the command and output, and 15 seconds on the proof scope and repository link. Leave longer runs uncut or clearly disclose any edits.

The NS replay does not independently regenerate a fluid simulation. PNP semantic closure does not establish a conventional polynomial-time bound. Collatz address-fold closure does not establish termination of every Collatz orbit.
