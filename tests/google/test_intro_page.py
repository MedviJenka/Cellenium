from core.infrastructure.driver.engine import DriverEngine



class TestIntroPage:

    engine = DriverEngine(screen='IntroPage')

    def test_setup(self) -> None:
        self.engine.get_web(web_link='https://www.google.com', maximize_window=True)

    def test_navigate(self) -> None:
        self.engine.get_element('search').send_keys('cats')
        self.engine.get_element('button').click()

    def test_exit_all(self) -> None:
        self.engine.teardown()
