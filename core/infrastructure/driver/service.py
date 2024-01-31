from typing import Optional
from dataclasses import dataclass
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


@dataclass
class ServiceManager:

    """
    :param: chrome_driver .............. driver.exe (for now supports only chrome)
    :param: service ...................  for now supports only chrome

    """

    service: any = Service()
    options: any = Options()
