import pygame
from pygame.locals import *
from src.entities.character import Character
from src.utils.map import Map
from src.utils.color import Colors


class AttackBubble(Character):
    speed = 10
    max_timer = 2500

    # Sprite sheet path
    base_path = ["attack_bubble"]
    base_scale = 0.5

    def __init__(self, map: map, pos=(0,0), direction = "right", sheets_path = base_path, scale=base_scale, animation_speed=10):
        super().__init__(sheets_path, pos, scale, animation_speed)
        self.map = map
        self.direction = direction
        self.timer: int = pygame.time.get_ticks()
        self.rect.center = pos
        # self.rect.bottomleft = pos

    def update(self):
        match self.direction:
            case "left":
                self.rect.x -= self.speed
            case "right":
                self.rect.x += self.speed
            case "up":
                self.rect.y -= self.speed

        if not self.rect.colliderect(self.map.map_rect) or self.timer + self.max_timer < pygame.time.get_ticks():
            self.kill()