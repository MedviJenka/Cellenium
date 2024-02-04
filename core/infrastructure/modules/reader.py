import json
import gspread
import openpyxl
from functools import lru_cache
from google.oauth2.service_account import Credentials
from typing import Optional
from PIL import Image
from configparser import ConfigParser
from core.infrastructure.constants.data import *
from core.infrastructure.modules.logger import Logger
from dataclasses import dataclass


log = Logger()


def read_config(key: str, value: str) -> str:
    config = ConfigParser()
    config.read(CONFIG_PATH)
    return config.get(key, value)


def read_json(path: str, value: Optional[str] = None) -> str | dict:
    with open(path, 'r', encoding='utf-8') as json_file:
        if value:
            return json.load(json_file)[value]
        return json.load(json_file)


def write_json(path: str, key: str, value: Optional[any]) -> None:
    data = read_json(path)
    data[key] = value
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file)


def _read_excel(sheet_name: str, value: str) -> dict[str]:

    workbook = openpyxl.load_workbook(PAGE_BASE)
    sheet = workbook[sheet_name]

    for row in sheet.iter_rows(min_row=2, values_only=True):

        name, locator, element_type, actions, image = row[:5]

        if name == value:
            return {
                'name': name,
                'locator': locator,
                'type': element_type,
                'actions': actions,
                'image': image
            }


def get_name(sheet_name: str, value: str) -> str:
    return _read_excel(sheet_name, value)['name']


def get_locator(sheet_name: str, value: str) -> str:
    return _read_excel(sheet_name, value)['locator']


def get_type(sheet_name: str, value: str) -> str:
    return _read_excel(sheet_name, value)['type']


def get_actions(sheet_name: str, value: str) -> str:
    return _read_excel(sheet_name, value)['actions']


def get_image(sheet_name: str, value: str) -> str:
    return _read_excel(sheet_name, value)['image']


def write_excel(sheet_name: str, value: str) -> None:
    width = 100
    height = 100
    img = Image.open(value)
    img = img.resize((width, height), Image.NEAREST)
    img.save(value)
    workbook = openpyxl.load_workbook(PAGE_BASE)
    sheet = workbook[sheet_name]
    sheet.add_image(img, 'D2')
    workbook.save(fr'{GLOBAL_PATH}\{PAGE_BASE}')


def read_test_case(sheet_name: list[str]) -> list[str]:

    test_case = fr"{GLOBAL_PATH}\{TEST_SUITE}"
    workbook = openpyxl.load_workbook(test_case)
    test_dir = fr"{GLOBAL_PATH}\{TESTS}"
    sheet = []
    for each_sheet_name in sheet_name:
        sheet = workbook[each_sheet_name]
        # print(sheet)
    lists = []
    for row in sheet.iter_rows(min_row=2, min_col=1, values_only=True):
        result = {
            "test": row[0],
            "run": row[1],
        }

        for _, value in result.items():

            if value == '.':
                case = fr'{test_dir}\{sheet.title}\{result["test"]}'
                lists.append(case)

    return lists


@dataclass
class GoogleAPIAuth:

    sheet_id: str = '1HiBBUWKS_wheb3ANqCGVtOCpZPCFuN3KSae0hZOD0QE'

    def __post_init__(self) -> None:
        self.scopes = ['https://www.googleapis.com/auth/spreadsheets']
        self.credentials = Credentials.from_service_account_file(filename=GOOGLE_SHEET_JSON, scopes=self.scopes)
        self.client = gspread.authorize(self.credentials)

    @property
    def get_sheet(self) -> gspread.Spreadsheet:
        return self.client.open_by_key(self.sheet_id)

    @property
    def get_all_sheets(self) -> list[str]:
        return [sheet.title for sheet in self.client.open_by_key(self.sheet_id).worksheets()]


@lru_cache(maxsize=32)  # minimize repetitive API calls
def __read_google_sheet(sheet_name: str, value: str, api: GoogleAPIAuth) -> dict:

    sheet = api.get_sheet.worksheet(sheet_name)
    all_rows = sheet.get_all_values()
    headers = all_rows[0]

    for row in all_rows[1:]:
        row_dict = dict(zip(headers, row))
        if row_dict['name'] == value:
            return row_dict

    return {}


def get_row_data(sheet_name: str, value: str, api=GoogleAPIAuth()) -> dict:

    """
    Retrieve a row from a Google Sheet based on a specific value.

    :param sheet_name: Name of the sheet to search.
    :param value: The value to search for in the 'name' column.
    :param api: An instance of GoogleAPIAuth to use for accessing the sheet.
    :return: A dictionary containing the row data or an empty dict if not found.

    """

    return __read_google_sheet(sheet_name, value, api)


def get_name_api(sheet_name: str, value: str) -> str:
    return get_row_data(sheet_name=sheet_name, value=value)['name']


def get_locator_api(sheet_name: str, value: str) -> str:
    return get_row_data(sheet_name=sheet_name, value=value)['locator']


def get_type_api(sheet_name: str, value: str) -> str:
    return get_row_data(sheet_name=sheet_name, value=value)['type']


def get_action_api(sheet_name: str, value: str) -> str:
    return get_row_data(sheet_name=sheet_name, value=value)['action']
