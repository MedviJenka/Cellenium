from os import system
from core.components.config.reader import ConfigReader


config = ConfigReader()


def create() -> None:
    system(fr"python -m venv { config.read('path', 'project') }/venv")


def save_requirements() -> None:
    system(fr"pip freeze { config.read('path', 'project') }/venv")


def install_requirements() -> None:
    system(fr"pip install -r { config.read('path', 'requirement') }")


if __name__ == '__main__':
    ...
