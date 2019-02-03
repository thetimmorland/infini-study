from db import newDb, scheduler
from pathlib import Path
import os


if __name__ == '__main__':
    newDb(Path('boi.db'))
    scheduler(Path('boi.db'), 5)
