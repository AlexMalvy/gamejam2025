import pygame
from pygame.locals import *
from src.entities.character import Character
from src.utils.map import Map


class YellowFish(Character):
    # Sprite sheet path
    base_path = ["clown_fish"]
    base_scale = 1


    stunned = False
    stunned_max_timer = 400
    stunned_timer: int = 0

    def __init__(self, map: Map, pos=(0,0), sheets_path = base_path, scale=base_scale, animation_speed=10):
        super().__init__(sheets_path, pos, scale, animation_speed)
        self.map = map

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
        if self.stunned:
            player.velocity = -player.jump_strength
