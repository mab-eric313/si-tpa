```
$ grep -Rn "TODO:" . \
    --exclude-dir="node_modules" \
    --exclude-dir=".venv" \
    --exclude-dir=".git" \
    --exclude="TODO.md"
./backend/app/models.py:4:# TODO: (HIGH) Replace Column() with Mapped[] and mapped_column()
./backend/app/database.py:3:# TODO: (HIGH) Use asyncio
./backend/config.py:27:# TODO: (LOW) set PYTHONPATH inside pyproject.toml instead
```

- (HIGH) Use bootstrap for frontend
- (MEDIUM) Replace requirements.txt with pyproject.toml
- (MEDIUM) Use poetry
- (MEDIUM) use Alembic database migration
