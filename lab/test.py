
import undetected_chromedriver as uc
from selenium import webdriver
from time import sleep


options = webdriver.ChromeOptions()
# options.add_argument('--headless')
options.add_argument("start-maximized")
driver = uc.Chrome(options=options)
driver.get('https://chat.openai.com/')
sleep(400)
