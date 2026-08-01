import sqlite3


def create_database():

    connection = sqlite3.connect("campuscart.db")

    cursor = connection.cursor()


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT NOT NULL,

        email TEXT UNIQUE NOT NULL,

        password TEXT NOT NULL,

        college TEXT NOT NULL,

        year TEXT NOT NULL,

        branch TEXT NOT NULL

    )
    """)


    connection.commit()

    connection.close()



create_database()