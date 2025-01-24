import pygame
import time
import random
from utils.color import Colors
from pygame.locals import *
from character import Character
from utils.generaluse import GeneralUse

WIDTH, HEIGHT = 1600, 1000

pygame.init()
pygame.display.set_caption("The rise of the Axolotl")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

#############

### Font

font = pygame.font.SysFont("serif", 40)

#############
general_use = GeneralUse(screen)

class game_over:

    def draw_window(self):
        general_use.display_background()
        
        score_text = font.render(f"Score : {main.score}", 1, Colors.BLACK)
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
    player = Character(2, 10, (WIDTH//2, 0), "assets/player/player_idle.png")
    player_group = pygame.sprite.Group()
    player_group.add(player)
    floor = pygame.Rect(0, HEIGHT - 50, WIDTH, 10)
    velocity = 0
    falling_speed = 3
    speed = 25
    start_time = time.time()
    game_length = 15


    def draw_window(self):
        general_use.display_background()
        
        pygame.draw.rect(screen, Colors.BLACK, self.floor)

        # time_text = font.render(f"{self.game_length - (time.time() - self.start_time):.2f} s", 1, BLACK)
        # screen.blit(time_text, (WIDTH - time_text.get_width() - 10, 10))

        self.player_group.draw(screen)
        self.player_group.update()

        pygame.display.update()

    def game_loop(self):
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
                    general_use.close_the_game()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        run = False
                        general_use.close_the_game()
                    if event.key == K_q:
                        left = True
                    if event.key == K_d:
                        right = True
                    if event.key == K_z:
                        up = True
                if event.type == KEYUP:
                    if event.key == K_q:
                        left = False
                    if event.key == K_d:
                        right = False
                    
            self.draw_window()

main = main_game()
main.game_loop()