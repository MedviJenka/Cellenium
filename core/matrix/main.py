import pygame
from random import choice, randrange
from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Optional


WIDTH, HEIGHT = 400, 200
RESOLUTION = (WIDTH, HEIGHT)
FONT_SIZE = 10

chars = [
    'あ', 'み', 'む', 'め',
    'も', 'さ', 'し', 'す',
    'せ', 'そ', 'や', 'よ',
    'と', 'り', 'る', 'れ',
    'ゑ', 'を', 'あ', 'い',
    'う', 'え', 'か', 'り',
    '+', '=', '*', '/',
    '$', '1', '2', '3',
    '4', '5', '6', '7', '8',
    '9', '0', '#', "@"
]


pygame.init()
alpha_value = randrange(35, 40, 5)
font = r'C:\Users\medvi\OneDrive\Desktop\Cellenium\core\matrix\font\MS Mincho.ttf'
font_1 = pygame.font.Font(font, FONT_SIZE)
font_2 = pygame.font.Font(font, FONT_SIZE - FONT_SIZE // 10)
font_3 = pygame.font.Font(font, FONT_SIZE - FONT_SIZE // 3)

green_chars = [font_1.render(char, True, (0, 255, 0)) for char in chars]
green_chars_2 = [font_2.render(char, True, (0, 255, 0)) for char in chars]
green_chars_3 = [font_3.render(char, True, (0, 255, 0)) for char in chars]


screen = pygame.display.set_mode(RESOLUTION)
display_surface = pygame.Surface(RESOLUTION)
display_surface.set_alpha(alpha_value)
clock = pygame.time.Clock()


class Execute(ABC):

    @abstractmethod
    def execute(self, *args: Optional[any], **kwargs: Optional[any]) -> None:
        ...


@dataclass
class Symbol:

    x: int
    y: int
    speed = 15
    value_1 = choice(green_chars)
    value_2 = choice(green_chars)
    value_3 = choice(green_chars)

    def draw(self) -> None:
        self.value_1 = choice(green_chars)
        self.y = self.y + self.speed if self.y < HEIGHT else - FONT_SIZE * randrange(1, 10)
        screen.blit(self.value_1, (self.x, self.y))

    def draw1(self) -> None:
        self.value_2 = choice(green_chars)
        self.y = self.y + self.speed if self.y < HEIGHT else - FONT_SIZE * randrange(1, 10)
        screen.blit(self.value_2, (self.x, self.y))

    def draw2(self) -> None:
        self.value_3 = choice(green_chars)
        self.y = self.y + self.speed if self.y < HEIGHT else - FONT_SIZE * randrange(1, 10)
        screen.blit(self.value_3, (self.x, self.y))


@dataclass
class Matrix(Execute):

    run: bool = True

    def __post_init__(self) -> None:
        self.symbols_1 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE * 3)]
        self.symbols_2 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE, WIDTH, FONT_SIZE * 6)]
        self.symbols_3 = [Symbol(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE, WIDTH, FONT_SIZE * 9)]

    def execute(self) -> None:
        while self.run:
            screen.blit(display_surface, (0, 0))
            display_surface.fill(pygame.Color('black'))
            for symbol in self.symbols_1:
                symbol.draw()
            for symbol in self.symbols_2:
                symbol.draw()
            for symbol in self.symbols_3:
                symbol.draw()

            pygame.time.delay(100)
            pygame.display.update()
            clock.tick(10)


matrix = Matrix()
if __name__ == '__main__':
    matrix.execute()
