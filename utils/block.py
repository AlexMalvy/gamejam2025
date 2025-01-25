import pygame
from pygame.locals import *

class Block(pygame.sprite.Sprite):

    # Constructor. Pass in the color of the block,
    # and its x and y position
    def __init__(self, color, x, y, width, height):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self)

        # Create an image of the block, and fill it with a color.
        # This could also be an image loaded from the disk.
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
 
        # Fetch the rectangle object that has the dimensions of the image
        # Update the position of this object by setting the values of rect.x and rect.y
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
 
        self.mask = pygame.mask.from_surface(self.image)
       
        # Mask Diff
        self.mask_diff = {"left": 0, "top": 0, "right": 0, "bottom": 0}
        outline = self.mask.outline()
        # Define all length between the image rect border and the mask outline
        self.mask_diff["left"] = min(outline, key=lambda x: x[0])[0]
        self.mask_diff["top"] = min(outline, key=lambda x: x[1])[1]
        self.mask_diff["right"] = self.rect.width - max(outline, key=lambda x: x[0])[0]
        self.mask_diff["bottom"] = self.rect.height - max(outline, key=lambda x: x[1])[1]
