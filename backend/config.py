import os
from pathlib import Path

# TODO: (LOW) set PYTHONPATH inside pyproject.toml instead
os.environ["PYTHONPATH"] = str(Path(__file__).resolve().parents[0])
