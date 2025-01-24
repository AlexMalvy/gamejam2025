from pygame import Rect
from typing import Final
from ..models.configuration import Configuration
from ..models.player import Player
from ..models.tilemap import TileMap


class Camera:
    __player: Final[Player]
    __map_width: Final[int]
    __map_height: Final[int]
    __displayed_width: Final[int]
    __displayed_height: Final[int]
    __camera_rect: Final[Rect]

    def __init__(self, configuration: Configuration, tilemap: TileMap, player: Player) -> None:
        self.__player = player
        self.__map_width = tilemap.width * tilemap.tilewidth
        self.__map_height = tilemap.height * tilemap.tileheight
        self.__displayed_width = configuration.window.width
        self.__displayed_height = configuration.window.height
        self.__camera_rect = Rect(0, 0, self.__displayed_width, self.__displayed_height)

    def get_camera_rect(self) -> Rect:
        return self.__camera_rect

    def update_camera_rect(self) -> None:
        # Ensure camera is within the map boundaries
        self.__camera_rect.x = max(
            0, 
            min(
                self.__player.get_character_rect().x - self.__displayed_width // 2, # Center the player on the x axis
                self.__map_width - self.__displayed_width
            )
       )
        self.__camera_rect.y = max(
            0, 
            min(
                self.__player.get_character_rect().y - self.__displayed_height // 2, # Center the player on the y axis
                self.__map_height - self.__displayed_height
            )
        )
