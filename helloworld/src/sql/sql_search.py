import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("select firstname, lastname from employees")
    rows = c.fetchall()
   list(map(lambda row: print("{0}, {1}".format(row[0].strip(), row[1].strip())), rows))
#    print(*rows, sep="\n")

