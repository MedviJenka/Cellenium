from dataclasses import dataclass
from core.utils.driver.manager import DriverManager, DriverEngine
from core.utils.driver.run_tests import RunTests


@dataclass
class TestButton(DriverManager, DriverEngine):

    def setup(self) -> None:
        self.driver.get('https://www.google.com')

    def navigate(self) -> None:
        self.get_element('ST', 'calls').send_keys('cats')

    def find_button(self) -> None:
        self.get_element('ST', 'button')

    def exit_all(self) -> None:
        self.teardown()


def test() -> None:

    run_test = RunTests(class_name=TestButton())
    run_test.start(['setup',
                    'navigate',
                    'find_button',
                    'exit_all'])


if __name__ == '__main__':
    test()
