from dataclasses import dataclass
from typing import Any, Tuple, List


@dataclass(frozen=True)
class MapConfiguration:
    collisionables_layers: List[str]
    map_json_filename: str
    textures_filename: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "MapConfiguration":
        return MapConfiguration(
            collisionables_layers=data.get("collisionables_layers", []),
            map_json_filename=data.get("map_json_filename", ""),
            textures_filename=data.get("textures_filename", "")
        )


@dataclass(frozen=True)
class SpritesConfiguration:
    file_name: str
    mitigation_rate: float

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "SpritesConfiguration":
        return SpritesConfiguration(
            file_name=data.get("file_name", ""),
            mitigation_rate=data.get("mitigation_rate", 0.0),
        )


@dataclass(frozen=True)
class PlayerConfiguration:
    health: int
    height: int
    width: int
    sprites: SpritesConfiguration
    velocity: int

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "PlayerConfiguration":
        return PlayerConfiguration(
            health=data.get("health", 0),
            height=data.get("height", 0),
            width=data.get("width", 0),
            sprites=SpritesConfiguration.from_dict(data.get("sprites", {})),
            velocity=data.get("velocity", 0),
        )


@dataclass(frozen=True)
class WindowConfiguration:
    caption: str
    default_color: Tuple[int, int, int]
    doublebuf: bool
    fullscreen: bool
    height: int
    width: int
    hidden: bool
    hwsurface: bool
    noframe: bool
    opengl: bool
    resizable: bool
    scaled: bool
    shown: bool

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "WindowConfiguration":
        # Unpacking conversion
        return WindowConfiguration(
            caption=data.get("caption", ""),
            default_color=data.get("default_color", (0, 0, 0)),
            doublebuf=data.get("doublebuf", False),
            fullscreen=data.get("fullscreen", False),
            height=data.get("height", 0),
            hidden=data.get("hidden", False),
            hwsurface=data.get("hwsurface", False),
            width=data.get("width", 0),
            noframe=data.get("noframe", False),
            opengl=data.get("opengl", False),
            resizable=data.get("resizable", False),
            scaled=data.get("scaled", False),
            shown=data.get("shown", False),
        )


@dataclass(frozen=True)
class Configuration:
    framerate: int
    map: MapConfiguration
    player: PlayerConfiguration
    window: WindowConfiguration

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "Configuration":
        return Configuration(
            framerate=data.get("framerate", 0),
            map=MapConfiguration.from_dict(data.get("map", {})),
            player=PlayerConfiguration.from_dict(data.get("player", {})),
            window=WindowConfiguration.from_dict(data.get("window", {})),
        )
