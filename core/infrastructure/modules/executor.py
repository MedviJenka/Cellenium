from abc import ABC, abstractmethod


class Executor(ABC):

    """"
    abstract executor method for each complex tool
    """

    @abstractmethod
    def execute(self, *args: any, **kwargs: any) -> any:
        ...
