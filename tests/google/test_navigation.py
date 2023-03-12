from core.infrastructure.constants.data import Type
from core.infrastructure.driver.engine import DriverEngine


class TestIntroPage:

    driver = DriverEngine(sheet_name='ST')

    def setup(self) -> None:
        self.driver.get_web(web_link='https://nextgenkube.ai-logix.net/interactions', maximize_window=False)

    def test_navigate(self) -> None:
        assert self.driver.count_elements(name='table', tag='div', selector=Type.XPATH) == 100
