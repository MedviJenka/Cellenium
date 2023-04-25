import pygame
from random import randrange


class Constant:

    pygame.init()
    alpha_value = randrange(35, 40, 5)

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
