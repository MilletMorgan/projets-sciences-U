import pygame
from constantes import *


class Raquette:
    def __init__(self, ecran: pygame.Surface):
        self.ecran = ecran
        self.ecran_large = self.ecran.get_width()  # ca vous nous servir pour centrer la raquette et regarder
        # si la raquette sort de l'écran ou non
        self.ecran_haut = self.ecran.get_height()  # idem
        self.image = pygame.image.load("images/raquette.png").convert_alpha()
        self.pos = [20, (self.ecran_haut - self.image.get_height()) // 2]  # on centre notre raquette à droite

    def render(self):
        self.ecran.blit(self.image, self.pos)

    def move(self, dir: int = RIEN):
        # on test toutes les collisions possibles
        # et voici l'utilité de nos constantes !
        if dir == HAUT:
            if self.pos[1] - VITESSE_RAQUETTE >= 0:
                self.pos[1] -= VITESSE_RAQUETTE
            else:
                self.pos[1] = 0
        elif dir == BAS:
            if self.pos[1] + VITESSE_RAQUETTE <= self.ecran_haut - self.image.get_height():
                self.pos[1] += VITESSE_RAQUETTE
            else:
                self.pos[1] = self.ecran_haut - self.image.get_height()

    def collide_with_me(self, pos_objet: tuple, taille_objet: tuple):
        # utile pour savoir si la balle collide avec la raquette
        if self.pos[0] <= pos_objet[0] <= self.pos[0] + self.image.get_width() and \
                self.pos[1] <= pos_objet[1] <= self.pos[1] + self.image.get_height():
            # le coté gauche de la balle est dans la raquette
            return True
        elif self.pos[0] <= pos_objet[0] + taille_objet[0] <= self.pos[0] + self.image.get_width() and \
                self.pos[1] <= pos_objet[1] + taille_objet[1] <= self.pos[1] + self.image.get_height():
            # le coté droit de la balle est dans la raquette
            return True
        # enfin, on a pas eu de collision, donc on return False
        return False