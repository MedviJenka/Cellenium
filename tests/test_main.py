from core.infrastructure.modules.methods import generate_tests
from core.infrastructure.modules.methods import log
import allure


def test_automation() -> None:
    allure.attach(log(text="test 1"))
    generate_tests(test_dir='google', suite_name='test_dummy.py', show_test_coverage_state=True)
