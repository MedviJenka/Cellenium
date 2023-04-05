from dataclasses import dataclass
from core.infrastructure.modules.decorators import Decorators


test = Decorators()


@dataclass
class Person:

    name: str
    age: int

    @property
    def name(self) -> str:
        return self.name

    @property
    def age(self) -> int:
        return self.age

    @name.setter
    def name(self, new: str) -> None:
        self.name = new

    @age.setter
    def age(self, new) -> None:
        self.age = new

    def get_data(self) -> str:
        return f'name: {self.name}, age: {self.age}'


class TestPerson:

    @test.negative
    def test_name(self) -> None:
        person = Person(name='jenia', age=29)
        person.name = 'gabriel'
        person.age = 30
        assert person.get_data() == 'name: alex, age: 30'
