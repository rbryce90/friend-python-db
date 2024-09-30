import sqlite3
print('starting')

# creates db or conntet to it 
con = sqlite3.connect("tutorial.db")
# create cursor to do queries in db 
cur = con.cursor()

# create a table

cur.execute("""
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL
  )""")

# create a second table with keys referencing the first 


# CRUD

# Create
# Insert 1: 
cur.execute("""
    INSERT into users (first_name, last_name) values ("Danielle", "W")
""")

cur.execute("""
    INSERT into users (first_name, last_name) values ("Bryce", "Bond")
""")

con.commit()

# Read
res = cur.execute("""
    Select * from users
""")

print('before update: ', res.fetchall())

# Update
cur.execute("""
    Update users set last_name = 'yells' where first_name = 'Danielle'
    """)
con.commit()
res = cur.execute("""
    Select * from users
""")

print("After update: ", res.fetchall())

# Delete

cur.execute(""" 
    delete from users;
""")
con.commit()

print('The End')