from typing import Final
import pygame
from pygame.locals import *
from src.entities.fish import Fish
from src.entities.rock import Rock
from src.entities.seaweed import Seaweed
from src.entities.clown_fish import ClownFish
from src.entities.doris import Doris
from src.entities.cat import Cat
from src.utils.map import Map
from src.utils.color import Colors
import random

class BackgroundEntities():
    FISH_COOLDOWN: Final[int] = 500
    fish_timer_1 = 0
    fish_timer_2 = 0
    fish_timer_3 = 0
    fish_max = 25

    def __init__(
            self, 
            map: Map
        ) -> None:
        self.map: Map = map
        self.cat_group = pygame.sprite.Group()
        self.fish_school_1 = pygame.sprite.Group()
        self.fish_school_2 = pygame.sprite.Group()
        self.fish_school_3 = pygame.sprite.Group()
        self.clown_fish_group = pygame.sprite.Group()
        self.foreground_group = pygame.sprite.Group()
        
        self.background_group = [
            self.cat_group,
            self.fish_school_1,
            self.fish_school_2,
            self.fish_school_3,
            self.clown_fish_group
        ]

        # Init Rock
        self.foreground_group.add(Rock(pos=(self.map.map_rect.left, self.map.map_rect.bottom)))
        
        # Init Seaweed
        self.foreground_group.add(Seaweed(pos=(self.map.map_rect.right - 300, self.map.map_rect.bottom)))

        # Init Cat
        self.cat_group.add(Cat(map=self.map, pos=(1400, 4000)))

    def spawn_fish(
            self, 
            y: int, 
            group_id: int, 
            facing_right: bool = True
        ) -> None:
        new_fish: Fish = Fish(
            map=self.map, 
            pos=(
                self.map.map_rect.left if facing_right else self.map.map_rect.right, 
                y + random.randint(a=0, b=500)
            ), 
            facing_right=facing_right, 
            speed=random.randint(a=2,b=4), 
            scale=random.randint(15,30) / 100
        )
        match group_id:
            case 1:
                self.fish_school_1.add(new_fish)
            case 2:
                self.fish_school_2.add(new_fish)
            case 3:
                self.fish_school_3.add(new_fish)
            case _:
                pass

    def spawn_clown_fish(self, corals: pygame.sprite.Group):
        clown_fish_list = []
        for coral in corals:
            clown_fish_list.append(ClownFish(pos = (coral.rect.centerx, coral.rect.bottom - 50)))
        # self.clown_fish_group.add(clown_fish_list)
        self.foreground_group.add(clown_fish_list)

    def spawn_doris(self, corals: pygame.sprite.Group):
        doris_list = []
        for coral in corals:
            doris_list.append(Doris(pos = (coral.rect.centerx, coral.rect.bottom - 100)))
        self.foreground_group.add(doris_list)


    def update(self):
        if len(self.fish_school_1) < self.fish_max and self.FISH_COOLDOWN + self.fish_timer_1 < pygame.time.get_ticks():
            self.spawn_fish(y = 4800, group_id=1, facing_right = False)
            self.fish_timer_1 = pygame.time.get_ticks()
        if len(self.fish_school_2) < self.fish_max and self.FISH_COOLDOWN + self.fish_timer_2 < pygame.time.get_ticks():
            self.spawn_fish(y = 2200, group_id=2, facing_right = True)
            self.fish_timer_2 = pygame.time.get_ticks()
        if len(self.fish_school_2) < self.fish_max and self.FISH_COOLDOWN + self.fish_timer_3 < pygame.time.get_ticks():
            self.spawn_fish(y = 500, group_id=3, facing_right = False)
            self.fish_timer_3 = pygame.time.get_ticks()


        for group in self.background_group:
            group.draw(self.map.map)

            # Debug
            for sprite in group:
                pygame.draw.rect(self.map.map, Colors.WHITE, sprite.rect, 2)
            
            group.update()

    def update_foreground(self):
        self.foreground_group.draw(self.map.map)

        # Debug
        # for sprite in self.foreground_group:
        #     pygame.draw.rect(self.map.map, Colors.WHITE, sprite.rect, 2)
        
        self.foreground_group.update()
