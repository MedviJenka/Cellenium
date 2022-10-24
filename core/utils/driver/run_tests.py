from dataclasses import dataclass
from core.utils.logs.generator import get_logger


@dataclass
class RunTests:

    log = get_logger(__name__)

    def start(self, class_name: object, methods: list[str]) -> None:
        for each_method in methods:
            getattr(class_name, each_method)()
            return self.log
