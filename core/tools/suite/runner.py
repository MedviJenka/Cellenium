import openpyxl
from dataclasses import dataclass
from core.infrastructure.modules.executor import Executor
from core.infrastructure.constants.data import *
from core.infrastructure.modules.logger import Logger
from threading import Thread


log = Logger()


@dataclass
class SuiteRunner(Executor):

    """"
    :param: workbook ...................... excel screen sheet name
    :param: report ........................ generate allure report bool

    """

    report: bool = False
    workbook: openpyxl.Workbook = openpyxl.load_workbook(TEST_SUITE)

    @staticmethod
    def multi_process(function: callable) -> None:
        thread = Thread(target=function)
        thread.start()

    def logic(self) -> None:

        log.level.debug(f'allure report files in: {REPORTS}')

        # gets each sheet title
        for each_sheet_name in [sheet.title for sheet in self.workbook]:
            sheet = self.workbook[each_sheet_name]

            # for each title iterates through all tests
            for row in sheet.iter_rows(min_row=2, min_col=1, values_only=True):
                test_name, action = row[0], row[1]

                # runs each test that is marked with 'run'
                if action == 'RUN':
                    path = fr'{os.path.join(TESTS, sheet.title, test_name)} --alluredir={REPORTS}'

                    os.system(fr'py -m pytest {path}')
                    log.level.debug(f'items tested: {test_name}')

        # generate allure web report
        if self.report:
            os.system(fr'allure serve {REPORTS}')

        log.level.debug(f'executing: {self.execute.__name__}')

    def execute(self, multi_process: bool = False) -> any:
        match multi_process:
            case True:
                self.multi_process(function=self.logic)
            case _:
                self.logic()
