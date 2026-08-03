import sqlite3


connection = sqlite3.connect("campuscart.db")

cursor = connection.cursor()



# Users Table

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    name TEXT NOT NULL,

    email TEXT UNIQUE NOT NULL,

    password TEXT NOT NULL,

    phone TEXT NOT NULL,

    college TEXT NOT NULL,

    year TEXT NOT NULL,

    branch TEXT NOT NULL

)
""")



# Products Table

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER NOT NULL,

    name TEXT NOT NULL,

    category TEXT NOT NULL,

    price INTEGER NOT NULL,

    description TEXT NOT NULL,

    condition TEXT NOT NULL,

    image TEXT,

    FOREIGN KEY(user_id) REFERENCES users(id)

)
""")



connection.commit()

connection.close()


print("Database created successfully!")