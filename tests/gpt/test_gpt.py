from core.infrastructure.driver.engine import DriverEngine


engine = DriverEngine('IntroPage')


class TestIntroPage:

    def test_setup(self) -> None:
        engine.get_web(web_link='https://chat.openai.com/', maximize_window=True)
