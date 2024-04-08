"""An abstraction of canvas, on which the scene is drawn."""

import pygame
from src.constants import MAP_CONSTANTS, STATIC, COLORS, PYGAME_CONSTANTS
from src.datamodels import Node, Path


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

        self._init_pygame()
        self._init_surface()
        self._init_map()

    def _init_pygame(self) -> None:
        """
        Initializes pygame stuff.
        """
        self._default_label_font = pygame.font.Font(
            None, PYGAME_CONSTANTS.DEFAULT_FONT_SIZE
        )

    def _init_surface(self) -> None:
        """
        Initializes pygame surface.
        """
        self._surface = pygame.Surface(
            (MAP_CONSTANTS.MAP_WIDTH, MAP_CONSTANTS.MAP_HEIGHT)
        )

    def _init_map(self) -> None:
        """
        Initializes the map.
        """
        self._map = pygame.image.load(STATIC.MAP_IMG)
        self._map = pygame.transform.scale(
            self._map, (MAP_CONSTANTS.MAP_WIDTH, MAP_CONSTANTS.MAP_HEIGHT)
        )
        self._map_rect = self._map.get_rect(center=self._surface.get_rect().center)
        self._blitmap()

    def _blitmap(self) -> None:
        """
        Blits the map onto the surface.
        """
        scaled_map = pygame.transform.scale(self._map, self._map_rect.size)
        self._surface.fill(color=COLORS.BACKGROUND_COLOR)
        self._surface.blit(scaled_map, self._map_rect)

    def _draw_node_point(self, node: Node, color) -> None:
        """
        Draws a node on the map.
        """
        pygame.draw.circle(
            self._map,
            COLORS.BLACK,
            (node.coordinates.x, node.coordinates.y),
            MAP_CONSTANTS.NODE_SIZE + MAP_CONSTANTS.NODE_BORDER_SIZE,
        )
        pygame.draw.circle(
            self._map,
            color,
            (node.coordinates.x, node.coordinates.y),
            MAP_CONSTANTS.NODE_SIZE,
        )

    def _draw_node_label(self, node: Node) -> None:
        """
        Draws a label for a node on the map.
        """
        label_surface = self._default_label_font.render(node.name, True, COLORS.BLACK)
        label_rect = label_surface.get_rect(
            center=(
                node.coordinates.x + MAP_CONSTANTS.NODE_SIZE,
                node.coordinates.y - MAP_CONSTANTS.NODE_SIZE,
            )
        )
        label_rect.x -= MAP_CONSTANTS.NODE_SIZE
        label_rect.y -= MAP_CONSTANTS.NODE_SIZE + MAP_CONSTANTS.NODE_BORDER_SIZE
        pygame.draw.rect(self._map, COLORS.WHITE, label_rect)
        self._map.blit(label_surface, label_rect)

    def _draw_path(self, path: Path, color) -> None:
        """
        Draws a path on the map.
        """
        pygame.draw.line(
            self._map,
            COLORS.BLACK,
            (path.from_node.coordinates.x, path.from_node.coordinates.y),
            (path.to_node.coordinates.x, path.to_node.coordinates.y),
            MAP_CONSTANTS.PATH_WIDTH + MAP_CONSTANTS.PATH_BORDER_SIZE,
        )
        pygame.draw.line(
            self._map,
            color,
            (path.from_node.coordinates.x, path.from_node.coordinates.y),
            (path.to_node.coordinates.x, path.to_node.coordinates.y),
            MAP_CONSTANTS.PATH_WIDTH,
        )

    def _draw_path_label(self, path: Path) -> None:
        """
        Draws a label for a path on the map.
        """
        label_surface = self._default_label_font.render(
            f"D {str(path.distance)}, T {str(path.travel_time)}", True, COLORS.BLACK
        )
        label_rect = label_surface.get_rect(
            center=(
                (path.from_node.coordinates.x + path.to_node.coordinates.x) / 2,
                (path.from_node.coordinates.y + path.to_node.coordinates.y) / 2
                + MAP_CONSTANTS.PATH_LABEL_Y_OFFSET,
            )
        )
        label_rect.x -= MAP_CONSTANTS.NODE_SIZE
        label_rect.y -= MAP_CONSTANTS.NODE_SIZE
        pygame.draw.rect(self._map, COLORS.WHITE, label_rect)
        self._map.blit(label_surface, label_rect)

    # ============== PUBLIC METHODS =============== #

    def zoom(self, zoom: float) -> None:
        """
        Zooms the map.
        :param pos: position of the mouse.
        :param zoom: zoom factor.
        """
        new_width = min(
            max(
                MAP_CONSTANTS.MAP_WIDTH * MAP_CONSTANTS.MIN_ZOOM,
                int(self._map_rect.width * zoom),
            ),
            MAP_CONSTANTS.MAP_WIDTH * MAP_CONSTANTS.MAX_ZOOM,
        )
        new_height = min(
            max(
                MAP_CONSTANTS.MAP_HEIGHT * MAP_CONSTANTS.MIN_ZOOM,
                int(self._map_rect.height * zoom),
            ),
            MAP_CONSTANTS.MAP_HEIGHT * MAP_CONSTANTS.MAX_ZOOM,
        )

        # Calculate the difference between the old and new width and height
        width_diff = new_width - self._map_rect.width
        height_diff = new_height - self._map_rect.height

        # Adjust the map rectangle to maintain the zoom towards the center
        self._map_rect.width = new_width
        self._map_rect.height = new_height
        self._map_rect.center = (
            self._map_rect.centerx - width_diff / 2,
            self._map_rect.centery - height_diff / 2,
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

    def draw_nodes(self, nodes: list[Node]) -> None:
        """
        Draws nodes on the map.
        :param nodes: list of nodes.
        """
        for node in nodes:
            self._draw_node_point(node, color=COLORS.RED)
            self._draw_node_label(node)

    def draw_selected_nodes(self, nodes: list[Node]) -> None:
        """
        Draws selected nodes on the map.
        :param nodes: list of selected nodes.
        """
        for node in nodes:
            self._draw_node_point(node, color=COLORS.GREEN)
        # first node as blue
        if len(nodes) > 0:
            self._draw_node_point(nodes[0], color=COLORS.ANGRY_YELLOW)

    def draw_paths(self, paths: list[Path]) -> None:
        """
        Draws paths on the map.
        :param paths: list of paths.
        """
        for path in paths:
            self._draw_path(path, color=COLORS.BLUE)
            self._draw_path_label(path)

    def draw_selected_paths_from_nodes(self, nodes: list[Node]) -> None:
        """
        Draws paths from selected nodes on the map.
        :param nodes: list of selected nodes.
        """
        for idx in range(len(nodes) - 1):
            path = Path(-1, nodes[idx], nodes[idx + 1], 0, 0)
            self._draw_path(path, color=COLORS.GREEN)

    def get_coordinates(self, x: int, y: int) -> tuple:
        """
        Returns the coordinates of the map.
        :param x: x-coordinate.
        :param y: y-coordinate.
        """
        return (
            (x - self._map_rect.left)
            / (self._map_rect.width / MAP_CONSTANTS.MAP_WIDTH),
            (y - self._map_rect.top)
            / (self._map_rect.height / MAP_CONSTANTS.MAP_HEIGHT),
        )

    def draw(self):
        """
        Draws the map.
        """
        self._blitmap()
        self._win.blit(self._surface, (0, 0))
