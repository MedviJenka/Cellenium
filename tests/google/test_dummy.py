from dataclasses import dataclass
from core.components.functional.methods import get_test_coverage_state


@dataclass
class Person:

    _name: str

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, new: str) -> None:
        self._name = new

    def get_data(self) -> str:
        return f'persons name is {self.name}'


person = Person('jenia')


class TestPerson:

    def test_name(self) -> None:
        try:
            person.name = 'alex'
            assert person.get_data() == 'persons name is alex'

        finally:
            get_test_coverage_state("google")
