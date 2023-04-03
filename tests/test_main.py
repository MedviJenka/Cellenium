from core.tools.suite_runner.suite_runner import TestSuite


# _list = ["call_service", "retention", ...]


def test_automation() -> None:
    run = TestSuite()
    run.execute(report=True)
