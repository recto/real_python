import sqlite3

with sqlite3.connect("new.db") as connection:
    cursor = connection.cursor()

    try:
        cursor.execute("insert into populations vaues('New York City', \
                'NY', 82000000)")
        cursor.execute("insert into populations vaues('San Francisco', \
                'CA', 800000)")
    except sqlite3.OperationalError:
        print("Opps! Something went wront. Try again...")

    connection.commit()
    connection.close()

