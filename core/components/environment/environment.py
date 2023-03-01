from os import system
from core.components.functional.methods import get_project_path


path = get_project_path()


def create(interpreter='py') -> None:

    match interpreter:
        case 'py':
            system(fr"py -m venv {path}/venv")
        case 'python':
            system(fr"py -m venv {path}/venv")
        case 'python.exe':
            system(fr"py -m venv {path}/venv")
        case _:
            raise Exception


def run_venv() -> None:
    system(f'{path}/venv/Scripts/activate.bat')


def save_requirements() -> None:
    system(fr"pip freeze {path}/venv")


def install_requirements() -> None:
    system(fr"pip install -r {path}/requirements.txt")


if __name__ == '__main__':
    # create()
    # install_requirements()
    run_venv()
