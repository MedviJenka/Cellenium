from abc import ABC, abstractmethod


class AbstractBlock(ABC):

    @abstractmethod
    def open(self, *args: any, **kwargs: any) -> None: ...

    @abstractmethod
    def teardown(self) -> None: ...
