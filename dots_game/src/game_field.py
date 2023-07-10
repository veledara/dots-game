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
        self.red_captured_territory = {}
        self.blue_captured_territory = {}

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

        self.draw_borders(
            win, DotState.RED, captured_territory=self.red_captured_territory
        )
        self.draw_borders(
            win, DotState.BLUE, captured_territory=self.blue_captured_territory
        )

    def draw_borders(self, win, color, captured_territory):
        for borders in captured_territory.values():
            border_color = self.field[borders[0][0]][borders[0][1]].color
            for i in range(len(borders)):
                pygame.draw.line(
                    surface=win,
                    color=border_color,
                    start_pos=(self.field[borders[i][0]][borders[i][1]].coords),
                    end_pos=(
                        self.field[borders[(i + 1) % len(borders)][0]][
                            borders[(i + 1) % len(borders)][1]
                        ].coords
                    ),
                    width=4,
                )

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

    def capturing_check(self):
        visit = set()
        dfs_for_white_visit = set()
        red_captured_territory = {}
        blue_captured_territory = {}
        borders = []
        captured_dots = []

        def dfs_for_white(r, c, color):
            if r < 0 or c < 0 or r == self.lines or c == self.lines:
                return 0
            if self.field[r][c].state == color:
                borders.append(self.field[r][c].pos)
            if (
                self.field[r][c].state == color
                or (
                    self.field[r][c].state == get_opposite_color(color)
                    and (r, c) in visit
                )
            ) or (r, c) in dfs_for_white_visit:
                return 1
            dfs_for_white_visit.add((r, c))
            return min(
                dfs_for_white(r + 1, c, color),
                dfs_for_white(r - 1, c, color),
                dfs_for_white(r, c + 1, color),
                dfs_for_white(r, c - 1, color),
            )

        def dfs(r, c, color):
            if r < 0 or c < 0 or r == self.lines or c == self.lines:
                return 0

            if self.field[r][c].state == color:
                borders.append(self.field[r][c].pos)
            if self.field[r][c].state == get_opposite_color(color):
                captured_dots.append(self.field[r][c])

            if (
                self.field[r][c].state == DotState.WHITE
                and dfs_for_white(r, c, color) == 0
            ):
                return 0
            dfs_for_white_visit.clear()
            if self.field[r][c].state == color and self.field[r][c].captured == True:
                return 0
            if self.field[r][c].state == color or (r, c) in visit:
                return 1
            visit.add((r, c))
            return min(
                dfs(r + 1, c, color),
                dfs(r - 1, c, color),
                dfs(r, c + 1, color),
                dfs(r, c - 1, color),
            )

        for r in range(self.lines):
            for c in range(self.lines):
                if (
                    self.field[r][c].state not in [DotState.WHITE, DotState.RED]
                    and (r, c) not in visit
                ):
                    temp = dfs(r, c, DotState.RED)
                    if temp == 1:
                        sorted_borders = closest_neighbor_sort(borders)
                        for dot in captured_dots:
                            dot.captured = True
                            dot.state = DotState.EXBLUE
                        red_captured_territory[tuple(captured_dots)] = list(sorted_borders)
                        # red_captured_territory.append(list(sorted_borders))
                    captured_dots.clear()
                    borders.clear()

                if (
                    self.field[r][c].state not in [DotState.WHITE, DotState.BLUE]
                    and (r, c) not in visit
                ):
                    temp = dfs(r, c, DotState.BLUE)
                    if temp == 1:
                        sorted_borders = closest_neighbor_sort(borders)
                        for dot in captured_dots:
                            dot.captured = True
                            dot.state = DotState.EXRED
                        blue_captured_territory[tuple(captured_dots)] = list(sorted_borders)
                        # blue_captured_territory.append(list(sorted_borders))
                    captured_dots.clear()
                    borders.clear()
        return red_captured_territory, blue_captured_territory


def distance(point1, point2):
    x1, y1 = point1
    x2, y2 = point2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def closest_neighbor_sort(coords):
    sorted_coords = [coords[0]]
    coords.pop(0)

    while coords:
        min_distance = float("inf")
        closest_point = None
        for coord in coords:
            dist = distance(sorted_coords[-1], coord)
            if dist < min_distance:
                min_distance = dist
                closest_point = coord

        if min_distance <= sqrt(2):
            sorted_coords.append(closest_point)
            coords.remove(closest_point)
        else:
            break

    return sorted_coords


def get_opposite_color(color):
    if color == DotState.BLUE:
        return DotState.RED
    else:
        return DotState.BLUE


if __name__ == "__main__":
    game_field = GameField()
    print(game_field.field)
