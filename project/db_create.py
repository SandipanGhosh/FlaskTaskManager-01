# project/db_create.py

import sqlite3
from _config import DATABASE_PATH

with sqlite3.connect(DATABASE_PATH) as connection:
	cur = connection.cursor()

	cur.execute("""CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT,
		name TEXT NOT NULL,
		due_date TEXT NOT NULL,
		priority INTEGER NOT NULL,
		status INTEGER NOT NULL)""")

	cur.execute("""INSERT INTO tasks (name, due_date, priority, status) \
		VALUES ("Complete the tutorial", "01/26/2018", 10, 1)""")
	cur.execute("""INSERT INTO tasks (name, due_date, priority, status) \
		VALUES ("Complete the course", "01/31/2018", 10, 1)""")