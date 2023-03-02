from core.components.functional.methods import generate_tests


if __name__ == '__main__':
    generate_tests(test_dir='google',
                   suite_name=['test_dummy.py'],
                   show_test_coverage_state=False)
