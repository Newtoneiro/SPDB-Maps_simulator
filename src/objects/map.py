"""An abstraction of canvas, on which the scene is drawn."""

import pygame
from src.constants import MAP_CONSTANTS, STATIC


class Map:
    """
    Class representing the map object.
    """

    # ============== INITIALIZATION =============== #

    def __init__(
        self,
        win: pygame.Surface,
        clock: pygame.time.Clock,
    ) -> None:
        self._win = win
        self._clock = clock

        self._init_surface()

    def _init_surface(self) -> None:
        """
        Initializes pygame surface.
        """
        self._surface = pygame.Surface(
            (MAP_CONSTANTS.MAP_WIDTH, MAP_CONSTANTS.MAP_HEIGHT)
        )

    # ============== PUBLIC METHODS =============== #

    def draw(self):
        """
        Draws the map.
        """
        img = pygame.image.load(STATIC.MAP_IMG)
        img = pygame.transform.scale(img, (MAP_CONSTANTS.MAP_WIDTH, MAP_CONSTANTS.MAP_HEIGHT))
        self._surface.blit(img, (0, 0))
        self._win.blit(self._surface, (0, 0))
