import MySQLdb
import os
from dotenv import load_dotenv, find_dotenv

TABLES_DIR = os.path.join(os.path.dirname(__file__), "tables")

if __name__ == "__main__":
    load_dotenv(find_dotenv())
    db = MySQLdb.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        passwd=os.environ.get("DB_PASSWORD"),
        db=os.environ.get("DB_NAME")
    )
    
    mycursor = db.cursor()

    # INIT STOPS
    with open(os.path.join(TABLES_DIR, "STOPS.sql"), "r") as f:
        mycursor.execute(f.read())
    print("STOPS INITIALIZED")

    # INIT BUS_ROUTES
    with open(os.path.join(TABLES_DIR, "BUS_ROUTES.sql"), "r") as f:
        mycursor.execute(f.read())
    print("BUS_ROUTES INITIALIZED")

    # INIT BUS_STOPS
    with open(os.path.join(TABLES_DIR, "BUS_ROUTES_STOPS.sql"), "r") as f:
        mycursor.execute(f.read())
    print("BUS_ROUTES_STOPS INITIALIZED")
    
    db.commit()
    db.close()
