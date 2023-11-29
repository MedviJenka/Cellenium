from dataclasses import dataclass
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@dataclass
class ServiceManager:

    """
    :TODO: fix webdriver version ........................ WIP

    :param: chrome_driver .............. driver.exe (for now supports only chrome)
    :param: service ...................  for now supports only chrome

    """

    # older_version = '114.0.5735.90'
    chrome_driver = ChromeDriverManager()
    service = Service(executable_path=chrome_driver.install())
    options = Options()

    def __post_init__(self) -> None:
        self.options.add_argument('--headless')
