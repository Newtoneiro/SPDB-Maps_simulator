"""An abstraction of canvas, on which the scene is drawn."""

import pygame
from src.constants import MAP_CONSTANTS, STATIC, COLORS


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
        self._init_map()

    def _init_map(self) -> None:
        """
        Initializes the map.
        """
        self._map = pygame.image.load(STATIC.MAP_IMG)
        self._map = pygame.transform.scale(self._map, (MAP_CONSTANTS.MAP_WIDTH, MAP_CONSTANTS.MAP_HEIGHT))
        self._map_rect = self._map.get_rect(center=self._surface.get_rect().center)
        self._blitmap()

    def _init_surface(self) -> None:
        """
        Initializes pygame surface.
        """
        self._surface = pygame.Surface(
            (MAP_CONSTANTS.MAP_WIDTH, MAP_CONSTANTS.MAP_HEIGHT)
        )

    def _blitmap(self) -> None:
        """
        Blits the map onto the surface.
        """
        scaled_map = pygame.transform.scale(self._map, self._map_rect.size)
        self._surface.fill(color=COLORS.BACKGROUND_COLOR)
        self._surface.blit(scaled_map, self._map_rect)

    # ============== PUBLIC METHODS =============== #
        
    def zoom(self, pos: tuple, zoom: float) -> None:
        """
        Zooms the map.
        :param pos: position of the mouse.
        :param zoom: zoom factor.
        """
        new_width = min(
            max(
                MAP_CONSTANTS.MAP_WIDTH * MAP_CONSTANTS.MIN_ZOOM,
                int(self._map_rect.width * zoom)
            ),
            MAP_CONSTANTS.MAP_WIDTH * MAP_CONSTANTS.MAX_ZOOM
        )
        new_height = min(
            max(
                MAP_CONSTANTS.MAP_HEIGHT * MAP_CONSTANTS.MIN_ZOOM,
                int(self._map_rect.height * zoom)
            ),
            MAP_CONSTANTS.MAP_HEIGHT * MAP_CONSTANTS.MAX_ZOOM
        )

        # Calculate the difference between the old and new width and height
        width_diff = new_width - self._map_rect.width
        height_diff = new_height - self._map_rect.height

        # Adjust the map rectangle to maintain the zoom towards the center
        self._map_rect.width = new_width
        self._map_rect.height = new_height
        self._map_rect.center = (
            self._map_rect.centerx - width_diff / 2,
            self._map_rect.centery - height_diff / 2
        )

        # Re-blit the map onto the surface
        self._blitmap()

    def move_pos(self, dx: int, dy: int) -> None:
        """
        Moves the center of the map to a new position.
        :param dx: Change in x-coordinate.
        :param dy: Change in y-coordinate.
        """
        # Move the center of the map by dx and dy
        self._map_rect.centerx += dx
        self._map_rect.centery += dy

        # Re-blit the map onto the surface
        self._blitmap()

    def draw_bus_stops(self, bus_stops: list) -> None:
        """
        Draws bus stops on the map.
        :param bus_stops: list of bus stops.
        """
        for bus_stop in bus_stops:
            pygame.draw.circle(
                self._map,
                COLORS.RED,
                (bus_stop.coordinates.x, bus_stop.coordinates.y),
                MAP_CONSTANTS.BUS_STOP_SIZE
            )

    def get_coordinates(self, x: int, y: int) -> tuple:
        """
        Returns the coordinates of the map.
        :param x: x-coordinate.
        :param y: y-coordinate.
        """
        return x - self._map_rect.left, y - self._map_rect.top

    def draw(self):
        """
        Draws the map.
        """
        self._blitmap()
        self._win.blit(self._surface, (0, 0))