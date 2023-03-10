from dataclasses import dataclass
from core.infrastructure.modules.decorators import Decorators


test = Decorators()


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
    @test.negative
    def test_negative_name(self) -> None:
        person.name = 'jenia'
        assert person.get_data() == 'persons name is alex'

    def test_name(self) -> None:
        person.name = 'alex'
        assert person.get_data() == 'persons name is alex'

    def test_math(self) -> None:
        assert 1 + 1 == 2
