import pygame
from pygame.locals import *
from src.entities.placeholder import Placeholder
from src.entities.coral import Coral
from src.entities.jellyfish import Jellyfish
from src.entities.shark import Shark
from src.entities.yellow_fish import YellowFish
from src.entities.shark import Shark
from src.utils.map import Map
from src.utils.color import Colors
from src.entities.boat import Boat  

class Obstacle():
    def __init__(
            self, 
            map: Map
        ) -> None:
        self.map: Map = map
        self.obstacle_group = pygame.sprite.Group()
        self.coral_group = pygame.sprite.Group()
        self.jellyfish_group = pygame.sprite.Group()
        self.shark_group = pygame.sprite.Group()
        self.yellow_fish_group = pygame.sprite.Group()
        self.projectiles_group = pygame.sprite.Group()
        self.boat_group = pygame.sprite.Group()

        self.all_groups = [
            # self.obstacle_group,
            self.coral_group,
            self.jellyfish_group,
            self.shark_group,
            self.boat_group,
            self.yellow_fish_group,
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
                pos=(1350,6050)
            ),
            Jellyfish( # Bottom right 2
                pos=(1125,6250)
            ),
            Jellyfish( # Cornice left 1
                pos=(400,4050)
            ),
            Jellyfish( # Cornice left 2
                pos=(700,3250)
            ),
            Jellyfish( # Cornice right 1
                pos=(1150,2200)
            ),
            Jellyfish( # Cornice right 2
                pos=(1560,1700)
            ),
        )

        # Init Sharks
        self.shark_group.add(
            Shark( # Real Sharck
                pos=(400,3550)
            ),
            # Shark( # Nougat <3
            #     color=Colors.RED,
            #     x=1400, 
            #     y=4700,
            #     width=150,
            #     height=100
            # ),
        )

        # Init corals
        self.coral_group.add(
            Coral( # Bubles bottom right
                pos=(1650,6050)
            ),
            Coral( # Bubles cornice bottom left
                pos=(200,4200)
            ),
            Coral( # Bubles cornice top right
                pos=(1670,1200)
            ),
        )
            
        # Init yellow fish
        self.yellow_fish_group.add(
            YellowFish( # Premier banc de poisson, poisson 1
                pos=(750,5200),
                facing_right=False
            ),
            YellowFish( # Premier banc de poisson, poisson 2
                pos=(410,4875),
                facing_right=False
            ),
            YellowFish( # Second banc de poisson, poisson 
                pos=(1050,2750),
            ),
            YellowFish( # Second banc de poisson, poisson 2
                pos=(1375,2450),
            ),
            YellowFish( # Troisième banc de poisson, poisson 1
                pos=(920,950),
            ),
            YellowFish( # Troisième banc de poisson, poisson 2
                pos=(470,690),
            ),
        )

        # Init Boat
        self.boat_group.add(
            Boat(
                pos=(800,250)
            )
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
        )


    def update(self):
        for group in self.all_groups:
            group.draw(self.map.map)

            # # Debug
            # for sprite in group:
            #     pygame.draw.rect(self.map.map, Colors.WHITE, sprite.rect, 2)
            
            group.update()
    
    def reset_boat(self):
        self.boat_group.empty()
        self.boat_group.add(
            Boat(
                pos=(800,250)
            )
        )      