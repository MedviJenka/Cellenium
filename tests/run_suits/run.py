from core.components.functional.methods import generate_test


if __name__ == '__main__':
    generate_test(test_dir='google',
                  suite_name=[
                      'test_dummy.py',
                      'test_dummy2.py',
                      'test_intro_page.py',
                      'test_navigation.py'
                  ],
                  show_test_coverage_state=True)
