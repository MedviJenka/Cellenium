import allure
import os
import logging
from datetime import datetime
from core.infrastructure.constants.data import GLOBAL_PATH, LOGS
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


def allure_log(header: str, content: str, file_type=allure.attachment_type.TEXT) -> allure:
    return allure.attach(f'{content}', header, file_type)


@property
def log() -> callable:

    """"
    logger method
    :params: level ........... logging level, debug, info, etc...
             text ............ text displayed in logger
    """

    _time = datetime.now()
    time_format = f'{_time: %A | %d/%m/%Y | %X}'
    logging.basicConfig(filename=LOGS,
                        filemode='w',
                        datefmt=time_format,
                        format=f'%(levelname)s:{time_format} | %(message)s | function: %(funcName)s | line: %(lineno)d',
                        level=logging.INFO)
    return logging


def generate_tests(test_dir: str, suite_name: list[str] | str, parallel=1, show_test_coverage_state=False) -> None:

    path = read_config('path', 'tests')
    tests = fr"{GLOBAL_PATH}\{path}\{test_dir}"
    report_dir = fr"{GLOBAL_PATH}\{read_config('path', 'allure')}"
    log().info(fr'allure report located in : {report_dir}')

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
        os.system(fr'pytest --cov={GLOBAL_PATH}\{tests}\{folder_name}')
    except ValueError as ve:
        raise ve


def get_test_files(directory: str) -> list[str]:
    test = read_config('path', 'tests')
    tests = fr"{GLOBAL_PATH}\{test}\{directory}"
    python_files = []
    for root, dirs, files in os.walk(tests):
        for file in files:
            if file.endswith('.py'):
                python_files.append(os.path.join(root, file))

    return python_files
