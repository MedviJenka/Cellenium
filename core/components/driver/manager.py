from abc import ABC
from functools import wraps
import xlsxwriter
from selenium import webdriver
from dataclasses import dataclass
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdrivermanager.edge import EdgeDriverManager
from core.components.config.reader import ConfigReader
from core.components.excel.reader import ExcelReader
from os import system
from core.components.screenshots.embed_image import Screenshot
from selenium.webdriver.support.ui import Select


@dataclass
class ServiceManager:

    chrome_driver = ChromeDriverManager()
    edge_driver = EdgeDriverManager()

    def set_service(self, browser='chrome'):
        if browser:
            return Service(executable_path=self.chrome_driver.install())
        elif browser == 'edge':
            return Service(executable_path=self.edge_driver.get_latest_version())


@dataclass
class DriverManager(ABC):

    service = ServiceManager()
    _options = Options()
    driver: None = webdriver.Chrome(service=service.set_service(), options=_options)


@dataclass
class DriverEngine(DriverManager):

    excel      = ExcelReader()
    config     = ConfigReader()
    screenshot = Screenshot()

    def get_web(self, web_link: str, maximize_window=False) -> None:
        self.driver.get(web_link)
        if maximize_window:
            self.driver.maximize_window()

    def wait_for_element(self, element: str, seconds=3) -> None:
        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.visibility_of_element_located(element))

    def get_element(self, sheet: str, name: str) -> webdriver:
        element_locator = self.excel.get_locator(sheet, name)
        element_type = self.excel.get_type(sheet, name)

        if element_type == 'NAME':
            self.save_element_screenshot(sheet, name)
            return self.driver.find_element(By.NAME, element_locator)

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

    def save_element_screenshot(self, sheet: str, name: str) -> None:
        element = self.get_element(sheet, name)
        element_name = self.excel.get_name(sheet, name)
        path = self.config.read('path', 'screenshots')
        element.screenshot(f'{path}/{element_name}.jpeg')

    # def __embed_image_into_cell(self, sheet: str, name: str) -> None:
    #     path = self.config.read('path', 'screenshots')
    #     element = self.get_element(sheet, name)
    #     image_location = fr'{path}/{self.excel.get_name(sheet, name)}.png'
    #
    #     try:
    #         element.screenshot(image_location)
    #     finally:
    #         workbook = xlsxwriter.Workbook(image_location)
    #         worksheet = workbook.add_worksheet()
    #         worksheet.insert_image(self.excel.get_image(sheet, name), image_location)
    #         workbook.close()

    def dropdown(self, sheet: str, name: str, text: str = '', value: str = '') -> None:
        select = Select(self.driver.find_element(sheet, name))
        if text:
            select.select_by_value(text)
        elif value:
            select.select_by_visible_text(value)

    def validate_css_value(self, sheet: str, name: str) -> DriverManager:
        element_locator = self.excel.get_locator(sheet, name)
        return self.driver.value_of_css_property(element_locator)

    @staticmethod
    def validate() -> callable:
        @wraps
        def text() -> any:
            assert ...
        return text

    def teardown(self) -> None:
        try:
            self.driver.close()
            self.driver.quit()
        except not self.driver:
            system("taskkill /f /im chromedriver.exe")
            system("taskkill /f /im chrome.exe")
