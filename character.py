import pygame
from pygame.locals import *
import os

class Character(pygame.sprite.Sprite):
    def __init__(self, scale = 1, animation_speed = 10, pos = (0,0), *sheets_path):
        pygame.sprite.Sprite.__init__(self)
        self.images_list = []
        self.masks_list = []
        for sheet_path in sheets_path:
            # Load entire sprite sheet
            path = sheet_path.split("/")
            sheet = pygame.image.load(os.path.join(*path)).convert_alpha()
            sheet = pygame.transform.scale(sheet, (sheet.get_width() * scale, sheet.get_height() * scale))

            height = sheet.get_height()
            # Extract each individual image
            temp_images_list = []
            temp_masks_list = []
            for i in range(sheet.get_width()// height):
                # Images
                temp_image = pygame.Surface((height, height))
                temp_image.fill((1, 1, 1))
                temp_image.blit(sheet, (0,0), (i * height, 0, height, height))
                temp_image.set_colorkey((1, 1, 1))
                temp_images_list.append(temp_image)
                # Mask
                temp_mask = pygame.mask.from_surface(temp_image)
                temp_masks_list.append(temp_mask)

            self.images_list.append(temp_images_list)
            self.masks_list.append(temp_masks_list)

        # ///////////
        self.state = 0
        self.max_state = len(self.images_list)
        self.max_index_list = []
        for images in self.images_list:
            
        self.index = 0
        self.max_index = len(self.images) - 1
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.mask = self.masks[self.index]
        self.counter = 0
        self.animation_speed = animation_speed

    def update(self):
        self.counter += 1

        if self.counter >= self.animation_speed and self.index < self.max_index:
            self.counter = 0
            self.index += 1
            self.image = self.images[self.index]
            self.mask = self.masks[self.index]

        if self.index >= self.max_index and self.counter >= self.animation_speed:
            self.index = 0