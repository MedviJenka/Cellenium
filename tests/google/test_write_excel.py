from core.infrastructure.driver.engine import DriverEngine, ScreenshotEngine


class TestIntroPage:

    engine = DriverEngine('TerminalX')

    def test_setup(self) -> None:
        self.engine.get_web(web_link='https://www.terminalx.com/', maximize_window=False)

    def test_navigate(self) -> None:

        self.engine.scroll_page(direction='down', px=-500)

        # heart_icon = self.engine.get_element('heart_icon')
        # suite_case = self.engine.get_element('suite_case')
        # welcome = self.engine.get_element('welcome')
        #
        # screen.take_screenshot(element=heart_icon, name='heart_icon')
        # screen.take_screenshot(element=suite_case, name='suite')
        # screen.take_screenshot(element=welcome, name='welcome')

    def test_exit_all(self) -> None:
        self.engine.teardown()
