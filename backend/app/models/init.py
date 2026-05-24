"""Initialize Mariadb database"""

from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import declarative_base
from mariadb import connect, Connection, Cursor, Error
from config import DB_NAME, DB_HOST, DB_PORT, DB_USER, DB_PASSWORD

conn: Connection | None = None
curs: Cursor | None = None
engine: Engine | None = None

DB_URL = f"mariadb+mariadbconnector://" \
         f"{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
Base = declarative_base()

def create_db():
    tmp_conn = None
    try:
        tmp_conn = connect(
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=int(DB_PORT),
        )
        tmp_curs = tmp_conn.cursor()

        print(f"Creating database with name {DB_NAME}")
        tmp_curs.execute(f"CREATE DATABASE IF NOT EXISTS `{DB_NAME}`")
        tmp_conn.commit()
        print("Database successfully created")

    except Error as e:
        print(f"create_db() Mariadb Error: {e}")
        raise

    finally:
        if tmp_conn:
            tmp_conn.close()


def get_db(DB_URL: str = DB_URL, db_reset: bool = False):
    """Connect to SQLite database file"""
    global conn, curs, engine
    if conn:
        if not db_reset:
            return
        conn = None

    try:
        engine = create_engine(DB_URL)

    except Exception as e:
        print(f"Mariadb Error: {e}")
        if "Unknown database" in str(e):
            create_db()
            conn = connect(
                user=DB_USER,
                password=DB_PASSWORD,
                host=DB_HOST,
                port=int(DB_PORT),
                database=DB_NAME
            )
            curs = conn.cursor()
        else:
            raise
