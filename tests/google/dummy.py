from selenium import webdriver


PATH = r'C:\blablabla\chromedriver.exe'
driver = webdriver.Chrome(executable_path=PATH)
driver.get('https://www.google.com')
