from dataclasses import dataclass
from core.components.driver.manager import DriverEngine
from core.components.driver.run_tests import run_single_test
from core.components.config.reader import ConfigReader
from core.components.excel.reader import ExcelReader


@dataclass
class App(DriverEngine):

    config = ConfigReader()
    excel = ExcelReader()

    def startup(self) -> None:
        self.get_web(web_link='https://www.google.com', maximize_window=True)

    def test1(self) -> None:
        element = self.get_element('FirstPage', 'search')
        element.send_keys('test')

    def exit(self) -> None:
        self.teardown()


def test() -> None:
    run_single_test(class_name=App(),
                    methods=['startup',
                             'test1',
                             'exit'])


if __name__ == "__main__":
    test()
