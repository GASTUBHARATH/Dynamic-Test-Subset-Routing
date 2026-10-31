# Dynamic Test-Subset Routing

This beginner-friendly project uses Git changes to run only the relevant
Pytest files. It contains independent authentication, payment, and user
modules, plus a routing engine used locally and in GitHub Actions.

## Run locally

The existing `venv` is preserved. Activate it, install the requirements, and
run the full suite:

```powershell
.\venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -m pytest
```

To route tests between two Git references:

```powershell
python router/test_router.py --base HEAD~1 --head HEAD
```

The router maps `src/auth.py`, `src/payment.py`, and `src/user.py` to their
matching test files. Multiple mapped changes select multiple files. Changes
to tests, configuration, workflows, documentation, or unknown source files
run `tests` as a safe fallback. Missing Git history also falls back to the
complete suite.

## Project layout

- `src/`: application code
- `tests/`: application and router tests
- `router/test_router.py`: Git diff and Pytest execution engine
- `.github/workflows/test-routing.yml`: pull request and `main` push workflow

## GitHub Actions

The workflow checks out full history, installs the pinned dependency range,
and supplies the pull request or push base and head commits to the router.
The router prints changed files, the routing decision, selected tests, and
returns Pytest's exit code.
