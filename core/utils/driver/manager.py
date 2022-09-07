from selenium import webdriver
from dataclasses import dataclass
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from abc import ABC
from core.utils.config.reader import ConfigReader
from core.utils.excel.reader import ExcelReader
from os import system


@dataclass
class DriverManager(ABC):

    _webdriver = ChromeDriverManager()
    _options = Options()
    driver: webdriver = webdriver.Chrome(service=Service(executable_path=_webdriver.install()), options=_options)


@dataclass
class DriverEngine:

    driver = None
    excel = ExcelReader()
    config = ConfigReader()

    def wait_for_element(self, element: str, seconds=3) -> None:
        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.visibility_of_element_located(element))

    def get_element(self, sheet: str, name: str) -> driver:

        element_name = self.excel.get_name(sheet, name)
        element_locator = self.excel.get_locator(sheet, name)
        element_type = self.excel.get_type(sheet, name)

        if element_type == 'NAME':
            try:
                self.embed_image_into_cell(element_name)
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

    def embed_image_into_cell(self, element_name: str) -> None:
        path = self.config.read('path', 'screenshots')
        return self.driver.save_screenshot(fr'{ path }/{ element_name }.png')

    def teardown(self) -> None:
        try:
            self.driver.close()
            self.driver.quit()
        except not self.driver:
            system("taskkill /f /im chromedriver.exe")
            system("taskkill /f /im chrome.exe")


@dataclass
class RunTest:

    class_name: object = __name__

    def start(self, methods: list[str]) -> None:
        [getattr(self.class_name, each_method)() for each_method in methods]
