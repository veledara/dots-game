# Example file showing a basic pygame "game loop"
import pygame
from constants import WIDTH, HEIGHT
from game_field import GameField

FPS = 60
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dots")


def main():
    run = True
    game_field = GameField(dots_amount=144)

    clock = pygame.time.Clock()
    turn: int = 0
    while run:
        clock.tick(FPS)
        pass
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                temp = game_field.check_for_dot_hit(pos, turn)
                turn = temp
                print(turn)

        game_field.draw_field(WIN)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
