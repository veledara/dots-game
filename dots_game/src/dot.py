import pygame
from constants import DotState


class Dot:
    def __init__(self, coords) -> None:
        self.coords = coords
        self.state = DotState.BLACK
        self.captured = False

    def __repr__(self) -> str:
        return f"This dot on {self.coords} is {self.state}"
