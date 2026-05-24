# TODO: (MEDIUM) Use SQLAlchemy instead

"""Mariadb CRUD Operations"""

from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from app.errors import Missing, Duplicate
from .tables import Siswa
from . import init

init.get_db()

init.Base.metadata.create_all(init.engine)
Session = sessionmaker(bind=init.engine)
session = Session()

def row_to_model(row: tuple) -> Siswa:
    user_id, nama, jenis_kelamin, tanggal_lahir, alamat, wali_id, kelas_id = row
    return Siswa(
        user_id=user_id, 
        nama=nama, 
        jenis_kelamin=jenis_kelamin, 
        tanggal_lahir=tanggal_lahir, 
        alamat=alamat, 
        wali_id=wali_id, 
        kelas_id=kelas_id
    )

def model_to_dict(siswa: Siswa) -> dict:
    return siswa.model_dump()

def get_all() -> list[Siswa]:
    qry = "SELECT * FROM siswa"
    init.curs.execute(qry)
    init.conn.commit()
    rows = list(init.curs.fetchall())
    return [row_to_model(row) for row in rows]

'''
def get_one(user_id: int) -> Siswa:
    qry = "SELECT * FROM siswa WHERE id = id"
    params = {"id": user_id}
    init.curs.execute(qry, params)
    init.conn.commit()
    row = init.curs.fetchone()
    if row:
        return row_to_model(row)
    else:
        raise Missing(msg=f"Siswa {user_id} not found")
'''
def get_one(id: int):
    siswa = session.query(Siswa).filter_by(id=id).first()
    print(siswa)

'''
def create(siswa: Siswa) -> Siswa:
    qry = """
        INSERT INTO siswa (user_id, name, attendance, note)
        values (:user_id, :name, :attendance, :note)
    """
    params = model_to_dict(siswa)
    try:
        init.curs.execute(qry, params)
        init.conn.commit()
    except mariadb.Error as e:
        # raise Duplicate(msg=f"Siswa {siswa.user_id} already exists")
        print(f"Mariadb Error: {e}")
    return get_one(siswa.user_id)
'''

def create(siswa: Siswa) -> Siswa:
    new_siswa = Siswa(
        id=siswa.id,
        nama=siswa.nama,
        jenis_kelamin=siswa.jenis_kelamin,
        tanggal_lahir=siswa.tanggal_lahir,
        alamat=siswa.alamat,
        wali_id=siswa.wali_id,
        kelas_id=siswa.kelas_id
    )
    session.add(new_siswa)
    session.commit()
    return get_one(siswa.id)

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

session.close()
