import MySQLdb
import os
from common import DB_Manager

TABLES_DIR = os.path.join(os.path.dirname(__file__), "tables")


def init_table(db: MySQLdb.Connection, table_name: str):
    """
    Initializes a table in the database
    :param db: MySQLdb.Connection
    :param table_name: str
    :param columns: dict
    """
    table_path = os.path.join(TABLES_DIR, f"{table_name}.sql")
    mycursor = db.cursor()
    with open(table_path, "r") as f:
        mycursor.execute(f.read())
    print(f"Table {table_name} initialized.")
    mycursor.close()


if __name__ == "__main__":
    with DB_Manager() as db:
        mycursor = db.cursor()

        init_table(db, "BUS_ROUTES")
        init_table(db, "BUS_STOPS")
        init_table(db, "BUS_ROUTES_BUS_STOPS")

        db.commit()
