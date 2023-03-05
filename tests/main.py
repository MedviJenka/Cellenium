from core.infrastructure.modules.methods import generate_tests

if __name__ == '__main__':
    generate_tests(test_dir='google', suite_name=['*'], show_test_coverage_state=True)

