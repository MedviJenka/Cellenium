from core.infrastructure.driver.engine import DriverEngine


class TestTipalti:

    engine = DriverEngine(screen='tipalti')

    def test_web(self) -> None:
        self.engine.get_web("https://tipalti.com/en-uk/")

    def test_navigation(self) -> None:
        self.engine.get_dynamic_element('class', 'ap_automation').click()

