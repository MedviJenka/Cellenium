from dataclasses import dataclass
from core.components.driver.engine import DriverEngine
from core.components.functional.methods import run_single_test
from core.components.tools.image_compare import CompareImages


@dataclass
class IntroPage(DriverEngine):

    def setup(self) -> None:
        self.get_web(web_link='https://www.google.com', maximize_window=True)

    def navigate(self) -> None:
        self.get_element('FirstPage', 'search').send_keys('cats')
        self.take_screenshot('web2')
        self.wait_for_element('FirstPage', 'search', seconds=3)
        self.press_keyboard_key('ENTER')

    @staticmethod
    def compare() -> None:
        compare_images = CompareImages()
        compare_images.find_difference(r'C:\Users\medvi\IdeaProjects\CelleniumProject\core\static\json\data.json')

    def find_button(self) -> None:
        self.get_element('FirstPage', 'button')

    def exit_all(self) -> None:
        self.teardown()


def test() -> callable:
    run_single_test(IntroPage(), ['setup', 'exit_all'])


if __name__ == '__main__':
    test()
