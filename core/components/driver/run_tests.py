from dataclasses import dataclass
from core.components.logs.log_generator import Log


class DummyClass:

    def test1(self) -> None: ...
    def test2(self) -> None: ...
    def test3(self) -> None: ...


@dataclass
class RunTests(Log):

    def start(self, class_name: object, methods: list[str]) -> None:
        for each_method in methods:
            getattr(class_name, each_method)()
        self.get_log()


def main() -> None:
    run = RunTests()
    run.start(DummyClass(), ['test1', 'test2', 'test3'])


if __name__ == "__main__":
    main()
