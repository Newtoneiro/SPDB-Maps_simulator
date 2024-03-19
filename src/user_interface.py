""" User interface module. """
import pygame
from src.objects import Map
from src.constants import PYGAME_CONSTANTS, COLORS


class UserInterface:
    """
    Class managing the simulations.
    """

    # ============== INITIALIZATION =============== #

    def __init__(
        self,
    ) -> None:
        self._run = True

        self._init_pygame()
        self._init_map()

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
        }

        self._key_callbacks = {
            pygame.K_v: self._handle_example,
        }

    # ================== EVENT HANDLERS ================== #

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

    # ================== KEY CALLBACKS ================== #

    def _handle_example(self) -> None:
        """
        Handles show vectors event.
        """
        print("Example")

    # ================== PUBLIC METHODS ================== #

    def run(self) -> None:
        """
        Runs the simulations.
        """
        self._init_event_callbacks()
        while self._run:
            self._clock.tick(PYGAME_CONSTANTS.FPS)
            self._win.fill(COLORS.BACKGROUND_COLOR)
            self._draw_map()
            self._handle_events()
            pygame.display.flip()