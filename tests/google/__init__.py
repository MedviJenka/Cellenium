from pathlib import Path


def get_project_path() -> None:
    project_path = str(Path.cwd())
    text = project_path.split('\\')
    for each in text:
        if each == '/Cellenium':
            print(each)



get_project_path()
