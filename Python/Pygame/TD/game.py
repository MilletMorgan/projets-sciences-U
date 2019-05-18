import pygame
from pygame import locals as const
from constantes import *
from raquette import Raquette
from balle import Balle


class Game:
    def __init__(self, ecran: pygame.Surface):
        self.ecran = ecran
        self.raquette = Raquette(self.ecran)
        self.balle = Balle(self.ecran)
        self.continuer = True
        self.controles = {
            HAUT: const.K_UP,
            BAS: const.K_DOWN
        }

    def prepare(self):
        pygame.key.set_repeat(200, 50)
        self.continuer = True
        self.raquette = Raquette(self.ecran)
        self.balle = Balle(self.ecran)

    def update_screen(self):
        pygame.draw.rect(self.ecran, (0, 0, 0), (0, 0) + self.ecran.get_size())  # on dessine le fond
        pygame.draw.rect(self.ecran, (255, 255, 255), (
        self.ecran.get_width() // 2 - 1, 0, 2, self.ecran.get_height()))  # la séparation au milieu du terrain
        self.raquette.render()  # on dessine notre raquette
        self.balle.render()  # on dessine notre balle

    def process_event(self, event: pygame.event):
        if event.type == const.KEYDOWN:
            # et revoici l'utilité de nos constantes, utilisées comme clé de dictionnaire :)
            # comme ça on peut plus facilement changer les controles ;)
            if event.key == self.controles[HAUT]:
                self.raquette.move(HAUT)
            if event.key == self.controles[BAS]:
                self.raquette.move(BAS)
        if event.type == const.QUIT:
            self.continuer = False

    def start(self):
        self.prepare()

        while self.continuer:
            for event in pygame.event.get():
                self.process_event(event)

            self.update_screen()

            self.balle.move(self.raquette)  # on déplace notre balle

            pygame.display.flip()