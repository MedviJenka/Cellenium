from abc import ABC
from selenium import webdriver
from dataclasses import dataclass
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from core.components.config.reader import ConfigReader
from core.components.driver.run_tests import RunTests
from core.components.excel.reader import ExcelReader
from core.components.screenshots.embed_image import Screenshot
from functools import wraps


@dataclass
class DriverManager(ABC):

    _driver = ChromeDriverManager()
    _options = Options()
    driver: None = webdriver.Chrome(service=Service(_driver.install()), options=_options)


@dataclass
class DriverEngine(DriverManager):

    excel = ExcelReader()
    config = ConfigReader()
    screenshot = Screenshot()

    @staticmethod
    def setup(func) -> any:
        @wraps(func)
        def get_web(web_link='https://www.google.com', web_driver='chrome', maximize_window=False) -> None:
            if web_driver:
                DriverManager.driver.get(web_link)

                if maximize_window:
                    DriverManager.driver.maximize_window()
            func()
        return get_web


@dataclass
class IntroPage(DriverEngine):

    @DriverEngine.setup
    def setup(self) -> None: ...


def main() -> None:
    run_test = RunTests()
    run_test.start(IntroPage(), ['setup'])


if __name__ == '__main__':
    main()
