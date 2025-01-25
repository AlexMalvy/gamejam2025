import pygame
from pygame.locals import *
from utils.placeholder import Placeholder


class Bubble(Placeholder):
    lift_strength = 0.25
    max_lift = 10

    def __init__(self, color, x, y, width, height):
        super().__init__(color, x, y, width, height)

    def lift(self, player):
        if player.velocity > -self.max_lift:
            player.velocity -= self.lift_strength + player.falling_speed