from dataclasses import dataclass
from core.infrastructure.modules.logger import Logger


log = Logger()


@dataclass
class App:

    numbers: list

    def sun_last_2_numbers(self) -> int:

        self.numbers.sort(reverse=True)
        outcome = self.numbers[0] + self.numbers[1]
        log.level.info(f'result is: {outcome}')
        return outcome


app = App([1, 4, 40, 2])
if __name__ == '__main__':
    app.sun_last_2_numbers()
