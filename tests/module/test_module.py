from dataclasses import dataclass


@dataclass
class Person:

    name: str
    age: int

    @property
    def name(self) -> str:
        return self.name

    @name.setter
    def name(self, new: str) -> None:
        self.name = new

    def get_data(self) -> str:
        return f'name: {self.name}'


@dataclass
class TestPerson:

    person = Person('jenia', 29)

    def test_name(self) -> None:
        self.person.name = 'gabriel'
        assert self.person.get_data() == 'name: gabriel'
