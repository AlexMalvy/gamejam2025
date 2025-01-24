from ..models.configuration import Configuration
from typing import cast
import json
import os
import sys


class ConfigurationBuilder:

    __base_path: str
    __config: Configuration

    def __init__(self) -> None:

        if hasattr(sys, "_MEIPASS"):  # Designed for PyInstaller
            self.__base_path = cast(str, sys._MEIPASS)  # type: ignore
        else:
            self.__base_path = os.path.abspath(".")

        file_path: str = os.path.join(self.__base_path, "config.json")
        with open(file_path, "r", encoding="utf-8") as f:
            self.__config = Configuration.from_dict(json.load(f))

    def get_configuration(self) -> Configuration:
        return self.__config
