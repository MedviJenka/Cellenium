from abc import ABC
from selenium import webdriver
from dataclasses import dataclass
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
global driver


@dataclass
class ServiceManager:

    """
    :param: chrome_driver .............. driver.exe (for now supports only chrome)
    :param: edge_driver ...............  driver.exe (for now supports only chrome)
    :param: browser ...................  for now supports only chrome
    """

    chrome_driver = ChromeDriverManager()
    edge_driver = EdgeChromiumDriverManager()

    def set_service(self, browser='chrome'):
        if browser:
            return Service(executable_path=self.chrome_driver.install())
        elif browser == 'edge':
            return Service(executable_path=self.edge_driver.install())


class DriverManager(ABC):

    _service = ServiceManager()
    _options = Options()
    driver: webdriver = webdriver.Chrome(service=_service.set_service(), options=_options)
