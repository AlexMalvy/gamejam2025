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
        pygame.display.update()

    def draw_menu(self):
        self.screen.fill(self.colors["WHITE"])
        text = self.font.render("The rise of the Axolotl", True, self.colors["BLACK"])
        self.screen.blit(text, (500, 100))
        instructions = self.font.render("Pressez ENTRER pour commencer", True, self.colors["DARK_GRAY"])
        self.screen.blit(instructions, (400, 400))
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
                    if event.key == pygame.K_RETURN:
                        running = False