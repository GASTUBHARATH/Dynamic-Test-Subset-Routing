# Learnings

- Running a focused test subset can reduce feedback time when a change is
  limited to one independent module.
- A router must prefer a complete test run when it cannot confidently map a
  change. This prevents unrelated tests from being missed.
- GitHub Actions needs full history for reliable comparisons between commits.
- The same router script can be used locally and in CI by accepting explicit
  base and head references.
