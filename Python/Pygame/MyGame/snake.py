import pygame
from constantes import *


class Snake:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.window_large = self.window.get_width()
        self.window_haut = self.window.get_height()
        self.image = pygame.image.load("images/snake.png").convert_alpha()
        self.pos = [50, 50]
        self.vect_dir = [-VITESSE_SNAKE, VITESSE_SNAKE]

    def render(self):
        self.window.blit(self.image, self.pos)

    def move(self, dir: int = RIEN):
        if dir == HAUT:
            if self.pos[1] - VITESSE_SNAKE >= 0:
                self.pos[1] -= VITESSE_SNAKE
            else:
                self.pos[1] = 0
        if dir == BAS:
            if self.pos[1] + VITESSE_SNAKE <= self.window_haut - self.image.get_height():
                self.pos[1] += VITESSE_SNAKE
            else:
                self.pos[1] = self.window_haut - self.image.get_height()
        if dir == GAUCHE:
            if self.pos[0] - VITESSE_SNAKE >= 0:
                self.pos[0] -= VITESSE_SNAKE
            else:
                self.pos[0] = 0
        if dir == DROITE:
            if self.pos[0] + VITESSE_SNAKE >= 0:
                self.pos[0] += VITESSE_SNAKE
            else:
                self.pos[0] = 0

    def collide_with_me(self, pos_objet: tuple, taille_objet: tuple):
        if self.pos[0] <= pos_objet[0] <= self.pos[0] + self.image.get_width() and self.pos[1] <= pos_objet[1] <= self.pos[1] + self.image.get_height():
            return True
        elif self.pos[0] <= pos_objet[0] + taille_objet[0] <= self.pos[0] + self.image.get_width() and self.pos[1] <= pos_objet[1] + taille_objet[1] <= self.pos[1] + self.image.get_height():
            return True

        return False

