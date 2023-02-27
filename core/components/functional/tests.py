from unittest import TestCase
from core.components.functional.methods import run_test, Decorators
from time import sleep


decorator = Decorators()


@decorator.measure_execution_time
def test_runtime() -> None:
    for a in range(3):
        sleep(3)
        print(a)

