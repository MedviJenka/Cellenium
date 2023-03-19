from core.infrastructure.modules.methods import run_test_suite


def test_automation() -> None:
    run_test_suite(suite_name=['module'])
