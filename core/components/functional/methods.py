import openpyxl
import json
import logging
import os
from datetime import datetime
from configparser import ConfigParser
from pathlib import Path
from time import time


def get_project_path() -> str:
    project_path = str(Path.cwd())
    return project_path.split('core')[0][:-1]


PATH = get_project_path()


def measure_execution_time(func: callable) -> callable:
    def wrapper() -> None:
        start = time()
        func()
        end = time() - start
        log(text=f'function run took {end} sec')
    return wrapper


def read_config(key: str, value: str) -> str:
    config = ConfigParser()
    path: str = fr'{PATH}\core\static\utils\config.ini'
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
    try:
        match cache[value]['name']:
            case _:
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


def run_test(class_name: object, methods: list[str]) -> None:

    try:
        match ['*']:
            case _:
                for each_step in dir(class_name):
                    if callable(getattr(class_name, each_step) and not each_step.startswith('__')):
                        getattr(class_name, each_step)()

        for each_method in methods:
            getattr(class_name, each_method)()

    except Exception:
        raise

    finally:
        generate_allure_report()


def log(level=logging.INFO, text='') -> None:
    _time = datetime.now()
    time_format = f'{_time: %A | %d/%m/%Y | %X}'
    path = fr'{PATH}\core\static\logs\reports\logs.log'
    logging.basicConfig(filename=path,
                        datefmt=time_format,
                        format=f'%(levelname)s:{time_format} :: %(message)s',
                        level=level)
    match level:
        case logging.INFO:
            logging.info(text)
        case logging.DEBUG:
            logging.debug(text)
        case logging.ERROR:
            logging.error(text)
        case logging.CRITICAL:
            logging.critical(text)
        case logging.FATAL:
            logging.fatal(text)
        case _:
            raise Exception('no such logging level')


def generate_allure_report(file=__file__):
    path = r"C:\Cellenium\core\static\allure\reports"
    os.system(fr"pytest {file} --alluredir={path}")
    os.system(fr'allure serve {path}')


def get_test_coverage_state(folder_name: str) -> None:
    try:
        os.system(fr'pytest --cov={PATH}\tests\{folder_name}')
    except ValueError as ve:
        raise ve


def negative(exception_type: Exception(any)):

    """
    This decorator function takes in a function as an argument
    and returns a new function that wraps the original function.
    When the new function is called, it calls the original
    function with the same arguments and catches any AssertionError that might be raised.
    If an AssertionError is caught, it prints out the error message and then re-raises the exception.
    """

    def decorator(func):
        def wrapper(*args: any, **kwargs: any):
            try:
                func(*args, **kwargs)
            except exception_type:
                log(text=f"{func.__name__} did not raise {exception_type.__name__}")
                return
            raise AssertionError(f"{func.__name__} did not raise {exception_type.__name__}")
        return wrapper
    return decorator
