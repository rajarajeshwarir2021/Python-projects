import sqlite3


# Establish a connection and cursor
connection = sqlite3.connect("data_1.db")
sql_cursor = connection.cursor()

# Create a table
sql_cursor.execute("CREATE TABLE events ('band' TEXT, 'city' TEXT, 'date' INTEGER)")

"""
# Insert new data records
new_data = [('Dogs', 'Dogs City', '2088.10.17'), ('Cats', 'Cats City', '2088.10.18')]
sql_cursor.executemany("INSERT into events VALUES(?,?,?)", new_data)
connection.commit()


# Query all data based on a condition
sql_cursor.execute("SELECT * FROM events WHERE date='2088.10.17'")
rows = sql_cursor.fetchall()
print(rows)


# Query certain column data based on a condition
sql_cursor.execute("SELECT band, date FROM events WHERE date='2088.10.17'")
rows = sql_cursor.fetchall()
print(rows)

# Query all data
sql_cursor.execute("SELECT * FROM events")
rows = sql_cursor.fetchall()
print(rows)
"""