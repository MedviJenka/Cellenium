from dash import Dash, html, dcc
from dash.dependencies import Input, Output
import ids
import css
from core.infrastructure.modules.reader import get_name


def render(app: Dash) -> html.Div:

    tests = [get_name('IntroPage', 'button'), get_name('IntroPage', 'search')]

    @app.callback(Output(ids.TESTS_DROPDOWN, 'value'), Input(ids.SELECT_ALL_TESTS, 'n_click'))
    def select_all_tests(_: int) -> list[str]:
        return tests

    return html.Div(children=[html.H6('Tests'), dcc.Dropdown(
                id=ids.TESTS_DROPDOWN,
                multi=True,
                options=[{'label': test, 'value': test} for test in tests],
                value=tests,
                style=css.tests_dropdown
            ),
            html.Button(
                id=ids.SELECT_ALL_TESTS,
                className='dropdown',
                children=['select all'],
                key=print("ok"),
                style=css.dropdown_button,
            )
        ]
    )
