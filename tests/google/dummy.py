from core.infrastructure.driver.engine import DriverEngine


class TestTitle:

    engine = DriverEngine(screen='IntroPage')

    def test_web(self) -> None:
        self.engine.get_web("https://www.google.com")
        title = self.engine.driver.title
        assert title == 'Google'
        self.engine.get_element('search').send_keys('google')
        self.engine.get_element('button').click()
        self.engine.teardown()
