import pygame
from pygame.locals import *
from src.entities.character import Character


class Boat(Character):
    # Sprite sheet path
    base_path = ["boat_idle", "boat_rising", "boat_active"]
    base_scale = 1

    animation_done_timer = 0
    animation_done_cooldown = 5000
    animation_done = False

    def __init__(self, pos=(0,0), sheets_path = base_path, scale=base_scale, animation_speed=10):
        super().__init__(sheets_path, pos, scale, animation_speed)
        self.animation_speed = 20

    def update(self):
        super().update()
        if self.state == 1:
            if self.index >= self.max_index_list[self.state] and self.ticks >= self.animation_speed - 1:
                self.animation_done_timer = pygame.time.get_ticks()
                self.state = 2

        if self.state == 2:
            if self.animation_done_timer + self.animation_done_cooldown < pygame.time.get_ticks():
                self.animation_done = True

    def start_endgame(self):
        if self.state == 0:
            self.state = 1
            self.ticks = 0
            self.index = 0
            self.image = self.images_list[self.state][self.index]
            self.mask = self.masks_list[self.state][self.index]
            self.mask_diff = self.masks_diff_list[self.state][self.index]

