import xlsxwriter

from core.components.config.reader import ConfigReader

from dataclasses import dataclass

from core.components.excel.reader import ExcelReader


@dataclass
class Screenshot:

    excel = ExcelReader()
    config = ConfigReader()

    def embed_image_into_cell(self, *args) -> None:
        path = self.config.read('path', 'screenshots')
        element = self.get_element(*args)
        image_location = fr'{path}/{self.excel.get_name(*args)}.png'
        try:
            return element.save_screenshot(image_location)
        finally:
            workbook = xlsxwriter.Workbook(image_location)
            worksheet = workbook.add_worksheet()
            worksheet.insert_image(self.excel.get_image(*args), image_location)
            workbook.close()
