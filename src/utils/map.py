import pygame
from pygame.locals import *
import os

class Map:
    def __init__(self, player: pygame.sprite.Sprite, screen: pygame.Surface):
        self.index = 0
        self.ticks = 0
        self.animation_speed = 35
        self.background_frames = [
            pygame.image.load(f'assets/background/animated/fond_{i}.jpg').convert() for i in range(1, 5)
        ]
        self.background_img = self.background_frames[self.index]
        self.map = pygame.Surface(self.background_img.size)
        self.map_rect = self.map.get_rect()
        self.camera = pygame.Rect(screen.get_rect())
        self.screen = screen
        self.player = player

    def update(self):
        self.ticks += 1
        self.camera.x = self.player.rect.centerx - self.camera.width//2
        if self.camera.x < 0:
            self.camera.x = 0
        if self.camera.right > self.map.get_width():
            self.camera.right = self.map.get_width()
        self.camera.y = self.player.rect.centery - self.camera.height//2
        if self.camera.y < 0:
            self.camera.y = 0
        if self.camera.bottom > self.map.get_height():
            self.camera.bottom = self.map.get_height()
        self.screen.blit(self.map, (0,0), self.camera)

        if self.ticks >= self.animation_speed and self.index < len(self.background_frames) - 1:
            self.index += 1
            self.ticks = 0
            self.background_img = self.background_frames[self.index]
            print(self.index)

        if self.index >= len(self.background_frames) - 1 and self.ticks >= self.animation_speed:
            self.index = 0
            self.ticks = 0
            self.background_img = self.background_frames[self.index]
        

    def draw_bg(self):
        self.map.blit(self.background_img)