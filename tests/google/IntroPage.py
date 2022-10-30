from dataclasses import dataclass
from core.components.driver.manager import DriverManager, DriverEngine
from core.components.driver.run_tests import RunTests


@dataclass
class IntroPage(DriverManager, DriverEngine):

    def setup(self):
        return self.get_web('https://www.google.com')

    def navigate(self):
        return self.get_element('FirstPage', 'search').send_keys('cats')

    def find_button(self):
        self.get_element('FirstPage', 'button')

    def exit_all(self) -> None:
        self.teardown()


def test() -> None:
    run_test = RunTests()
    run_test.start(IntroPage(),
                   ['setup',
                    'navigate',
                    'find_button',
                    'exit_all'])


if __name__ == '__main__':
    test()
