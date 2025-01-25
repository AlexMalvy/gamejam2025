import pygame
import random

class BubbleScreenMenu(pygame.sprite.Sprite):
    def __init__(self, screen_width, screen_height, images):
        super().__init__()
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.images = images
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        self.reset()

    def reset(self):
        self.rect.x = random.choice([random.randint(0, self.screen_width // 4), random.randint(self.screen_width * 3 // 4, self.screen_width)])
        self.rect.y = self.screen_height + random.randint(0, self.screen_height) 
        self.speed = random.uniform(1, 3)
        self.is_popped = False
        self.image_index = 0
        self.image = self.images[self.image_index]

    def update(self):
        if self.is_popped:
            self.pop_timer += 20
            if self.pop_timer % 5 == 0 and self.image_index < len(self.images) - 1:
                self.image_index += 1
                self.image = self.images[self.image_index]
            if self.image_index == len(self.images) - 1:
                self.reset()
        else:
            self.rect.y -= self.speed
            if self.rect.y < -self.image.get_height():
                self.reset()
    
    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)

    def pop(self):
        self.is_popped = True
        self.pop_timer = 0