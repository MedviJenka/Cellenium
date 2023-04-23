import pygame
from random import randrange
from dataclasses import dataclass
from core.matrix.executor import Execute
from core.matrix.symbols import Symbols
from core.matrix.ui import Screen
from core.matrix.globals import *


@dataclass
class Matrix(Execute):

    run: bool = True

    def __post_init__(self) -> None:
        self.symbols_1 = [Symbols(x, randrange(-HEIGHT, 0)) for x in range(0, WIDTH, FONT_SIZE * 3)]
        self.symbols_2 = [Symbols(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE, WIDTH, FONT_SIZE * 6)]
        self.symbols_3 = [Symbols(x, randrange(-HEIGHT, 0)) for x in range(FONT_SIZE, WIDTH, FONT_SIZE * 9)]

    def execute(self) -> None:
        while self.run:
            Screen.screen.blit(Screen.display_surface, (0, 0))
            Screen.display_surface.fill(pygame.Color('black'))
            for symbol in self.symbols_1:
                symbol.draw()
            for symbol in self.symbols_2:
                symbol.draw()
            for symbol in self.symbols_3:
                symbol.draw()

            pygame.time.delay(100)
            pygame.display.update()
            Screen.clock.tick(10)


matrix = Matrix()
if __name__ == '__main__':
    matrix.execute()
