import pygame
import sys
import time
import random
import os
import sys
import math
from color import Colors
from pygame.locals import *
from character import Character

WIDTH, HEIGHT = 1600, 1000

pygame.init()
pygame.display.set_caption("Rebound !")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

#############

### Font

font = pygame.font.SysFont("serif", 40)

### Colors

RED = (255, 0, 0)
DARK_RED = (180, 0, 0)
YELLOW = (255,235,42)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
GRAYISH = (150, 150, 150)
DARK_GRAY = (100, 100, 100)
GREEN = (0, 128, 0)
BROWN = (83, 61, 50)

#############

class general_use:
    background_color = WHITE

    def display_background(self):
        screen.fill(self.background_color)

    def close_the_game(self):
        pygame.quit()
        sys.exit()

general_use = general_use()


class game_over:

    def draw_window(self):
        general_use.display_background()
        
        score_text = font.render(f"Score : {main.score}", 1, BLACK)
        screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 - score_text.get_height()//2))

        pygame.display.update()

    def game_over(self):
        run = True
        while run:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    general_use.close_the_game()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
                        general_use.close_the_game()
            self.draw_window()

game_over = game_over()



class main_game:
    player = Character(2, 10, (WIDTH//2, HEIGHT//2), "assets/player/player_idle.png")
    player_group = pygame.sprite.Group()
    player_group.add(player)
    player = pygame.Rect(WIDTH//2, 10, 50, 50)
    floor = pygame.Rect(0, HEIGHT - 50, WIDTH, 10)
    velocity = 0
    falling_speed = 3
    speed = 25
    item = None
    score = 0
    start_time = time.time()
    game_length = 15

    def get_random_item_x(self):
        x = random.random() * WIDTH
        if x < 50:
            x = 50
        elif x > WIDTH - 50:
            x = WIDTH - 50
        return x


    def spawn_item(self):
        run = True
        if self.item == None:
            x = self.get_random_item_x()
        else:
            while run:
                x = self.get_random_item_x()
                if abs(self.item.x - x) >= 300:
                    run = False
        self.item = pygame.Rect(x, 200 + random.random() * 250, 30, 30)

    def pickup_item(self):
        if self.item:
            if self.player.colliderect(self.item):
                self.score += 1
                self.spawn_item()

    def draw_window(self):
        general_use.display_background()

        pygame.draw.circle(screen, RED, self.player.center, self.player.width//2)
        
        if self.item:
            pygame.draw.rect(screen, YELLOW, self.item)
        
        pygame.draw.rect(screen, BLACK, self.floor)

        score_text = font.render(f"Score : {self.score}", 1, BLACK)
        screen.blit(score_text, (10, 10))

        time_text = font.render(f"{self.game_length - (time.time() - self.start_time):.2f} s", 1, BLACK)
        screen.blit(time_text, (WIDTH - time_text.get_width() - 10, 10))

        self.player_group.draw(screen)
        self.player_group.update()

        pygame.display.update()

    def game_loop(self):
        run = True
        left = False
        right = False
        while run:
            clock.tick(60)

            mouse_pos = pygame.mouse.get_pos()


            # Event Handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    general_use.close_the_game()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
                        general_use.close_the_game()
                    if event.key == K_q:
                        left = True
                    if event.key == K_d:
                        right = True
                if event.type == KEYUP:
                    if event.key == K_q:
                        left = False
                    if event.key == K_d:
                        right = False
                    
            self.draw_window()

main = main_game()
main.game_loop()