import sqlite3

DB_NAME = "lib.db"

connection = sqlite3.connect(DB_NAME)
connection.row_factory = sqlite3.Row
cursor = connection.cursor()
