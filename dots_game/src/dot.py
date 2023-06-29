import pygame
from constants import DotState


class Dot:
    def __init__(self, pos, coords=None) -> None:
        self.pos = pos
        self.coords = coords
        self.state = DotState.WHITE
        self.captured = False
        self.circle = None

    def draw(self, win):
        self.circle = pygame.draw.circle(
            surface=win,
            color=self.state.value,
            center=self.coords,
            radius=6,
        )

    def __repr__(self) -> str:
        return f"This dot on {self.coords} is {self.state}"
