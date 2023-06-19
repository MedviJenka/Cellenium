from core.tools.suite.runner import SuiteRunner


def run_suite() -> None:
    run = SuiteRunner(report=True)
    run.execute()


run_suite()
