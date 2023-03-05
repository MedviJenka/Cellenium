from time import time
from core.infrastructure.modules.methods import log


class Decorators:

    @staticmethod
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

    @staticmethod
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
