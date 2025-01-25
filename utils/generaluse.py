import pygame
import sys

class GeneralUse:
    background_color = (255, 255, 255)  # WHITE

    def __init__(self, screen: pygame.Surface):
        self.screen = screen

    def display_background(self):
        self.screen.fill(self.background_color)

    def close_the_game(self):
        pygame.quit()
        sys.exit()
