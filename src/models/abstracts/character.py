from abc import ABC
from typing import List, Tuple, Final
from pygame import Surface, Rect
from pygame.image import load as load_image
from ...models.tilemap import TileMap


class Character(ABC):  # Abstract class == cannot be instantiated
    __SPRITE_MAX_NUMBER_ROW: Final[int] = 4
    __SPRITE_MAX_NUMBER_COLUMN: Final[int] = 4

    __tilemap: Final[TileMap]
    __collisionables_layers: Final[List[str]]
    __mitigation_framerate: Final[int]
    __health: int
    __width: Final[int]
    __height: Final[int]
    __velocity: Final[int]
    __player_sprites: Final[Surface]
    __current_frame_row_index: int
    __current_frame_column_index: int
    __current_frame_counter: int
    __current_frame_direction_updated: bool
    __current_frame: Surface
    __character_rect: Rect
    _hitbox: Rect # Protected attribute


    def __init__(
        self,
        sprites_path: str,
        health: int,
        width: int,
        height: int,
        velocity: int,
        mitigation_rate: float,
        framerate: int,
        tilemap: TileMap,
        collisionables_layers: List[str]
    ) -> None:
        self.__health = health
        self.__tilemap = tilemap
        self.__collisionables_layers = collisionables_layers
        max_framerate: int = int(mitigation_rate * framerate)
        self.__mitigation_framerate = (
            max_framerate
            if max_framerate % 2 != 0
            else max_framerate + 1  # Odd number only
        )
        self.__width = width
        self.__height = height
        self.__velocity = velocity
        self.__current_frame_row_index = 0
        self.__current_frame_column_index = 0
        self.__current_frame_counter = 0
        self.__current_frame_direction_updated = False
        self.__player_sprites = load_image(sprites_path)
        self.__current_frame = self.__player_sprites.subsurface(
            Rect(
                0,  # X position
                0,  # Y position
                self.__player_sprites.get_width()
                // self.__SPRITE_MAX_NUMBER_COLUMN,  # Width
                self.__player_sprites.get_height()
                // self.__SPRITE_MAX_NUMBER_ROW,  # Height
            )
        )
        # Set player position (top-left corner always !)
        position_x = ((self.__tilemap.width * self.__tilemap.tilewidth) - self.__width) // 2
        position_y = ((self.__tilemap.height * self.__tilemap.tileheight) - self.__height) // 2
        self.__character_rect = Rect(
            position_x, position_y, self.__width, self.__height
        )
        self._hitbox = Rect(
            self.__character_rect.x,  # X position
            self.__character_rect.y + self.__height // 2,  # Y position
            self.__character_rect.width,  # Width
            self.__height // 2 # Half height
        )

    def __update_current_frame(self) -> None:
        self.__current_frame_counter += 1
        if (
            self.__current_frame_counter >= self.__mitigation_framerate
            or self.__current_frame_direction_updated
        ):
            self.__current_frame_counter = 0
            self.__current_frame_direction_updated = False
            frame_width: int = (
                self.__player_sprites.get_width() // self.__SPRITE_MAX_NUMBER_COLUMN
            )
            frame_height: int = (
                self.__player_sprites.get_height() // self.__SPRITE_MAX_NUMBER_ROW
            )
            self.__current_frame = self.__player_sprites.subsurface(
                Rect(
                    self.__current_frame_column_index * frame_width,  # X position
                    self.__current_frame_row_index * frame_height,  # Y position
                    frame_width,  # Width
                    frame_height,  # Height
                )
            )

    def __reset_current_frame(self) -> None:
        self.__current_frame_counter = 0
        self.__current_frame_direction_updated = True
        self.__current_frame_column_index = 0

    def __in_collision(self) -> bool:
        # Iterate over all collisionable layers
        for layer in self.__tilemap.layers:
            # Check if the layer is collisionable
            if layer.name in self.__collisionables_layers:
                # Iterate over all tiles in the layer
                for row_offset in range(layer.height): # Iterate over all rows
                    for col_offset in range(layer.width): # Iterate over all columns
                        # Get the tile id
                        tile_id: int = layer.data[row_offset * layer.width + col_offset]
                        if tile_id > 0: # Check if the tile is not empty
                            # Generate the tile rectangle
                            tile_rect = Rect(
                                self.__tilemap.tilewidth * col_offset,
                                self.__tilemap.tileheight * row_offset,
                                self.__tilemap.tilewidth,
                                self.__tilemap.tileheight,
                            )
                            # Check if the player is in collision with the tile
                            if self._hitbox.colliderect(tile_rect):
                                return True
        # No collision detected if we reach this point
        return False
    
    def receive_damage(self, damage: int) -> None:
        self.__health = max(0, self.__health - damage)
    
    def get_health(self) -> int:
        return self.__health

    def get_shape(self) -> Tuple[int, int]:
        return self.__width, self.__height

    def get_current_frame(self) -> Surface:
        return self.__current_frame

    def get_character_rect(self) -> Rect:
        return self.__character_rect

    def get_hitbox(self) -> Rect:
        return self._hitbox

    def go_up(self) -> None:
        # Updating the Character Sprite direction
        if self.__current_frame_row_index != 3:
            self.__reset_current_frame()
        self.__current_frame_row_index = 3
        self.__current_frame_column_index = (
            self.__current_frame_column_index + 1
        ) % self.__SPRITE_MAX_NUMBER_ROW
        self.__update_current_frame()
        # Updating the Character coordinates
        self.__character_rect.y = max(0, self.__character_rect.y - self.__velocity)
        # Update hitbox
        self._hitbox.x = self.__character_rect.x
        self._hitbox.y = self.__character_rect.y + self.__character_rect.height // 2
        # Check collision
        if self.__in_collision():
            # Rollback to previous position
            self.__character_rect.y += self.__velocity
            # Update hitbox
            self._hitbox.x = self.__character_rect.x
            self._hitbox.y = self.__character_rect.y + self.__character_rect.height // 2

    def go_down(self) -> None:
        # Updating the Character Sprite direction
        if self.__current_frame_row_index != 0:
            self.__reset_current_frame()
        self.__current_frame_row_index = 0
        self.__current_frame_column_index = (
            self.__current_frame_column_index + 1
        ) % self.__SPRITE_MAX_NUMBER_ROW
        self.__update_current_frame()
        # Updating the Character coordinates
        self.__character_rect.y = min(
            (self.__tilemap.height * self.__tilemap.tileheight) - self.__height,
            self.__character_rect.y + self.__velocity,
        )
        # Update hitbox
        self._hitbox.x = self.__character_rect.x
        self._hitbox.y = self.__character_rect.y + self.__character_rect.height // 2
        # Check collision
        if self.__in_collision():
            # Rollback to previous position
            self.__character_rect.y -= self.__velocity
            # Update hitbox
            self._hitbox.x = self.__character_rect.x
            self._hitbox.y = self.__character_rect.y + self.__character_rect.height // 2

    def go_left(self) -> None:
        # Updating the Character Sprite direction
        if self.__current_frame_row_index != 2:
            self.__reset_current_frame()
        self.__current_frame_row_index = 2
        self.__current_frame_column_index = (
            self.__current_frame_column_index + 1
        ) % self.__SPRITE_MAX_NUMBER_COLUMN
        self.__update_current_frame()
        # Updating the Character coordinates
        self.__character_rect.x = max(0, self.__character_rect.x - self.__velocity)
        # Update hitbox
        self._hitbox.x = self.__character_rect.x
        self._hitbox.y = self.__character_rect.y + self.__character_rect.height // 2
        # Check collision
        if self.__in_collision():
            # Rollback to previous position
            self.__character_rect.x += self.__velocity
            # Update hitbox
            self._hitbox.x = self.__character_rect.x
            self._hitbox.y = self.__character_rect.y + self.__character_rect.height // 2


    def go_right(self) -> None:
        # Updating the Character Sprite direction
        if self.__current_frame_row_index != 1:
            self.__reset_current_frame()
        self.__current_frame_row_index = 1
        self.__current_frame_column_index = (
            self.__current_frame_column_index + 1
        ) % self.__SPRITE_MAX_NUMBER_COLUMN
        self.__update_current_frame()
        # Updating the Character coordinates
        self.__character_rect.x = min(
            (self.__tilemap.width * self.__tilemap.tilewidth) - self.__width,
            self.__character_rect.x + self.__velocity,
        )
        # Update hitbox
        self._hitbox.x = self.__character_rect.x
        self._hitbox.y = self.__character_rect.y + self.__character_rect.height // 2
        # Check collision
        if self.__in_collision():
            # Rollback to previous position
            self.__character_rect.x -= self.__velocity
            # Update hitbox
            self._hitbox.x = self.__character_rect.x
            self._hitbox.y = self.__character_rect.y + self.__character_rect.height // 2
