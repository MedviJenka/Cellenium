from dataclasses import dataclass


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

    def test_negative_name(self) -> None:
        person.name = 'alex'
        assert not person.get_data() == 'persons name is alex'

    def test_name(self) -> None:
        person.name = 'alex'
        assert person.get_data() == 'persons name is alex'

    def test_math(self) -> None:
        assert 1 + 1 == 2
