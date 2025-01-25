import pygame
from pygame.locals import *
from src.entities.placeholder import Placeholder


class Jellyfish(Placeholder):
    def __init__(self, color, x, y, width = 100, height = 100):
        super().__init__(color, x, y, width, height)

    def bounce(self, player):
        player.velocity = -player.jump_strength