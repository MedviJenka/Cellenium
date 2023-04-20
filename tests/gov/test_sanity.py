from selenium.webdriver.common.by import By
from core.infrastructure.driver.engine import DriverEngine


class TestIntroPage:

    engine = DriverEngine(screen='Gov')

    def test_setup(self) -> None:
        self.engine.get_web(web_link='https://www.gov.il', maximize_window=True)
        image = self.engine.get_element('image')
        print(image.text)
        assert image

    def test_language(self) -> None:
        self.engine.get_element('language').click()
        self.engine.dropdown(By.CLASS_NAME, 'language')

    def test_exit(self) -> None:
        self.engine.teardown()
