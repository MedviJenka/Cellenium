from selenium.webdriver.common.by import By
import os


current_dir = os.getcwd()
path = os.path.abspath(os.path.join(current_dir, '..'))

PROJECT_PATH = path.split('core')[0][:-1]
CONFIG_PATH = fr'{PROJECT_PATH}\core\static\utils\config.ini'


class Type:
    CLASS = By.CLASS_NAME
    ID = By.ID
    NAME = By.NAME
    CSS = By.CSS_SELECTOR
    XPATH = By.XPATH
    TEXT = By.LINK_TEXT
