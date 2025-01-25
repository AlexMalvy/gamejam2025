import pygame
import random

class SoundManager:
    def __init__(self):
        self.sfx = {
            "special": [pygame.mixer.Sound("assets/sfx/bubble_haut_1.ogg"),
                        pygame.mixer.Sound("assets/sfx/bubble_bas.ogg"),
                        pygame.mixer.Sound("assets/sfx/bubble_haut_2.ogg"),],
            "bubble_up": pygame.mixer.Sound("assets/sfx/bubble_up_2.ogg"),
            # "attack": pygame.mixer.Sound("assets/sfx/attack.wav"),
            # "stun": pygame.mixer.Sound("assets/sfx/stun.wav"),
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