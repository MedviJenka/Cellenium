from dataclasses import dataclass
from core.components.driver.manager import DriverEngine
from core.components.driver.run_tests import run_single_test


@dataclass
class IntroPage(DriverEngine):

    def setup(self) -> None:
        self.get_web(web_link='https://www.google.com', maximize_window=True)

    def navigate(self):
        self.get_element('FirstPage', 'search').send_keys('cats')
        self.wait_for_element('FirstPage', 'search', seconds=3)
        self.press_keyboard_key('ENTER')

    def find_button(self):
        self.get_element('FirstPage', 'button')

    def exit_all(self) -> None:
        self.teardown()


def main() -> callable:
    run_single_test(IntroPage(), ['setup',
                                  'navigate',
                                  'find_button',
                                  'exit_all'])


if __name__ == '__main__':
    main()
