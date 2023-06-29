import pygame
from enum import Enum


class DotState(Enum):
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    WHITE = (255, 255, 255)


WIDTH, HEIGHT = 600, 600
DOTS = 16

LIGHTGRAY = (211, 211, 211)
WHITE = (255, 255, 255)
