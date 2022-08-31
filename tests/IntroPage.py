from dataclasses import dataclass
from core.utils.driver.manager import DriverManager, Engine, RunMethods


@dataclass
class IntroPage(DriverManager, Engine):

    def setup(self) -> None:
        self.driver.get('https://www.google.com')

    def navigate(self) -> None:
        self.get_element('FirstPage', 'search').send_keys('cats')

    def exit_all(self):
        self.teardown()


def test() -> None:
    methods = ['setup', 'navigate', 'exit_all']
    RunMethods(class_name=IntroPage(), methods=methods).start()


if __name__ == '__main__':
    test()
