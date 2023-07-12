import pygame
from constants import DotState, WHITE, BLACK, FONT, SCREEN_WIDTH, SCREEN_HEIGHT, GAME_HEIGHT


class GameInterface:
    def __init__(self) -> None:
        self.score: tuple

    def draw_interface(self, surface, score):
        surface.fill(WHITE)
        blue_score = score[0]
        red_score = score[1]
        score_text = FONT.render(f"{blue_score} - {red_score}", True, BLACK)   

        textRect = score_text.get_rect()
        textRect.center = (SCREEN_WIDTH // 2, (SCREEN_HEIGHT - GAME_HEIGHT) // 2)
        surface.blit(score_text, textRect)
