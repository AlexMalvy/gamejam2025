import pygame
import time
import random
from utils.color import Colors
from utils.game_over import GameOver
from character import Character
from utils.generaluse import GeneralUse
from utils.camera import Camera
from utils.window import HEIGHT, WIDTH
from pygame.font import SysFont
from game_menu import GameMenu
from pygame.locals import *


WIDTH, HEIGHT = 1600, 1000

pygame.init()
pygame.display.set_caption("The rise of the Axolotl")
screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
background = pygame.image.load("assets/background/gamejam-2025-axolotl-fond-provisoire-1920x12959.jpg")
map = pygame.surface.Surface((background.get_width(), background.get_height()))
clock = pygame.time.Clock()
font40 = SysFont(name="serif", size=40)
font50 = SysFont(name="serif", size=50)

class MainGame:
    def __init__(self):
        self.player = Character(2, 10, (WIDTH//2, 0), "assets/player/player_idle.png")
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)
        self.floor = pygame.Rect(0, HEIGHT - 50, WIDTH, 10)
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
    

    def draw_window(self):
        self.general_use.display_background()
        
        pygame.draw.rect(screen, Colors.BLACK, self.floor)

        self.player_group.draw(screen)
        self.player_group.update()

        pygame.display.update()

    def game_loop(self):
        camera = Camera()
        run = True
        left = False
        right = False
        up = False
        while run:
            clock.tick(60)
            mouse_pos = pygame.mouse.get_pos()

            # Movements
            if left and self.player.rect.left > 0:
                self.player.rect.left -= self.speed
                if self.player.rect.left < 0:
                    self.player.rect.left = 0
                    
            if right and self.player.rect.right < WIDTH:
                self.player.rect.right += self.speed
                if self.player.rect.right > WIDTH:
                    self.player.rect.right = WIDTH

            # Jump
            if up:
                self.velocity = -30

            # Gravity
            if self.player.rect.bottom < self.floor.top or self.velocity < 0:
                self.velocity += self.falling_speed
                self.player.rect.y += self.velocity
                if self.player.rect.bottom > self.floor.top:
                    self.player.rect.bottom = self.floor.top

            up = False
            # Event Handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    GeneralUse.close_the_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        GeneralUse.close_the_game()
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
        self.game_menu.menu_loop()
        self.game_loop()

main = MainGame()
main.run() 