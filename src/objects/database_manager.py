import MySQLdb
import os
from src.datamodels import Node, Coordinates, Path


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
            db=os.environ.get("DB_NAME"),
        )

    def fetch_nodes(self) -> list[Node]:
        """
        Fetches all nodes from the database.
        """
        if not self._db:
            raise Exception("Database connection not initialized.")
        cursor = self._db.cursor()
        cursor.execute("SELECT * FROM NODES")
        return [
            Node(id, name, Coordinates(x, y)) for id, name, x, y in cursor.fetchall()
        ]

    def fetch_paths(self) -> list[Path]:
        """
        Fetches all paths from the database.
        """
        if not self._db:
            raise Exception("Database connection not initialized.")

        # Fetch nodes from the database
        nodes = self.fetch_nodes()

        cursor = self._db.cursor()
        cursor.execute(
            "SELECT id, from_node_id, to_node_id, distance, travel_time FROM PATHS"
        )

        paths = []
        for path_data in cursor.fetchall():
            # Find corresponding nodes
            from_node_id, to_node_id = path_data[1], path_data[2]
            from_node = next(node for node in nodes if node.id == from_node_id)
            to_node = next(node for node in nodes if node.id == to_node_id)

            # Create Path object and append to paths list
            path = Path(path_data[0], from_node, to_node, path_data[3], path_data[4])
            paths.append(path)

        return paths
