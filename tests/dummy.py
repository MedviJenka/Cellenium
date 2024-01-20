from dataclasses import dataclass
from enum import Enum


class Function:

    @staticmethod
    def func1() -> int:
        return 1

    @staticmethod
    def func2() -> int:
        return 2


class Types(Enum):

    ONE = Function.func1()
    TWO = Function.func2()


print(Types.__members__)
