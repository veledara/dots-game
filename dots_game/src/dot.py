import pygame
from constants import DotState, SMOOTHNESS_OF_COLORING


class Dot:
    def __init__(self, pos, coords=None) -> None:
        self.pos = pos
        self.coords = coords
        self.state = DotState.WHITE
        self.color = self.state.value
        self.captured = False
        self.circle = None
        self.next = None
        self.last = None

    def gradient(self):
        r, g, b = self.color
        sm = SMOOTHNESS_OF_COLORING
        if self.state == DotState.BLUE:
            self.color = (max(r - sm, 0), max(g - sm, 0), min(b + sm, 255))
        else:
            self.color = (min(r + sm, 255), max(g - sm, 0), max(b - sm, 0))
        return self.color

    def draw(self, win):
        current_color = (
            DotState.WHITE.value if self.state == DotState.WHITE else self.gradient()
        )
        self.circle = pygame.draw.circle(
            surface=win,
            color=current_color,
            center=self.coords,
            radius=6,
        )

    def __repr__(self) -> str:
        return f"This dot on {self.coords} is {self.state}"
