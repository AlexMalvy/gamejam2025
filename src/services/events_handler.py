from typing import Callable, List
from pygame import QUIT
from pygame.event import Event


class EventsHandler:
    __stop_game: Callable[[], None]

    def __init__(self, stop_game: Callable[[], None]) -> None:
        self.__stop_game = stop_game

    def handle(self, events: List[Event]) -> None:
        for event in events:
            if event.type == QUIT:
                self.__stop_game()
