from dataclasses import dataclass
from core.infrastructure.driver.engine import DriverEngine
from core.infrastructure.modules.methods import run_test


@dataclass
class IntroPage(DriverEngine):

    def setup(self) -> None:
        self.get_web(web_link='https://www.google.com', maximize_window=True)

    def test_screenshot_method(self) -> None:
        element = self.get_element('FirstPage', 'search').send_keys('cats')
        self.take_screenshot(name=element,
                             compare_images=True,
                             original_image_path=r"C:\Users\medvi\OneDrive\Desktop\Screenshot.png")

    def navigate(self) -> None:
        self.get_element('FirstPage', 'search').send_keys('cats')
        self.take_screenshot('web2')
        self.wait_for_element('FirstPage', 'search', seconds=3)
        self.press_keyboard_key('ENTER')

    def exit_all(self) -> None:
        self.teardown()


def test() -> callable:
    run_test(IntroPage(), ['setup', 'test_screenshot_method', 'exit_all'])

