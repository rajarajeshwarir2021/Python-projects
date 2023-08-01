import sqlite3

# Establish a connection and cursor
connection = sqlite3.connect("student_database.db")
sql_cursor = connection.cursor()

# Create a table
#sql_cursor.execute("CREATE TABLE students ('ID' INTEGER, 'Name' TEXT, 'Course' TEXT, 'Mobile No.' INTEGER)")

# Insert new data records
new_data = [('1', 'John Smith', 'Math', '49111222333')]
sql_cursor.executemany("INSERT into students VALUES(?, ?, ?, ?)", new_data)
connection.commit()