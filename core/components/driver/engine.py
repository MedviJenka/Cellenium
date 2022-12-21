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
from PIL import Image, ImageChops
import json



@dataclass
class DriverEngine(DriverManager):

    excel  = ExcelReader()
    config = ConfigReader()

    def get_web(self, web_link: str, maximize_window=False) -> None:
        self.driver.get(web_link)
        if maximize_window:
            self.driver.maximize_window()

    def take_screenshot(self, name: str) -> None:
        path = self.config.read('path', 'screenshots')
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
        path = self.config.read('path', 'screenshots')
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


class CompareImages:

    """
    :param: original ................ path for original image to compare
    :param: compare ................. path for screenshot
    :param: percentage_threshold .... wanted percentage of success
    :param: resolution .......... image resolution
    """

    @staticmethod
    def _read_json(path: str) -> dict:
        output = json.load(open(path))
        return {
            'original': output['original'],
            'actual': output['actual'],
            'percentage_threshold': output['percentage_threshold'],
            'resolution': output['resolution']
        }

    def find_difference(self, path: str) -> str:
        data = self._read_json(path)

        # load and resize images
        before = cv2.imread(data['original'])
        after = cv2.imread(data['actual'])
        before = cv2.resize(before, (data['resolution']))
        after = cv2.resize(after, (data['resolution']))

        # Convert images to grayscale
        before_gray = cv2.cvtColor(before, cv2.COLOR_BGR2GRAY)
        after_gray = cv2.cvtColor(after, cv2.COLOR_BGR2GRAY)
        score, diff = structural_similarity(before_gray, after_gray, full=True)

        diff = (diff * 255).astype("uint8")
        diff_box = cv2.merge([diff, diff, diff])

        # Threshold the difference image, followed by finding contours to
        # obtain the regions of the two input images that differ
        thresh = cv2.threshold(diff, 0, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)[1]
        contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = contours[0] if len(contours) == 2 else contours[1]

        mask = np.zeros(before.shape, dtype='uint8')
        filled_after = after.copy()

        for i in contours:
            area = cv2.contourArea(i)
            if area > 40:
                x, y, w, h = cv2.boundingRect(i)
                cv2.rectangle(before, (x, y), (x + w, y + h), (36, 255, 12), 1)
                cv2.rectangle(after, (x, y), (x + w, y + h), (36, 255, 12), 1)
                cv2.rectangle(diff_box, (x, y), (x + w, y + h), (0, 255, 0), 1)
                cv2.drawContours(mask, [i], 0, (255, 255, 255), -1)
                cv2.drawContours(filled_after, [i], 0, (250, 0, 0), -1)

        cv2.imshow('before', before)
        cv2.imshow('after', after)
        cv2.waitKey()

        result = score * 100
        result_text = f"Image Similarity: {result:.1f}%"
        print(result_text)
        print("LOW SIMILARITY, CONSULT WITH THE DEVELOPER") if result < data['percentage_threshold'] else print("GOOD")

        return result_text
