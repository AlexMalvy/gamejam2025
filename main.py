import pygame
import time
import random
from utils.color import Colors
from pygame.locals import *
from utils.generaluse import GeneralUse


WIDTH, HEIGHT = 1600, 1000

pygame.init()
pygame.display.set_caption("The rise of the Axolotl")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

#############

### Font

font = pygame.font.SysFont("serif", 40)

print(Colors.DARK_GRAY)

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
        if self.item is None:
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

        pygame.draw.circle(screen, Colors.RED, self.player.center, self.player.width//2)
        
        if self.item:
            pygame.draw.rect(screen, Colors.YELLOW, self.item)
        
        pygame.draw.rect(screen, Colors.BLACK, self.floor)

        score_text = font.render(f"Score : {self.score}", 1, Colors.BLACK)
        screen.blit(score_text, (10, 10))

        time_text = font.render(f"{self.game_length - (time.time() - self.start_time):.2f} s", 1, Colors.BLACK)
        screen.blit(time_text, (WIDTH - time_text.get_width() - 10, 10))

        pygame.display.update()

    def game_loop(self):
        run = True
        left = False
        right = False
        while run:
            clock.tick(60)
            # mouse_x, mouse_y = pygame.mouse.get_pos()

            if left and self.player.left > 0:
                self.player.x -= self.speed
            if right and self.player.right < WIDTH:
                self.player.x += self.speed

            self.velocity += self.falling_speed

            self.player.y += self.velocity

            if self.player.bottom >= self.floor.top:
                self.player.bottom = self.floor.top
                self.velocity = -70
                if self.item is None:
                    self.spawn_item()

            self.pickup_item()

            if (self.game_length - (time.time() - main.start_time)) <= 0:
                game_over.game_over()

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