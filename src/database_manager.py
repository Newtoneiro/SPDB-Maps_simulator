import MySQLdb
import os
from src.datamodels import Landmark, Coordinates


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

    def fetch_landmarks(self) -> list[Landmark]:
        """
        Fetches all landmarks from the database.
        """
        if not self._db:
            raise Exception("Database connection not initialized.")
        cursor = self._db.cursor()
        cursor.execute("SELECT * FROM LANDMARKS")
        return [Landmark(id, name, desc, Coordinates(x, y)) for id, name, desc, x, y in cursor.fetchall()]
