from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from core.tools.image_compare.image_compare_executor import ImageCompare
from core.infrastructure.modules.methods import *
from core.infrastructure.modules.reader import *
from os import system
from core.infrastructure.driver.manager import DriverManager
from core.infrastructure.constants.data import PROJECT_PATH, Type
from dataclasses import dataclass


@dataclass
class DriverEngine(DriverManager):

    screen: str

    def get_web(self, web_link: str, maximize_window=False) -> None:
        self.driver.get(web_link)
        if maximize_window:
            self.driver.maximize_window()

    def take_screenshot(self,
                        element: WebElement,
                        name: str,
                        compare_images=False,
                        embed_into_cell=True,
                        original_image_path=None) -> None:

        path = fr"{PROJECT_PATH}\{read_config('path', 'screenshots')}"
        image_compare_data = fr"{PROJECT_PATH}\{read_config('json', 'image_compare_data')}"
        updated_image_path = fr'{path}\{name}.png'
        element.screenshot(updated_image_path)

        if compare_images:
            write_json(path=image_compare_data, key="original_image_path", value=original_image_path)
            write_json(path=image_compare_data, key="actual_image_path", value=updated_image_path)
            app = ImageCompare()
            path = fr'{PROJECT_PATH}\{read_config("json", "image_compare_data")}'
            app.execute(path)

        if embed_into_cell:
            write_excel(sheet_name=self.screen, screenshot_path=updated_image_path)

        log(text=f"screenshot location: {updated_image_path}")

    def wait_for_element(self, name: str, seconds=3) -> None:
        element_locator = get_locator(self.screen, name)
        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.visibility_of_element_located(element_locator))

    def get_element(self, name: str) -> webdriver:

        element_locator = get_locator(self.screen, name)
        element_type    = get_type(self.screen, name)

        match element_type:

            case 'NAME':
                log(level=logging.DEBUG, text='element selected by NAME')
                return self.driver.find_element(Type.NAME, element_locator)

            case 'ID':
                log(level=logging.DEBUG, text='element selected by ID')
                return self.driver.find_element(Type.ID, element_locator)

            case 'CSS':
                return self.driver.find_element(Type.CSS, element_locator)

            case 'XPATH':
                return self.driver.find_element(Type.XPATH, element_locator)

            case 'LINK_TEXT':
                return self.driver.find_element(Type.TEXT, element_locator)

            case 'CLASS_NAME':
                return self.driver.find_element(Type.CLASS, element_locator)

            case _:
                raise Exception

    def dropdown(self, text=None, value=None) -> None:
        select = Select(self.driver.get_element)
        if text:
            select.select_by_value(text)
        elif value:
            select.select_by_visible_text(value)

    def count_elements(self, name: str, tag: str, selector: Type) -> int:

        """
        :param: name ............... name is retrieved from get_element()
        :param: tag ................ div, tr, etc... type it as it is
        :param: selector ........... inherits By class
        """

        table = self.get_element(name)
        rows = len(table.find_elements(selector, f'.//{tag}'))
        print(fr'number of rows in this page is: {rows}')
        log(level=logging.INFO, text=f'number of rows: {rows}')
        return rows

    def press_keyboard_key(self, key: str) -> ActionChains:
        action = ActionChains(self.driver)
        press = action.key_down(Keys.CONTROL).send_keys(key).key_up(Keys.CONTROL)
        return press.perform()

    def teardown(self) -> None:
        try:
            self.driver.close()
            self.driver.quit()
        except not self.driver:
            system("taskkill /f /im chromedriver.exe")
            system("taskkill /f /im chrome.exe")
            raise Exception("driver's N/A")

    def scroll_page(self, direction: str, px: int) -> None:

        """
        :param: px ................ pixels
        :param: up ................ px = negative number
        :param: down .............. px = positive number
        """

        match direction:
            case "up":
                self.driver.execute_script(f"window.scrollBy(0, {px});")

            case "down":
                self.driver.execute_script(f"window.scrollBy(0, {px});")

    def attach_screenshot(self) -> None:
        self.driver.save_screenshot(PROJECT_PATH)


@dataclass
class ScreenshotEngine(DriverManager):

    sheet_name: str

    def take_screenshot(self,
                        element: WebElement,
                        name: str,
                        compare_images=False,
                        embed_into_cell=True,
                        original_image_path=None) -> None:

        path = fr"{PROJECT_PATH}\{read_config('path', 'screenshots')}"
        image_compare_data = fr"{PROJECT_PATH}\{read_config('json', 'image_compare_data')}"
        updated_image_path = fr'{path}\{name}.png'
        element.screenshot(updated_image_path)

        if compare_images:
            app = ImageCompare()
            write_json(path=image_compare_data, key="original_image_path", value=original_image_path)
            write_json(path=image_compare_data, key="actual_image_path", value=updated_image_path)
            path = fr'{PROJECT_PATH}\{read_config("json", "image_compare_data")}'
            app.execute(path)

        if embed_into_cell:
            write_excel(sheet_name=self.sheet_name, screenshot_path=updated_image_path)
