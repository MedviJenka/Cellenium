import json
import undetected_chromedriver as uc
from selenium import webdriver
from time import sleep
from core.infrastructure.constants.data import COOKIES
from core.infrastructure.modules.decorators import memoize


@memoize
def test() -> None:
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument("start-maximized")
    driver = uc.Chrome(options=options)
    driver.get('https://chat.openai.com/')

    with open(COOKIES) as file:
        cookies = json.load(file)
        for each in cookies:
            output = {
                "name": each["name"],
                "value": each["value"]
            }
        driver.add_cookie(output)

    driver.refresh()

    with open(COOKIES, "r") as file:
        local_storage = json.load(file)
    for each in local_storage:
        for key, value in each.items():
            driver.execute_script(f"window.localStorage.setItem('{key}', '{value}')")

    driver.refresh()
    sleep(400)
