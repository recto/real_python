import sqlite3

conn = sqlite3.connect("new.db")
cursor = conn.cursor()
cursor.execute("""create table population (city text, state text, population int)""")
conn.close()

