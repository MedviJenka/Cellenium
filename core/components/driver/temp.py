from selenium import webdriver
from dataclasses import dataclass
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from core.components.config.reader import ConfigReader
from core.components.excel.reader import ExcelReader
from os import system
from core.components.screenshots.embed_image import Screenshot


@dataclass
class ServiceManager:

    chrome_webdriver  = ChromeDriverManager()
    chrome_options    = ChromeOptions()
    # edge_webdriver    = EdgeChromiumDriverManager()
    # edge_options      = EdgeOptions()

    def get_service(self, value='chrome_driver'):
        if value:
            return Service(executable_path=self.chrome_webdriver.install())
        # elif value == 'edge_driver':
        #     return Service(executable_path=self.edge_webdriver.install())


@dataclass
class DriverManager:

    service = ServiceManager()
    chrome_driver:  None = webdriver.Chrome(service=service.get_service(), options=service.chrome_options)
    # edge_driver:    None = webdriver.ChromiumEdge(service=service.get_service('edge_driver'), options=service.edge_options)


@dataclass
class DriverEngine(DriverManager):

    excel          = ExcelReader()
    config         = ConfigReader()
    screenshot     = Screenshot()

    def get_web(self, web_link: str, web_driver='chrome', maximize_window=False) -> None:

        if web_driver:
            self.chrome_driver.get(web_link)
            if maximize_window:
                self.chrome_driver.maximize_window()
        #
        # elif web_driver == 'edge':
        #     self.edge_driver.get(web_link)
        #     if maximize_window:
        #         self.edge_driver.maximize_window()

        else:
            raise 'no webdriver available'

    def wait_for_element(self, element: str, seconds=3) -> None:
        wait = WebDriverWait(self.edge_driver, seconds)
        wait.until(expected_conditions.visibility_of_element_located(element))

    def get_element(self, sheet: str, name: str):
        # element_name = self.excel.get_name(sheet, name)
        element_locator = self.excel.get_locator(sheet, name)
        element_type = self.excel.get_type(sheet, name)
        element_image = self.excel.get_image(sheet, name)

        if element_type == 'NAME':
            if self.chrome_driver:
                return self.chrome_driver.find_element(By.NAME, element_locator)
            # elif self.edge_driver:
            #     return self.edge_driver.find_element(By.NAME, element_locator)

        # elif element_type == 'ID':
        #     return self.edge_driver.find_element(By.ID, element_locator)
        # elif element_type == 'CSS':
        #     return self.edge_driver.find_element(By.CSS_SELECTOR, element_locator)
        # elif element_type == 'XPATH':
        #     return self.edge_driver.find_element(By.XPATH, element_locator)
        # elif element_type == 'LINK_TEXT':
        #     return self.edge_driver.find_element(By.LINK_TEXT, element_locator)
        # elif element_type == 'CLASS_NAME':
        #     return self.edge_driver.find_element(By.CLASS_NAME, element_locator)

    # def embed_image_into_cell(self, *args) -> None:
    #     path = self.config.read('path', 'screenshots')
    #     image_location = fr'{path}/{self.excel.get_name(*args)}.png'
    #     try:
    #         return self.chrome_driver.save_screenshot(image_location)
    #     finally:
    #         workbook = xlsxwriter.Workbook(image_location)
    #         worksheet = workbook.add_worksheet()
    #         worksheet.insert_image(self.excel.get_image(*args), image_location)
    #         workbook.close()

    def teardown(self) -> None:

        if self.chrome_driver:
            try:
                self.chrome_driver.close()
                self.chrome_driver.quit()
            except not self.chrome_driver:
                system("taskkill /f /im chromedriver.exe")
                system("taskkill /f /im chrome.exe")

        # elif self.edge_driver:
        #     try:
        #         self.edge_driver.close()
        #         self.edge_driver.quit()
        #     except not self.edge_driver:
        #         system("taskkill /f /im msedgedriver.exe")
