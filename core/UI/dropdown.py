from dash import Dash, html, dcc
from dash.dependencies import Input, Output
from core.utils.excel.reader import ExcelReader
import ids


excel = ExcelReader()


def render(app: Dash) -> html.Div:

    tests = [excel.get_name('FirstPage', 'button'), excel.get_name('FirstPage', 'search')]

    @app.callback(
        Output(ids.TESTS_DROPDOWN, 'value'),
        Input(ids.SELECT_ALL_TESTS, 'n_click')
    )
    def select_all_tests(_: int) -> list[str]:
        return tests

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
                children=['select all'],
                key=print("ok"),
                style={
                    'height': '10%',
                    'width': '100%',
                    'backgroundColor': 'RGBA(144,238,144,50)',
                    'fontSize': '20px',
                    'fontWeight': 'bold'
                },
            )
        ]
    )
