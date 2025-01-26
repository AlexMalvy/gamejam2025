import pygame
from pygame.locals import *
from src.entities.fish import Fish
from src.entities.rock import Rock
from src.entities.seaweed import Seaweed
from src.utils.map import Map
from src.utils.color import Colors
import random

class BackgroundEntities():
    fish_cooldown = 500
    fish_timer = 0
    fish_max = 25

    def __init__(
            self, 
            map: Map
        ) -> None:
        self.map: Map = map
        self.fish_school = pygame.sprite.Group()
        self.foreground_group = pygame.sprite.Group()
        
        self.all_groups = [
            self.fish_school
        ]

        # Init Rock
        self.foreground_group.add(Rock(pos=(self.map.map_rect.left, self.map.map_rect.bottom)))
        
        # Init Seaweed
        self.foreground_group.add(Seaweed(pos=(self.map.map_rect.right - 300, self.map.map_rect.bottom)))

        # Init Jellyfishes

        # self.fish_school.add(
        #     Fish( # Premier banc de poisson, poisson 1
        #         map=self.map,
        #         pos=(750,5200)
        #     ),
            # Placeholder( # TODO: à refaire : Premier banc de poisson, poisson 2
            #     color=Colors.YELLOW,                 
            #     x=410, 
            #     y=4875, 
            #     width=100, 
            #     height=50
            # ),
            # Placeholder( # TODO: à refaire : Second banc de poisson, poisson 
            #     color=Colors.YELLOW,                 
            #     x=1050, 
            #     y=2750, 
            #     width=100, 
            #     height=50
            # ),
            # Placeholder( # TODO: à refaire : Second banc de poisson, poisson 2
            #     color=Colors.YELLOW,                 
            #     x=1375, 
            #     y=2450, 
            #     width=100, 
            #     height=50
            # ),
            # Placeholder( # TODO: à refaire : Troisième banc de poisson, poisson 1
            #     color=Colors.YELLOW,                 
            #     x=920, 
            #     y=950, 
            #     width=100, 
            #     height=50
            # ),
            # Placeholder( # TODO: à refaire : Troisième banc de poisson, poisson 2
            #     color=Colors.YELLOW,                 
            #     x=470, 
            #     y=690, 
            #     width=100, 
            #     height=50
            # ),
        # )

    def spawn_fish(self, y, facing_right = True):
        scale = random.randint(15,30) / 100
        if facing_right:
            self.fish_school.add(Fish(map = self.map, pos = (self.map.map_rect.left - 1000, y + random.randint(0, 500)), speed = random.randint(2,4), scale=scale))
        else:
            self.fish_school.add(Fish(map = self.map, pos = (self.map.map_rect.right, y + random.randint(0, 500)), facing_right = False, speed = random.randint(2,4), scale=scale))


    def update(self):
        if len(self.fish_school) < self.fish_max and self.fish_cooldown + self.fish_timer < pygame.time.get_ticks():
            self.spawn_fish(y = 4800, facing_right = False)
            self.fish_timer = pygame.time.get_ticks()


        for group in self.all_groups:
            group.draw(self.map.map)

            # # Debug
            # for sprite in group:
            #     pygame.draw.rect(self.map.map, Colors.WHITE, sprite.rect, 2)
            
            group.update()

    def update_foreground(self):
        self.foreground_group.draw(self.map.map)

        # Debug
        # for sprite in self.foreground_group:
        #     pygame.draw.rect(self.map.map, Colors.WHITE, sprite.rect, 2)
        
        self.foreground_group.update()
