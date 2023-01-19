import xlsxwriter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from core.components.functional.methods import *
from os import system
from dataclasses import dataclass
from core.components.driver.manager import DriverManager
from core.components.tools.image_compare import CompareImages


@dataclass
class DriverEngine(DriverManager):

    def get_web(self, web_link: str, maximize_window=False) -> None:
        self.driver.get(web_link)
        if maximize_window:
            self.driver.maximize_window()

    def take_screenshot(self, name: str, compare_images=False, original_image_path=None) -> None:
        path = read_config('path', 'screenshots')
        image_compare_data = read_config('json', 'image_compare_data')
        updated_image_path = fr'{path}/{name}.png'
        self.driver.save_screenshot(updated_image_path)

        if compare_images:
            write_json(path=image_compare_data, key="original_image_path", value=original_image_path)
            write_json(path=image_compare_data, key="actual_image_path", value=updated_image_path)
            app = CompareImages()
            app.compare_images(read_config('json', 'image_compare_data'))

    def wait_for_element(self, sheet: str, name: str, seconds=3) -> None:
        element_locator = get_locator(sheet, name)
        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.visibility_of_element_located(element_locator))

    def get_element(self, sheet: str, name: str) -> webdriver:
        element_locator = get_locator(sheet, name)
        element_type    = get_type(sheet, name)
        # element_name    = self.excel.get_name(sheet, name)
        # path            = self.config.read('path', 'screenshots')

        if element_type == 'NAME':
            element = self.driver.find_element(By.NAME, element_locator)
            return element
            # try:
            #     return element
            # finally:
            #     element.screenshot(f'{path}/{element_name}.png')

        elif element_type == 'ID':
            return self.driver.find_element(By.ID, element_locator)

        elif element_type == 'CSS':
            return self.driver.find_element(By.CSS_SELECTOR, element_locator)

        elif element_type == 'XPATH':
            return self.driver.find_element(By.XPATH, element_locator)

        elif element_type == 'LINK_TEXT':
            return self.driver.find_element(By.LINK_TEXT, element_locator)

        elif element_type == 'CLASS_NAME':
            return self.driver.find_element(By.CLASS_NAME, element_locator)

    def _embed_image_into_cell(self, sheet: str, name: str) -> any:
        path = read_config('path', 'screenshots')
        element = self.get_element(sheet, name)
        image_location = fr'{path}/{get_name(sheet, name)}.png'

        try:
            return element.screenshot(image_location)

        finally:
            workbook = xlsxwriter.Workbook(image_location)
            worksheet = workbook.add_worksheet()
            worksheet.insert_image(get_image(sheet, name), image_location)
            workbook.close()

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
