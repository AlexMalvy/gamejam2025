import pygame
from pygame.locals import *
from utils.placeholder import Placeholder
from utils.bubble import Bubble
from utils.map import Map
from utils.color import Colors

class Obstacle():
    obstacle_group = pygame.sprite.Group()
    bubble_group = pygame.sprite.Group()
    jellyfish_group = pygame.sprite.Group()
    all_groups = [obstacle_group, bubble_group, jellyfish_group]

    def __init__(self, map: Map):
        self.map = map

        # Init Floor
        self.obstacle_group.add(Placeholder(Colors.BLACK, 0, self.map.map_rect.bottom - 50, map.map_rect.width, 100))

        # Init bubbles
        self.bubble_group.add(Bubble(Colors.YELLOW, 300, map.map_rect.height - 650, 100, 500))

        # Init Placeholder
        placeholders = []
        placeholders.append(Placeholder(Colors.YELLOW, 50, self.map.map_rect.bottom - 100, 50, 50))
        placeholders.append(Placeholder(Colors.YELLOW, self.map.map_rect.width - 100, self.map.map_rect.bottom - 100, 50, 50))
        self.obstacle_group.add(placeholders)


    def update(self):
        for group in self.all_groups:
            group.draw(self.map.map)
            group.update()