import pygame
from pygame.locals import *
from src.entities.character import Character


class Coral(Character):
    lift_strength = 0.25
    max_lift = 10

    # Sprite sheet path
    base_path = ["coral"]
    base_scale = 0.55

    # State
    state = 0
    state_timer = 0
    state_duration = 100

    def __init__(self, pos=(0,0), sheets_path = base_path, scale=base_scale, animation_speed=10):
        super().__init__(sheets_path, pos, scale, animation_speed)

    def lift(self, player):
        if player.velocity > -self.max_lift:
            player.velocity -= self.lift_strength + player.falling_speed