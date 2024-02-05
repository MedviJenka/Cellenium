from core.infrastructure.driver.engine import DriverEngine


class TestTitle:

    engine = DriverEngine(screen='Google')

    def test_web(self) -> None:
        self.engine.get_web("https://www.google.com")
        title = self.engine.driver.title
        self.engine.get_element('search').send_keys('cats')
        self.engine.get_element('button').click()
        self.engine.teardown()
        assert title == 'Google'
