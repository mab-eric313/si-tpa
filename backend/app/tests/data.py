import pytest
from app.datas.data import Siswa
from app.errors import Missing, Duplicate
from app.datas import init, data

@pytest.fixture(autouse=True)
def use_memory_db():
    init.get_db(name=":memory:", reset=True)
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
    yield
    init.conn.close()
    init.conn = None

@pytest.fixture
def sample() -> Siswa:
    return Siswa(
        user_id=1,
        name="yeti",
        attendance="Hadir",
        note="Himalayas",
    )

def test_create(sample):
    resp = data.create(sample)
    assert resp == sample

def test_create_duplicate(sample):
    data.create(sample)
    with pytest.raises(Duplicate):
        data.create(sample)

def test_get_one(sample):
    data.create(sample)
    resp=data.get_one(sample.user_id)
    assert resp == sample

def test_one_missing():
    with pytest.raises(Missing):
        data.get_one(0)

def test_modify(sample):
    data.create(sample)
    sample.name = "Budi"
    resp = data.modify(1, sample)
    assert resp == sample

def test_modify_missing():
    thing: Siswa = Siswa(
        user_id=0,
        name="snurfle",
        attendance="Hadir",
        note=""
    )

    with pytest.raises(Missing):
        data.modify(0, thing)

def test_delete(sample):
    data.create(sample)
    resp = data.delete(1)
    assert resp is None

def test_delete_missing(sample):
    data.create(sample)
    with pytest.raises(Missing):
        data.delete(0)

