import pygame
from pygame.locals import *
from src.entities.character import Character
from src.utils.map import Map
from src.utils.sounds import SoundManager


class YellowFish(Character):
    # Sprite sheet path
    base_path = ["yellow_fish", "yellow_fish_bubble_idle", "yellow_fish_bubble"]
    base_scale = 0.4


    stunned = False
    stunned_max_timer = 3000
    stunned_timer: int = 0

    accelerated_animation_speed = 3

    def __init__(self, pos=(0,0), sheets_path = base_path, scale=base_scale, animation_speed=10):
        super().__init__(sheets_path, pos, scale, animation_speed)
        self.sound_manager = SoundManager()
        self.base_animation_speed = self.animation_speed

    def update(self):
        super().update()

        # Stun fading
        if self.stunned:
            if self.stunned_timer + self.stunned_max_timer < pygame.time.get_ticks():
                self.stunned = False
                self.state = 2

        if self.state == 2:
            if self.animation_speed != self.accelerated_animation_speed:
                self.animation_speed = self.accelerated_animation_speed
            if self.index == 5 and not pygame.mixer.get_busy():
                self.sound_manager.play_random("special")
            if self.index >= self.max_index_list[self.state] and self.ticks >= self.animation_speed - 2:
                self.state = 0
        elif self.animation_speed == self.accelerated_animation_speed:
            self.animation_speed = self.base_animation_speed

    def get_stunned(self):
        self.stunned = True
        self.stunned_timer = pygame.time.get_ticks()
        self.state = 1

    def bounce(self, player):
        if self.stunned:
            player.velocity = -player.jump_strength
