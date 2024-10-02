import sqlite3
import os

db_conn = sqlite3.connect(os.path.expanduser('~/.config/joplin-desktop/database.sqlite')) #connection_established :)
cursor = db_conn.cursor()

#cursor is a substance desinged to interact with DB just how you do it in console

# cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
# tables = cursor.fetchall()

# for t in tables:
#     print(t[0])

# cursor.execute('SELECT * from "folders"')
# folders = cursor.fetchall()
# 
# for f in folders:
    # print(f)
poems_folder = "c659769b0ccf4a6cafa677081237780d"
cursor.execute(f'SELECT * from notes WHERE parent_id = "{poems_folder}";')
# cursor.execute(f'PRAGMA table_info("notes");')
poems = cursor.fetchall()

print(poems)