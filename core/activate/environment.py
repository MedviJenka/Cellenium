from os import system
from core.utils.config.reader import ConfigReader


config = ConfigReader()


def create() -> None:
    system(fr"python -m venv { config.read('path', 'project') }/venv")


if __name__ == '__main__':
    create()
