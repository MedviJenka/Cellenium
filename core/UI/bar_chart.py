from dash import Dash, dcc, html
import plotly.express as px
import ids


TEST_DATA = px.data.wind()


def render(app: Dash) -> html.Div:
    figure = px.bar(TEST_DATA,
                    x='direction',
                    y='strength'
                    )
    return html.Div(
        dcc.Graph(figure),
        id=ids.BAR_CHART,
    )
