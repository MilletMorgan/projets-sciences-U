import pygame
from pygame import locals as const
from game import Game
from constantes import *


def main():
    pygame.init()

    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    fond = pygame.image.load("images/fond.png").convert_alpha()
    proceed = True
    game = Game(window)

    while proceed:
        for event in pygame.event.get():
            if event.type == const.QUIT or (event.type == const.KEYDOWN and event.key == const.K_ESCAPE):
                proceed = 0
            if event.type == const.KEYDOWN:
                game.start()

        window.blit(fond, (0, 0))

        pygame.display.flip()

    pygame.quit()


if __name__ == '__main__':
    main()
