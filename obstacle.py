import pygame
from pygame.locals import *
from src.entities.placeholder import Placeholder
from src.entities.bubble import Bubble
from src.entities.jellyfish import Jellyfish
from src.entities.shark import Shark
from src.utils.map import Map
from src.utils.color import Colors

class Obstacle():
    def __init__(self, map: Map):
        self.map = map
        self.obstacle_group = pygame.sprite.Group()
        self.bubble_group = pygame.sprite.Group()
        self.jellyfish_group = pygame.sprite.Group()
        self.shark_group = pygame.sprite.Group()
        self.projectiles_group = pygame.sprite.Group()
        
        self.all_groups = [
            self.obstacle_group, 
            self.bubble_group, 
            self.jellyfish_group, 
            self.shark_group, 
            self.projectiles_group
        ]

        # Init Floor
        self.obstacle_group.add(
            Placeholder(
                color=Colors.BLACK, 
                x=0, 
                y=self.map.map_rect.bottom - 50, 
                width=map.map_rect.width, 
                height=100
            )
        )

        # Init Jellyfishes
        self.jellyfish_group.add(
            Jellyfish(
                color=Colors.BROWN, 
                x=500, 
                y=self.map.map_rect.bottom - 1200
            ),
            Jellyfish(
                color=Colors.BROWN, 
                x=1000, 
                y=self.map.map_rect.bottom - 1500
            )
        )

        # Init Sharks
        self.shark_group.add(
            Shark(
                color=Colors.RED, 
                x=400, 
                y=self.map.map_rect.bottom - 800
            ),
            Shark(
                color=Colors.RED, 
                x=600, 
                y=self.map.map_rect.bottom - 1500
            ),
            Shark(
                color=Colors.RED, 
                x=500, 
                y=self.map.map_rect.height - 2500, 
            )
        )

        # Init bubbles
        self.bubble_group.add(
            Bubble(
                color=Colors.GREEN, 
                x=self.map.map_rect.width - 500, 
                y=self.map.map_rect.height - 1200, 
                width=100, 
                height=500
            ),
            Bubble(
                color=Colors.GREEN, 
                x=0, 
                y=self.map.map_rect.height - 1700, 
                width=100, 
                height=500
            ),
            Bubble(
                color=Colors.GREEN, 
                x=0, 
                y=self.map.map_rect.height - 2000, 
                width=100, 
                height=500
            )
        )

        # Init Placeholder
        self.obstacle_group.add(
            Placeholder(
                color=Colors.YELLOW, 
                x=0, 
                y=self.map.map_rect.bottom - 150, 
                width=100, 
                height=100
            ),
            Placeholder(
                color=Colors.YELLOW, 
                x=300, 
                y=self.map.map_rect.bottom - 500, 
                width=1000, 
                height=100
            ),
            Placeholder(
                color=Colors.YELLOW,                 
                x=self.map.map_rect.width - 400, 
                y=self.map.map_rect.bottom - 1200, 
                width=100, 
                height=100
            ),
            Placeholder(
                color=Colors.YELLOW,                 
                x=200, 
                y=self.map.map_rect.height - 2000, 
                width=100, 
                height=100
            )
        )


    def update(self):
        for group in self.all_groups:
            group.draw(self.map.map)
            group.update()