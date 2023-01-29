import logging
from abc import ABC, abstractmethod
from math import sqrt
from time import perf_counter


class AbstractComponent(ABC):
    @abstractmethod
    def execute(self, upper_bound: int) -> int:
        ...


class AbstractDecorator(AbstractComponent, ABC):
    def __init__(self, decorated: AbstractComponent) -> None:
        self._decorated = decorated


def is_prime(number: int) -> bool:
    if number < 2:
        return False
    for element in range(2, int(sqrt(number)) + 1):
        if number % element == 0:
            return False
    return True


class ConcreteComponent(AbstractComponent):
    def execute(self, upper_bound: int) -> int:
        count = 0
        for number in range(upper_bound):
            if is_prime(number):
                count += 1
        return count


class BenchmarkDecorator(AbstractDecorator):
    def execute(self, upper_bound: int) -> int:
        start_time = perf_counter()
        value = self._decorated.execute(upper_bound)
        end_time = perf_counter()
        run_time = end_time - start_time
        logging.info(
            f'Execution of {self._decorated.__class__.__name__} took {run_time:.1f} sec'
        )
        return value


def main() -> None:
    logging.basicConfig(level=logging.INFO)
    component = ConcreteComponent()
    component = BenchmarkDecorator(component)
    component.execute(1000000)


if __name__ == '__main__':
    main()
