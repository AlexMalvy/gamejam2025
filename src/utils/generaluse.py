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

    def update_timer(self, start_time, end_time):
        if end_time is None:
            elapsed_time = pygame.time.get_ticks() - start_time
        else:
            elapsed_time = end_time - start_time
        minutes = int(elapsed_time // 60000)
        seconds = int((elapsed_time % 60000) // 1000)
        return f"{minutes:02}:{seconds:02}"