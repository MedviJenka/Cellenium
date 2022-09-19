from dash import Dash, html, dcc
from core.utils.excel.reader import ExcelReader
import ids


excel = ExcelReader()


def render(app: Dash) -> html.Div:
    tests = [excel.get_name('FirstPage', 'button'), excel.get_name('FirstPage', 'search')]
    return html.Div(
        children=[
            html.H6('Tests'),
            dcc.Dropdown(
                id=ids.TESTS_DROPDOWN,
                multi=True,
                options=[{'label': test, 'value': test} for test in tests],
                value=tests
            ),
            html.Button(
                id=ids.SELECT_ALL_TESTS,
                className='dropdown',
                children=['select-all']
            )
        ]
    )
