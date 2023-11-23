from core.infrastructure.driver.engine import DriverEngine


engine = DriverEngine('ChatGPT')


class TestGetDataFromChatGPT:

    def test_setup(self) -> None:
        engine.get_web(web_link='https://chat.openai.com/', maximize_window=True)
        engine.get_element('login').click()


