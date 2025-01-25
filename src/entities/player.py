import pygame
from pygame.locals import *
from src.entities.character import Character


class Player(Character):
    # Movements
    velocity = 0
    falling_speed = 1
    max_falling_speed = 15
    jump_strength = 30
    speed = 15

    # Stun
    stunned = False
    stunned_max_timer = 400
    stunned_timer: int = 0

    def __init__(self, scale=1, animation_speed=10, pos=(0,0), *sheets_path):
        super().__init__(scale, animation_speed, pos, *sheets_path)


    def update(self):
        super().update()

        # Stun fading
        if self.stunned:
            if self.stunned_timer + self.stunned_max_timer < pygame.time.get_ticks():
                self.stunned = False
    

    def get_stunned(self):
        self.stunned = True
        self.stunned_timer = pygame.time.get_ticks()