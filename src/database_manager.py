import MySQLdb
import os
from src.datamodels import BusStop, Coordinates


class DataBaseManager:
    """
    This class is responsible for managing the database.
    """
    def __init__(self):
        self._db = None

    def connect(self) -> None:
        """
        Initializes the connection to the database.
        """
        self._db = MySQLdb.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USER"),
            passwd=os.environ.get("DB_PASSWORD"),
            db=os.environ.get("DB_NAME")
        )

    def fetch_bus_stops(self) -> list[BusStop]:
        """
        Fetches all bus stops from the database.
        """
        if not self._db:
            raise Exception("Database connection not initialized.")
        cursor = self._db.cursor()
        cursor.execute("SELECT * FROM BUS_STOPS")
        return [BusStop(id, name, is_active, Coordinates(x, y)) for id, name, is_active, x, y in cursor.fetchall()]
