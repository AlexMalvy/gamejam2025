import pygame
from pygame.locals import *
from src.entities.character import Character

class ClownFish(Character):
    # Sprite sheet path
    base_path = ["clown_fish"]
    base_scale = 1

    speed = 1
    max_range = 30

    def __init__(self, pos=(0,0), sheets_path = base_path, scale=base_scale, animation_speed=10):
        super().__init__(sheets_path, pos, scale, animation_speed)
        self.rect.center = pos
        self.middle_x = pos[0]
        self.animation_speed = 10

    def update(self):
        super().update()

        # Going right
        if self.index >= self.max_index_list[self.state] // 2 and self.rect.centerx - self.middle_x < self.max_range:
            self.rect.x += self.speed
        # Going left
        elif self.rect.centerx - self.middle_x > -self.max_range:
            self.rect.x -= self.speed
