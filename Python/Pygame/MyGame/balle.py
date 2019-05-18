import pygame
from constantes import *
import random
from random import randint


class Balle:
    def __init__(self, window: pygame.Surface):
        self.x = 0
        self.y = 0
        self.pos = [self.x, self.y]
        self.change_x = 0
        self.change_y = 0
        self.window = window
        self.vect_dir = [-VITESSE_BALLE, VITESSE_BALLE]

    def render(self):
        pygame.draw.circle(self.window, WHITE, [self.x, self.y], BALL_SIZE)

    def make_ball(self):
        self.x = random.randrange(BALL_SIZE, SCREEN_WIDTH - BALL_SIZE)
        self.y = random.randrange(BALL_SIZE, SCREEN_HEIGHT - BALL_SIZE)
        self.change_x = random.randrange(-2, 3)
        self.change_y = random.randrange(-2, 3)

    def move(self, barre):
        self.x += self.change_x
        self.y += self.change_y

        collision = barre.collide_with_me(self.pos, (BALL_SIZE, BALL_SIZE))
        if collision or self.pos[0] <= 0 or self.pos[0] + BALL_SIZE >= self.window.get_width():
            self.change_x *= -1
            self.change_y *= -1
        if self.pos[1] <= 0 or self.pos[1] + BALL_SIZE >= self.window.get_height():
            self.change_x *= -1
            self.change_y *= -1

        if self.y > SCREEN_HEIGHT - BALL_SIZE or self.y < BALL_SIZE:
            self.change_y *= -1
        if self.x > SCREEN_WIDTH - BALL_SIZE or self.x < BALL_SIZE:
            self.change_x *= -1

