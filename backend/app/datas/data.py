# TODO: (MEDIUM) Use SQLAlchemy instead

"""SQLite CRUD Operations"""

from sqlite3 import IntegrityError
from pydantic import BaseModel
from . import init
from app.errors import Missing, Duplicate

init.get_db()

# TODO: (MEDIUM) make attendances tuple ("Hadir", "Izin", "Sakit", "Alpha")
class Siswa(BaseModel):
    user_id: int
    name: str
    attendance: str
    note: str


init.curs.execute(
    """
    CREATE TABLE IF NOT EXISTS siswa(
        user_id INTEGER PRIMARY KEY,
        name TEXT,
        attendance TEXT,
        note TEXT
    )
    """
)
init.conn.commit()

def row_to_model(row: tuple) -> Siswa:
    user_id, name, attendance, note = row
    return Siswa(user_id=user_id, name=name, attendance=attendance, note=note)

def model_to_dict(siswa: Siswa) -> dict:
    return siswa.model_dump()

def get_all() -> list[Siswa]:
    qry = "SELECT * FROM siswa"
    init.curs.execute(qry)
    init.conn.commit()
    rows = list(init.curs.fetchall())
    return [row_to_model(row) for row in rows]

def get_one(user_id: int) -> Siswa:
    qry = "SELECT * FROM siswa WHERE user_id=:user_id"
    params = {"user_id": user_id}
    init.curs.execute(qry, params)
    init.conn.commit()
    row = init.curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Siswa {user_id} not found")

def create(siswa: Siswa) -> Siswa:
    qry = """
        INSERT INTO siswa (user_id, name, attendance, note)
        values (:user_id, :name, :attendance, :note)
    """
    params = model_to_dict(siswa)
    try:
        init.curs.execute(qry, params)
        init.conn.commit()
    except IntegrityError:
        raise Duplicate(msg=f"Siswa {siswa.user_id} already exists")
    return get_one(siswa.user_id)

def modify(user_id: int, siswa: Siswa) -> Siswa | None:
    qry = """
        UPDATE siswa
        SET user_id=:user_id,
            name=:name,
            attendance=:attendance,
            note=:note
        WHERE user_id=:user_id_orig
    """
    params = model_to_dict(siswa)
    params["user_id_orig"] = siswa.user_id
    init.curs.execute(qry, params)
    init.conn.commit()
    if init.curs.rowcount == 1:
        return get_one(siswa.user_id)
    else:
        raise Missing(msg=f"Siswa {user_id} not found")

# TODO: (MEDIUM) make query for replace()
# def replace(siswa: Siswa):
#     return siswa

def delete(user_id: int) -> None:
    qry = "DELETE FROM siswa where user_id = :user_id"
    params = {"user_id": user_id}
    init.curs.execute(qry, params)
    init.conn.commit()
    if init.curs.rowcount != 1:
        raise Missing(msg=f"Siswa {user_id} not found")
    else:
        return None

