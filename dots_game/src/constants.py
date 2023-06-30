import pygame
from enum import Enum


class DotState(Enum):
    WHITE = (255, 255, 255)
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)


WIDTH, HEIGHT = 600, 600
DOTS = 16
SMOOTHNESS_OF_COLORING = 8

LIGHTGRAY = (211, 211, 211)
WHITE = (255, 255, 255)
