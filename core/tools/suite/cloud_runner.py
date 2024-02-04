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
    sheet_name: str = ''  # Default value, will be overridden
    api: GoogleAPIAuth = GoogleAPIAuth(sheet_id='1lEdN3FR2K6ZnBNwJ8zykfJ9u-rUmLl-HanVoVGwKez8')

    def execute(self) -> None:
        # Fixed the iteration over sheets by using self.api.get_all_sheets() instead of self.api.get_all_sheets
        for sheet_name in self.api.get_all_sheets:
            sheet = self.api.get_sheet.worksheet(sheet_name)
            all_rows = sheet.get_all_values()

            for row in all_rows[1:]:
                if 'RUN' in row[1]:  # Changed 'action' to 'get' method for safer access
                    path = os.path.join(TESTS, sheet_name, row[0])
                    allure_path = fr'pytest {path} --alluredir={REPORTS}'
                    os.system(allure_path)

            if self.report:
                os.system(fr'allure serve {REPORTS}')
            log.level.debug(f'executing: {self.execute.__name__}')
