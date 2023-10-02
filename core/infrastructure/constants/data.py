import os
from selenium.webdriver.common.by import By


# Full project path which used to strip to get global path
abstract_dir = os.path.dirname(os.path.abspath(__file__))

# Automation
GLOBAL_PATH = abstract_dir.split('core')[0][:-1]
TESTS = fr'{GLOBAL_PATH}\tests'
CONFIG_PATH = fr'{GLOBAL_PATH}\core\utils\data\config.ini'
TEST_LIST = fr'{GLOBAL_PATH}\core\utils\data\test_list.json'
SCREENSHOTS = fr'{GLOBAL_PATH}\core\utils\data\screenshots\reports'
JENKINS = fr'{GLOBAL_PATH}\jenkins\jenkins.war'
LOGS = fr'{TESTS}\_data\logs\logs.log'
REPORTS = fr'{TESTS}\_reports'
PAGE_BASE = fr'{TESTS}\_data\page_base.xlsx'
TEST_SUITE = fr'{TESTS}\_data\test_suite.xlsx'
PLAYER_DATA = fr'{GLOBAL_PATH}\app\player\data.json'
IMAGE_COMPARE_DATA = fr'{GLOBAL_PATH}\core\tools\image_compare\data.json'

# DEVSECOPS
EC2 = fr'{GLOBAL_PATH}\devops\infrastructure\core\deployment\data\ec2.json'
IAM_SECRETS_CSV = ''


class Type:
    CLASS = By.CLASS_NAME
    ID = By.ID
    NAME = By.NAME
    CSS = By.CSS_SELECTOR
    XPATH = By.XPATH
    TEXT = By.LINK_TEXT
