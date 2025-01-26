import pygame
from pygame.locals import *
from src.entities.character import Character
from src.utils.collision import Collision


class Boat(Character):

    ascend_speed = 2
    total_ascent = 0
    max_ascent = 400

    # Sprite sheet path
    base_path = ["boat_idle","boat_active"]
    base_scale = 1
    

    # State
    state = 0
    state_timer = 0
    state_duration = 100

    def __init__(self, pos=(0,0), sheets_path = base_path, scale=base_scale, animation_speed=10):
        super().__init__(sheets_path, pos, scale, animation_speed)

    def __init__(self, pos=(0,0), sheets_path = base_path, scale=base_scale, animation_speed=10):
        super().__init__(sheets_path, pos, scale, animation_speed)

    def update(self):
        super().update()
        if self.state_timer + self.state_duration < pygame.time.get_ticks() and self.total_ascent > 0:
            self.rect.y += self.ascend_speed
            self.total_ascent -= self.ascend_speed
            if self.state == 1:
                self.state = 0

    def ascend(self, player):
        player.velocity = 0
        if self.total_ascent < self.max_ascent:
            # player.rect.y -= self.ascend_speed
            self.rect.y -= self.ascend_speed
            self.total_ascent += self.ascend_speed
            self.state_timer = pygame.time.get_ticks()
            self.state = 1

            player.rect.bottom = Collision.mask_collide_mask(player, self, "bottom") + 5

    def ascend_rect(self, player):
        if self.total_ascent < self.max_ascent:
            player.velocity = 0
            # player.rect.y -= self.ascend_speed
            self.rect.y -= self.ascend_speed
            self.total_ascent += self.ascend_speed
            self.state_timer = pygame.time.get_ticks()
            self.state = 1

            player.rect.bottom = self.rect.top
