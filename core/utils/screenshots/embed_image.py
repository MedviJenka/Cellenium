import xlsxwriter
from core.infrastructure.config.reader import ConfigReader
from core.infrastructure.excel.reader import ExcelReader
from dataclasses import dataclass


@dataclass
class Screenshot:

    excel = ExcelReader()
    config = ConfigReader()
    driver = None

    def embed_image_into_cell(self, sheet: str, name: str) -> None:
        path = self.config.read('path', 'screenshots')
        element = self.driver.get_element(sheet, name)
        image_location = fr'{path}/{self.excel.get_name(sheet, name)}.png'
        try:
            return element.save_screenshot(image_location)
        finally:
            workbook = xlsxwriter.Workbook(image_location)
            worksheet = workbook.add_worksheet()
            worksheet.insert_image(self.excel.get_image(sheet, name), image_location)
            workbook.close()
