from core.components.functional.methods import generate_allure_report


if __name__ == '__main__':
    generate_allure_report('google', ['test_dummy.py'], show_test_coverage_state=True)
