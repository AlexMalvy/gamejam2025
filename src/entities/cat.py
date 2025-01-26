import pygame
from pygame.locals import *
from src.entities.character import Character
from src.utils.map import Map


class Cat(Character):
    speed = 3

    # Sprite sheet path
    base_path = ["cat_swimming"]
    base_scale = 3

    def __init__(self, map: Map, pos=(0,0), sheets_path = base_path, scale=base_scale, animation_speed=10):
        super().__init__(sheets_path, pos, scale, animation_speed)
        self.map = map
        self.animation_speed = 20

    def update(self):
        super().update()

        if not self.rect.colliderect(self.map.map_rect):
            self.turn_around()

        # Move
        self.rect.x += self.speed

    def turn_around(self):
        self.speed = -self.speed
        self.facing_right = not self.facing_right