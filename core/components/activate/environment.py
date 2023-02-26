import subprocess
from os import system
from core.components.functional.methods import read_config, get_project_path


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
    subprocess.Popen(['powershell.exe', f'{path}/venv/Scripts/Activate.ps1'])


def save_requirements() -> None:
    system(fr"pip freeze {path}/venv")


def install_requirements() -> None:
    system(fr"pip install -r {path}/requirements.txt")


if __name__ == '__main__':
    install_requirements()
