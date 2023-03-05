from typing import overload


@overload
def func(a: str, b: str) -> any: ...
@overload
def func(a: str, b: bool) -> any: ...


def func(a: int, b: int) -> list[int]:
    return [a, b]


if __name__ == '__main__':
    print(type(func("1", True)))
