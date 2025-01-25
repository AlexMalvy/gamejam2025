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
            Jellyfish( # Bottom right 1
                pos=(1350,5850)
            ),
            Jellyfish( # Bottom right 2
                pos=(1225,6050)
            ),
            Jellyfish( # Cornice left 1
                pos=(400,3750)
            ),
            Jellyfish( # Cornice left 2
                pos=(700,3250)
            ),
            Jellyfish( # Cornice right 1
                pos=(1350,1900)
            ),
            Jellyfish( # Cornice right 2
                pos=(1560,1700)
            ),
        )

        # Init Sharks
        self.shark_group.add(
            Shark( # Real Sharck
                color=Colors.RED, 
                x=400, 
                y=3550,
                width=1400,
                height=700
            ),
            Shark( # Nougat <3
                color=Colors.RED, 
                x=1400, 
                y=4700,
                width=150,
                height=100
            ),
        )

        # Init bubbles
        self.bubble_group.add(
            Bubble( # Bubles bottom right
                color=Colors.GREEN, 
                x=1600, 
                y=5600, 
                width=200, 
                height=830
            ),
            Bubble( # Bubles cornice bottom left
                color=Colors.GREEN, 
                x=65, 
                y=3850,
                width=210, 
                height=685
            ),
            Bubble( # Bubles cornice top right
                color=Colors.GREEN, 
                x=1670, 
                y=800,
                width=200, 
                height=700
            ),
        )

        # Init Placeholder
        self.obstacle_group.add(
            Placeholder( # Cornice bottom left
                color=Colors.YELLOW,                 
                x=0, 
                y=4535, 
                width=525, 
                height=25
            ),
            Placeholder( # Cornice top right
                color=Colors.YELLOW,                 
                x=1360, 
                y=1500, 
                width=1920-1360, 
                height=50
            ),
            Placeholder( # TODO: à refaire : Premier banc de poisson, poisson 1
                color=Colors.YELLOW,                 
                x=750, 
                y=5200, 
                width=100, 
                height=50
            ),
            Placeholder( # TODO: à refaire : Premier banc de poisson, poisson 2
                color=Colors.YELLOW,                 
                x=410, 
                y=4875, 
                width=100, 
                height=50
            ),
            Placeholder( # TODO: à refaire : Second banc de poisson, poisson 
                color=Colors.YELLOW,                 
                x=1050, 
                y=2750, 
                width=100, 
                height=50
            ),
            Placeholder( # TODO: à refaire : Second banc de poisson, poisson 2
                color=Colors.YELLOW,                 
                x=1375, 
                y=2450, 
                width=100, 
                height=50
            ),
            Placeholder( # TODO: à refaire : Troisième banc de poisson, poisson 1
                color=Colors.YELLOW,                 
                x=920, 
                y=950, 
                width=100, 
                height=50
            ),
            Placeholder( # TODO: à refaire : Troisième banc de poisson, poisson 2
                color=Colors.YELLOW,                 
                x=470, 
                y=690, 
                width=100, 
                height=50
            ),
        )


    def update(self):
        for group in self.all_groups:
            group.draw(self.map.map)

            # Debug
            for sprite in group:
                pygame.draw.rect(self.map.map, Colors.WHITE, sprite.rect, 2)
            
            group.update()