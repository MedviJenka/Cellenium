from dataclasses import dataclass
from core.utils.driver.manager import DriverManager, DriverEngine, RunTest


@dataclass
class IntroPage(DriverManager, DriverEngine):

    def setup(self) -> None:
        self.driver.get('https://www.google.com')

    def navigate(self) -> None:
        self.get_element('FirstPage', 'search').send_keys('cats')

    def find_button(self) -> None:
        self.get_element('FirstPage', 'button')

    def exit_all(self) -> None:
        self.teardown()


def test() -> None:

    run_test = RunTest(class_name=IntroPage())
    run_test.start(['setup',
                    'navigate',
                    'find_button',
                    'exit_all'])


if __name__ == '__main__':
    test()
