from core.tools.suite_runner.suite_runner import TestSuite


def test_automation() -> None:
    run = TestSuite()
    run.execute(report=True)
