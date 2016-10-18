#
# import sqlite3
# 
# conn = sqlite3.connect("new.db")
# cursor = conn.cursor()
# cursor.execute("insert into population values('New York City', \
#         'NY', 8200000)")
# cursor.execute("insert into population values('San Francisco', \
#         'CA', 800000)")
# conn.commit()
# conn.close()

import sqlite3
with sqlite3.connect("new.db") as connection:
    c = connection.cursor()
    c.execute("insert into population values('New York City', \
             'NY', 8200000)")
    c.execute("insert into population values('San Francisco', \
             'CA', 800000)")

