import pygame
from pygame.locals import *
from src.entities.placeholder import Placeholder


class Shark(Placeholder):
    stunned = False
    stunned_max_timer = 400
    stunned_timer: int = 0

    def __init__(self, color, x, y, width = 250, height = 75):
        super().__init__(color, x, y, width, height)

    def update(self):
        super().update()

        # Stun fading
        if self.stunned:
            if self.stunned_timer + self.stunned_max_timer < pygame.time.get_ticks():
                self.stunned = False

    def get_stunned(self):
        self.stunned = True
        self.stunned_timer = pygame.time.get_ticks()

    def bounce(self, player):
        player.velocity = -player.jump_strength