import pygame
from constantes import *
from random import randint

class Balle:
    def __init__(self, ecran: pygame.Surface):
        self.ecran = ecran
        self.vect_dir = [-VITESSE_BALLE, VITESSE_BALLE]
        self.image = pygame.image.load("images/balle.png").convert_alpha()
        self.b_large = self.image.get_width()
        self.b_haut = self.image.get_height()
        self.pos = [(self.ecran.get_width() - self.b_large) // 2, (self.ecran.get_height() - self.b_haut) // 2]

    def move(self, raquette):
        self.pos[0] += self.vect_dir[0] * VITESSE_BALLE
        self.pos[1] += self.vect_dir[1] * VITESSE_BALLE

        collision = raquette.collide_with_me(self.pos, (self.b_large, self.b_haut))
        if collision or self.pos[0] <= 0 or self.pos[0] + self.b_large >= self.ecran.get_width():
            self.vect_dir[0] = - self.vect_dir[0] + randint(100, 225) / 1000
            self.vect_dir[1] = randint(100, 225) / 100
        if self.pos[1] <= 0 or self.pos[1] + self.b_haut >= self.ecran.get_height():
            self.vect_dir[0] = randint(100, 225) / 100
            self.vect_dir[1] = - self.vect_dir[1] + randint(100, 225) / 1000

    def render(self):
        self.ecran.blit(self.image, self.pos)
