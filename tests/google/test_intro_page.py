from core.infrastructure.driver.engine import DriverEngine


# TODO: find why i cant put engine as init
engine = DriverEngine('IntroPage')


class TestIntroPage:

    def test_setup(self) -> None:
        engine.get_web(web_link='https://www.google.com', maximize_window=True)

    def test_navigate(self) -> None:
        engine.get_element('search').send_keys('cats')
        engine.wait_for_element('search', seconds=3)
        engine.press_keyboard_key('ENTER')

    def test_exit_all(self) -> None:
        engine.teardown()
