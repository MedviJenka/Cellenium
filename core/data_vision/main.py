from dash import Dash, html, dcc
from dataclasses import dataclass
from dash_bootstrap_components.themes import BOOTSTRAP
from core.utils.excel.reader import ExcelReader


TESTS_DROPDOWN = 'tests-dropdown'


@dataclass
class TestVisualization:

    excel = ExcelReader()
    app = Dash(external_stylesheets=[BOOTSTRAP])

    def create_layout(self) -> html.Div:
        return html.Div(
            className='app-div',
            children=[
                html.H1(self.app.title),
                html.Hr(),
                html.Div(
                    className='dropdown-container',
                    children=[self.render()]
                )
            ]
        )

    def render(self):
        all_tests: list = [self.excel.get_name('FirstPage', 'button')]
        return html.Div(
            children=[
                html.H6("Test Cases", self.app.title),
                dcc.Dropdown(
                    id=TESTS_DROPDOWN,
                    options=[{'label': test, 'value': test} for test in all_tests],
                    value=all_tests,
                    multi=True
                )
            ]
        )

    def create(self) -> None:
        self.app.title = 'Test Visualization'
        self.app.layout = self.create_layout()
        self.app.run()


def main() -> None:
    test_visualization = TestVisualization()
    test_visualization.create()


if __name__ == '__main__':
    main()
