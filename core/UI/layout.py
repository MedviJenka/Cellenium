from dash import Dash, html
from core.UI import dropdown
import bar_chart
import css


def create_layout(app: Dash) -> html.Div:
    return html.Div(
        style=css.layout,
        className='app',
        children=[
            html.H1(app.title),
            html.Hr(),
            html.Div(
                className='dropdown-container',
                children=[
                    dropdown.render(app)
                ]
            ),
            html.Hr()
        ],
    )
