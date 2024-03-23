from src.database_manager import DataBaseManager
from src.user_interface import UserInterface


class SimulationManager:
    def __init__(self):
        self._init_database()
        self._init_user_interface()

    def _init_database(self) -> None:
        """
        Initializes the database.
        """
        self._dbm = DataBaseManager()
        self._dbm.connect()

    def _init_user_interface(self) -> None:
        """
        Initializes the user interface.
        """
        self._ui = UserInterface()

    def run(self) -> None:
        """
        Runs the simulation.
        """
        self._ui.load_landmarks(self._dbm.fetch_landmarks())
        self._ui.run()