from dash import Dash, dcc, html
import plotly.express as px
import ids


TEST_DATA = px.data.medals_long()


def render(app: Dash) -> html.Div:
    figure = px.bar(TEST_DATA,
                    x='medal',
                    y='count',
                    color='nation',
                    text='nation')
    return html.Div(
        dcc.Graph(figure),
        id=ids.BAR_CHART,
    )
