from dataclasses import dataclass
from core.components.driver.engine import DriverEngine
from core.components.tests.run_tests import run_single_test


@dataclass
class IntroPage(DriverEngine):

    def setup(self) -> None:
        self.get_web(web_link='https://www.google.com', maximize_window=True)

    def navigate(self) -> None:
        self.get_element('FirstPage', 'search').send_keys('cats')
        self.take_screenshot('web2')
        self.wait_for_element('FirstPage', 'search', seconds=3)
        self.press_keyboard_key('ENTER')

    def find_button(self) -> None:
        self.get_element('FirstPage', 'button')

    def exit_all(self) -> None:
        self.teardown()


def main() -> callable:
    run_single_test(IntroPage(), ['setup', 'exit_all'])


if __name__ == '__main__':
    main()
