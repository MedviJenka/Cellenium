import os
from core.infrastructure.constants.data import ALLURE
from core.tools.suite_runner.suite_runner import TestSuite


suite = ['google', 'app1', 'module']


def test_automation() -> None:
    try:
        run = TestSuite(suite, display_coverage_state=False)
        run.execute()
    finally:
        os.system(fr'allure serve {ALLURE}')
