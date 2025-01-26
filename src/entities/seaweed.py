import pygame
from pygame.locals import *
from src.entities.character import Character
from src.utils.map import Map

class Seaweed(Character):
    # Sprite sheet path
    base_path = ["seaweed"]
    base_scale = 0.5

    def __init__(self, pos=(0,0), facing_right = True, sheets_path = base_path, scale=base_scale, animation_speed=10):
        super().__init__(sheets_path, pos, scale, animation_speed)
        self.map = map
        self.facing_right = facing_right
        self.rect.bottomleft = pos
