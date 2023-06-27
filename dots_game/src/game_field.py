from math import sqrt
import pygame
from constants import BLACK, HEIGHT, WHITE, WIDTH
from dot import Dot


class GameField:
    def __init__(self, dots_amount=16) -> None:
        self.dots_amount = dots_amount
        self.lines = int(sqrt(dots_amount))
        self.field = [[None for dot in range(self.lines)] for line in range(self.lines)]

    def draw_dots(self, win):
        win.fill(WHITE)
        distance = WIDTH / (self.lines + 1)
        for i in range(1, self.lines + 1):
            pygame.draw.line(
                surface=win,
                color=BLACK,
                start_pos=((distance * (i)), 0),
                end_pos=((distance * (i)), HEIGHT),
                width=3,
            )
            pygame.draw.line(
                surface=win,
                color=BLACK,
                start_pos=(0, (distance * (i))),
                end_pos=(WIDTH, (distance * (i))),
            )
            for j in range(1, self.lines + 1):
                dot_coords = ((i) * distance, (j) * distance)
                self.field[i - 1][j - 1] = Dot(dot_coords)
                pygame.draw.circle(
                    surface=win,
                    color=BLACK,
                    center=dot_coords,
                    radius=5,
                )
        # print(self.board)


if __name__ == "__main__":
    game_field = GameField()
    print(game_field.field)
