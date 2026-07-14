# context manager sqlite3

import sqlite3

with sqlite3.connect("library.db") as myconn:
    cursor = myconn.cursor()

    cursor.execute("""
                CREATE TABLE IF NOT EXISTS books(
                   id INTEGER,
                    title TEXT
                   )
                   """)
    book_title = [
        (1, "The Pragmatic Programmer"),
        (2, "Clean Code"),
        (3, "Fluent Python")
    ]
    
    cursor.manyexecute(INSERT INTO )
