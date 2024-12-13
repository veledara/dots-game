from tkinter.font import Font
import pygame
from enum import Enum

class DotState(Enum):
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)
    EXBLUE = (0, 0, 128)
    EXRED = (128, 0, 0)


FPS = 60
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 875
GAME_WIDTH, GAME_HEIGHT = 800, 800
DOTS = 256
SMOOTHNESS_OF_COLORING = 8

pygame.init()
SCORE_FONT = pygame.font.Font(r"src\fonts\pixel_font.ttf", 64)
TEXT_FONT = pygame.font.Font(r"src\fonts\pixel_font.ttf", 24)

LIGHTGRAY = (211, 211, 211)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

