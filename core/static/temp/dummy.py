def func1() -> any:
    for a in range(1, 5):
        yield a


def func2() -> any:
    for b in range(6, 10):
        yield b


def generator() -> any:
    yield from func1()
    print('ok')
    yield from func2()


if __name__ == '__main__':
    gen = generator()
    print(gen.__next__())
    for a in range(10):
        print(next(gen))
