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

    chrome_driver = ChromeDriverManager(driver_version=versions['current'])
    service = Service(executable_path=chrome_driver.install())
    options = ChromeOptions()
    # options.add_argument('--headless')
    # options.add_argument("start-maximized")
    # options.add_experimental_option("excludeSwitches", ["enable-automation"])
    # options.add_experimental_option('useAutomationExtension', False)
