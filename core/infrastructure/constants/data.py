from selenium.webdriver.common.by import By


GLOBAL_PATH = r'C:\Cellenium'
CONFIG_PATH = fr'{GLOBAL_PATH}\core\utils\data\config.ini'
TEST_LIST = fr'{GLOBAL_PATH}\core\utils\data\test_list.json'
SCREENSHOTS = fr'{GLOBAL_PATH}\core\utils\data\screenshots\reports'
JENKINS = fr'{GLOBAL_PATH}\jenkins\jenkins.war'
TESTS = fr'{GLOBAL_PATH}\tests'
LOGS = fr'{TESTS}\_data\logs\logs.log'
ALLURE = fr'{TESTS}\_data\reports'
PAGE_BASE = fr'{TESTS}\_data\page_base.xlsx'
TEST_SUITE = fr'{TESTS}\_data\test_suite.xlsx'


class Type:
    CLASS = By.CLASS_NAME
    ID = By.ID
    NAME = By.NAME
    CSS = By.CSS_SELECTOR
    XPATH = By.XPATH
    TEXT = By.LINK_TEXT
