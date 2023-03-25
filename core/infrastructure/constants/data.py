from selenium.webdriver.common.by import By


# :TODO: make a class for these, solve circular import problem


PROJECT_PATH = r'C:\Users\medvi\OneDrive\Desktop\Cellenium'
CONFIG_PATH = fr'{PROJECT_PATH}\core\utils\data\config.ini'
PAGE_BASE = fr'{PROJECT_PATH}\core\utils\data\page_base.xlsx'
TEST_SUITE = fr'{PROJECT_PATH}\core\utils\data\test_suite.xlsx'
SCREENSHOTS = fr'{PROJECT_PATH}\core\utils\data\screenshots\reports'
LOGS = fr'{PROJECT_PATH}\core\utils\data\logs\logs.log'
ALLURE = fr'{PROJECT_PATH}\core\utils\reports'
TESTS = fr'{PROJECT_PATH}\tests'
JENKINS = fr'{PROJECT_PATH}\jenkins\jenkins.war'


class Type:
    CLASS = By.CLASS_NAME
    ID = By.ID
    NAME = By.NAME
    CSS = By.CSS_SELECTOR
    XPATH = By.XPATH
    TEXT = By.LINK_TEXT
