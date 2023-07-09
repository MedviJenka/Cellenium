from enum import Enum


class Data:

    def method1(self) -> str:
        return 'method'


def data(func: Data) -> None:
    print(func.method1)


data(Data())
