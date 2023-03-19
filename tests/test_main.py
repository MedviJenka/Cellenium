from core.tools.suite_runner.suite_runner import RunSuite


def test_automation() -> None:
    run = RunSuite(['module', 'app1'])
    run.execute()
