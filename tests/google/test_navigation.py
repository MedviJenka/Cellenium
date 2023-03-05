from core.infrastructure.driver.engine import DriverEngine
from core.infrastructure.modules.methods import run_test


class TestIntroPage(DriverEngine):

    __test__ = False

    def test_setup(self) -> None:
        self.get_web(web_link='https://www.terminalx.com/', maximize_window=False)

    def navigate(self) -> None:
        self.get_element('TermianlX', 'men_dropdown')

    def test_exit_all(self) -> None:
        self.teardown()


def test() -> None:
    run_test(TestIntroPage(), ['test_setup', 'test_exit_all'])
