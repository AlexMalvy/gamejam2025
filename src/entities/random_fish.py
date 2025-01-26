from pygame.locals import *
from src.entities.character import Character
from src.utils.map import Map
import math


class RandomFish(Character):
    def __init__(
            self, 
            map: Map, 
            pos: tuple[int, int]=(0,0), 
            scale: float=1.0, 
            animation_speed: int=10, 
            isWhite: bool = False
        ) -> None:
        super().__init__(
            ["random_fishs/white"] if isWhite else ["random_fishs/transparent"], 
            pos, 
            scale, 
            animation_speed
        )
        self.speed = 3
        self.map = map
        self.animation_speed = 20
        self.base_y = self.rect.centery

    def update(self):
        super().update()

        self.image.set_alpha(100)

        if not self.rect.colliderect(self.map.map_rect):
            self.turn_around()

        # Move
        self.rect.x += self.speed

        self.rect.y = self.base_y + 50 * math.sin(self.rect.x / 50)

    def turn_around(self):
        self.speed = -self.speed
        self.facing_right = not self.facing_right