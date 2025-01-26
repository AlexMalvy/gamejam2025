import pygame

from src.entities.bubble import Bubble

class Controller:
    def __init__(self, screen: pygame.Surface, font_path: str, font_size: int, colors: dict[str, tuple[int, int, int]], background: pygame.Surface, bubbles: list[Bubble]):
        self.screen: pygame.Surface = screen
        self.font: pygame.font.Font = pygame.font.Font(font_path, font_size)
        self.colors: dict[str, tuple[int, int, int]] = colors
        self.logo : pygame.Surface = pygame.image.load('assets/logo/game_logo.png').convert_alpha()
        self.logo = pygame.transform.scale(self.logo, (300, 150))
        self.background: pygame.Surface = background
        self.bubbles = bubbles
        self.clock = pygame.time.Clock()
        self.z_pressed = False

        self.z_not_pressed_image = pygame.image.load('assets/keyboard/letter_z_not_pressed.png')
        self.z_pressed_image = pygame.image.load('assets/keyboard/letter_z_pressed.png')
        self.q_not_pressed_image = pygame.image.load('assets/keyboard/letter_q_not_pressed.png')
        self.q_pressed_image = pygame.image.load('assets/keyboard/letter_q_pressed.png')
        self.d_not_pressed_image = pygame.image.load('assets/keyboard/letter_d_not_pressed.png')
        self.d_pressed_image = pygame.image.load('assets/keyboard/letter_d_pressed.png')
        self.space_bar_not_pressed = pygame.image.load('assets/keyboard/space_bar_not_pressed.png')
        self.space_bar_pressed = pygame.image.load('assets/keyboard/space_bar_pressed.png')
        self.image_toggle_counter = 0

    def draw_bubbles(self):
        for bubble in self.bubbles:
            bubble.update()
            bubble.draw(self.screen)
    
    def draw_controller(self):
        # Background
        self.screen.blit(self.background, (0, 0))
        
        # Logo
        logo_x = (self.screen.get_width() - self.logo.get_width()) // 2
        self.screen.blit(self.logo, (logo_x, 40))
        
        text1 = self.font.render("RACCOURCIS", True, self.colors["BLUE_MORGANE"],)
        text_rect1 = text1.get_rect(center=(self.screen.get_width() // 2, 250))
        self.screen.blit(text1, text_rect1)
        
        z_picture = self.z_pressed_image if self.image_toggle_counter // 30 % 2 == 0 else self.z_not_pressed_image
        z_rect1 = z_picture.get_rect(center=(500, 350))
        self.screen.blit(z_picture, z_rect1)

        text_z = self.font.render("Sauter", True, self.colors["WHITE"])
        text_rect_z = text_z.get_rect(midleft=(700, 350))
        self.screen.blit(text_z, text_rect_z)

        q_picture = self.q_pressed_image if self.image_toggle_counter // 30 % 2 == 0 else self.q_not_pressed_image
        q_rect1 = q_picture.get_rect(center=(500, 450))
        self.screen.blit(q_picture, q_rect1)

        text_q = self.font.render("Aller vers la gauche", True, self.colors["WHITE"])
        text_rect_q = text_q.get_rect(midleft=(700, 450))
        self.screen.blit(text_q, text_rect_q)

        d_picture = self.d_pressed_image if self.image_toggle_counter // 30 % 2 == 0 else self.d_not_pressed_image
        d_rect1 = d_picture.get_rect(center=(500, 550))
        self.screen.blit(d_picture, d_rect1)

        text_d = self.font.render("Aller vers la droite", True, self.colors["WHITE"])
        text_rect_d = text_d.get_rect(midleft=(700, 550))
        self.screen.blit(text_d, text_rect_d)

        space_picture = self.space_bar_pressed if self.image_toggle_counter // 30 % 2 == 0 else self.space_bar_not_pressed
        space_rect1 = space_picture.get_rect(center=(500, 650))
        self.screen.blit(space_picture, space_rect1)

        text_space = self.font.render("Tirer des bulles", True, self.colors["WHITE"])
        text_rect_space = text_space.get_rect(midleft=(700, 650))
        self.screen.blit(text_space, text_rect_space)

        text7 = self.font.render("Appuyez sur ESC pour revenir au menu", True, self.colors["BLUE_MORGANE"])
        text_rect7 = text7.get_rect(center=(self.screen.get_width() // 2, 800))
        self.screen.blit(text7, text_rect7)

    def controller_loop(self):
        running = True
        while running:
            self.screen.fill(self.colors["BLACK"])
            self.draw_controller()
            self.draw_bubbles()
            pygame.display.flip()
            self.clock.tick(60)
            self.image_toggle_counter += 1
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                        break
