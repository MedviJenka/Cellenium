from dataclasses import dataclass
from core.components.logs.log_generator import Log


@dataclass
class RunTests(Log):

    @Log.get_log()
    def start(self, class_name: object, methods: list[str]) -> None:
        for each_method in methods:
            getattr(class_name, each_method)()
            print(f'test steps: {each_method}')
