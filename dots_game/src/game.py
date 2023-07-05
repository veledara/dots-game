from game_field import GameField, get_opposite_color
from constants import DotState
import pygame


class Game:
    def __init__(self, win, dots_amount) -> None:
        self.win = win
        self.game_field = GameField(dots_amount)
        self.turn = DotState.BLUE

    def update(self):
        self.game_field.draw_field(self.win)
        pygame.display.update()

    def move(self):
        pos = pygame.mouse.get_pos()
        if self.game_field.check_for_dot_hit(pos=pos, turn=self.turn):
            self.turn = get_opposite_color(self.turn)
            self.game_field.red_captured_territory, self.game_field.blue_captured_territory = self.game_field.capturing_check()

    def change_turn(self):
        if self.turn == DotState.BLUE:
            self.turn = DotState.RED
        else:
            self.turn = DotState.BLUE


