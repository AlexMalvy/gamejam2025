import pygame
from pygame.locals import *
from src.entities.character import Character
from src.entities.attack_bubble import AttackBubble

class Player(Character):
    # Movements
    velocity = 0
    falling_speed = 1
    max_falling_speed = 15
    jump_strength = 30
    speed = 15
    grounded = False
    fall_timer = 0
    max_fall_duration = 150

    # Stun
    stunned = False
    stunned_max_timer = 400
    stunned_timer: int = 0

    # Sprite sheet path
    base_path = ["axolotl_idle"]
    base_scale = 0.5

    def __init__(self, pos=(0,0), sheets_path = base_path, scale=base_scale, animation_speed=10):
        super().__init__(sheets_path, pos, scale, animation_speed)


    def update(self):
        super().update()

        if self.grounded and self.fall_timer + self.max_fall_duration < pygame.time.get_ticks():
            self.grounded = False

        # Stun fading
        if self.stunned:
            if self.stunned_timer + self.stunned_max_timer < pygame.time.get_ticks():
                self.stunned = False
    
    def attack_bubble(self, map, up: bool = False):
        if up:
            if self.facing_right:
                return AttackBubble(map, self.rect.right - 50, self.rect.top, "up")
            else:
                return AttackBubble(map, self.rect.left, self.rect.top, "up")
        elif self.facing_right:
            return AttackBubble(map, self.rect.right, self.rect.top + 20, "right")
        else:
            return AttackBubble(map, self.rect.left - 50, self.rect.top + 20, "left")

    def get_stunned(self):
        self.stunned = True
        self.stunned_timer = pygame.time.get_ticks()