import openpyxl
from dataclasses import dataclass
from core.utils.config.reader import ConfigReader


@dataclass
class ExcelReader:

    config = ConfigReader()
    path: str = config.read('path', 'page_base')

    def _read(self, sheet_name: str, value: str) -> dict[str]:
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
            try:
                return {
                    'name': cache[value]['name'],
                    'locator': cache[value]['locator'],
                    'type': cache[value]['type'],
                    'image': cache[value]['image']
                }
            except Exception:
                raise "no such name in the cell sheet"

    def get_name(self, key: str, value: str) -> str:
        return self._read(key, value)['name']

    def get_locator(self, key: str, value: str) -> str:
        return self._read(key, value)['locator']

    def get_type(self, key: str, value: str) -> str:
        return self._read(key, value)['type']

    def get_image(self, key: str, value: str) -> str:
        return self._read(key, value)['image']
