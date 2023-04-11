from core.infrastructure.modules.suite_runner import TestSuite


def test_run() -> None:
    run = TestSuite()
    run.execute(report=True)
