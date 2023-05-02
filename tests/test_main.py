from core.tools.suite_runner.suite_runner import TestSuite


def test_run_suite() -> None:
    run = TestSuite()
    run.execute(report=False)
