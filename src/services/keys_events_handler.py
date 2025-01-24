from src.models.abstracts.character import Character
from pygame.key import ScancodeWrapper
from pygame import K_UP, K_DOWN, K_LEFT, K_RIGHT, K_ESCAPE


class KeysEventsHandler:
    __character: Character

    def __init__(
            self, 
            character: Character, 
            # TODO : add other parameters for menu singleton class
            ) -> None:
        self.__character = character

    def handle(self, keys: ScancodeWrapper) -> None:
        match keys:
            case k if k[K_ESCAPE]:
                # TODO : call menu function here
                pass
            case k if k[K_UP]:
                self.__character.go_up()
            case k if k[K_DOWN]:
                self.__character.go_down()
            case k if k[K_LEFT]:
                self.__character.go_left()
            case k if k[K_RIGHT]:
                self.__character.go_right()
            case _:
                pass
