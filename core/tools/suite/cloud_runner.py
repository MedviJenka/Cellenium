import os
from dataclasses import dataclass
from core.infrastructure.constants.data import REPORTS, TESTS
from core.infrastructure.modules.executor import Executor
from core.infrastructure.modules.logger import Logger
from core.infrastructure.modules.reader import GoogleAPIAuth


log = Logger()


@dataclass
class SuiteRunnerAPI(Executor):

    report: bool = False
    sheet_name: str = 'google'
    api: GoogleAPIAuth = GoogleAPIAuth(sheet_id='1PS8E2AJlQEQhXAqCVsKOC5bCJhUy3GziCGGYNRgzgWU')

    def execute(self) -> None:
        log.level.debug(f'allure report files in: {REPORTS}')
        sheet = self.api.get_sheet.worksheet(self.sheet_name)
        all_rows = sheet.get_all_values()
        headers = all_rows[0]
        tests = [dict(zip(headers, row)) for row in all_rows[1:]]

        for test in tests:
            if test['action'] == 'RUN':
                test_name = test['test']
                path = fr'{os.path.join(TESTS, self.sheet_name, test_name)} --alluredir={REPORTS}'
                print(path)
                os.system(fr'py -m pytest {path}')
                log.level.debug(f'items tested: {test_name}')

        if self.report:
            os.system(fr'allure serve {REPORTS}')
        log.level.debug(f'executing: {self.execute.__name__}')


suite = SuiteRunnerAPI()
if __name__ == '__main__':
    suite.execute()
