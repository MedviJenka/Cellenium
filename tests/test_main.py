from core.tools.suite.cloud_runner import SuiteRunnerAPI


def test_run_suite() -> None:
    run = SuiteRunnerAPI()
    run.execute()
