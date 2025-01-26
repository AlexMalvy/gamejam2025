import pygame
from pygame.locals import *
from src.entities.character import Character


class Shark(Character):
    stunned = False
    stunned_max_timer = 400
    stunned_timer: int = 0

    speed = 2

    # Sprite sheet path
    base_path = ["shark"]
    base_scale = 0.45

    def __init__(self, pos=(0,0), sheets_path = base_path, scale=base_scale, animation_speed=10):
        super().__init__(sheets_path, pos, scale, animation_speed)

    def update(self):
        super().update()

        # Move
        self.rect.x += self.speed

        # Stun fading
        if self.stunned:
            if self.stunned_timer + self.stunned_max_timer < pygame.time.get_ticks():
                self.stunned = False

    def get_stunned(self):
        self.stunned = True
        self.stunned_timer = pygame.time.get_ticks()

    def bounce(self, player):
        player.velocity = -player.jump_strength

    def turn_around(self):
        self.speed = -self.speed
        self.facing_right = not self.facing_right