from core.tools.suite_runner.suite_runner import RunSuite


def test_automation() -> None:
    run = RunSuite(['app1', 'module'], display_coverage_state=True)
    run.execute()
