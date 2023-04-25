from dataclasses import dataclass
from random import choice, randrange
from app.matrix.globals import HEIGHT, FONT_SIZE
from app.matrix.ui import GreenChars, Screen


@dataclass
class Symbols(GreenChars):

    x: int
    y: int
    speed = 15
    value_1 = choice(GreenChars.green_chars)
    value_2 = choice(GreenChars.green_chars)
    value_3 = choice(GreenChars.green_chars)

    def draw(self) -> None:
        self.value_1 = choice(GreenChars.green_chars)
        self.y = self.y + self.speed if self.y < HEIGHT else - FONT_SIZE * randrange(1, 10)
        Screen.screen.blit(self.value_1, (self.x, self.y))

    def draw1(self) -> None:
        self.value_2 = choice(GreenChars.green_chars)
        self.y = self.y + self.speed if self.y < HEIGHT else - FONT_SIZE * randrange(1, 10)
        Screen.screen.blit(self.value_2, (self.x, self.y))

    def draw2(self) -> None:
        self.value_3 = choice(GreenChars.green_chars)
        self.y = self.y + self.speed if self.y < HEIGHT else - FONT_SIZE * randrange(1, 10)
        Screen.screen.blit(self.value_3, (self.x, self.y))
