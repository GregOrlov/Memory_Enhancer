import sqlite3
import os
import psycopg2
import sys
project_dir = os.path.expanduser("~/DoingAfterFailure/projects/memory_bot")
sys.path.append(project_dir)
from config import DB_HOST, DB_NAME, DB_PASSWORD, DB_USER, DB_PORT



sqlite3_conn = sqlite3.connect((os.path.expanduser('~/.config/joplin-desktop/database.sqlite')))
pg_conn = psycopg2.connect(host = DB_HOST, dbname = DB_NAME, user = DB_USER, password = DB_PASSWORD)

sqlite_cursor = sqlite3_conn.cursor()
pg_cursor = pg_conn.cursor()

poems_folder = "c659769b0ccf4a6cafa677081237780d"
sqlite_cursor.execute(f'SELECT title, body FROM notes WHERE parent_id = "{poems_folder}"')
poems = sqlite_cursor.fetchall()

insert_query = 'INSERT INTO Poems (title, body) VALUES(%s, %s);'
for poem in poems:
    pg_cursor.execute(insert_query, poem)

pg_conn.commit()
sqlite3_conn.close()
pg_conn.close()
