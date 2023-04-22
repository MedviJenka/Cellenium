import json
from typing import Optional
from abc import ABC, abstractmethod


class Abstract(ABC):

    @staticmethod
    def read_json(path: str) -> dict[str]:
        with open(path, 'r', encoding='utf-8') as file:
            json_file = json.load(file)
        return json_file

    @abstractmethod
    def execute(self, *args: Optional[any], **kwargs: Optional[any]) -> None:
        ...
