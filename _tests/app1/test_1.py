from core.infrastructure.driver.engine import DriverEngine


class TestIntroPage:

    driver = DriverEngine(screen='IntroPage')

    def test_setup(self) -> None:
        self.driver.get_web(web_link='https://www.google.com')

    def test_navigate(self) -> None:
        self.driver.get_element('search').send_keys('adsf')
        self.driver.get_element('X').click()
        self.driver.get_element('search').send_keys('cats')
        self.driver.get_element('row1').click()
        self.driver.press_keyboard_key('ENTER')
