import pygame
import random

from src.screens.credits import Credits
from src.screens.controller import Controller
from src.entities.bubble_screen_menu import BubbleScreenMenu

class GameMenu:
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
        pygame.mixer.init()
        pygame.mixer.music.load('assets/music/water_flow_ambient_nature_drone.mp3')
        pygame.mixer.music.play(-1)

        # Bubbles
        self.bubble = pygame.image.load('assets/entities/bubble_1.png').convert_alpha()
        self.min_bubble_size = 20
        self.max_bubble_size = 100

        self.bubbles = [self.create_bubble() for _ in range(10)]

        # Clock
        self.clock = pygame.time.Clock()
    
    def create_bubble(self):
        size = random.randint(self.min_bubble_size, self.max_bubble_size)
        bubble = pygame.transform.scale(self.bubble, (size, size))
        return BubbleScreenMenu(self.screen.get_width(), self.screen.get_height(), bubble)

    def draw_bubbles(self):
        for bubble in self.bubbles:
            bubble.update()
            bubble.draw(self.screen)

    def draw_menu(self):
        # Background
        self.screen.blit(self.background, (0, 0))
        # Logo
        logo_x = (self.screen.get_width() - self.logo.get_width()) // 2
        self.screen.blit(self.logo, (logo_x, 40))
        # Menu
        instructions1 = self.font.render("NOUVELLE PARTIE", True, self.colors["WHITE" if self.index != 0 else "BLUE_MORGANE"])
        text_rect1 = instructions1.get_rect(center=(self.screen.get_width() // 2, 400))
        self.screen.blit(instructions1, text_rect1)
    
        instructions2 = self.font.render("CONTRÔLES", True, self.colors["WHITE" if self.index != 1 else "BLUE_MORGANE"])
        text_rect2 = instructions2.get_rect(center=(self.screen.get_width() // 2, 500))
        self.screen.blit(instructions2, text_rect2)
        
        instructions3 = self.font.render("CREDITS", True, self.colors["WHITE" if self.index != 2 else "BLUE_MORGANE"])
        text_rect3 = instructions3.get_rect(center=(self.screen.get_width() // 2, 600))
        self.screen.blit(instructions3, text_rect3)
        
        instructions4 = self.font.render("QUITTER", True, self.colors["WHITE" if self.index != 3 else "BLUE_MORGANE"])
        text_rect4 = instructions4.get_rect(center=(self.screen.get_width() // 2, 700))
        self.screen.blit(instructions4, text_rect4)

    def menu_loop(self):
        running = True
        while running:
            self.screen.fill(self.colors["BLACK"])
            self.draw_menu()
            self.draw_bubbles()
            pygame.display.flip()
            self.clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    match event.key:
                        case pygame.K_z:
                            self.index = (self.index - 1) % 4
                        case pygame.K_s:
                            self.index = (self.index + 1) % 4
                        case pygame.K_RETURN:
                            # Selected index
                            match self.index:
                                case 0:
                                    # Start the game
                                    pygame.mixer.music.stop()
                                    running = False
                                case 1:
                                    # Display controls
                                    controller = Controller(self.screen, 'assets/fonts/nexa_heavy.ttf', 30, self.colors, self.background, self.bubbles)
                                    controller.controller_loop()
                                    running = True
                                case 2:
                                    # Display credits
                                    credits = Credits(self.screen, 'assets/fonts/nexa_heavy.ttf', 30, self.colors, self.background, self.bubbles)
                                    credits.credits_loop()
                                    running = True
                                case _:
                                    running = False
                                    pygame.quit()
                                    exit()
                        case pygame.K_ESCAPE:
                            running = False
                            pygame.quit()
                            exit()
                        case _:
                            pass