from abc import ABC, abstractmethod


class Executor(ABC):

    @abstractmethod
    def execute(self, *args: any, **kwargs: any) -> None:
        ...
