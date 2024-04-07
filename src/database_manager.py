import MySQLdb
import os
from src.datamodels import Node, Coordinates


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

    def fetch_nodes(self) -> list[Node]:
        """
        Fetches all nodes from the database.
        """
        if not self._db:
            raise Exception("Database connection not initialized.")
        cursor = self._db.cursor()
        cursor.execute("SELECT * FROM NODES")
        return [Node(id, name, Coordinates(x, y)) for id, name, x, y in cursor.fetchall()]
