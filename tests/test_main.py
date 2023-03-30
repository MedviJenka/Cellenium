from core.tools.suite_runner.suite_runner import TestSuite


suite = ['module']


def test_automation() -> None:
    run = TestSuite(suite)
    run.execute(debug=True)
