import MySQLdb
import os
from common import DB_Manager

DATA_DIR = os.path.join(os.path.dirname(__file__), "data")


def fill_table(db: MySQLdb.Connection, table_fill_sql: str):
    """
    Fills a table in the database
    :param db: MySQLdb.Connection
    :param table_name: str
    :param columns: dict
    """
    table_path = os.path.join(DATA_DIR, f"{table_fill_sql}.sql")
    mycursor = db.cursor()
    with open(table_path, "r") as f:
        mycursor.execute(f.read())
    print(f"Table {table_fill_sql} filled.")
    mycursor.close()


if __name__ == "__main__":
    with DB_Manager() as db: 
        mycursor = db.cursor()

        fill_table(db, "BUS_ROUTES")
        fill_table(db, "BUS_STOPS")
        fill_table(db, "BUS_ROUTES_BUS_STOPS")

        db.commit()
