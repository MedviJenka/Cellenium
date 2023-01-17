from dataclasses import dataclass
from typing import Self


@dataclass(frozen=True)
class InfiniteNumberIterator:

    num: int = 0

    def __iter__(self) -> Self:
        return self

    def __next__(self) -> int:
        self.num += 1
        return self.num


def main() -> None:
    ...


if __name__ == '__main__':
    main()
