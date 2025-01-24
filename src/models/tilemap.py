from typing import Dict, List, Any
from dataclasses import dataclass


@dataclass(frozen=True)
class TileSet:
    firstgid: int
    source: str

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "TileSet":
        return TileSet(
            firstgid=data.get("firstgid", ""),
            source=data.get("source", ""),
        )


@dataclass(frozen=True)
class TileLayer:
    name: str
    data: List[int]
    width: int
    height: int
    id: int
    locked: bool
    opacity: float
    type: str
    visible: bool
    x: int
    y: int

    @staticmethod
    def from_dict(data: dict[str, Any]) -> "TileLayer":
        return TileLayer(
            name=data.get("name", ""),
            data=data.get("data", []),
            width=data.get("width", 0),
            height=data.get("height", 0),
            id=data.get("id", 0),
            locked=data.get("locked", False),
            opacity=data.get("opacity", 0.0),
            type=data.get("type", ""),
            visible=data.get("visible", False),
            x=data.get("x", 0),
            y=data.get("y", 0),
        )


@dataclass(frozen=True)
class TileMap:
    compressionlevel: int
    height: int
    infinite: bool
    layers: List[TileLayer]
    nextlayerid: int
    nextobjectid: int
    orientation: str
    renderorder: str
    tiledversion: str
    tileheight: int
    tilesets: List[TileSet]
    tilewidth: int
    type: str
    version: str
    width: int

    @staticmethod
    def from_dict(data: Dict[str, Any]) -> "TileMap":
        return TileMap(
            compressionlevel=data.get("compressionlevel", 0),
            height=data.get("height", 0),
            infinite=data.get("infinite", False),
            layers=[TileLayer.from_dict(layer) for layer in data.get("layers", [])],
            nextlayerid=data.get("nextlayerid", 0),
            nextobjectid=data.get("nextobjectid", 0),
            orientation=data.get("orientation", ""),
            renderorder=data.get("renderorder", ""),
            tiledversion=data.get("tiledversion", ""),
            tileheight=data.get("tileheight", 0),
            tilesets=[
                TileSet.from_dict(tileset) for tileset in data.get("tilesets", [])
            ],
            tilewidth=data.get("tilewidth", 0),
            type=data.get("type", ""),
            version=data.get("version", ""),
            width=data.get("width", 0),
        )
