from dataclasses import dataclass
from core.utils.driver.manager import DriverManager, DriverEngine
from core.utils.driver.run_tests import RunTests
from selenium.webdriver.common.action_chains import ActionChains

@dataclass
class TestButton(DriverManager, DriverEngine):

    def setup(self) -> None:
        self.driver.get('https://st-env-03.ai-logix.net')
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        self.get_element('ST', 'user').send_keys('admin')
        self.get_element('ST', 'password').send_keys('admin')
        self.get_element('ST', 'login').click()

    def navigate(self) -> None:
        self.get_element('ST', 'calls').click()

    def _find_button(self) -> None:
        media_panel = self.get_element('ST', 'media_panel')
        height = 190
        # removing the px from the number and converting to int
        w = media_panel.value_of_css_property("width")[:-2]
        width = int(w)
        action = ActionChains(self.driver)
        action.move_to_element_with_offset(to_element=media_panel, xoffset=width/2, yoffset=height)
        action.click()
        action.perform()

    def exit_all(self) -> None:
        self.teardown()


def test() -> None:

    run_test = RunTests(class_name=TestButton())
    run_test.start(['setup',
                    'navigate',
                    '_find_button',
                    'exit_all'])


if __name__ == '__main__':
    test()
