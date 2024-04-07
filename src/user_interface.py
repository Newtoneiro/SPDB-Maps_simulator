""" User interface module. """

import pygame
from src.objects import Map
from src.constants import PYGAME_CONSTANTS, COLORS, MAP_CONSTANTS
from src.datamodels import Node, Path


class UserInterface:
    """
    Class managing the simulations.
    """

    # ============== INITIALIZATION =============== #

    def __init__(
        self,
    ) -> None:
        self._run = True
        self._dragging = False

        self._init_pygame()
        self._init_map()

        self._selected_nodes = []

    def _init_pygame(self) -> None:
        """
        Initializes pygame.
        """
        pygame.init()
        pygame.display.set_caption(PYGAME_CONSTANTS.WINDOW_TITLE)
        self._win = pygame.display.set_mode(
            (PYGAME_CONSTANTS.WIDTH, PYGAME_CONSTANTS.HEIGHT)
        )
        self._clock = pygame.time.Clock()

    def _init_map(self) -> None:
        """
        Initializes the map.
        """
        self._map = Map(self._win, self._clock)

    # ============== PRIVATE METHODS =============== #

    def _draw_map(self) -> None:
        """
        Draws the map.
        """
        self._map.draw_paths(self._paths)
        self._map.draw_nodes(self._nodes)
        self._map.draw_selected_nodes(self._selected_nodes)
        self._map.draw()

    def _handle_events(self) -> None:
        """
        Handles all events.
        """
        for event in pygame.event.get():
            self._event_callbacks.get(event.type, lambda _: None)(event)

    def _init_event_callbacks(self) -> None:
        """
        Initializes pygame callbacks.
        """
        self._event_callbacks = {
            pygame.QUIT: lambda event: self._handle_stop(event),
            pygame.KEYDOWN: lambda event: self._handle_key_down(event),
            pygame.MOUSEWHEEL: lambda event: self._handle_scroll(event),
            pygame.MOUSEBUTTONDOWN: lambda event: self._handle_mouse_down(event),
            pygame.MOUSEBUTTONUP: lambda event: self._handle_mouse_up(event),
            pygame.MOUSEMOTION: lambda event: self._handle_mouse_motion(event),
        }

        self._key_callbacks = {
            pygame.K_v: self._handle_example,
        }

    def _handle_mouse_down(self, event: pygame.event.Event) -> None:
        """
        Handles mouse button down event.
        """
        if event.button == pygame.BUTTON_LEFT:
            # Store the initial mouse position when left mouse button is pressed
            self._dragging = True
            self._drag_start_pos = event.pos
            self._handle_node_click(event)

        if event.button == pygame.BUTTON_RIGHT:
            x, y = pygame.mouse.get_pos()
            print(self._map.get_coordinates(x, y))
            self._selected_nodes.clear()

    def _handle_node_click(self, event: pygame.event.Event) -> None:
        x, y = pygame.mouse.get_pos()
        clicked = self._map.get_coordinates(x, y)
        for node in self._nodes:
            if (
                node.coordinates.x - PYGAME_CONSTANTS.NODE_CLICK_RANGE
                <= clicked[0]
                <= node.coordinates.x + PYGAME_CONSTANTS.NODE_CLICK_RANGE
                and node.coordinates.y - PYGAME_CONSTANTS.NODE_CLICK_RANGE
                <= clicked[1]
                <= node.coordinates.y + PYGAME_CONSTANTS.NODE_CLICK_RANGE
            ):
                if node in self._selected_nodes:
                    self._selected_nodes.remove(node)
                    print("Deselected node", node.id)
                else:
                    self._selected_nodes.append(node)
                    print("Selected node", node.id)

    def _handle_mouse_up(self, event: pygame.event.Event) -> None:
        """
        Handles mouse button up event.
        """
        if event.button == pygame.BUTTON_LEFT:
            # Reset dragging state when left mouse button is released
            self._dragging = False

    def _handle_mouse_motion(self, event: pygame.event.Event) -> None:
        """
        Handles mouse motion event.
        """
        if self._dragging:
            # Calculate the change in mouse position
            dx = event.pos[0] - self._drag_start_pos[0]
            dy = event.pos[1] - self._drag_start_pos[1]

            # Move the map based on the change in mouse position
            self._map.move_pos(dx, dy)

            # Update the initial mouse position for the next drag operation
            self._drag_start_pos = event.pos

    def _handle_stop(self, _: pygame.event.Event) -> None:
        """
        Stops the simulation.
        """
        self._run = False

    def _handle_key_down(self, event: pygame.event.Event) -> None:
        """
        Handles key down event.
        """
        self._key_callbacks.get(event.key, lambda: None)()

    def _handle_scroll(self, event: pygame.event.Event) -> None:
        """
        Handles scroll event.
        """
        if not self._dragging:  # Zoom only if not dragging
            zoom_factor = 1 + event.y * 0.1
            self._map.zoom(zoom_factor)

    # ================== KEY CALLBACKS ================== #

    def _handle_example(self) -> None:
        """
        Handles show vectors event.
        """
        print("Example")

    # ================== PUBLIC METHODS ================== #

    def load_nodes(self, nodes: list[Node]) -> None:
        """
        Loads nodes onto the map.
        :param nodes: list of nodes.
        """
        self._nodes = nodes

    def load_paths(self, paths: list[Path]) -> None:
        """
        Loads paths onto the map.
        :param paths: list of paths.
        """
        self._paths = paths

    def run(self) -> None:
        """
        Runs the simulations.
        """
        self._init_event_callbacks()
        while self._run:
            self._clock.tick(PYGAME_CONSTANTS.FPS)
            self._draw_map()
            self._handle_events()
            pygame.display.flip()
