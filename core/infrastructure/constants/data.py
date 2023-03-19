from selenium.webdriver.common.by import By
import os


current_dir = os.getcwd()
path = os.path.abspath(os.path.join(current_dir, '..'))


_PROJECT_PATH = path.split('core')[0][:-1]
"""
TODO: make _PROJECT_PATH work cross directions,
      for some reason its not getting the pass
      although its the same path and same type.
"""
PROJECT_PATH = r'C:\Users\medvi\OneDrive\Desktop\Cellenium'
CONFIG_PATH = fr'{PROJECT_PATH}\core\static\utils\config.ini'


class Type:
    CLASS = By.CLASS_NAME
    ID = By.ID
    NAME = By.NAME
    CSS = By.CSS_SELECTOR
    XPATH = By.XPATH
    TEXT = By.LINK_TEXT
