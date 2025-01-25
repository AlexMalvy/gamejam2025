import pygame
from pygame.locals import *

class Collision:
    def mask_collide_mask(sprite1: pygame.sprite.Sprite, sprite2: pygame.sprite.Sprite, direction: str):
        match direction:
            case "left":
                return sprite2.rect.right - sprite1.mask_diff["left"] + sprite2.mask_diff["right"] + 1
            case "top":
                return sprite2.rect.bottom - sprite1.mask_diff["top"] + sprite2.mask_diff["bottom"] + 1
            case "right":
                return sprite2.rect.left + sprite1.mask_diff["right"] + sprite2.mask_diff["left"] - 1
            case "bottom":
                return sprite2.rect.top + sprite1.mask_diff["bottom"] + sprite2.mask_diff["top"] - 1
    
    def mask_collidepoint(sprite1: pygame.sprite.Sprite, pos: tuple[int, int], direction: str):
        match direction:
            case "left":
                return pos[0] - sprite1.mask_diff["left"] + 1
            case "top":
                return pos[1] - sprite1.mask_diff["top"] + 1
            case "right":
                return pos[0] + sprite1.mask_diff["right"] - 1
            case "bottom":
                return pos[1] + sprite1.mask_diff["bottom"] - 1