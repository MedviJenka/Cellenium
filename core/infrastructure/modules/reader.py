import json
import openpyxl
from PIL import Image
from configparser import ConfigParser
from core.infrastructure.constants.data import PROJECT_PATH, CONFIG_PATH


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
    path = fr"{PROJECT_PATH}\{read_config('path', 'page_base')}"
    workbook = openpyxl.load_workbook(path)
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
    try:
        if cache[value]['name']:
            return {
                'name': cache[value]['name'],
                'locator': cache[value]['locator'],
                'type': cache[value]['type'],
                'image': cache[value]['image']
            }
    except ValueError:
        raise Exception('no such type')


def get_name(*args: str) -> str:
    return read_excel(*args)['name']


def get_locator(*args: str) -> str:
    return read_excel(*args)['locator']


def get_type(*args: str) -> str:
    return read_excel(*args)['type']


def get_image(*args: str) -> str:
    return read_excel(*args)['image']


def write_excel(sheet_name: str, screenshot_path: str):

    width = 23
    height = 23

    img = Image.open(screenshot_path)
    img = img.resize((width, height), Image.BOX)
    img.save(screenshot_path)

    path = fr"{PROJECT_PATH}\{read_config('path', 'page_base')}"

    workbook = openpyxl.load_workbook(path)
    sheet = workbook[sheet_name]

    img = openpyxl.drawing.image.Image(screenshot_path)
    sheet.add_image(img, 'D2')
    workbook.save(fr'{PROJECT_PATH}\{read_config("path", "page_base")}')


if __name__ == '__main__':
    write_excel(sheet_name='TerminalX', screenshot_path=r'C:\Users\medvi\OneDrive\Desktop\Cellenium\icon.png')
