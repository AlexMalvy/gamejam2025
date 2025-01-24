import os
import sys
from typing import cast


class ResourceLocator:

    __base_path: str
    __resouce_dir: str

    def __init__(self, resouce_dir: str) -> None:

        self.__resouce_dir = resouce_dir

        if hasattr(sys, "_MEIPASS"):  # Designed for PyInstaller
            self.__base_path = cast(str, sys._MEIPASS)  # type: ignore
        else:
            self.__base_path = os.path.abspath(".")

    def fetch(self, name: str) -> str:
        return os.path.join(self.__base_path, self.__resouce_dir, name)
