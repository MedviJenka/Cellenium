from time import sleep

from selenium.webdriver.common.by import By

from core.infrastructure.driver.engine import DriverEngine


engine = DriverEngine(screen='ChatGPT')


class TestGetDataFromChatGPT:

    def test_setup(self) -> None:
        engine.get_web(web_link='https://chat.openai.com/', maximize_window=True)

    def test_load_cookies(self) -> None:
        engine.load_cookies()
        engine.driver.refresh()
        engine.save_storage()
        engine.load_storage()
        sleep(10)

    def test(self) -> None:
        print(engine.driver.find_element(By.XPATH, '//*[@id="__next"]/div[1]/div[2]/main/div[2]/div[1]/div/div[2]/div[2]').text)
