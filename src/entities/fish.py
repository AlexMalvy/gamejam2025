import pygame
from pygame.locals import *
from src.entities.character import Character
from src.utils.map import Map
import random
import math


class Fish(Character):
    speed = 3

    # Sprite sheet path
    base_path = ["fish"]
    base_scale = 0.25

    spawn_immunity_timer = 1000

    def __init__(self, map: Map, pos=(0,0), facing_right = True, speed = 3, sheets_path = base_path, scale=base_scale, animation_speed=10):
        super().__init__(sheets_path, pos, scale, animation_speed)
        self.map = map
        self.facing_right = facing_right
        self.spawn_timer = pygame.time.get_ticks()
        self.base_y = pos[1]

    def update(self):
        super().update()
        if self.facing_right:
            self.rect.x += self.speed
            if self.rect.left > self.map.map_rect.right:
                self.kill()
        else:
            self.rect.x -= self.speed
            if self.rect.right < self.map.map_rect.left:
                self.kill()

        self.rect.y = self.base_y + 50 * math.sin(self.rect.x / 50)

        if not self.rect.colliderect(self.map.map_rect):
            self.kill()