import pygame
from pygame.locals import *
from src.entities.placeholder import Placeholder
from src.entities.character import Character


class Jellyfish(Character):
    # Sprite sheet path
    base_path = ["meduse_idle", "meduse_active"]
    base_scale = 0.3

    def __init__(self, pos=(0,0), sheets_path = base_path, scale=base_scale, animation_speed=10):
        super().__init__(sheets_path, pos, scale, animation_speed)


    def bounce(self, player):
        player.velocity = -player.jump_strength