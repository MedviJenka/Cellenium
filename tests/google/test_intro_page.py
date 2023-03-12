from dataclasses import dataclass
from core.infrastructure.driver.engine import DriverEngine


@dataclass
class TestIntroPage:

    engine = DriverEngine('IntroPage')

    def test_setup(self) -> None:
        self.engine.get_web(web_link='https://www.google.com', maximize_window=True)

    def test_navigate(self) -> None:
        self.engine.get_element('search').send_keys('cats')
        self.engine.wait_for_element('search', seconds=3)
        self.engine.press_keyboard_key('ENTER')

    def test_exit_all(self) -> None:
        self.engine.teardown()
