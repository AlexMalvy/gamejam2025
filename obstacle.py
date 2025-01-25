import pygame
from pygame.locals import *
from regex import F
from src.entities.placeholder import Placeholder
from src.entities.bubble import Bubble
from src.entities.jellyfish import Jellyfish
from src.entities.shark import Shark
from src.utils.map import Map
from src.utils.color import Colors

class Obstacle():
    def __init__(
            self, 
            map: Map
        ) -> None:
        self.map: Map = map
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
                x=self.map.map_rect.width - 500, 
                y=self.map.map_rect.height - 1050, 
            ),
            Jellyfish(
                color=Colors.BROWN, 
                x=self.map.map_rect.width - 1000, 
                y=self.map.map_rect.height - 1250, 
            ),
            Jellyfish(
                color=Colors.BROWN, 
                x=self.map.map_rect.width - 750, 
                y=self.map.map_rect.height - 1750, 
            ),
        )

        # Init Sharks
        self.shark_group.add(
            Shark(
                color=Colors.RED, 
                x=self.map.map_rect.width - 200, 
                y=self.map.map_rect.bottom - 3500,
                width=1000,
                height=300
            ),
        )

        # Init bubbles
        self.bubble_group.add(
            Bubble( # Bubles bottom right
                color=Colors.GREEN, 
                x=self.map.map_rect.width - 300, 
                y=self.map.map_rect.height - 1050, 
                width=200, 
                height=1000
            ),
            Bubble( # Bubles cornice left
                color=Colors.GREEN, 
                x=0, 
                y=self.map.map_rect.bottom - 3500,
                width=100, 
                height=750
            ),
        )

        # Init Placeholder
        self.obstacle_group.add(
            Placeholder( # Cornice bottom left
                color=Colors.YELLOW,                 
                x=0, 
                y=self.map.map_rect.height - 2750, 
                width=200, 
                height=25
            ),
            Placeholder( # TODO: à refaire : Premier banc de poisson, poisson 1
                color=Colors.YELLOW,                 
                x=self.map.map_rect.width - 300, 
                y=self.map.map_rect.height - 2000, 
                width=50, 
                height=25
            ),
            Placeholder( # TODO: à refaire : Premier banc de poisson, poisson 2
                color=Colors.YELLOW,                 
                x=self.map.map_rect.width - 900, 
                y=self.map.map_rect.height - 2300, 
                width=50, 
                height=25
            ),
            Placeholder( # TODO: à refaire : Premier banc de poisson, poisson 3
                color=Colors.YELLOW,                 
                x=300, 
                y=self.map.map_rect.height - 2350, 
                width=50, 
                height=25
            ),
        )


    def update(self):
        for group in self.all_groups:
            group.draw(self.map.map)
            group.update()