from dataclasses import dataclass
from core.components.driver.engine import DriverEngine
from core.components.functional.methods import run_single_test


@dataclass
class IntroPage(DriverEngine):

    def setup(self) -> None:
        self.get_web(web_link='https://www.terminalx.com/', maximize_window=False)

    def navigate(self) -> None:
        element = self.get_element('TermianlX', 'men_dropdown')

    def exit_all(self) -> None:
        self.teardown()


def test() -> callable:
    run_single_test(IntroPage(), ['setup', 'navigate', 'exit_all'])


if __name__ == '__main__':
    test()
