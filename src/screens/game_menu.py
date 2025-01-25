import pygame
from src.screens.credits import Credits

class GameMenu:
    def __init__(self, screen: pygame.Surface, font: pygame.font.Font):
        self.screen: pygame.Surface = screen
        self.colors: dict[str, tuple[int, int, int]] = \
            {
                "BLACK": (0, 0, 0),
                "BLUE_MORGANE": (40, 40, 101),
                "WHITE": (255, 255, 255),
                "OCEAN_BLUE":(67, 118, 180)
            }
        self.font: pygame.Font = font
        self.index : int = 0
        self.logo : pygame.Surface = pygame.image.load('assets/logo/game_logo.png').convert_alpha()
        self.logo = pygame.transform.scale(self.logo, (600, 300)) 

        # Music
        pygame.mixer.init()
        pygame.mixer.music.load('assets/music/retro_music.mp3')
        pygame.mixer.music.play(-1)

    def setup(self):
        self.screen.fill(self.colors["BLACK"])
        pygame.display.update()

    def draw_menu(self):
        # Background color
        self.screen.fill(self.colors["OCEAN_BLUE"])
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

        pygame.display.update()

    def menu_loop(self):
        running = True
        while running:
            self.draw_menu()
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
                                    # Dispay controls
                                    running = True
                                case 2:
                                    # Display credits
                                    credits = Credits(self.screen, 'assets/fonts/nexa_heavy.ttf', 30, self.colors)
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