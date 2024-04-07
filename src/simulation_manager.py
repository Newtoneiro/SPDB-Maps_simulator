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
        self._nodes = self._dbm.fetch_nodes()
        self._paths = self._dbm.fetch_paths()

    def _init_user_interface(self) -> None:
        """
        Initializes the user interface.
        """
        self._ui = UserInterface()

    def _prerun(self) -> None:
        """
        Prepares the simulation for running.
        """
        self._ui.load_nodes(self._nodes)
        self._ui.load_paths(self._paths)

    # ================= Public methods ================= #

    def run(self) -> None:
        """
        Runs the simulation.
        """
        self._prerun()
        self._ui.run()
