from dataclasses import dataclass
from core.infrastructure.modules.executor import Executor


@dataclass
class Nessus(Executor):

    def execute(self) -> any:
        ...
