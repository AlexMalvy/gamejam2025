import pygame
import time
import random
from utils.color import Colors
from utils.game_over import GameOver
from character import Character
from utils.generaluse import GeneralUse
from utils.window import HEIGHT, WIDTH
from pygame.font import SysFont
from game_menu import GameMenu

pygame.init()
pygame.display.set_caption("The rise of the Axolotl")
screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))

clock = pygame.time.Clock()
font40 = SysFont(name="serif", size=40)
font50 = SysFont(name="serif", size=50)

class MainGame:
    def __init__(self):
        self.player = pygame.Rect(WIDTH // 2, 10, 50, 50)
        self.floor = pygame.Rect(0, HEIGHT - 50, WIDTH, 10)
        self.velocity = 0
        self.falling_speed = 3
        self.speed = 25
        self.item = None
        self.score = 0
        self.start_time = time.time()
        self.game_length = 15
        self.get_score_text = lambda: font40.render(f"Score : {self.score}", True, Colors.BLACK)
        self.general_use = GeneralUse(screen)
        self.game_over = GameOver(
            self.general_use,
            clock,
            self.get_score_text,
            screen,
        )
        self.game_menu = GameMenu(screen, font50)
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
        self.general_use.display_background()

        pygame.draw.circle(screen, Colors.RED, self.player.center, self.player.width//2)
        
        if self.item:
            pygame.draw.rect(screen, Colors.YELLOW, self.item)
        
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
        self.game_menu.menu_loop()
        self.game_loop()

main = MainGame()
main.run() 