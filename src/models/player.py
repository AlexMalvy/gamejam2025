from typing import List
from ..models.tilemap import TileMap
from .abstracts.character import Character
from .configuration import Configuration


class Player(Character):
    def __init__(
        self, 
        sprites_path: str, 
        config: Configuration, 
        tilemap: TileMap, 
        collisionables_layers: List[str]
    ) -> None:
        super().__init__(
            sprites_path,
            config.player.health,
            config.player.width,
            config.player.height,
            config.player.velocity,
            config.player.sprites.mitigation_rate,
            config.framerate,
            tilemap,
            collisionables_layers
        )
