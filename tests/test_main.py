from core.tools.suite_runner.suite_runner import TestSuite


suite = ['cupid']


def test_automation() -> None:
    run = TestSuite(suite)
    run.execute()
    # os.system(fr'allure serve {ALLURE}')
