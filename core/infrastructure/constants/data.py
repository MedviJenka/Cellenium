from selenium.webdriver.common.by import By


PROJECT_PATH = r'C:\Users\medvi\OneDrive\Desktop\Cellenium'
CONFIG_PATH = fr'{PROJECT_PATH}\core\static\utils\config.ini'


class Type:
    CLASS = By.CLASS_NAME
    ID = By.ID
    NAME = By.NAME
    CSS = By.CSS_SELECTOR
    XPATH = By.XPATH
    TEXT = By.LINK_TEXT

