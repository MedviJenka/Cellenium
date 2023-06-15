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

    workbook: openpyxl.Workbook = field(default_factory=lambda: openpyxl.load_workbook(TEST_SUITE))

    @staticmethod
    def _generate_random_id() -> str:
        random_id = str(uuid.uuid4())
        return random_id

    @property
    def _get_sheet_titles(self) -> list[str]:
        result = [sheet.title for sheet in self.workbook]
        log(logging.DEBUG, text=f'tests list: {result}')
        return result

    def algorythm(self, report=True) -> None:

        allure_path = fr'{ALLURE}\{self._generate_random_id()}'
        log(logging.DEBUG, text=f'allure report files in: {allure_path}')

        # gets each sheet title
        for each_sheet_name in self._get_sheet_titles:
            sheet = self.workbook[each_sheet_name]

            # for each title iterates through all tests
            for row in sheet.iter_rows(min_row=2, min_col=1, values_only=True):
                test_name, action = row[0], row[1]

                # runs each test that is marked with 'run'
                if action == 'run':
                    path = fr'{os.path.join(TESTS, sheet.title, test_name)} --alluredir={allure_path}'
                    os.system(fr'pytest {path}')
                    log(logging.DEBUG, text=f'items tested: {test_name}')

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
