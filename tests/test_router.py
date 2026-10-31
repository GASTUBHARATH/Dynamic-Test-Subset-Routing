from router.test_router import select_tests


def test_auth_change_selects_only_auth_tests():
    assert select_tests(["src/auth.py"]) == (
        ["tests/test_auth.py"],
        "Only mapped application modules changed.",
    )


def test_multiple_module_changes_select_matching_tests():
    tests, _ = select_tests(["src/user.py", "src/payment.py"])
    assert tests == ["tests/test_payment.py", "tests/test_user.py"]


def test_unknown_or_shared_change_runs_full_suite():
    tests, _ = select_tests(["requirements.txt"])
    assert tests == ["tests"]


def test_empty_change_set_runs_full_suite():
    tests, _ = select_tests([])
    assert tests == ["tests"]
