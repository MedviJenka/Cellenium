from enum import Enum
from selenium.webdriver.common.by import By


class Type(Enum):
    CLASS = By.CLASS_NAME
    ID = By.ID
    NAME = By.NAME
    CSS = By.CSS_SELECTOR
    XPATH = By.XPATH
    TEXT = By.LINK_TEXT
