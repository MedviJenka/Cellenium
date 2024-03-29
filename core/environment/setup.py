from os import system
from core.infrastructure.constants.data import GLOBAL_PATH


def create_venv(interpreter='py') -> None:

    try:

        system(fr"{interpreter} -m venv ./venv")
    except ValueError:
        system(fr"{interpreter} -m venv ./venv")

    match interpreter:
        case 'python':
            system(fr"{interpreter} -m venv {GLOBAL_PATH}/venv")
        case 'python.exe':
            system(fr"{interpreter} -m venv {GLOBAL_PATH}/venv")
        case _:
            system(fr"{interpreter} -m venv {GLOBAL_PATH}/venv")


def run_venv() -> None:
    system(f'{GLOBAL_PATH}/venv/Scripts/activate.bat')


def __save_requirements(interpreter='py') -> None:
    system(fr"{interpreter} -m pip freeze > {GLOBAL_PATH}/venv")


def install_requirements(interpreter='py') -> None:
    system(fr"{interpreter} -m pip install -r {GLOBAL_PATH}/requirements.txt")


if __name__ == '__main__':
    create_venv()
    run_venv()
    install_requirements()

