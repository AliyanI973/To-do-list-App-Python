import sqlite3

conn = sqlite3.connect('database.db')



c = conn.cursor()


# c.execute("""CREATE TABLE customers (
#           first_name text,
#           last_name text,
#           email text
# ) """)
# NULL
# INTEGER
# REAL
# TEXT
# BLOB


# c.execute("INSERT INTO customers VALUES ('Jhon', 'Elder', 'jhon@codemy.com)")

many_customers = [
    ('West', 'Brown', 'west@brown.come'), 
    ('Steph', 'Kuewa', 'steph@kuewa.com'), 
    ('Dan', 'Pas', 'dan@pas.com')
]

# c.executemany("INSERT INTO customers VALUES(?,?,?)", many_customers)

c.execute("SELECT * FROM customers")

# print(c.fetchall())

# c.fetchone()[0] #firstname

# c.execute("SELECT * FROM customers WHERE last_name = 'Brown' ")
# c.execute("SELECT * FROM customers WHERE last_name LIKE 'K%' ")
# c.execute("SELECT * FROM customers WHERE email LIKE '%.com' ")
# print(c.fetchone())


# c.execute("""UPDATE customers SET first_name= 'West'
#         WHERE last_name= 'Brown'
# """)

# c.execute("DELETE from customers WHERE rowid=1")
# c.execute("SELECT * FROM customers")
print(c.fetchall())

conn.commit()