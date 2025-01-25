import pygame
from pygame.locals import *
from utils.character import Character


class Player(Character):
    velocity = 0
    falling_speed = 3
    max_falling_speed = 30
    jump_strength = 30
    speed = 20

    def __init__(self, scale=1, animation_speed=10, pos=(0,0), *sheets_path):
        super().__init__(scale, animation_speed, pos, *sheets_path)