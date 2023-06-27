# Example file showing a basic pygame "game loop"
import pygame
from constants import WIDTH, HEIGHT
from game_field import GameField

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dots")


def main():
    run = True
    game_field = GameField(16)

    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
        game_field.draw_dots(WIN)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
