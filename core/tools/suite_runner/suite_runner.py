import logging
import os
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

    def algorythm(self, report=True) -> None:

        log(logging.DEBUG, text=f'allure report files in: {ALLURE}')

        # gets each sheet title
        for each_sheet_name in [sheet.title for sheet in self.workbook]:
            sheet = self.workbook[each_sheet_name]

            # for each title iterates through all tests
            for row in sheet.iter_rows(min_row=2, min_col=1, values_only=True):
                test_name, action = row[0], row[1]

                # runs each test that is marked with 'run'
                if action == 'run':
                    path = fr'{os.path.join(TESTS, sheet.title, test_name)} --alluredir={ALLURE}'
                    os.system(fr'pytest {path}')
                    log(logging.DEBUG, text=f'items tested: {test_name}')

        # generate allure web report
        if report:
            os.system(fr'allure serve {ALLURE}')

    def execute(self, report=True) -> None:

        match report:
            case False:
                self.algorythm(report=False)

            case _:
                self.algorythm()
        log(logging.DEBUG, text=f'executing: {self.algorythm()}')
