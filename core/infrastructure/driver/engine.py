from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from core.infrastructure.tools.image_compare.image_compare_executor import ImageCompare
from core.infrastructure.modules.methods import *
from core.infrastructure.modules.reader import *
from os import system
from core.infrastructure.driver.manager import DriverManager
from core.infrastructure.constants.data import PROJECT_PATH
from dataclasses import dataclass


@dataclass
class DriverEngine(DriverManager):

    sheet_name: str

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
            write_excel(sheet_name=self.sheet_name, screenshot_path=updated_image_path)

    def wait_for_element(self, name: str, seconds=3) -> None:
        element_locator = get_locator(self.sheet_name, name)
        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.visibility_of_element_located(element_locator))

    def get_element(self, name: str) -> webdriver:
        element_locator = get_locator(self.sheet_name, name)
        element_type    = get_type(self.sheet_name, name)

        match element_type:

            case 'NAME':
                log(level=logging.DEBUG, text='element selected by NAME')
                return self.driver.find_element(By.NAME, element_locator)

            case 'ID':
                log(level=logging.DEBUG, text='element selected by ID')
                return self.driver.find_element(By.ID, element_locator)

            case 'CSS':
                return self.driver.find_element(By.CSS_SELECTOR, element_locator)

            case 'XPATH':
                return self.driver.find_element(By.XPATH, element_locator)

            case 'LINK_TEXT':
                return self.driver.find_element(By.LINK_TEXT, element_locator)

            case 'CLASS_NAME':
                return self.driver.find_element(By.CLASS_NAME, element_locator)

            case _:
                raise Exception

    def dropdown(self, text=None, value=None) -> None:
        select = Select(self.driver.get_element)
        if text:
            select.select_by_value(text)
        elif value:
            select.select_by_visible_text(value)

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
            write_json(path=image_compare_data, key="original_image_path", value=original_image_path)
            write_json(path=image_compare_data, key="actual_image_path", value=updated_image_path)
            app = ImageCompare()
            path = fr'{PROJECT_PATH}\{read_config("json", "image_compare_data")}'
            app.execute(path)

        if embed_into_cell:
            write_excel(sheet_name=self.sheet_name, screenshot_path=updated_image_path)
