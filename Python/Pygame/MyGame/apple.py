import pygame
from constantes import *
from random import randint


class Apple:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.vect_dir = [-VITESSE_APPLE, VITESSE_APPLE]
        self.image = pygame.image.load("images/apple.png").convert_alpha()
        self.b_large = self.image.get_width()
        self.b_haut = self.image.get_height()
        self.pos = [(self.window.get_width() - self.b_large) // 2, (self.window.get_height() - self.b_haut) // 2]

    def move(self, snake, dir: int = REBOND):
        self.pos[0] += self.vect_dir[0] * VITESSE_APPLE
        self.pos[1] += self.vect_dir[1] * VITESSE_APPLE

        collision = snake.collide_with_me(self.pos, (self.b_large, self.b_haut))
        if collision or self.pos[0] <= 0 or self.pos[0] + self.b_large >= self.window.get_width():
            self.vect_dir[0] = - self.vect_dir[0] + randint(1, 225) / 1000
            self.vect_dir[1] = randint(1, 225) / 1000
            dir += 1
        if self.pos[1] <= 0 or self.pos[1] + self.b_haut >= self.window.get_height():
            self.vect_dir[0] = randint(1, 225) / 1000
            self.vect_dir[1] = - self.vect_dir[1] + randint(1, 225) / 1000
            dir += 1

        myfont = pygame.font.SysFont("monospace", 15)

        text = myfont.render(str(dir), 1, (150, 150, 150))
        self.window.blit(text, (50 - text.get_width() // 2, 15 - text.get_height() // 2))

    def render(self):
        self.window.blit(self.image, self.pos)
