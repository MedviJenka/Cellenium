from os import system
from core.infrastructure.constants.data import GLOBAL_PATH


def create(interpreter='py') -> None:

    match interpreter:
        case 'py':
            system(fr"py -m venv {GLOBAL_PATH}/venv")
        case 'python':
            system(fr"py -m venv {GLOBAL_PATH}/venv")
        case 'python.exe':
            system(fr"py -m venv {GLOBAL_PATH}/venv")
        case _:
            raise Exception


def run_venv() -> None:
    system(f'{GLOBAL_PATH}/venv/Scripts/activate.bat')


def save_requirements() -> None:
    system(fr"pip freeze {GLOBAL_PATH}/venv")


def install_requirements() -> None:
    system(fr"pip install -r {GLOBAL_PATH}/requirements.txt")


if __name__ == '__main__':
    create()
    install_requirements()
    run_venv()
