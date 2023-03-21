from selenium.webdriver.common.by import By
import os


current_dir = os.getcwd()
path = os.path.abspath(os.path.join(current_dir, '..'))

"""
:TODO: make a class for these, solve circular import problem 
"""

PROJECT_PATH = r'C:\Cellenium'
CONFIG_PATH = fr'{PROJECT_PATH}\core\static\utils\config.ini'
PAGE_BASE = fr'{PROJECT_PATH}\core\static\utils\page_base.xlsx'
TEST_SUITE = fr'{PROJECT_PATH}\core\static\utils\test_suite.xlsx'
SCREENSHOTS = fr'{PROJECT_PATH}\core\static\screenshots\reports'
LOGS = fr'{PROJECT_PATH}\core\static\logs\logs.log'
ALLURE = fr'{PROJECT_PATH}\core\static\reports'
TESTS = fr'{PROJECT_PATH}\tests'


class Type:
    CLASS = By.CLASS_NAME
    ID = By.ID
    NAME = By.NAME
    CSS = By.CSS_SELECTOR
    XPATH = By.XPATH
    TEXT = By.LINK_TEXT
