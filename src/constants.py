"""
Constants defined for other files.
"""

import os


class PYGAME_CONSTANTS:
    """
    Constants for pygame config.
    """

    WIDTH: int = 1920
    HEIGHT: int = 1080
    FPS: int = 120
    WINDOW_TITLE: str = "map simulation"
    DEFAULT_FONT_SIZE: int = 30

    NODE_CLICK_RANGE: int = 12


class MAP_CONSTANTS:
    """
    Constants for map.
    """

    MAP_WIDTH: int = 1920
    MAP_HEIGHT: int = 1080

    MAX_ZOOM: float = 3.0
    MIN_ZOOM: float = 0.5

    NODE_BORDER_SIZE: int = 3
    NODE_SIZE: int = 12

    PATH_BORDER_SIZE: int = 3
    PATH_WIDTH: int = 4
    PATH_LABEL_Y_OFFSET: int = 10


class COLORS:
    """
    Colors.
    """

    BLACK: tuple = 20, 52, 62
    WHITE: tuple = 249, 247, 243
    RED: tuple = 239, 71, 111
    YELLOW: tuple = 255, 209, 102
    GREEN: tuple = 6, 214, 160
    BLUE: tuple = 0, 126, 167
    ANGRY_YELLOW: tuple = 255, 255, 0

    BACKGROUND_COLOR: tuple = BLACK


class STATIC:
    """
    Static constants.
    """

    STATIC_DIR: str = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static")
    MAP_IMG: str = os.path.join(STATIC_DIR, "map_image.jpg")
