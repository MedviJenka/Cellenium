from configparser import ConfigParser
import openpyxl
import unittest
from typing import Type
from unittest import TestCase
from unittest.suite import TestSuite
import json
import logging
from datetime import datetime


def read_config(key: str, value: str) -> str:
    config = ConfigParser()
    path: str = r'C:\Cellenium\core\static\utils\config.ini'
    config.read(path)
    return config.get(key, value)


def read_json(path: str) -> dict:
    with open(path, 'r', encoding='utf-8') as json_file:
        file = json.load(json_file)
        return file


def write_json(path: str,  key: str, value: str) -> None:
    data = read_json(path)
    data[key] = value
    with open(path, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file)


def read_excel(sheet_name: str, value: str) -> dict[str]:
    path = read_config('path', 'page_base')
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

    if cache[value]['name']:
        try:
            return {
                'name': cache[value]['name'],
                'locator': cache[value]['locator'],
                'type': cache[value]['type'],
                'image': cache[value]['image']
            }
        except Exception:
            raise Exception("no such name in the cell sheet")


def get_name(*args: str) -> str:
    return read_excel(*args)['name']


def get_locator(*args: str) -> str:
    return read_excel(*args)['locator']


def get_type(*args: str) -> str:
    return read_excel(*args)['type']


def get_image(*args: str) -> str:
    return read_excel(*args)['image']


def run_single_test(class_name: object, methods: list[str]) -> None:
    logs = log()
    for each_method in methods:
        getattr(class_name, each_method)()
        logs.info(f'test steps: {each_method}')


def run_multiple_tests(class_name: Type[TestCase]) -> None:
    suite = TestSuite()
    tests = unittest.TestLoader()
    suite.addTest(tests.loadTestsFromTestCase(class_name))
    suite.addTest(tests.loadTestsFromTestCase(class_name))
    run = unittest.TextTestRunner()
    run.run(suite)


def log() -> logging:
    time = datetime.now()
    time_format = f'{time: %A | %B | %X}'
    path = read_config('path', 'logs')
    logging.basicConfig(filename=path,
                        format=f'%(levelname)s:{time_format} :: %(message)s',
                        level=logging.DEBUG)
    logging.getLogger()
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    file_handler = logging.FileHandler(path)
    file_handler.setLevel(logging.DEBUG)
    formatter = logging.Formatter(f'% {time_format} - %(name)s - %(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)
    return logger
