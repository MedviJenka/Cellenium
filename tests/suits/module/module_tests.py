import json
from dataclasses import dataclass


def data_dict() -> dict:
    with open('person.json', 'r', encoding='utf-8') as file:
        file = json.load(file)
        return file


@dataclass
class Person:
    name: str
    age: int


person = Person(**data_dict())
print(person.name)
