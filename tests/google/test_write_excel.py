from core.infrastructure.driver.engine import DriverEngine, Element
from core.infrastructure.modules.methods import run_test


element = Element('TerminalX')


class TestIntroPage(DriverEngine):

    def test_setup(self) -> None:
        self.get_web(web_link='https://www.terminalx.com/', maximize_window=False)

    def navigate(self) -> None:
        icon = element.get_element('heart_icon')
        icon.screenshot(r'C:\Users\medvi\OneDrive\Desktop\Cellenium\icon.png')

    def exit_all(self) -> None:
        self.teardown()


def test() -> None:
    run_test(TestIntroPage(), ['test_setup', 'navigate', 'exit_all'])
