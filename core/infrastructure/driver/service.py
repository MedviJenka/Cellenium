from dataclasses import dataclass
from typing import Optional
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


@dataclass
class ServiceManager:

    version: Optional[str] = None
    use_chrome_driver_manager: Optional[bool] = False
    chrome = ChromeDriverManager()
    options: Options = Options()
    service: Service = Service()

    def __post_init__(self) -> None:
        if self.use_chrome_driver_manager:
            self.chrome = ChromeDriverManager(version=self.version)
            self.service: Service = Service(executable_path=self.chrome.install())
