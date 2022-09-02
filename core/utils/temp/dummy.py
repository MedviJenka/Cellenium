from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from core.utils.config.reader import ConfigReader

config = ConfigReader()

driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=Options())
driver.get("https://www.google.com")
driver.find_element(By.NAME, 'q').screenshot(fr'{ config.read("path", "screenshots") }/img.png')

