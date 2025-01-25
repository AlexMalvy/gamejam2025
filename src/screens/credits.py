import pygame

class Credits:
    def __init__(self, screen: pygame.Surface, font_path: str, font_size: int, colors: dict[str, tuple[int, int, int]]):
        self.screen: pygame.Surface = screen
        self.font: pygame.font.Font = pygame.font.Font(font_path, font_size)
        self.colors: dict[str, tuple[int, int, int]] = colors
        self.logo : pygame.Surface = pygame.image.load('assets/logo/game_logo.png').convert_alpha()
        self.logo = pygame.transform.scale(self.logo, (300, 150)) 


    def draw_credits(self):
        # Background color
        self.screen.fill(self.colors["OCEAN_BLUE"])

        # Logo
        self.screen.blit(self.logo, (600,40) )

        # Credits
        text1 = self.font.render("CREDITS", True, self.colors["BLUE_MORGANE"],)
        text_rect1 = text1.get_rect(center=(self.screen.get_width() // 2, 250))
        self.screen.blit(text1, text_rect1)

        text2 = self.font.render("Jeu développé par : Groupe A - CCI Campus Alsace", True, self.colors["WHITE"])
        text_rect2 = text2.get_rect(center=(self.screen.get_width() // 2, 300))
        self.screen.blit(text2, text_rect2)

        text3 = self.font.render("Graphisme par : Leatitia LANG, Morgane SUTTER", True, self.colors["WHITE"])
        text_rect3 = text3.get_rect(center=(self.screen.get_width() // 2, 450))
        self.screen.blit(text3, text_rect3)

        text4 = self.font.render("Développement par : Alex MALVY, Thomas DO, Thomas KARCHER, Thomas MILTON", True, self.colors["WHITE"])
        text_rect4 = text4.get_rect(center=(self.screen.get_width() // 2, 500))
        self.screen.blit(text4, text_rect4)

        text5 = self.font.render("Music by: Den ELBRIGGS / Eddie LUNG -> Pixabay", True, self.colors["WHITE"])
        text_rect5 = text5.get_rect(center=(self.screen.get_width() // 2, 550))
        self.screen.blit(text5, text_rect5)

        text6 = self.font.render("GameJam - 2025 - Strasbourg", True, self.colors["WHITE"])
        text_rect6 = text6.get_rect(center=(self.screen.get_width() // 2, 700))
        self.screen.blit(text6, text_rect6)

        text7 = self.font.render("Appuyez sur ESC pour revenir au menu", True, self.colors["BLUE_MORGANE"])
        text_rect7 = text7.get_rect(center=(self.screen.get_width() // 2, 800))
        self.screen.blit(text7, text_rect7)

        pygame.display.update()

    
    def credits_loop(self):
        running = True
        while running:
            self.draw_credits()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        break