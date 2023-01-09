from configparser import ConfigParser
import openpyxl
import unittest
from typing import Type
from unittest import TestCase
from unittest.suite import TestSuite


def read_config(key: str, value: str) -> str:
    config = ConfigParser()
    path: str = r'C:\Users\medvi\IdeaProjects\CelleniumProject\core\static\utils\config.ini'
    config.read(path)
    return config.get(key, value)


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
    for each_method in methods:
        getattr(class_name, each_method)()
        print(f'test steps: {each_method}')


def run_multiple_tests(class_name: Type[TestCase]) -> None:
    suite = TestSuite()
    tests = unittest.TestLoader()
    suite.addTest(tests.loadTestsFromTestCase(class_name))
    suite.addTest(tests.loadTestsFromTestCase(class_name))
    run = unittest.TextTestRunner()
    run.run(suite)
