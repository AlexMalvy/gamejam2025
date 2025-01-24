from ..models.configuration import Configuration
from ..models.tilemap import TileMap
from .resource_locator import ResourceLocator
from pygame.surface import Surface
from typing import Dict, List
import pygame
import json
from json import JSONDecodeError


class MapBuilder:
    __textures_file_img: Surface
    __tilemap: TileMap
    __tiles: Dict[int, Surface]  # Get subsurface from texture file
    __collisionables_layers: List[str]

    def __init__(
            self, 
            resource_locator: ResourceLocator, 
            configuration: Configuration
        ) -> None:
        # Player
        # Register image
        self.__textures_file_img = pygame.image.load(resource_locator.fetch(configuration.map.textures_filename))
        # Read JSON file
        try:
            with open(resource_locator.fetch(configuration.map.map_json_filename), "r") as f:
                data = json.load(f)
            # Create a TileMap configuration object from the JSON data
            self.__tilemap = TileMap.from_dict(data)
        except (FileNotFoundError, JSONDecodeError) as e:
            raise ValueError(f"Cannot load JSON file : {e}")
        # Init a tiles container
        self.__tiles: Dict[int, Surface] = {}
        # Fetch first tile id
        tile_id: int = self.__tilemap.tilesets[0].firstgid
        # Get the height and width of one tile
        tile_height: int = self.__tilemap.tileheight
        tile_width: int = self.__tilemap.tilewidth
        # Ensure that the tile has a positive height and width
        if tile_width <= 0 or tile_height <= 0:
            raise ValueError("Tile width and height of one tile must be positive.")
        # Get the height and width of the texture file
        texture_height: int = self.__textures_file_img.get_height()
        texture_width: int = self.__textures_file_img.get_width()
        # Iterate over the texture file to get the tiles
        for row_offset in range(
            texture_height // tile_height  # Get the number of rows
        ):
            for col_offset in range(
                texture_width // tile_width  # Get the number of columns
            ):
                # Generate a rect object with the position and size of the tile
                rect = pygame.Rect(
                    tile_width * col_offset,  # Get the x position of the tile
                    tile_height * row_offset,  # Get the y position of the tile
                    tile_width,  # Width of the tile
                    tile_height,  # Height of the tile
                )
                # Add the tile to the tiles dictionary
                self.__tiles[tile_id] = self.__textures_file_img.subsurface(rect)
                # Increment the tile
                tile_id += 1
        # Get the collisionable layers
        self.__collisionables_layers = [layer.name for layer in self.__tilemap.layers if layer.name in configuration.map.collisionables_layers]

    def get_tilemap(self) -> TileMap:
        return self.__tilemap
    
    def get_collisionables_layers(self) -> List[str]:
        return self.__collisionables_layers

    def get_tile(self, tile_id: int) -> Surface:
        if tile_id not in self.__tiles:
            raise KeyError(f"Tile with ID {tile_id} not found.")
        return self.__tiles[tile_id]
