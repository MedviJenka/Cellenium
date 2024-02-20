from core.tools.suite.runner import SuiteRunner


def test_run_suite() -> None:
    run = SuiteRunner(report=False, run_with_google_sheets=True)
    run.execute()
