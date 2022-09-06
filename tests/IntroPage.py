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
    methods = ['setup', 'navigate', 'find_button', 'exit_all']
    RunTest(class_name=IntroPage(), methods=methods).start()


if __name__ == '__main__':
    test()
