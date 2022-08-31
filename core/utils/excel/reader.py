import openpyxl
from dataclasses import dataclass
from core.utils.config.reader import ConfigReader


@dataclass
class ExcelReader:

    config = ConfigReader()
    path: str = config.read('path', 'page_base')

    def read(self, sheet_name: str, value: str) -> dict[str]:
        workbook = openpyxl.load_workbook(self.path)
        sheet = workbook[sheet_name]
        cache = {}
        for row in sheet.iter_rows(min_row=2, values_only=True):
            result = {
                'name': row[0],
                'locator': row[1],
                'type': row[2],
                'image': row[3]
            }
            cache[result['name']] = result

        if cache[value]['name']:
            return {
                'locator': cache[value]['locator'],
                'type': cache[value]['type'],
                'image': cache[value]['image']
            }
