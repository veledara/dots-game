from math import sqrt
from xmlrpc.client import Boolean
import pygame
from constants import LIGHTGRAY, HEIGHT, WHITE, WIDTH, DotState
from dot import Dot


class GameField:
    def __init__(self, dots_amount=16) -> None:
        self.dots_amount = dots_amount
        self.lines = int(sqrt(dots_amount))
        self.distance_between_dots = WIDTH / (self.lines + 1)
        self.field = self.fill_field()

    def fill_field(self):
        field = [[None for dot in range(self.lines)] for line in range(self.lines)]
        for i in range(self.lines):
            for j in range(self.lines):
                dot_coords = (
                    (i + 1) * self.distance_between_dots,
                    (j + 1) * self.distance_between_dots,
                )
                field[i][j] = Dot(pos=(i, j), coords=dot_coords)
        return field

    def draw_field(self, win):
        win.fill(WHITE)
        for i in range(1, self.lines + 1):
            pygame.draw.line(
                surface=win,
                color=LIGHTGRAY,
                start_pos=((self.distance_between_dots * (i)), 0),
                end_pos=((self.distance_between_dots * (i)), HEIGHT),
                width=3,
            )
            pygame.draw.line(
                surface=win,
                color=LIGHTGRAY,
                start_pos=(0, (self.distance_between_dots * (i))),
                end_pos=(WIDTH, (self.distance_between_dots * (i))),
                width=3,
            )
        for i in range(1, self.lines + 1):
            for j in range(1, self.lines + 1):
                dot = self.field[i - 1][j - 1]
                dot.draw(win)

    def check_for_dot_hit(self, pos, turn) -> Boolean:
        for i in range(self.lines):
            for j in range(self.lines):
                dot = self.field[i][j]
                if dot.circle.collidepoint(pos):
                    if dot.state in [DotState.RED, DotState.BLUE]:
                        return False
                    dot.state = turn
                    return True
        return False


if __name__ == "__main__":
    game_field = GameField()
    print(game_field.field)
