import os
from core.infrastructure.constants.data import ALLURE
from core.tools.suite_runner.suite_runner import TestSuite


suite = ['app1']


def test_automation() -> None:
    run = TestSuite(suite, display_coverage_state=True)
    run.execute()
    os.system(fr'allure serve {ALLURE}')
