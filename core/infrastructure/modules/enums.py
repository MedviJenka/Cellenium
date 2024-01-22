import openpyxl
from enum import Enum
from typing import Optional
from selenium.webdriver.common.by import By
from core.infrastructure.constants.data import TEST_SUITE


class Type(Enum):
    CLASS = By.CLASS_NAME
    ID = By.ID
    NAME = By.NAME
    CSS = By.CSS_SELECTOR
    XPATH = By.XPATH
    TEXT = By.LINK_TEXT


class Workbook(Enum):
    report: bool = False
    workbook: openpyxl.Workbook = openpyxl.load_workbook(TEST_SUITE)
    multiprocessing: Optional[int] = None
