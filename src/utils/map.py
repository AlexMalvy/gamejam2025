import pygame
from pygame.locals import *
import os

class Map:
    def __init__(self, player: pygame.sprite.Sprite, screen: pygame.Surface):
        self.background_img = pygame.image.load(os.path.join("assets", "background", "background.jpg")).convert()
        self.map = pygame.Surface(self.background_img.size)
        self.map_rect = self.map.get_rect()
        self.camera = pygame.Rect(screen.get_rect())
        self.screen = screen
        self.player = player

    def update(self):
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

    def draw_bg(self):
        self.map.blit(self.background_img)