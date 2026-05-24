```
$ grep -Rn "TODO:" . \
    --exclude-dir="node_modules" \
    --exclude-dir=".venv" \
    --exclude-dir=".git" \
    --exclude="TODO.md"
./backend/app/service.py:19:# TODO: (MEDIUM) replace query currently is not available
./backend/app/datas/data.py:1:# TODO: (MEDIUM) Use SQLAlchemy instead
./backend/app/datas/data.py:12:# TODO: (MEDIUM) make attendances tuple ("Hadir", "Izin", "Sakit", "Alpha")
./backend/app/datas/data.py:88:# TODO: (MEDIUM) make query for replace()
./backend/app/models.py:1:# TODO: (LOW) Is models module needed? Currently this module is not used.
./backend/app/web.py:28:# TODO: (MEDIUM) replace query currently is not available
./backend/config.py:4:# TODO: (LOW) set PYTHONPATH inside pyproject.toml instead
```

- Use bootstrap for frontend

# Important: The code is broken and need to refactor
# Priority: HIGH, Big refactoring
`backend/app/models/`:
- `init.py` -> should have engine and session factory
- `tables.py` -> should have SQLAlchemy models and Pydantic schemas
- `data.py` -> should have CRUD operations

1. `backend/app/models/init.py`
    - Remove `conn`, `curs`, and `mariadb` import
    - Rename `get_db()` to `init_db()` or `setup_engine()`
    - Move session factory here

2. `backend/app/models/data.py`
    - Remove all raw SQL.
    - move session into `init.py`
    - `get_one()` should have return `siswa`
    - import `session` from `init.py`
    - remove `session.close()` in end of file and use context manager or dependency 
      injection FastAPI

3. `backend/app/models/tables.py`
    - Split `SiswaBaseResponse` into `SiswaCreate`, `SiswaUpdate`, `SiswaResponse`
