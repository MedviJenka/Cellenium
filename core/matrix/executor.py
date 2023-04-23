from typing import Optional
from abc import ABC, abstractmethod


class Execute(ABC):

    @abstractmethod
    def execute(self, *args: Optional[any], **kwargs: Optional[any]) -> None:
        ...
