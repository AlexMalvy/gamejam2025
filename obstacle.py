import pygame
from pygame.locals import *
from src.entities.placeholder import Placeholder
from src.entities.bubble import Bubble
from src.entities.jellyfish import Jellyfish
from src.entities.shark import Shark
from src.utils.map import Map
from src.utils.color import Colors

class Obstacle():
    obstacle_group = pygame.sprite.Group()
    bubble_group = pygame.sprite.Group()
    jellyfish_group = pygame.sprite.Group()
    shark_group = pygame.sprite.Group()
    all_groups = [obstacle_group, bubble_group, jellyfish_group, shark_group]

    def __init__(self, map: Map):
        self.map = map

        # Init Floor
        self.obstacle_group.add(Placeholder(Colors.BLACK, 0, self.map.map_rect.bottom - 50, map.map_rect.width, 100))

        # Init bubbles
        self.bubble_group.add(Bubble(Colors.YELLOW, 300, map.map_rect.height - 650, 100, 500))

        # Init Jellyfishes
        jellyfish_list = []
        jellyfish_list.append(Jellyfish(Colors.BROWN, 600, self.map.map_rect.bottom - 500))
        jellyfish_list.append(Jellyfish(Colors.BROWN, 900, self.map.map_rect.bottom - 700))
        jellyfish_list.append(Jellyfish(Colors.BROWN, 1200, self.map.map_rect.bottom - 900))
        self.jellyfish_group.add(jellyfish_list)

        # Init Sharks
        shark_list = []
        shark_list.append(Shark(Colors.RED, self.map.map_rect.width - 400, self.map.map_rect.bottom - 1300))
        self.shark_group.add(shark_list)

        # Init Placeholder
        placeholders = []
        placeholders.append(Placeholder(Colors.YELLOW, 50, self.map.map_rect.bottom - 100, 50, 50))
        placeholders.append(Placeholder(Colors.YELLOW, self.map.map_rect.width - 100, self.map.map_rect.bottom - 100, 50, 50))
        self.obstacle_group.add(placeholders)


    def update(self):
        for group in self.all_groups:
            group.draw(self.map.map)
            group.update()