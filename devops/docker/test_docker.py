import time
from selenium.webdriver.common.by import By
from core.infrastructure.driver.engine import DriverEngine
from core.infrastructure.modules.methods import log

engine = DriverEngine()


class TestIntroPage:

    def test_setup(self) -> None:
        log(text="Test Execution Started")
        engine.get_web('http://localhost:4444/wd/hub')
        time.sleep(10)
        engine.driver.get("https://www.browserstack.com/")
        time.sleep(10)
        engine.driver.find_element(By.LINK_TEXT, "Get started free").click()
        time.sleep(10)
        engine.teardown()
        print("Test Execution Successfully Completed!")
