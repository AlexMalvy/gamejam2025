import pygame
from pygame.locals import *
from src.entities.character import Character
from src.utils.map import Map
import math


class Cat(Character):
    speed = 3

    # Sprite sheet path
    base_path = ["cat_swimming"]
    base_scale = 3

    def __init__(self, map: Map, pos=(0,0), sheets_path = base_path, scale=base_scale, animation_speed=10):
        super().__init__(sheets_path, pos, scale, animation_speed)
        self.map = map
        self.animation_speed = 20
        self.base_y = self.rect.centery

    def update(self):
        super().update()

        self.image.set_alpha(100)

        if not self.rect.colliderect(self.map.map_rect):
            self.turn_around()

        # Move
        self.rect.x += self.speed

        self.rect.y = self.base_y + 50 * math.sin(self.rect.x / 50)

    def turn_around(self):
        self.speed = -self.speed
        self.facing_right = not self.facing_right