import sqlite3

# Establish a connection and a cursor
connection = sqlite3.connect("data.db")
cursor = connection.cursor()

# Query all data based on a condition
cursor.execute("select * from events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

# Query certain columns based on a condition
cursor.execute("select band, date from events WHERE date='2088.10.15'")
rows = cursor.fetchall()
print(rows)

# Insert new rows
new_rows = [('Cats', 'Cat City', '2088.10.15'),
            ('Hens', 'Hen City', '2088.10.17')]

cursor.executemany("INSERT INTO events VALUES(?,?,?)", new_rows)
connection.commit()

# Query all data
cursor.execute("select * from events")
rows = cursor.fetchall()
print(rows)
