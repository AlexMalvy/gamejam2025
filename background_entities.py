import pygame
from pygame.locals import *
from src.entities.fish import Fish
from src.entities.rock import Rock
from src.entities.seaweed import Seaweed
from src.entities.clown_fish import ClownFish
from src.entities.bubble import Bubble
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
        self.clown_fish_group = pygame.sprite.Group()
        self.foreground_group = pygame.sprite.Group()
        
        self.background_group = [
            self.fish_school,
            self.clown_fish_group
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

        bubble_images = [pygame.image.load(f'assets/sprites/bubble_{i}.png').convert_alpha() for i in range(1, 11)]
        self.bubble_group = pygame.sprite.Group()

        for _ in range(50):
            bubble = Bubble(self.map.map_rect.width, self.map.map_rect.height, bubble_images)

            scale_factor = random.uniform(2.0, 5.0)
            original_image = bubble.image
            bubble.image = pygame.transform.scale(original_image, (int(original_image.get_width() * scale_factor), int(original_image.get_height() * scale_factor)))
            bubble.rect = bubble.image.get_rect(center=bubble.rect.center)
            
            opacity = random.randint(50, 250)
            bubble.image.set_alpha(opacity)
            
            bubble.rect.x = random.randint(0, self.map.map_rect.width)
            bubble.rect.y = random.randint(0, self.map.map_rect.height)
            
            self.bubble_group.add(bubble)
            self.foreground_group.add(bubble) 


    def spawn_fish(self, y, facing_right = True):
        scale = random.randint(15,30) / 100
        if facing_right:
            self.fish_school.add(Fish(map = self.map, pos = (self.map.map_rect.left - 1000, y + random.randint(0, 500)), speed = random.randint(2,4), scale=scale))
        else:
            self.fish_school.add(Fish(map = self.map, pos = (self.map.map_rect.right, y + random.randint(0, 500)), facing_right = False, speed = random.randint(2,4), scale=scale))

    def spawn_clown_fish(self, corals: pygame.sprite.Group):
        clown_fish_list = []
        for coral in corals:
            clown_fish_list.append(ClownFish(pos = (coral.rect.centerx, coral.rect.bottom - 50)))
        self.foreground_group.add(clown_fish_list)


    def update(self):
        if len(self.fish_school) < self.fish_max and self.fish_cooldown + self.fish_timer < pygame.time.get_ticks():
            self.spawn_fish(y = 4800, facing_right = False)
            self.fish_timer = pygame.time.get_ticks()


        for group in self.background_group:
            group.draw(self.map.map)

            # # Debug
            # for sprite in group:
            #     pygame.draw.rect(self.map.map, Colors.WHITE, sprite.rect, 2)
            
            group.update()
        
        # Bubbles
        self.bubble_group.update()
        self.bubble_group.draw(self.map.map)

    def update_foreground(self):
        self.foreground_group.draw(self.map.map)
        self.foreground_group.update()


        # Debug
        # for sprite in self.foreground_group:
        #     pygame.draw.rect(self.map.map, Colors.WHITE, sprite.rect, 2)
        
        self.foreground_group.update()
