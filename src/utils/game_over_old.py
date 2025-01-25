from typing import Callable
import pygame
from src.utils.generaluse import GeneralUse
from .window import HEIGHT, WIDTH


class GameOver:

    __general_use: GeneralUse
    __clock: pygame.time.Clock
    __get_score_text: Callable[[], pygame.Surface]
    __screen: pygame.Surface

    def __init__(
            self, 
            general_use: GeneralUse, 
            clock: pygame.time.Clock, 
            # get_score_text: Callable[[], pygame.Surface],          
            screen: pygame.Surface,
        ) -> None:
        self.__general_use = general_use
        self.__clock = clock
        # self.__get_score_text = get_score_text
        self.__screen = screen

    def draw_window(self):
        self.__general_use.display_background()
        
        score_text = self.__get_score_text()
        self.__screen.blit(score_text, (WIDTH//2 - score_text.get_width()//2, HEIGHT//2 - score_text.get_height()//2))

        pygame.display.update()

    def game_over(self):
        run = True
        while run:
            self.__clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.__general_use.close_the_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        self.__general_use.close_the_game()
            self.draw_window()
