from dataclasses import dataclass
from selenium import webdriver

from core.infrastructure.constants.data import COOKIES
from core.infrastructure.driver.service import ServiceManager
from core.infrastructure.modules.reader import read_json


@dataclass
class DriverManager(ServiceManager):

    """
    This class extends the `ServiceManager` class and provides a convenient way to initialize and manage
    a Selenium web driver instance.


    :params: driver (webdriver) .................... The Selenium web driver instance.
    :args: service (Service) ....................... The service object to use for managing the driver.
                                                     It should be an instance of
                                                     a class that extends the `Service` class from
                                                     the `selenium.webdriver` module.

    """

    def __post_init__(self) -> None:

        self.driver: webdriver = webdriver.Chrome(service=self.service, options=self.options)
        self.cookies = [read_json(COOKIES)]
        self.driver.get("https://chat.openai.com/")

        for cookie in self.cookies:

            if isinstance(cookie, dict) and 'name' in cookie and 'value' in cookie:
                self.driver.add_cookie(cookie)
            else:
                print(f"Invalid cookie format: {cookie}")
