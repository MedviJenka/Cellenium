from functools import wraps
from time import perf_counter
import sys


def memorize(func: callable) -> callable:

    cache = {}

    @wraps(func)
    def wrapper(*args: any, **kw) -> any:
        key = str(args) + str(kw)
        if key not in cache:
            cache[key] = func(*args, **kw)
        return cache[key]
    return wrapper


@memorize
def fibonacci(n: int) -> int:
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    start = perf_counter()
    fib = fibonacci(36)
    end = perf_counter()
    print(fib)
    print(f'time: {end - start}')
