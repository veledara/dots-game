import pygame
from constants import WIDTH, HEIGHT
from game import Game

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dots")


def main():
    run = True
    game = Game(WIN, 144)
    clock = pygame.time.Clock()
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.move()
        game.update()
    pygame.quit()


if __name__ == "__main__":
    main()
