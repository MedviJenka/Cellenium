from dataclasses import dataclass
from selenium import webdriver
from core.infrastructure.driver.service import ServiceManager


@dataclass
class DriverManager(ServiceManager):

    def __post_init__(self) -> None:
        self.driver: webdriver = webdriver.Chrome(service=self.service)
