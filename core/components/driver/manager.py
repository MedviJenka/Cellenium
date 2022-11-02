from abc import ABC
import xlsxwriter
from selenium import webdriver
from dataclasses import dataclass
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from core.components.config.reader import ConfigReader
from core.components.excel.reader import ExcelReader
from os import system
from core.components.screenshots.embed_image import Screenshot


@dataclass
class ServiceManager:

    chrome_driver = ChromeDriverManager()

    def set_service(self, value='chrome'):
        if value:
            return Service(executable_path=self.chrome_driver.install())
        else:
            ...


@dataclass
class DriverManager(ABC):

    service = ServiceManager()
    _options = Options()
    driver: None = webdriver.Chrome(service=service.set_service(), options=_options)


@dataclass
class DriverEngine(DriverManager):

    excel = ExcelReader()
    config = ConfigReader()
    screenshot = Screenshot()

    def get_web(self, web_link: str, maximize_window=False) -> None:
        if self.driver:
            self.driver.get(web_link)
            if maximize_window:
                self.driver.maximize_window()

    def wait_for_element(self, element: str, seconds=3) -> None:
        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.visibility_of_element_located(element))

    def get_element(self, sheet: str, name: str) -> DriverManager().driver:
        # element_name = self.excel.get_name(sheet, name)
        element_locator = self.excel.get_locator(sheet, name)
        element_type = self.excel.get_type(sheet, name)
        element_image = self.excel.get_image(sheet, name)

        if element_type == 'NAME':
            try:
                self.embed_image_into_cell(sheet, name, element_image)
            finally:
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

    def embed_image_into_cell(self, *args) -> None:
        path = self.config.read('path', 'screenshots')
        image_location = fr'{path}/{self.excel.get_name(*args)}.png'
        try:
            return self.driver.save_screenshot(image_location)
        finally:
            workbook = xlsxwriter.Workbook(image_location)
            worksheet = workbook.add_worksheet()
            worksheet.insert_image(self.excel.get_image(*args), image_location)
            workbook.close()

    def teardown(self) -> None:
        try:
            self.driver.close()
            self.driver.quit()
        except not self.driver:
            system("taskkill /f /im chromedriver.exe")
            system("taskkill /f /im chrome.exe")
