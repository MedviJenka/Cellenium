from abc import ABC, abstractmethod
from typing import Optional


class Service(ABC):

    @abstractmethod
    def run(self, args: Optional[any]) -> any:
        ...
