from dataclasses import dataclass, field
from random import randint


@dataclass
class Random:

    _list: list = field(default_factory=list)
    num = randint(0, 50000)

    def __post_init__(self):
        self.result = self.num/50000
        self._list.append(self.result)

    def random(self) -> None:

        if self.result > 0.5:
            print(round(self.result))
        else:
            print(0)

        print(self._list)


random = Random()
if __name__ == '__main__':
    random.random()
