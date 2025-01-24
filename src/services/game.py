
from ..models.tilemap import TileMap
from ..models.configuration import Configuration
from ..models.player import Player
from .map_builder import MapBuilder
from .configuration_builder import ConfigurationBuilder
from .events_handler import EventsHandler
from .keys_events_handler import KeysEventsHandler
from .resource_locator import ResourceLocator
from .camera import Camera
from typing import Tuple
import pygame

"""
debug : print(pygame.display.Info())
"""


class Game:
    __launched: bool
    __configuration: Configuration
    __resource_locator: ResourceLocator
    __window: pygame.Surface
    __clock: pygame.time.Clock
    __map_builder: MapBuilder
    __player: Player
    __handler: EventsHandler
    __keys_handler: KeysEventsHandler
    __camera: Camera

    def __init__(self) -> None:
        # Game state init
        self.__launched = True
        # Get configuration from config.json file
        self.__configuration = ConfigurationBuilder().get_configuration()
        # Init resources locator
        self.__resource_locator = ResourceLocator("assets")
        # Initialize pygame library
        pygame.init()
        # Init window
        self.__set_window()
        # Fill window with a default color
        self.__window.fill(self.__configuration.window.default_color)
        # Set window caption
        pygame.display.set_caption(self.__configuration.window.caption)
        # Set window icon
        pygame.display.set_icon(
            pygame.image.load(self.__resource_locator.fetch("icon.png"))
        )
        # Clock init (for framerate regulation)
        self.__clock = pygame.time.Clock()
        # Init map builder
        self.__map_builder = MapBuilder(
            self.__resource_locator,
            self.__configuration
        )
        # Init player
        self.__player = Player(
            self.__resource_locator.fetch(self.__configuration.player.sprites.file_name),
            self.__configuration,
            self.__map_builder.get_tilemap(),
            self.__map_builder.get_collisionables_layers()
        )
        # Init events handler
        self.__handler = EventsHandler(
            stop_game=(lambda: setattr(self, "_Game__launched", False))
        )
        # Init keys events handler
        self.__keys_handler = KeysEventsHandler(self.__player)
        # Init camera
        self.__camera = Camera(self.__configuration, self.__map_builder.get_tilemap(), self.__player)

    def __set_window(self, width: int | None = None, heigth: int | None = None) -> None:
        self.__window = pygame.display.set_mode(
            size=(
                width if width != None else self.__configuration.window.width,
                heigth if heigth != None else self.__configuration.window.height,
            ),
            flags=(
                (
                    # Fullscreen mode
                    pygame.FULLSCREEN
                    if self.__configuration.window.fullscreen
                    else 0
                )
                | (
                    # Resizable window
                    pygame.RESIZABLE
                    if self.__configuration.window.resizable
                    else 0
                )
                | (
                    # Remove window decorations
                    pygame.NOFRAME
                    if self.__configuration.window.noframe
                    else 0
                )
                | (
                    # Enable rendering with OpenGL API (3D only)
                    pygame.OPENGL
                    if self.__configuration.window.opengl
                    else 0
                )
                | (
                    # Enable Hardware acceleration
                    pygame.HWSURFACE
                    if self.__configuration.window.hwsurface
                    else 0
                )
                | (
                    # Enable double buffer memory
                    pygame.DOUBLEBUF
                    if self.__configuration.window.doublebuf
                    else 0
                )
                | (
                    # Enable window scaling
                    pygame.SCALED
                    if self.__configuration.window.scaled
                    else 0
                )
                | (
                    # Force the window to be shown immediately
                    pygame.SHOWN
                    if self.__configuration.window.shown
                    else 0
                )
                | (
                    # Start the window in hidden mode
                    pygame.HIDDEN
                    if self.__configuration.window.hidden
                    else 0
                )
            ),
        )

    def __draw_map(self) -> None:
        # Fetch camera rect
        camera_rect = self.__camera.get_camera_rect()
        # Fetch the tilemap
        tilemap: TileMap = self.__map_builder.get_tilemap()
        # Iterate over the layers of the tilemap
        for layer in tilemap.layers:
            # Check if the layer is visible
            if layer.visible:
                # Iterate over the rows of the layer
                for row in range(layer.height):
                    # Iterate over the columns of the layer
                    for col in range(layer.width):
                        # Get the tile id
                        tile_id: int = layer.data[row * layer.width + col]
                        # Check if the tile id is greater than 0
                        if tile_id > 0:  # Ignore les cases vides
                            tile_image: pygame.Surface = self.__map_builder.get_tile(
                                tile_id  # Get the tile image related to the tile id
                            )
                            tile_x: int = (
                                # Get the x position of the tile
                                col
                                * tilemap.tilewidth
                            )
                            tile_y: int = (
                                # Get the y position of the tile
                                row
                                * tilemap.tileheight
                            )
                            tile_rect = pygame.Rect(tile_x, tile_y, tilemap.tilewidth, tilemap.tileheight)
                            # Check if the tile is in the camera
                            if camera_rect.colliderect(tile_rect):
                                # Adjust the tile position to the camera
                                adjusted_rect: pygame.Rect = tile_rect.move(-1 * camera_rect.x, -1 * camera_rect.y)
                                # Draw the tile on the screen
                                self.__window.blit(tile_image, adjusted_rect)
    
    def run(self) -> None:
        # Game loop
        while self.__launched:
            # Fill screen with default color
            self.__window.fill(self.__configuration.window.default_color)
            # Listen events
            self.__handler.handle(pygame.event.get())
            # Listen keys events
            self.__keys_handler.handle(pygame.key.get_pressed())
            # Update camera position
            self.__camera.update_camera_rect()
            # Draw map
            self.__draw_map()
            # Get player attributes
            player_size: Tuple[int, int] = self.__player.get_shape()
            player_image: pygame.Surface = self.__player.get_current_frame()
            # Resize the image if needed to match the player's shape
            resized_image: pygame.Surface = pygame.transform.scale(
                player_image, player_size
            )
            # Draw the resized image on the screen at the player's adjusted position
            self.__window.blit(resized_image, (
                self.__player.get_character_rect().x - self.__camera.get_camera_rect().x,
                self.__player.get_character_rect().y - self.__camera.get_camera_rect().y
            ))
            # Window framerate regulation
            self.__clock.tick(self.__configuration.framerate)
            # Update window
            pygame.display.flip()
        # Quit game
        pygame.quit()
