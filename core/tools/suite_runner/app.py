@dataclass
class SuiteRunner:

    workbook: openpyxl.Workbook = field(default_factory=lambda: openpyxl.load_workbook(TEST_SUITE))

    @property
    def get_sheet_titles(self) -> list[str]:
        return [sheet.title for sheet in self.workbook]

    def execute(self) -> None:
        for sheet_title in self.get_sheet_titles:
            sheet = self.workbook[sheet_title]
            for row in sheet.iter_rows(min_row=2, values_only=True):
                test_name, action = row[0], row[1]
                if action == 'RUN':
                    path = os.path.join(TESTS, sheet.title, test_name)
                    os.system(f'pytest {path}')