import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("""select population.city, population.population,
            regions.region from population, regions
            where population.city = regions.city""")

    rows = c.fetchall()
    list(map(lambda row: print("{0}, {1}, {2}".format(row[0], row[1], row[2])) , rows)) 

