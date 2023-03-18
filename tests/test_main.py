from core.infrastructure.modules.methods import generate_tests_from_excel


def test_automation() -> None:
    generate_tests_from_excel(suite_name='app1')
