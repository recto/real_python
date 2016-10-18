import sqlite3
import random

with sqlite3.connect("newnum.db") as connection:
    c = connection.cursor()
    c.execute("drop table if exists numbers")
    c.execute("create table numbers(num int)")

    for i in range(100):
        c.execute("insert into numbers values(?)", (random.randint(0, 100), ))

