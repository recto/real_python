import csv
import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    employees = csv.reader(open("employees.csv", "rU"))
    c.execute("create table employees(firstname text, lastname text)")
    c.executemany("insert into employees(firstname, lastname) \
            values(?, ?)", employees)

