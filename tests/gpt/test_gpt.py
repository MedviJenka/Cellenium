from dataclasses import dataclass
from core.infrastructure.driver.engine import DriverEngine
from core.infrastructure.modules.logger import Logger


log = Logger()


@dataclass
class TestIntroPage:

    engine = DriverEngine('IntroPage')

    def test_setup(self) -> None:
        self.engine.get_web(web_link='https://chat.openai.com/', maximize_window=True)
