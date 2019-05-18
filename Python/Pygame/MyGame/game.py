import pygame
from pygame import locals as const
from constantes import *
from barre import Barre
from balle import Balle


class Game:
    def __init__(self, window: pygame.Surface):
        self.window = window
        self.proceed = True
        self.barre = Barre(self.window)
        self.balle = Balle(self.window)
        self.controles = {
            HAUT:   const.K_UP,
            BAS:    const.K_DOWN
        }

    def prepare(self):
        pygame.key.set_repeat(200, 50)
        self.proceed = True
        self.barre = Barre(self.window)
        self.balle = Balle(self.window)

    def update_screen(self):
        pygame.draw.rect(self.window, (0, 0, 0), (0, 0) + self.window.get_size())
        pygame.draw.rect(self.window, (255, 255, 255), (
            self.window.get_width() // 2 - 1, 0, 2, self.window.get_height()))
        self.barre.render()
        self.balle.render()

    def process_event(self, event: pygame.event):
        if event.type == const.KEYDOWN:
            if event.key == self.controles[HAUT]:
                self.barre.move(HAUT)
            if event.key == self.controles[BAS]:
                self.barre.move(BAS)
        if event.type == const.QUIT:
            self.proceed = False

    def start(self):
        self.prepare()
        clock = pygame.time.Clock()
        done = False
        ball_list = []

        ball = self.balle.make_ball()
        ball_list.append(ball)

        while not done:
            # --- Event Processing
            for event in pygame.event.get():
                self.process_event(event)

                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    ball_list.append(ball)

            self.balle.move(self.barre)

            self.update_screen()

            clock.tick(60)

            pygame.display.flip()
