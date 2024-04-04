import MySQLdb
import os
import functools
from dotenv import load_dotenv, find_dotenv


def log_output(f):
    """
    Decorator to log the execution of a function
    """
    @functools.wraps(f)
    def wrapper(*args, **kwargs):
        log_text = f"Executing function: {f.__name__} "
        try:
            result = f(*args, **kwargs)
            log_text += "✅\n"
        except Exception as e:
            log_text += f"❌\nError: {str(e)}\n"
        print(log_text)
        return result
    return wrapper


@log_output
def connect_to_db() -> MySQLdb.Connection:
    """
    Connects to the database and returns the connection object
    :return: MySQLdb.connections.Connection
    """
    db = MySQLdb.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        passwd=os.environ.get("DB_PASSWORD"),
        db=os.environ.get("DB_NAME")
    )
    return db


@log_output
def create_table(db: MySQLdb.Connection, table_name: str, columns: dict):
    """
    Creates a table in the database
    :param db: MySQLdb.Connection
    :param table_name: str
    :param columns: dict
    """
    mycursor = db.cursor()
    columns_str = ", ".join(
        [f"{key} {value}" for key, value in columns.items()]
    )
    mycursor.execute(f"CREATE TABLE {table_name} ({columns_str})")


@log_output
def insert_into_table(db: MySQLdb.Connection, table_name: str, values: dict):
    """
    Inserts a row into the table
    :param db: MySQLdb.Connection
    :param table_name: str
    :param values: dict
    """
    mycursor = db.cursor()
    columns_str = ", ".join(values.keys())
    values_str = ", ".join([f"'{value}'" for value in values.values()])
    mycursor.execute(
        f"INSERT INTO {table_name} ({columns_str}) VALUES ({values_str})"
    )


@log_output
def select_from_table(db: MySQLdb.Connection, table_name: str, columns: list):
    """
    Selects rows from the table
    :param db: MySQLdb.Connection
    :param table_name: str
    :param columns: list
    """
    mycursor = db.cursor()
    columns_str = ", ".join(columns)
    mycursor.execute(f"SELECT {columns_str} FROM {table_name}")
    return mycursor.fetchall()


@log_output
def drop_table(db: MySQLdb.Connection, table_name: str):
    """
    Drops a table from the database
    :param db: MySQLdb.Connection
    :param table_name: str
    """
    mycursor = db.cursor()
    mycursor.execute(f"DROP TABLE {table_name}")


@log_output
def close_connection(db: MySQLdb.Connection):
    """
    Closes the connection to the database
    :param db: MySQLdb.Connection
    """
    db.close()


if __name__ == "__main__":
    load_dotenv(find_dotenv())

    db = connect_to_db()

    TABLE_NAME = "person"
    COLUMNS = {"name": "VARCHAR(255)", "surname": "VARCHAR(255)"}
    TEST_VALUES = {"name": "John", "surname": "Doe"}

    create_table(db, TABLE_NAME, COLUMNS)
    insert_into_table(db, TABLE_NAME, TEST_VALUES)
    select_from_table(db, TABLE_NAME, list(TEST_VALUES.keys()))
    drop_table(db, TABLE_NAME)
    close_connection(db)
