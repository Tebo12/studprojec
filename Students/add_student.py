import sqlite3
connection = sqlite3.connect('db/students.db')
cursor = connection.cursor()

# Adding a new user
cursor.execute("INSERT INTO Students (id, student_name) VALUES (1, 'Ivanov');")
cursor.execute("INSERT INTO Students (id, student_name) VALUES (2, 'Petrov');")
cursor.execute("INSERT INTO Students (id, student_name) VALUES (3, 'Sidorov');")

# Saving changes and closing connection
connection.commit()


connection.commit()
connection.close()
