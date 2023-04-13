from time import perf_counter
from core.infrastructure.modules.methods import log
from functools import wraps


def memoize(func: callable) -> callable:

    """
    optimizing the function runtime
    """

    cache = {}

    @wraps(func)
    def wrapper(*args: any, **kw: any) -> any:
        key = str(args) + str(kw)
        if key not in cache:
            cache[key] = func(*args, **kw)

        return cache[key]

    return wrapper


def measure_execution_time(func: callable) -> callable:

    """
    measuring run time of a function
    """

    def wrapper() -> None:
        start = perf_counter()
        func()
        end = perf_counter()
        result = end - start
        log(text=f'function run took {result:.3f} sec')
        print(f'function run took {result:.3f} sec')

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
