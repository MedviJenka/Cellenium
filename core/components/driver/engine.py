import xlsxwriter
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from core.components.config.reader import ConfigReader
from core.components.excel.reader import ExcelReader
from os import system
from dataclasses import dataclass
from skimage.metrics import structural_similarity
import cv2
from core.components.driver.manager import DriverManager
import numpy as np
import json


config = ConfigReader()


@dataclass
class DriverEngine(DriverManager):

    excel  = ExcelReader()

    def get_web(self, web_link: str, maximize_window=False) -> None:
        self.driver.get(web_link)
        if maximize_window:
            self.driver.maximize_window()

    def take_screenshot(self, name: str) -> None:
        path = config.read('path', 'screenshots')
        self.driver.save_screenshot(fr'{path}/{name}.jpg')

    def wait_for_element(self, sheet: str, name: str, seconds=3) -> None:
        element_locator = self.excel.get_locator(sheet, name)
        wait = WebDriverWait(self.driver, seconds)
        wait.until(expected_conditions.visibility_of_element_located(element_locator))

    def get_element(self, sheet: str, name: str) -> webdriver:
        element_locator = self.excel.get_locator(sheet, name)
        element_type    = self.excel.get_type(sheet, name)
        # element_name    = self.excel.get_name(sheet, name)
        # path            = self.config.read('path', 'screenshots')

        if element_type == 'NAME':
            element = self.driver.find_element(By.NAME, element_locator)
            return element
            # try:
            #     return element
            # finally:
            #     element.screenshot(f'{path}/{element_name}.png')

        elif element_type == 'ID':
            return self.driver.find_element(By.ID, element_locator)

        elif element_type == 'CSS':
            return self.driver.find_element(By.CSS_SELECTOR, element_locator)

        elif element_type == 'XPATH':
            return self.driver.find_element(By.XPATH, element_locator)

        elif element_type == 'LINK_TEXT':
            return self.driver.find_element(By.LINK_TEXT, element_locator)

        elif element_type == 'CLASS_NAME':
            return self.driver.find_element(By.CLASS_NAME, element_locator)

    def _embed_image_into_cell(self, sheet: str, name: str) -> any:
        path = config.read('path', 'screenshots')
        element = self.get_element(sheet, name)
        image_location = fr'{path}/{self.excel.get_name(sheet, name)}.png'

        try:
            return element.screenshot(image_location)

        finally:
            workbook = xlsxwriter.Workbook(image_location)
            worksheet = workbook.add_worksheet()
            worksheet.insert_image(self.excel.get_image(sheet, name), image_location)
            workbook.close()

    def dropdown(self, sheet: str, name: str, text: str, value: str) -> None:
        select = Select(self.driver.get_element(sheet, name))
        if text:
            select.select_by_value(text)
        elif value:
            select.select_by_visible_text(value)

    def press_keyboard_key(self, key: str) -> ActionChains:
        action = ActionChains(self.driver)
        press = action.key_down(Keys.CONTROL).send_keys(key).key_up(Keys.CONTROL)
        return press.perform()

    def teardown(self) -> None:
        try:
            self.driver.close()
            self.driver.quit()
        except not self.driver:
            system("taskkill /f /im chromedriver.exe")
            system("taskkill /f /im chrome.exe")


