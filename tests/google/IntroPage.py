from dataclasses import dataclass
from core.components.driver.manager import DriverEngine
from core.components.driver.run_tests import RunTests


@dataclass
class IntroPage(DriverEngine):

    def setup(self):
        return self.get_web(web_driver='chrome',
                            web_link='https://www.google.com',
                            maximize_window=True)

    def navigate(self):
        return self.get_element('FirstPage', 'search').send_keys('cats')

    def find_button(self):
        self.get_element('FirstPage', 'button')

    def exit_all(self) -> None:
        self.teardown()


def main() -> None:
    run_test = RunTests()
    run_test.start(IntroPage(),
                   ['setup',
                    'navigate',
                    'find_button',
                    'exit_all'])


if __name__ == '__main__':
    main()
