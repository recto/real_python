import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    sql = {'average': 'select avg(population) from population',
           'maximum': 'select max(population) from population',
           'minimum': 'select min(population) from population',
           'sum': 'select sum(population) from population',
           'count': 'select count(population) from population'}

    for k, v in sql.items():
        c.execute(v)
        result = c.fetchone()
        print("{0}: {1}".format(k, result[0]))

