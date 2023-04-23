import pygame
from core.matrix.constants import Constant
from core.matrix.globals import FONT_PATH, FONT_SIZE, RESOLUTION


class Fonts:

    font_1 = pygame.font.Font(FONT_PATH, FONT_SIZE)
    font_2 = pygame.font.Font(FONT_PATH, FONT_SIZE - FONT_SIZE // 10)
    font_3 = pygame.font.Font(FONT_PATH, FONT_SIZE - FONT_SIZE // 3)


class GreenChars:

    green_chars = [Fonts.font_1.render(char, True, (0, 255, 0)) for char in Constant.chars]
    green_chars_2 = [Fonts.font_2.render(char, True, (0, 255, 0)) for char in Constant.chars]
    green_chars_3 = [Fonts.font_3.render(char, True, (0, 255, 0)) for char in Constant.chars]


class Screen:

    screen = pygame.display.set_mode(RESOLUTION)
    display_surface = pygame.Surface(RESOLUTION)
    display_surface.set_alpha(Constant.alpha_value)
    clock = pygame.time.Clock()
