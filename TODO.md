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
