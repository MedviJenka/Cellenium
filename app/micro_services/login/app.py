from dataclasses import dataclass
from flask import Flask, render_template, request
from core.infrastructure.modules.executor import Executor


@dataclass
class App(Executor):

    app = Flask(__name__)

    def __post_init__(self) -> None:
        self.app.secret_key = ''

    @staticmethod
    @app.route('/')
    def home_page() -> render_template:
        return render_template('login.html')

    @staticmethod
    @app.route('/login', methods=['POST'])
    def login() -> str:
        username = request.form['username']
        password = request.form['password']
        if username and password == 'admin':
            return 'login successful'
        else:
            return 'unsuccessful login'

    def execute(self) -> None:
        self.app.run()


app = App()
if __name__ == '__main__':
    app.execute()
