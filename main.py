import pygame
import time
import random
from utils.color import Colors
from utils.game_over import GameOver
from character import Character
from utils.generaluse import GeneralUse
from utils.map import Map
from utils.window import HEIGHT, WIDTH
from pygame.font import SysFont
from game_menu import GameMenu
from pygame.locals import *
from utils.block import Block
from utils.collision import Collision


WIDTH, HEIGHT = 1600, 800

pygame.init()
pygame.display.set_caption("The rise of the Axolotl")
screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
# screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
# WIDTH, HEIGHT = screen.get_width(), screen.get_height()
clock = pygame.time.Clock()
font40 = SysFont(name="serif", size=40)
font50 = SysFont(name="serif", size=50)

class MainGame:
    def __init__(self):
        self.player = Character(3, 10, (WIDTH//2, 12500), "assets/player/player_idle.png")
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)
        self.velocity = 0
        self.falling_speed = 3
        self.speed = 25
        self.start_time = time.time()
        self.game_length = 15

        self.general_use = GeneralUse(screen)
        self.game_over = GameOver(
            self.general_use,
            clock,
            # self.get_score_text,
            screen,
        )
        self.game_menu = GameMenu(screen, font50)

        self.map = Map(self.player, screen)

        self.obstacle_group = pygame.sprite.Group()
        self.floor = Block(Colors.BLACK, 0, self.map.map.height - 50, WIDTH, 100)
        obstacles = []
        obstacles.append(Block(Colors.YELLOW, 50, self.floor.rect.top - 50, 50, 50))
        obstacles.append(Block(Colors.YELLOW, WIDTH - 100, self.floor.rect.top - 50, 50, 50))
        self.obstacle_group.add(self.floor, obstacles)
    

    def draw_window(self):
        self.map.draw_bg()
        
        pygame.draw.rect(self.map.map, Colors.BLACK, self.floor)

        self.obstacle_group.draw(self.map.map)
        self.obstacle_group.update()

        self.player_group.draw(self.map.map)
        self.player_group.update()

        # # Debug player rect
        # pygame.draw.rect(self.map.map, Colors.WHITE, self.player.rect, 2)

        self.map.update()

        pygame.display.update()

    def game_loop(self):
        run = True
        left = False
        right = False
        up = False
        grounded = False
        while run:
            clock.tick(60)

            # Movements
            # Left
            if left and self.player.rect.left + self.player.mask_diff["left"] > 0:
                self.player.rect.left -= self.speed
                if self.player.rect.left + self.player.mask_diff["left"] < 0:
                    self.player.rect.left = Collision.mask_collidepoint(self.player, (0,0), "left")
                # Flip player sprite
                if self.player.facing_right:
                    self.player.flip_facing = True
                    
                # Check for collision
                mask_collide = False
                rect_collide = pygame.sprite.spritecollide(self.player, self.obstacle_group, False)
                if rect_collide:
                    mask_collide = pygame.sprite.spritecollide(self.player, self.obstacle_group, False, pygame.sprite.collide_mask)
                    if mask_collide:
                        self.player.rect.left = Collision.mask_collide_mask(self.player, mask_collide[0], "left")
            
            # Right
            if right and self.player.rect.right - self.player.mask_diff["right"] < WIDTH:
                self.player.rect.right += self.speed
                if self.player.rect.right - self.player.mask_diff["right"] > WIDTH:
                    self.player.rect.right = Collision.mask_collidepoint(self.player, (WIDTH,0), "right")
                # Flip player sprite
                if not self.player.facing_right:
                    self.player.flip_facing = True
                    
                # Check for collision
                mask_collide = False
                rect_collide = pygame.sprite.spritecollide(self.player, self.obstacle_group, False)
                if rect_collide:
                    mask_collide = pygame.sprite.spritecollide(self.player, self.obstacle_group, False, pygame.sprite.collide_mask)
                    if mask_collide:
                        self.player.rect.right = Collision.mask_collide_mask(self.player, mask_collide[0], "right")

            # Jump
            if up and grounded:
                self.velocity = -30
                grounded = False
            
            # Apply Gravity
            if self.velocity < 30:
                self.velocity += self.falling_speed
            self.player.rect.y += self.velocity
            # Check for collision
            mask_collide = False
            rect_collide = pygame.sprite.spritecollide(self.player, self.obstacle_group, False)
            if rect_collide:
                mask_collide = pygame.sprite.spritecollide(self.player, self.obstacle_group, False, pygame.sprite.collide_mask)
                if mask_collide:
                    self.player.rect.bottom = Collision.mask_collide_mask(self.player, mask_collide[0], "bottom")
                    self.velocity = 0
                    grounded = True


            up = False
            # Event Handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.general_use.close_the_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        self.general_use.close_the_game()
                    if event.key == pygame.K_q:
                        left = True
                    if event.key == pygame.K_d:
                        right = True
                    if event.key == K_z:
                        up = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        left = False
                    if event.key == pygame.K_d:
                        right = False
            self.draw_window()

    def run(self):
        # self.game_menu.menu_loop()
        self.game_loop()

main = MainGame()
main.run() 