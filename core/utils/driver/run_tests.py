from dataclasses import dataclass


@dataclass
class RunTests:

    class_name: object = __name__

    def start(self, methods: list[str]) -> None:
        [getattr(self.class_name, each_method)() for each_method in methods]
