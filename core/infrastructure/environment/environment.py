from os import system
from core.infrastructure.constants.data import PROJECT_PATH


def create(interpreter='py') -> None:

    match interpreter:
        case 'py':
            system(fr"py -m venv {PROJECT_PATH}/venv")
        case 'python':
            system(fr"py -m venv {PROJECT_PATH}/venv")
        case 'python.exe':
            system(fr"py -m venv {PROJECT_PATH}/venv")
        case _:
            raise Exception


def run_venv() -> None:
    system(f'{PROJECT_PATH}/venv/Scripts/activate.bat')


def save_requirements() -> None:
    system(fr"pip freeze {PROJECT_PATH}/venv")


def install_requirements() -> None:
    system(fr"pip install -r {PROJECT_PATH}/requirements.txt")


if __name__ == '__main__':
    create()
    install_requirements()
    run_venv()
