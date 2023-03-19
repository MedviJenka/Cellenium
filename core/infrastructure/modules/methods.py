import logging
import os
from datetime import datetime
from core.infrastructure.constants.data import PROJECT_PATH
from core.infrastructure.modules.reader import read_config


def run_test(class_name: object, methods: list[str]) -> None:
    """
    maybe will be usable in the future
    """
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


def log(level=logging.INFO, text='') -> callable:
    _time = datetime.now()
    time_format = f'{_time: %A | %d/%m/%Y | %X}'
    logs = read_config('path', 'logs')
    path = fr'{PROJECT_PATH}\{logs}'
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


def generate_tests(test_dir: str, suite_name: list[str] | str, parallel=1, show_test_coverage_state=False) -> None:
    path = read_config('path', 'tests')
    tests = fr"{PROJECT_PATH}\{path}\{test_dir}"
    report_dir = fr"{PROJECT_PATH}\{read_config('path', 'allure')}"
    log(text=fr'allure report located in : {report_dir}')

    match suite_name:
        case '*':
            os.system(fr"pytest {tests} --alluredir={report_dir} -n {parallel}")

        case _:
            os.system(fr"pytest {tests}\{suite_name} --alluredir={report_dir} -n {parallel}")

    if show_test_coverage_state:
        coverage_state(test_dir)

    os.system(fr'allure serve {report_dir}')


def coverage_state(folder_name: str) -> None:
    tests = read_config("path", "tests")
    try:
        os.system(fr'pytest --cov={PROJECT_PATH}\{tests}\{folder_name}')
    except ValueError as ve:
        raise ve


def get_test_files(directory: str) -> list[str]:
    test = read_config('path', 'tests')
    tests = fr"{PROJECT_PATH}\{test}\{directory}"
    python_files = []
    for root, dirs, files in os.walk(tests):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))
    return python_files
