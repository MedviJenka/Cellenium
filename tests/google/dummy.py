from core.infrastructure.driver.engine import DriverEngine


class TestTitle:

    engine = DriverEngine()

    def test_web(self) -> None:
        self.engine.get_web("https://www.google.com")
        title = self.engine.driver.title
        assert title == 'Google'
        self.engine.teardown()
