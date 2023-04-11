from selenium.webdriver.common.by import By


# :TODO: make a class for these, solve circular import problem


GLOBAL_PATH = r'C:\Users\medvi\OneDrive\Desktop\Cellenium'

CONFIG_PATH = fr'{GLOBAL_PATH}\core\utils\data\config.ini'
PAGE_BASE = fr'{GLOBAL_PATH}\tests\_data\page_base.xlsx'
TEST_SUITE = fr'{GLOBAL_PATH}\tests\_data\test_suite.xlsx'
TEST_LIST = fr'{GLOBAL_PATH}\core\utils\data\test_list.json'
SCREENSHOTS = fr'{GLOBAL_PATH}\core\utils\data\screenshots\reports'
LOGS = fr'{GLOBAL_PATH}\tests\_data\logs\logs.log'
ALLURE = fr'{GLOBAL_PATH}\tests\_data\reports'
TESTS = fr'{GLOBAL_PATH}\tests'
JENKINS = fr'{GLOBAL_PATH}\jenkins\jenkins.war'


class Type:
    CLASS = By.CLASS_NAME
    ID = By.ID
    NAME = By.NAME
    CSS = By.CSS_SELECTOR
    XPATH = By.XPATH
    TEXT = By.LINK_TEXT
