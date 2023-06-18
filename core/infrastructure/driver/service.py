from dataclasses import dataclass
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@dataclass
class ServiceManager:

    """
    :param: chrome_driver .............. driver.exe (for now supports only chrome)
    :param: service ...................  for now supports only chrome
    """

    chrome_driver = ChromeDriverManager()
    service = Service(executable_path=chrome_driver.install())
