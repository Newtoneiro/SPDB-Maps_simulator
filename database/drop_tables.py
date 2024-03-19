import MySQLdb
import os
from dotenv import load_dotenv, find_dotenv


if __name__ == "__main__":
    load_dotenv(find_dotenv())
    db = MySQLdb.connect(
        host=os.environ.get("DB_HOST"),
        user=os.environ.get("DB_USER"),
        passwd=os.environ.get("DB_PASSWORD"),
        db=os.environ.get("DB_NAME")
    )
    
    mycursor = db.cursor()

    # DROP ALL TABLES
    mycursor.execute(f"DROP TABLE BUS_ROUTES_STOPS;")
    mycursor.execute(f"DROP TABLE BUS_ROUTES;")
    mycursor.execute(f"DROP TABLE STOPS;")
    
    db.commit()
    db.close()
