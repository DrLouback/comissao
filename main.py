import sqlite3
from pathlib import Path

ROOT_DIR = Path('__file__').parent
DB_NAME = 'db.sqlite3'
DB_FILE = ROOT_DIR

connection = sqlite3.connect(DB_FILE)
cursor = connection.cursor()

#sql
cursor.execute(
    'Create table '

)





cursor.close()
connection.close()