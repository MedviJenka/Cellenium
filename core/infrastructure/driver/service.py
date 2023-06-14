from dataclasses import dataclass
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@dataclass
class ServiceManager:

    """
    :param: chrome_driver .............. driver.exe (for now supports only chrome)
    :param: edge_driver ...............  driver.exe (for now supports only chrome)
    :param: browser ...................  for now supports only chrome
    """

    chrome_driver = ChromeDriverManager()
    service = Service(executable_path=chrome_driver.install())
    options = Options()

    def __post_init__(self) -> None:
        self.options.add_argument('--ignore-ssl-errors=yes')
        self.options.add_argument('--ignore-certificate-errors')
