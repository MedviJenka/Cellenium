from selenium import webdriver
from dataclasses import dataclass
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from abc import ABC
from core.utils.excel.reader import ExcelReader
from core.utils.exceptions.exceptions import NoSuchTypeException
from os import system


class DriverManager(ABC):

    _webdriver = ChromeDriverManager()
    _options = Options()
    driver: webdriver = webdriver.Chrome(service=Service(executable_path=_webdriver.install()), options=_options)


@dataclass
class Engine:

    driver = None
    excel = ExcelReader()

    def wait_for_element(self, element: str, seconds=3) -> None:
        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.presence_of_element_located(element))

    def get_element(self, sheet: str, name: str) -> driver:
        element = self.excel.read(sheet, name)['locator']
        try:
            self.wait_for_element(element)
        except NoSuchTypeException as e:
            raise e
        finally:
            if self.excel.read(sheet, name)['type'] == 'NAME':
                return self.driver.find_element(By.NAME, element)
            elif self.excel.read(sheet, name)['type'] == 'ID':
                return self.driver.find_element(By.ID, element)
            elif self.excel.read(sheet, name)['type'] == 'CSS':
                return self.driver.find_element(By.CSS_SELECTOR, element)
            elif self.excel.read(sheet, name)['type'] == 'XPATH':
                return self.driver.find_element(By.XPATH, element)

    def embed_image_into_cell(self, sheet_name) -> None:
        ...

    def teardown(self) -> None:
        if self.driver:
            self.driver.close()
            self.driver.quit()
        else:
            system("taskkill /f /im chromedriver.exe")
            system("taskkill /f /im chrome.exe")


@dataclass
class RunMethods:

    class_name: object
    methods: list[str]

    def start(self):
        for each_method in self.methods:
            getattr(self.class_name, each_method)()

        # [getattr(self.class_name, each_method)() for each_method in self.methods]
