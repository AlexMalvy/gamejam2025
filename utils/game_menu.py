import pygame

class GameMenu:
    def __init__(self, screen: pygame.Surface, font: pygame.font.Font):
        self.screen = screen
        self.colors = \
            {
                "WHITE": (255, 255, 255),
                "BLACK": (0, 0, 0),
                "DARK_GRAY": (169, 169, 169)
            }
        self.font = font

    def setup(self):
        self.screen.fill(self.colors["BLACK"])
        pygame.display.set_caption("Menu Test!")
        pygame.display.update()

    def draw_menu(self):
        self.screen.fill(self.colors["WHITE"])
        text = self.font.render("Welcome to the Game Menu", True, self.colors["RED"])
        self.screen.blit(text, (400, 300))
        pygame.display.update()