from os import system
from core.components.functional.methods import read_config
import subprocess


def create(interpreter='py') -> None:
    match interpreter:
        case 'py':
            system(fr"py -m venv { read_config('path', 'project') }/venv")
        case 'python':
            system(fr"py -m venv {read_config('path', 'project')}/venv")
        case 'python.exe':
            system(fr"py -m venv {read_config('path', 'project')}/venv")
        case _:
            raise Exception


def run_venv() -> None:
    subprocess.Popen(['powershell.exe',
                      fr'-ExecutionPolicy {read_config("path", "project")}/venv/Scripts/Activate.ps1'])


def save_requirements() -> None:
    system(fr"pip freeze {read_config('path', 'project') }/venv")


def install_requirements() -> None:
    system(fr"pip install -r {read_config('path', 'requirement') }")


if __name__ == '__main__':
    create()
    run_venv()
