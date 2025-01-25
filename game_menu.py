import pygame

class GameMenu:
    def __init__(self, screen: pygame.Surface, font: pygame.font.Font):
        self.screen: pygame.Surface = screen
        self.colors: dict[str, tuple[int, int, int]] = \
            {
                "WHITE": (255, 255, 255),
                "BLACK": (0, 0, 0),
                "DARK_GRAY": (169, 169, 169)
            }
        self.font: pygame.Font = font
        self.index : int = 0

    def setup(self):
        self.screen.fill(self.colors["BLACK"])
        pygame.display.update()

    def draw_menu(self):
        self.screen.fill(self.colors["WHITE"])
        text = self.font.render("The rise of the Axolotl", True, self.colors["BLACK"])
        self.screen.blit(text, (500, 100))
        instructions1 = self.font.render("Nouvelle partie", True, self.colors["DARK_GRAY" if self.index != 0 else "BLACK"])
        self.screen.blit(instructions1, (400, 400))
        instructions2 = self.font.render("Contrôles", True, self.colors["DARK_GRAY" if self.index != 1 else "BLACK"])
        self.screen.blit(instructions2, (400, 500))
        instructions3 = self.font.render("Crédits", True, self.colors["DARK_GRAY" if self.index != 2 else "BLACK"])
        self.screen.blit(instructions3, (400, 600))
        instructions4 = self.font.render("Quitter", True, self.colors["DARK_GRAY" if self.index != 3 else "BLACK"])
        self.screen.blit(instructions4, (400, 700))
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
                                    running = False
                                case 1:
                                    # Dispay controls
                                    running = True
                                case 2:
                                    # Display credits
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