from dataclasses import dataclass
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@dataclass
class ServiceManager:

    """
    :TODO: fix try if statements with older version and newer, because currently it doesnt work

    :param: chrome_driver .............. driver.exe (for now supports only chrome)
    :param: service ...................  for now supports only chrome

    """

    # older_version = '114.0.5735.90'
    chrome_driver = ChromeDriverManager()
    service = Service(executable_path=chrome_driver.install())
    options = Options()
    options.add_argument('--headless')
