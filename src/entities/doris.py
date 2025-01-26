import pygame
from pygame.locals import *
from src.entities.character import Character

class Doris(Character):
    # Sprite sheet path
    base_path = ["doris"]
    base_scale = 0.25

    speed = 1
    max_range = 30

    loop_counter = 0
    max_loop = 5

    def __init__(self, pos=(0,0), sheets_path = base_path, scale=base_scale, animation_speed=10):
        super().__init__(sheets_path, pos, scale, animation_speed)
        self.rect.center = pos
        self.middle_x = pos[0]
        self.animation_speed = 10

    def update(self):
        super().update()

        if self.index >= self.max_index_list[self.state] and self.ticks >= self.animation_speed - 1:
            self.loop_counter += 1

        if self.loop_counter >= self.max_loop:
            self.facing_right = not self.facing_right
            self.loop_counter = 0
        
        # Going right
        if self.facing_right and self.rect.centerx - self.middle_x < self.max_range:
            self.rect.x += self.speed
        # Going left
        elif self.rect.centerx - self.middle_x > -self.max_range:
            self.rect.x -= self.speed
