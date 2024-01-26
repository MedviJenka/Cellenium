from core.tools.suite.runner import SuiteRunner


def test_run_suite() -> None:
    run = SuiteRunner()
    run.execute()
