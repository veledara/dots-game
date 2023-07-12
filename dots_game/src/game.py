from game_field import GameField
from game_interface import GameInterface
from constants import (
    DotState,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    GAME_WIDTH,
    GAME_HEIGHT,
    FPS,
)
import pygame


class Game:
    def __init__(self, dots_amount) -> None:
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.game_field_surface = pygame.Surface([GAME_WIDTH, GAME_HEIGHT])
        self.game_field = GameField(dots_amount)
        self.game_interface_surface = pygame.Surface(
            [SCREEN_WIDTH, SCREEN_HEIGHT - GAME_HEIGHT]
        )
        self.game_interface = GameInterface()
        self.score = (0, 0)
        self.turn = DotState.BLUE

    def update(self):
        self.game_field.draw_field(self.game_field_surface)
        self.game_interface.draw_interface(self.game_interface_surface, self.score)
        pygame.display.update()

    def move(self):
        pos = pygame.mouse.get_pos()
        if self.game_field.check_for_dot_hit(pos=pos, turn=self.turn):
            self.change_turn()
            r, b = self.game_field.capturing_check()
            self.game_field.red_captured_territory.update(r)
            self.game_field.blue_captured_territory.update(b)
            print("\n")
            print(f"Red captured territory: {self.game_field.red_captured_territory}")
            print("\n")
            print(f"Blue captured territory: {self.game_field.blue_captured_territory}")
            print("\n")
            self.score = self.game_field.get_current_score()

    def change_turn(self):
        if self.turn == DotState.BLUE:
            self.turn = DotState.RED
        else:
            self.turn = DotState.BLUE

    def main(self):
        pygame.init()
        run = True
        clock = pygame.time.Clock()
        while run:
            clock.tick(FPS)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.move()
            self.update()
            self.screen.blit(self.game_field_surface, (0, 0))
            self.screen.blit(self.game_interface_surface, (0, GAME_HEIGHT))
        pygame.quit()
