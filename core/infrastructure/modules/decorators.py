from time import time
from core.infrastructure.modules.methods import log
from functools import wraps


def memoize(function: callable) -> wraps:

    cache = {}

    @wraps(function)
    def wrapper(*args: any, **kwargs: any) -> dict[str]:
        key = str(args) + str(kwargs)
        if key not in cache:
            cache[key] = function(*args, **kwargs)
        return cache[key]
    return wrapper


def measure_execution_time(func: callable) -> callable:

    """
    measuring run time of a function
    """

    def wrapper() -> None:
        start = time()
        func()
        end = time() - start
        log(text=f'function run took {end:.3f} sec')
        print(f'function run took {end:.3f} sec')

    return wrapper


def negative(exception_type: Exception(any)):

    """
    This decorator function takes in a function as an argument
    and returns a new function that wraps the original function.
    When the new function is called, it calls the original
    function with the same arguments and catches any AssertionError that might be raised.
    If an AssertionError is caught, it prints out the error message and then re-raises the exception.
    """

    def decorator(func):
        def wrapper(*args: any, **kwargs: any):
            try:
                log(text=f"{func.__name__} raised {exception_type.__name__}")
                func(*args, **kwargs)
            except exception_type:
                log(text=f"{func.__name__} did not raise {exception_type.__name__}")
                return
            raise AssertionError(f"{func.__name__} did not raise {exception_type.__name__}")

        return wrapper

    return decorator
