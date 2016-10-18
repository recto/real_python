import sqlite3

with sqlite3.connect("new.db") as connection:
    c = connection.cursor()

    c.execute("""select distinct population.city, population.population,
            regions.region from population, regions
            where population.city = regions.city""")

    rows = c.fetchall()
    list(map(lambda row: print("City: {0}\nPopulation: {1}\nRegion: {2}".format(\
         row[0], row[1], row[2])) , rows)) 

