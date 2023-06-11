import json
from dataclasses import dataclass


@dataclass
class Person:

    name: str
    age: int
    id: int
    employee: bool


@dataclass
class App(Person):

    def __init__(self):
        super(Person).__init__()

    @staticmethod
    def _read_json(path='person.json') -> any:
        with open(path, 'r', encoding='utf-8') as f:
            file = json.load(f)
            return file

    def get_data(self) -> str:
        person = Person(**self._read_json())
        if not person.employee:
            return f"{person.name} not an employee"
        else:
            return f"name: {person.name}, \nage: {person.age}, \nid: {person.id}"


if __name__ == '__main__':
    app = App()
    print(app.get_data())
