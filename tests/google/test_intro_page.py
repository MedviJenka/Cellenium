from core.infrastructure.driver.engine import DriverEngine
from core.tools.image_compare.image_compare_executor import ImageCompare


class TestIntroPage:

    engine = DriverEngine(screen='IntroPage')

    def test_setup(self) -> None:
        self.engine.get_web(web_link='https://www.google.com', maximize_window=True)

    def test_navigate(self) -> None:
        self.engine.get_element('search').send_keys('cats')
        self.engine.get_element('button').click()
        self.engine.switch_to_new_tab('https://www.gmail.com')

    def test_image_compare(self) -> None:
        image_compare = ImageCompare()
        image_compare.execute()

    def test_exit_all(self) -> None:
        self.engine.teardown()
