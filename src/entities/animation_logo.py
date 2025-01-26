import pygame
from pygame.locals import *
from src.entities.character import Character


class AnimationLogo(Character):

    # Sprite sheet path
    base_path = ["animation_logo"]
    base_scale = 0.25

    # State
    state = 0
    state_timer = 0
    state_duration = 100

    def __init__(self, pos=(0,0), sheets_path = base_path, scale=base_scale, animation_speed=10):
        super().__init__(sheets_path, pos, scale, animation_speed)