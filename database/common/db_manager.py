import MySQLdb
import os
from dotenv import load_dotenv, find_dotenv

class DB_Manager:
    """
    Context manager for database connections
    """
    def __init__(self) -> None:
        load_dotenv(find_dotenv())

    def __enter__(self):
        self.db = MySQLdb.connect(
            host=os.environ.get("DB_HOST"),
            user=os.environ.get("DB_USER"),
            passwd=os.environ.get("DB_PASSWORD"),
            db=os.environ.get("DB_NAME")
        )
        return self.db
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.db.close()