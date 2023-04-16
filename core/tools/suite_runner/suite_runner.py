import logging
import os
import uuid
import openpyxl
from dataclasses import dataclass, field
from core.infrastructure.modules.methods import log
from core.infrastructure.modules.reader import read_json, write_json
from core.infrastructure.modules.executor import Executor
from core.infrastructure.constants.data import *


@dataclass
class TestSuite(Executor):

    """"
    :TODO:  fix execution problem with coverage state

    :param: suite_name .................... reads data from json file
    :param: display_coverage_state ........ coverage state %

    """

    display_coverage_state: bool = False
    workbook = openpyxl.load_workbook(TEST_SUITE)
    _list: list = field(default_factory=list)

    @staticmethod
    def _generate_random_id() -> str:
        random_id = str(uuid.uuid4())
        return random_id

    @property
    def _get_sheet_titles(self) -> list[str]:

        # gets all titles from the test sheet
        for each in self.workbook:
            self._list.append(each.title)

        log(logging.DEBUG, text=f'tests list: {self._list}')
        return self._list

    def algorythm(self, report=True) -> None:

        allure_path = fr'{ALLURE}\{self._generate_random_id()}'

        # gets each sheet title
        for each_sheet_name in self._get_sheet_titles:
            sheet = self.workbook[each_sheet_name]

            # for each title iterates through all tests
            for row in sheet.iter_rows(min_row=2, min_col=1, values_only=True):
                result = {
                    "test": row[0],
                    "action": row[1]
                }

                # runs each test that is marked with 'run'
                for _, value in result.items():
                    if value == 'run':
                        path = fr'{TESTS}\{sheet.title}\{result["test"]} --alluredir={allure_path}'
                        os.system(fr'pytest {path}')

        # generate allure web report
        if report:
            os.system(fr'allure serve {allure_path}')

    def coverage_state(self) -> None:
        try:
            for each in self._get_sheet_titles:
                log(text=os.system(fr'pytest --cov={TESTS}\{each}'))

        except ValueError as ve:
            raise ve

    def execute(self, report=True) -> None:
        match report:
            case False:
                self.algorythm(report=False)
            case _:
                self.algorythm()


@dataclass
class __TestSuite(Executor):

    """"
    :TODO:  fix execution problem with coverage state

    :param: suite_name .................... reads data from json file
    :param: display_coverage_state ........ coverage state %

    """

    suite_name = read_json(TEST_LIST)['test_suites']
    display_coverage_state: bool = False
    workbook = openpyxl.load_workbook(TEST_SUITE)

    @staticmethod
    def _generate_random_id() -> str:
        random_id = str(uuid.uuid4())
        return random_id

    @property
    def _get_sheet_titles(self) -> list[str]:

        _list = []

        # gets all titles from the test sheet
        for each in self.workbook:
            _list.append(each.title)

        # log and updates in json
        for _ in self.suite_name:
            write_json(TEST_LIST, "test_suites", _list)

        log(logging.DEBUG, text=f'tests list: {_list}')
        return _list

    def algorythm(self, report=True) -> None:

        _list = []
        sheet_title = self._get_sheet_titles
        allure_path = fr'{ALLURE}\{self._generate_random_id()}'

        # gets each sheet title
        for each_sheet_name in sheet_title:
            sheet = self.workbook[each_sheet_name]

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

                        os.system(fr'pytest {path}')
                        _list.append(result['test'])

        write_json(TEST_LIST, "tested_scenarios", _list)
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
