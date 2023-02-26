from dataclasses import dataclass
from typing import Optional
import os


@dataclass
class Person:

    _name: str
    _id: Optional[str]

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    def get_data(self) -> str:
        return f'name: {self._name}, id: {self._id}'


person = Person('jenia', '123')


class TestPerson:

    def test_name(self) -> None:
        person.name = 'alex'
        assert person.get_data() == 'name: alex, id: 123'
