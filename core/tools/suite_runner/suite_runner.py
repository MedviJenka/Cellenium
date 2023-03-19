import os
import openpyxl
from dataclasses import dataclass
from core.infrastructure.constants.data import PROJECT_PATH
from core.infrastructure.modules.executor import Executor
from core.infrastructure.modules.reader import read_config


@dataclass
class RunSuite(Executor):

    suite_name: list[str]
    display_coverage_state: bool = False

    def get_sheet_titles(self) -> list[str]:
        test_case = fr"{PROJECT_PATH}\{read_config('path', 'test_case')}"
        workbook = openpyxl.load_workbook(test_case)
        _list = []
        for each_sheet_name in self.suite_name:
            sheet = workbook[each_sheet_name]
            _list.append(sheet.title)
        return _list

    def coverage_state(self) -> None:
        tests = read_config("path", "tests")
        try:
            for each in self.get_sheet_titles():
                print(fr'pytest --cov={PROJECT_PATH}\{tests}\{each}')
        except ValueError as ve:
            raise ve

    def algorythm(self) -> None:

        sheet_title = self.get_sheet_titles()
        report_dir = fr"{PROJECT_PATH}\{read_config('path', 'allure')}"
        test_case = fr"{PROJECT_PATH}\{read_config('path', 'test_case')}"
        workbook = openpyxl.load_workbook(test_case)
        test_dir = fr"{PROJECT_PATH}\{read_config('path', 'tests')}"

        for each_sheet_name in sheet_title:

            sheet = workbook[each_sheet_name]

            for row in sheet.iter_rows(min_row=2, min_col=1, values_only=True):
                result = {
                    "test": row[0],
                    "run": row[1],
                }

                for _, value in result.items():
                    if value == '.':
                        os.system(fr'pytest {test_dir}\{sheet.title}\{result["test"]} --alluredir={report_dir}')

            if self.display_coverage_state:
                os.system(fr'pytest --cov {test_dir}\{sheet.title}')

        os.system(fr'allure serve {report_dir}')

    def execute(self) -> None:
        self.algorythm()
        if self.display_coverage_state:
            self.coverage_state()
