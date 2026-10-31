"""Choose and run the smallest safe pytest subset for a Git change."""

from __future__ import annotations

import argparse
import os
import subprocess
import sys
from pathlib import Path
from typing import Sequence

PROJECT_ROOT = Path(__file__).resolve().parents[1]
ALL_TESTS = "tests"
MODULE_TO_TEST = {
    "src/auth.py": "tests/test_auth.py",
    "src/payment.py": "tests/test_payment.py",
    "src/user.py": "tests/test_user.py",
}


def _normalise(path: str) -> str:
    """Use repository-style paths regardless of the host operating system."""
    return path.replace("\\", "/").lstrip("./")


def _git_diff(base: str, head: str) -> list[str]:
    result = subprocess.run(
        ["git", "diff", "--name-only", "-z", base, head],
        cwd=PROJECT_ROOT,
        check=True,
        capture_output=True,
        text=True,
    )
    return [_normalise(path) for path in result.stdout.split("\0") if path]


def changed_files(base: str | None = None, head: str | None = None) -> tuple[list[str], str | None]:
    """Return changed files and a warning when Git history cannot be queried."""
    base = base or os.environ.get("BASE_REF") or os.environ.get("GITHUB_BASE_SHA")
    head = head or os.environ.get("HEAD_REF") or os.environ.get("GITHUB_SHA")

    attempts: list[tuple[str, str]] = []
    if base and head and not set(base) == {"0"}:
        attempts.append((base, head))
    if base and not set(base) == {"0"}:
        attempts.append((base, "HEAD"))
    attempts.append(("HEAD^", "HEAD"))

    for diff_base, diff_head in attempts:
        try:
            return _git_diff(diff_base, diff_head), None
        except (OSError, subprocess.CalledProcessError):
            continue

    return [], "Git history or the requested base reference is unavailable; running all tests."


def select_tests(files: Sequence[str]) -> tuple[list[str], str]:
    """Map changed files to tests, defaulting to all tests when unsure."""
    normalised = {_normalise(path) for path in files}
    if not normalised:
        return [ALL_TESTS], "No changed files were detected; running all tests."

    selected: set[str] = set()
    for path in normalised:
        if path in MODULE_TO_TEST:
            selected.add(MODULE_TO_TEST[path])
            continue
        return [ALL_TESTS], f"'{path}' is not a safely routable module; running all tests."

    return sorted(selected), "Only mapped application modules changed."


def run_tests(test_paths: Sequence[str]) -> int:
    """Run pytest and return its exit code unchanged."""
    command = [sys.executable, "-m", "pytest", *test_paths]
    print(f"Executing: {' '.join(command)}")
    completed = subprocess.run(command, cwd=PROJECT_ROOT)
    return completed.returncode


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--base", help="Git base commit or reference")
    parser.add_argument("--head", help="Git head commit or reference")
    args = parser.parse_args(argv)

    files, warning = changed_files(args.base, args.head)
    if warning:
        print(f"Warning: {warning}")
    print("Changed files:", ", ".join(files) if files else "(none)")
    tests, reason = select_tests(files)
    print(f"Routing decision: {reason}")
    print("Selected tests:", ", ".join(tests))
    return run_tests(tests)


if __name__ == "__main__":
    raise SystemExit(main())
