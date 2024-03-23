import MySQLdb
from common import DB_Manager


def drop_table(db: MySQLdb.Connection, table_name: str):
    """
    Drops a table from the database
    :param db: MySQLdb.Connection
    :param table_name: str
    """
    mycursor = db.cursor()
    mycursor.execute(f"DROP TABLE {table_name}")
    print(f"Table {table_name} dropped.")
    mycursor.close()


if __name__ == "__main__":
    with DB_Manager() as db: 
        mycursor = db.cursor()

        # DROP ALL TABLES
        drop_table(db, "BUS_ROUTES_BUS_STOPS")
        drop_table(db, "BUS_ROUTES")
        drop_table(db, "BUS_STOPS")

        db.commit()
