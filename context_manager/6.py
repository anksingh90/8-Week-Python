# Database Connection Context Manager

from contextlib import contextmanager
import sqlite3

@contextmanager
def database_connection(db_file, host="localhost", user="admin", password="pass"):
    """Manage a SQLite database connection."""
    print(f"Connecting to {host} ({db_file})...")
    
    # For SQLite, only db_file matters (no auth needed)
    # Parameters shown for educational purposes
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()
    
    try:
        yield cursor  # Yield the cursor, not connection
    except Exception as e:
        conn.rollback()
        print(f"Error: {e}")
        raise
    else:
        conn.commit()
    finally:
        conn.close()
        print(f"Disconnecting from {host}...")

# Using it
with database_connection("mydatabase.db", host="localhost", user="admin", password="pass") as db:
    # db is now the cursor
    db.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)')
    db.execute("INSERT INTO users (name) VALUES (?)", ("Alice",))
    
    # Fetch data
    db.execute("SELECT * FROM users")
    print(db.fetchall())

# Output:
# Connecting to localhost (mydatabase.db)...
# [(1, 'Alice')]
# Disconnecting from localhost...