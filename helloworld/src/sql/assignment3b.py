import sqlite3

OPERATIONS = {1: "avg", 2: "max", 3: "min", 4:"sum"}

conn= sqlite3.connect("newnum.db")
cursor = conn.cursor()


prompt = """
Select the operation that you want to perform [1 - 4].
1. Average
2. Max
3. Min
4. Sum
Exit if something else is entered.
"""

while True:
    x = int(input(prompt))

    try:
        operation = OPERATIONS[x]
        cursor.execute("select {0}(num) from numbers".format(operation))
        result = cursor.fetchone()
        print("{0}: {1:f}".format(operation, result[0]))
    except KeyError:
        print("Exit")
        break
        
