import sqlite3
conn = sqlite3.connect('ColorCoordinator.db')

c= conn.cursor()


# c.execute("""CREATE TABLE users(
#     username text,
#     first_name text,
#     last_name text,
#     password text
#           )""")

conn.commit()

conn.close()

