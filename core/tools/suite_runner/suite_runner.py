import openpyxl
from dataclasses import dataclass
from core.infrastructure.modules.executor import Executor
from core.infrastructure.constants.data import *


@dataclass
class TestSuite(Executor):

    suite_name: list[str]
    display_coverage_state: bool = False

    def get_sheet_titles(self) -> list[str]:
        workbook = openpyxl.load_workbook(TEST_SUITE)
        _list = []
        for each_sheet_name in self.suite_name:
            sheet = workbook[each_sheet_name]
            _list.append(sheet.title)
        return _list

    def algorythm(self) -> str:

        sheet_title = self.get_sheet_titles()
        workbook = openpyxl.load_workbook(TEST_SUITE)

        for each_sheet_name in sheet_title:

            sheet = workbook[each_sheet_name]

            for row in sheet.iter_rows(min_row=2, min_col=1, values_only=True):
                result = {
                    "test": row[0],
                    "run": row[1],
                }

                for _, value in result.items():
                    if value == '.':
                        return fr'{TESTS}\{sheet.title}\{result["test"]} --alluredir={ALLURE}'

    def coverage_state(self) -> None:
        try:
            for each in self.get_sheet_titles():
                os.system(fr'pytest --cov={TESTS}\{each}')
        except ValueError as ve:
            raise ve

    def execute(self, debug=False) -> None:
        os.system(fr'pytest {self.algorythm()}')
        if debug:
            os.system(fr'pytest -m pdb {self.algorythm()}')
        if self.display_coverage_state:
            self.coverage_state()
