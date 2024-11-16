import sqlite3
connection = sqlite3.connect('db/students.db')
cursor = connection.cursor()

cursor.execute("INSERT INTO Subjects (id,subject_name) VALUES(1, 'Math');")
cursor.execute("INSERT INTO Subjects (id,subject_name) VALUES(2,'Rus');")
cursor.execute("INSERT INTO Subjects (id,subject_name) VALUES(3, 'Chem');")

connection.commit()
connection.close()
