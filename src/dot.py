import pygame
from src.constants import DotState, SMOOTHNESS_OF_COLORING


class Dot:
    def __init__(self, pos, coords=None) -> None:
        self.pos = pos
        self.coords = coords
        self.state = DotState.WHITE
        self.color = self.state.value
        self.circle = None

    def gradient(self, end_color):
        r, g, b = self.color
        r_end, g_end, b_end = end_color
        sm = SMOOTHNESS_OF_COLORING
        r = min(r + sm, r_end) if r_end > r else max(r - sm, r_end)
        g = min(g + sm, g_end) if g_end > g else max(g - sm, g_end)
        b = min(b + sm, b_end) if b_end > b else max(b - sm, b_end)
        self.color = (r, g, b)
        return self.color

    def draw(self, win):
        if self.state == DotState.WHITE:
            current_color = DotState.WHITE.value
        else:
            current_color = self.gradient(self.state.value)
        self.circle = pygame.draw.circle(
            surface=win,
            color=current_color,
            center=self.coords,
            radius=6,
        )

    def __repr__(self) -> str:
        return f"This dot on {self.pos} is {self.state}"
