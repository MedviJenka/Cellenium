from functools import wraps


def say_hi(func) -> callable:
    @wraps(func)
    def __call__() -> None:
        print("hi")

    return __call__


@say_hi
def say_bye() -> None:
    print("bye")


if __name__ == "__main__":
    say_bye()
