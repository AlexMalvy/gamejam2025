import pygame
import sys

import random

from src.entities.bubble_screen_menu import BubbleScreenMenu
from src.utils.sounds import SoundManager


# Initialize Pygame
pygame.init()

# # Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# # Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# # Fonts
# FONT_SIZE = 50
# font = pygame.font.Font(None, FONT_SIZE)

# # Create the screen
# screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
# pygame.display.set_caption("Game Over")



# def game_over_menu(score):
#     while True:
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_RETURN:
#                     return  # Exit the game over menu

#         screen.fill(BLACK)

#         # Render the game over text
#         game_over_text = font.render("Game Over", True, WHITE)
#         game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
#         screen.blit(game_over_text, game_over_rect)

#        

#         pygame.display.flip()

# # # Example usage
# if __name__ == "__main__":
#     score = 123  # Example score
#     game_over_menu(score)

import pygame
import random

from src.screens.credits import Credits
from src.screens.controller import Controller
from src.entities.bubble_screen_menu import BubbleScreenMenu
from src.utils.sounds import SoundManager

class GameOver:
    def __init__(self, screen: pygame.Surface, font: pygame.font.Font):
        self.screen: pygame.Surface = screen
        self.colors: dict[str, tuple[int, int, int]] = {
            "BLACK": (0, 0, 0),
            "BLUE_MORGANE": (107, 168, 230),
            "WHITE": (255, 255, 255),
            "OCEAN_BLUE": (67, 118, 180)
        }
        self.font: pygame.font.Font = font
        self.index: int = 0

        # Logo
        self.logo: pygame.Surface = pygame.image.load('assets/logo/game_logo.png').convert_alpha()
        self.logo = pygame.transform.scale(self.logo, (600, 300))

        # Background
        self.background = pygame.image.load('assets/background/menu_background.jpg')
        self.background = pygame.transform.scale(self.background, (self.screen.get_width(), self.screen.get_height()))

        # Music
        # pygame.mixer.init()
        # pygame.mixer.music.load('assets/music/water_flow_ambient_nature_drone.mp3')
        # pygame.mixer.music.play(-1)
        self.sound_manager = SoundManager()
        

        # Bubbles
        self.bubble_images = [pygame.image.load(f'assets/sprites/bubble_{i}.png').convert_alpha() for i in range(1, 11)]
        for image in self.bubble_images:
            assert isinstance(image, pygame.Surface), "Chaque image doit être une surface Pygame"
        self.min_bubble_size = 20
        self.max_bubble_size = 100

        self.bubbles = pygame.sprite.Group()
        for _ in range(10):
            self.bubbles.add(self.create_bubble())

        # Clock
        self.clock = pygame.time.Clock()
    
    def create_bubble(self):
        size = random.randint(self.min_bubble_size, self.max_bubble_size)
        bubble = pygame.transform.scale(self.bubble, (size, size))
        return BubbleScreenMenu(self.screen.get_width(), self.screen.get_height(), bubble)
    
    def create_bubble(self):
        size = random.randint(self.min_bubble_size, self.max_bubble_size)
        bubble_images = [pygame.transform.scale(image, (size, size)) for image in self.bubble_images]
        return BubbleScreenMenu(self.screen.get_width(), self.screen.get_height(), bubble_images)

    def draw_menu(self):
        # Background
        self.screen.blit(self.background, (0, 0))
        # Logo
        logo_x = (self.screen.get_width() - self.logo.get_width()) // 2
        self.screen.blit(self.logo, (logo_x, 40))
       
       # Render the game over text
        game_over_text = self.font.render("GAME OVER", True, WHITE)
        game_over_rect = game_over_text.get_rect(center=(self.screen.get_width() // 2, 400))
        self.screen.blit(game_over_text, game_over_rect)

        #  Render the score text
        # score_text = self.font.render(f"Score: {score}", True, WHITE)
        # score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        # self.screen.blit(score_text, score_rect)

        # Render the instruction text
        instruction_text = self.font.render("Press Enter to Restart", True, WHITE)
        instruction_rect = instruction_text.get_rect(center=(self.screen.get_width() // 2, 700))
        self.screen.blit(instruction_text, instruction_rect)

    def game_over_loop(self):
        running = True
        while running:
            self.screen.fill(self.colors["BLACK"])
            self.draw_menu()
            self.bubbles.update()
            self.bubbles.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)
            self.sound_manager.play("menu")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_ESCAPE:
                            running = False
                            pygame.quit()
                            exit()
                        case pygame.K_RETURN:
                            running = False
                            # self.main.run()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = event.pos
                    for bubble in self.bubbles:
                        if bubble.rect.collidepoint(mouse_x, mouse_y):
                            bubble.pop()


