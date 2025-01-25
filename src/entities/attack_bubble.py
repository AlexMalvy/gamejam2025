import pygame
from pygame.locals import *
from src.entities.placeholder import Placeholder
from src.utils.map import Map
from src.utils.color import Colors


class AttackBubble(Placeholder):
    speed = 10
    max_timer = 500

    def __init__(self, map: Map, x, y, direction: str = "right", color = Colors.GREEN, width = 50, height = 50):
        super().__init__(color, x, y, width, height)
        self.map = map
        self.direction = direction
        self.timer: int = pygame.time.get_ticks()

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