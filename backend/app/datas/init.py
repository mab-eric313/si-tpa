"""Initialize SQLite database"""

from pathlib import Path
from sqlite3 import connect, Connection, Cursor

conn: Connection | None = None
curs: Cursor = None

def get_db(db_name: str = "database.db", db_reset: bool = False):
    """Connect to SQLite database file"""
    global conn, curs
    if conn:
        if not db_reset:
            return
        conn = None

    if db_name == ":memory:":
        db_path = ":memory:"
    else:
        db_path = str(Path(__file__).resolve().parents[0] / db_name)

    conn = connect(db_path, check_same_thread=False)
    curs = conn.cursor()
