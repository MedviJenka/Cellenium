from dash import Dash
from core.infrastructure.ui.layout import create_layout


def main() -> None:
    app = Dash(external_stylesheets=[])
    app.title = 'Report'
    app.layout = create_layout(app)
    app.run_server()


if __name__ == '__main__':
    main()
