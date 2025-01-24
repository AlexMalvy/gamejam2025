import pygame
import time
import random
import pygame.locals
from utils.color import Colors
from utils.game_over import GameOver
from utils.generaluse import GeneralUse
from utils.game_menu import GameMenu
from utils.window import HEIGHT, WIDTH
from pygame.font import SysFont

pygame.init()
pygame.display.set_caption("The rise of the Axolotl")
screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))

clock = pygame.time.Clock()
font40 = SysFont(name="serif", size=40)
font50 = SysFont(name="serif", size=50)

############################################

class MainGame:

    def __init__(self):
        self.player = pygame.Rect(WIDTH//2, 10, 50, 50)
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

    def get_random_item_x(self):
        x = random.random() * WIDTH
        if x < 50:
            x = 50
        elif x > WIDTH - 50:
            x = WIDTH - 50
        return x

    def spawn_item(self):
        run = True
        x: float = 0
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

        screen.blit(self.get_score_text(), (10, 10))

        time_text = font40.render(f"{self.game_length - (time.time() - self.start_time):.2f} s", True, Colors.BLACK)
        screen.blit(time_text, (WIDTH - time_text.get_width() - 10, 10))

        pygame.display.update()

    def game_loop(self):
        run = True
        left = False
        right = False
        self.game_menu.setup()
        while run:
            self.game_menu.draw_menu()
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
                self.game_over.game_over()

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
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        left = False
                    if event.key == pygame.K_d:
                        right = False
                    
            self.draw_window()

main = MainGame()
main.game_loop()