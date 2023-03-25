import json
import openpyxl
from PIL import Image
from configparser import ConfigParser
from core.infrastructure.constants.data import *


def read_config(key: str, value: str) -> str:
    config = ConfigParser()
    config.read(CONFIG_PATH)
    return config.get(key, value)


def read_json(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as json_file:
        file = json.load(json_file)
        return file


def write_json(path: str, key: str, value: str) -> None:
    data = read_json(path)
    data[key] = value
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file)


def read_excel(sheet_name: str, value: str) -> dict[str]:

    workbook = openpyxl.load_workbook(PAGE_BASE)
    sheet = workbook[sheet_name]
    data = {}

    for row in sheet.iter_rows(min_row=2, values_only=True):
        result = {
            'name': row[0],
            'locator': row[1],
            'type': row[2],
            'image': row[3]
        }
        data[result['name']] = result

    try:
        if data[value]['name']:
            return {
                'name': data[value]['name'],
                'locator': data[value]['locator'],
                'type': data[value]['type'],
                'image': data[value]['image']
            }

    except ValueError:
        raise Exception('no such type')


"""
:params: *args ........... sheet_name, value inherited from read_excel
"""


def get_name(*args) -> str:
    return read_excel(*args)['name']


def get_locator(*args: str) -> str:
    return read_excel(*args)['locator']


def get_type(*args: str) -> str:
    return read_excel(*args)['type']


def get_image(*args: str) -> str:
    return read_excel(*args)['image']


def write_excel(sheet_name: str, screenshot_path: str) -> None:

    width = 100
    height = 100

    img = Image.open(screenshot_path)
    img = img.resize((width, height), Image.NEAREST)
    img.save(screenshot_path)

    path = fr"{PROJECT_PATH}\{read_config('path', 'page_base')}"

    workbook = openpyxl.load_workbook(path)
    sheet = workbook[sheet_name]

    img = openpyxl.drawing.image.Image(screenshot_path)
    sheet.add_image(img, 'D2')
    workbook.save(fr'{PROJECT_PATH}\{read_config("path", "page_base")}')


def read_test_case(sheet_name: list[str]) -> list[str]:

    test_case = fr"{PROJECT_PATH}\{TEST_SUITE}"
    workbook = openpyxl.load_workbook(test_case)
    test_dir = fr"{PROJECT_PATH}\{TESTS}"
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
