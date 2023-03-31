import uuid
from selenium.webdriver.common.by import By
global GLOBAL_PATH

# :TODO: make a class for these, solve circular import problem


GLOBAL_PATH = r'C:\Users\medvi\OneDrive\Desktop\Cellenium'

CONFIG_PATH = fr'{GLOBAL_PATH}\core\utils\data\config.ini'
PAGE_BASE = fr'{GLOBAL_PATH}\core\utils\data\page_base.xlsx'
TEST_SUITE = fr'{GLOBAL_PATH}\core\utils\data\test_suite.xlsx'
TEST_LIST = fr'{GLOBAL_PATH}\core\utils\data\test_list.json'
SCREENSHOTS = fr'{GLOBAL_PATH}\core\utils\data\screenshots\reports'
LOGS = fr'{GLOBAL_PATH}\core\utils\logs\logs.log'
ALLURE = fr'{GLOBAL_PATH}\core\utils\reports'
TESTS = fr'{GLOBAL_PATH}\tests'
JENKINS = fr'{GLOBAL_PATH}\jenkins\jenkins.war'


class Type:
    CLASS = By.CLASS_NAME
    ID = By.ID
    NAME = By.NAME
    CSS = By.CSS_SELECTOR
    XPATH = By.XPATH
    TEXT = By.LINK_TEXT


def generate_random_id() -> str:
    random_id = str(uuid.uuid4())
    return random_id
