import sqlite3
connection = sqlite3.connect('db/students.db')
cursor = connection.cursor()

# Adding a new record
cursor.execute("INSERT INTO Achivments (id, student_id, subject_id, score) VALUES (1, 1, 1, 5);")
cursor.execute("INSERT INTO Achivments (id, student_id, subject_id, score) VALUES (2, 1, 2, 4);")
cursor.execute("INSERT INTO Achivments (id, student_id, subject_id, score) VALUES (3, 1, 3, 3);")

cursor.execute("INSERT INTO Achivments (id, student_id, subject_id, score) VALUES (4, 2, 1, 3);")
cursor.execute("INSERT INTO Achivments (id, student_id, subject_id, score) VALUES (5, 2, 2, 2);")
cursor.execute("INSERT INTO Achivments (id, student_id, subject_id, score) VALUES (6, 2, 3, 5);")

# Saving changes and closing the connection
connection.commit()

connection.commit()
connection.close()
