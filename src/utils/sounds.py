import pygame
import random


class SoundManager:
    def __init__(self):
        pygame.mixer.pre_init(44100,-16,2, 1024)
        pygame.mixer.init()
        self.sfx = {
            "special": [pygame.mixer.Sound("assets/sfx/bubble_haut_1.ogg"),
                        pygame.mixer.Sound("assets/sfx/bubble_bas.ogg"),
                        pygame.mixer.Sound("assets/sfx/bubble_haut_2.ogg"),],
            "bubble_up": pygame.mixer.Sound("assets/sfx/bubble_up_2.ogg"),
            "menu": pygame.mixer.Sound("assets/sfx/Musique/menu.ogg"),
            # "game": pygame.mixer.Sound("assets/sfx/musique/game.ogg"),
            # "bubble": pygame.mixer.Sound("assets/sfx/bubble.wav"),
            # "jellyfish": pygame.mixer.Sound("assets/sfx/jellyfish.wav"),
            # "shark": pygame.mixer.Sound("assets/sfx/shark.wav"),
            # "victory": pygame.mixer.Sound("assets/sfx/victory.wav"),
            # "defeat": pygame.mixer.Sound("assets/sfx/defeat.wav"),
        }
    
    def play_random(self, sound):
        random.choice(self.sfx[sound]).play()

    def play(self, sound):
        self.sfx[sound].play()

    def stop(self, sound):
        self.sfx[sound].stop()