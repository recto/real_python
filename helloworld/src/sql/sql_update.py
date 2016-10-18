import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("update population set population = 900000 where \
            city='New York City'")
    c.execute("delete from population where city='Boston'")
    print("\nNEW DATA:\n")
    c.execute("select * from population")
    rows = c.fetchall()
    list(map(lambda row : print("{0}, {1}, {2}".format(\
            row[0], row[1], row[2])), rows))
