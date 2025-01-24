from src.models.player import Player
from pygame.key import ScancodeWrapper
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT


class KeysEventsHandler:
    __player: Player

    def __init__(self, player: Player) -> None:
        self.__player = player

    def handle(self, keys: ScancodeWrapper) -> None:
        match keys:
            case k if k[K_UP]:
                self.__player.go_up()
            case k if k[K_DOWN]:
                self.__player.go_down()
            case k if k[K_LEFT]:
                self.__player.go_left()
            case k if k[K_RIGHT]:
                self.__player.go_right()
            case _:
                pass
