from os import system
from core.components.config.reader import ConfigReader
import subprocess


config = ConfigReader()


def create() -> None:
    system(fr"python -m venv { config.read('path', 'project') }/venv")


def run_venv() -> None:
    subprocess.Popen(['powershell.exe',
                      fr'-ExecutionPolicy {config.read("path", "project")}/venv/Scripts/Activate.ps1'])


def save_requirements() -> None:
    system(fr"pip freeze { config.read('path', 'project') }/venv")


def install_requirements() -> None:
    system(fr"pip install -r { config.read('path', 'requirement') }")


if __name__ == '__main__':
    run_venv()
