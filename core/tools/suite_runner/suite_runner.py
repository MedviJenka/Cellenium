import logging
import os
import uuid
import openpyxl
from dataclasses import dataclass, field
from core.infrastructure.modules.methods import log
from core.infrastructure.modules.executor import Executor
from core.infrastructure.constants.data import *


@dataclass
class TestSuite(Executor):

    """"
    :param: workbook ...................... excel screen sheet name
    :param: _list ......................... empty list to store values for farther iteration
    :param: report ........................ generate allure report bool

    """

    workbook: dict = openpyxl.load_workbook(TEST_SUITE)
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
        log(logging.DEBUG, text=f'allure report files in: {allure_path}')

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
                        log(logging.DEBUG, text=f'items tested: {result["test"]}')

        # generate allure web report
        if report:
            os.system(fr'allure serve {allure_path}')

    def execute(self, report=True) -> None:

        match report:
            case False:
                self.algorythm(report=False)

            case _:
                self.algorythm()
        log(logging.DEBUG, text=f'executing: {self.algorythm()}')
