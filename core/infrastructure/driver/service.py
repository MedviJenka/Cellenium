from typing import Optional
from dataclasses import dataclass
from selenium.webdriver import ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@dataclass
class ServiceManager:

    """
    :param: chrome_driver .............. driver.exe (for now supports only chrome)
    :param: service ...................  for now supports only chrome

    """

    versions = {
        'old': '114.0.5735.90',
        'current': '119.0.6045.105'
    }

    chrome_driver: any = ChromeDriverManager(driver_version=versions['current'])
    service: any = Service(executable_path=chrome_driver.install())
    options: any = ChromeOptions()
    enable_options: Optional[bool] = False

    def __enable_options(self) -> None:
        self.options.add_experimental_option("excludeSwitches", ["enable-automation"])
        # self.options.add_argument('--headless')
        # self.options.add_argument("start-maximized")
        # self.options.add_experimental_option('useAutomationExtension', False)
        # self.preferences = {"download.default_directory": GLOBAL_PATH}
        # self.options.add_experimental_option("prefs", preferences)
        # self.options.add_experimental_option("debuggerAddress", "127.0.0.1:8080")

    def enable_advanced_options(self) -> None:
        match self.enable_options:
            case True:
                self.__enable_options()
            case _:
                ...
