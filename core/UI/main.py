from dash import Dash
from dash_bootstrap_components.themes import BOOTSTRAP
from core.UI.layout import create_layout


def main() -> None:
    app = Dash(external_stylesheets=[BOOTSTRAP])
    app.title = 'Test Report'
    app.layout = create_layout(app)
    app.run_server()


if __name__ == '__main__':
    main()
