import os
import uuid
import openpyxl
from dataclasses import dataclass

from core.infrastructure.modules.methods import log
from core.infrastructure.modules.reader import read_json
from core.infrastructure.modules.executor import Executor
from core.infrastructure.constants.data import *


@dataclass
class TestSuite(Executor):

    """"
    :TODO:  fix execution problem with coverage state

    :param: suite_name .................... reads data from json file
    :param: display_coverage_state ........ coverage state %

    """

    suite_name = read_json(TEST_LIST)['test_suites']
    display_coverage_state: bool = False

    @staticmethod
    def _generate_random_id() -> str:
        random_id = str(uuid.uuid4())
        return random_id

    @property
    def _get_sheet_titles(self) -> list[str]:
        workbook = openpyxl.load_workbook(TEST_SUITE)
        _list = []
        for each_sheet_name in self.suite_name:
            sheet = workbook[each_sheet_name]
            _list.append(sheet.title)

        return _list

    def algorythm(self, report=True) -> None:

        sheet_title = self._get_sheet_titles
        workbook = openpyxl.load_workbook(TEST_SUITE)
        allure_path = fr'{ALLURE}\{self._generate_random_id()}'

        # gets each sheet title
        for each_sheet_name in sheet_title:
            sheet = workbook[each_sheet_name]

            # for each title iterates through all tests
            for row in sheet.iter_rows(min_row=2, min_col=1, values_only=True):
                result = {
                    "test": row[0],
                    "action": row[1],
                }

                # runs each test that is marked with 'run'
                for _, value in result.items():
                    if value == 'run':
                        path = fr'{TESTS}\{sheet.title}\{result["test"]} --alluredir={allure_path}'
                        log(text=f'tests: {path}')
                        os.system(fr'pytest {path}')

        # generate web allure report
        if report:
            os.system(fr'allure serve {allure_path}')

    def coverage_state(self) -> None:
        try:
            for each in self._get_sheet_titles:
                os.system(fr'pytest --cov={TESTS}\{each}')

        except ValueError as ve:
            raise ve

    def execute(self, report=True) -> None:
        match report:
            case False:
                self.algorythm(report=False)
            case _:
                self.algorythm()
