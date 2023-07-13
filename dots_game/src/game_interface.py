import pygame
from constants import (
    DotState,
    WHITE,
    BLACK,
    SCORE_FONT,
    TEXT_FONT,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    GAME_HEIGHT,
)


class GameInterface:
    def __init__(self, surface) -> None:
        self.game_interface_surface = surface

    def draw_interface(self, score, turn):
        self.game_interface_surface.fill(WHITE)
        self.draw_current_turn(turn)
        self.draw_score(score)

    def draw_current_turn(self, turn):
        if turn == DotState.BLUE:
            text = TEXT_FONT.render("Blue player's turn", True, turn.value)
            text_rect = text.get_rect()
        else:
            text = TEXT_FONT.render("Red player's turn", True, turn.value)
            text_rect = text.get_rect()
        text_rect.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT - GAME_HEIGHT) // 2 - 20)
        self.game_interface_surface.blit(text, text_rect)

    def draw_score(self, score):
        blue_score = score[0]
        red_score = score[1]

        blue_score_text = SCORE_FONT.render(str(blue_score), True, DotState.BLUE.value)
        blue_score_rect = blue_score_text.get_rect()
        blue_score_rect.center = (
            SCREEN_WIDTH // 2 - 70,
            (SCREEN_HEIGHT - GAME_HEIGHT) // 2 + 10,
        )
        self.game_interface_surface.blit(blue_score_text, blue_score_rect)

        dash_text = SCORE_FONT.render("-", True, BLACK)
        dash_rect = dash_text.get_rect()
        dash_rect.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT - GAME_HEIGHT) // 2 + 10)
        self.game_interface_surface.blit(dash_text, dash_rect)

        red_score_text = SCORE_FONT.render(str(red_score), True, DotState.RED.value)
        red_score_rect = red_score_text.get_rect()
        red_score_rect.center = (
            SCREEN_WIDTH // 2 + 70,
            (SCREEN_HEIGHT - GAME_HEIGHT) // 2 + 10,
        )
        self.game_interface_surface.blit(red_score_text, red_score_rect)
