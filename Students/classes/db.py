"""
import sqlite3
connection = sqlite3.connect('../db/students.db')

cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Students (
id INTEGER PRIMARY KEY,
student_name TEXT NOT NULL
)
''')
#Создаём таблицу Subjects
cursor.execute('''
CREATE TABLE IF NOT EXISTS Subjects (
id INTEGER PRIMARY KEY,
subject_name TEXT NOT NULL
)
''')
#Создаём таблицу Achivments
cursor.execute('''
CREATE TABLE IF NOT EXISTS Achivments (
id INTEGER PRIMARY KEY,
subject_id INTEGER NOT NULL,
student_id INTEGER NOT NULL,
score INTEGER NOT NULL,
FOREIGN KEY (subject_id) REFERENCES Subjects (id),
FOREIGN KEY (student_id) REFERENCES Students (id)
)
''')
# Сохраняем изменения и закрываем соединение
connection.commit()

connection.close()
"""
import sqlite3
from dataclasses import dataclass
import os
@dataclass
class DataBase:
    connectionString = None

    @classmethod
    def initialize(cls, db_path):
        cls.connectionString = db_path

    @classmethod
    def getDbConnection(cls):
        if cls.connectionString is None:
            raise Exception("Database not initialized. Call DataBase.initialize() first.")
        return cls.connectionString

    @staticmethod
    def createDB(connectionString):
        DataBase.createStudentsTable(connectionString)
        DataBase.createSubjectsTable(connectionString)
        DataBase.createAchievementsTable(connectionString)

    @staticmethod
    def createStudentsTable(connectionString):
        try:
            connection = sqlite3.connect(connectionString)
            cursor = connection.cursor()
            cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Students (
                       Id INTEGER PRIMARY KEY,
                       student_name TEXT NOT NULL
                   )
               ''')
            connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while creating the Subjects table: {e}")
        finally:
            connection.close()

    @staticmethod
    def createSubjectsTable(connectionString):
        try:
            connection = sqlite3.connect(connectionString)
            cursor = connection.cursor()
            cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Subjects (
                       Id INTEGER PRIMARY KEY,
                       SubjectName TEXT NOT NULL
                   )
               ''')
            connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while creating the Subjects table: {e}")
        finally:
            connection.close()
    def createAchievementsTable(connectionString):
        connection = sqlite3.connect(connectionString)
        try:
            cursor = connection.cursor()
            cursor.execute('''
            CREATE TABLE IF NOT EXISTS Achivments (
                id INTEGER PRIMARY KEY,
                subject_id INTEGER NOT NULL,
                student_id INTEGER NOT NULL,
                score INTEGER NOT NULL,
                FOREIGN KEY (subject_id) REFERENCES Subjects (id),
                FOREIGN KEY (student_id) REFERENCES Students (id)
            )
            ''')

            connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred while creating the Subjects table: {e}")
        finally:
            connection.close()

    @staticmethod
    def insertTable(connection, Table, data):
        connection = sqlite3.connect(connection)
        cursor = connection.cursor()
        columns = ""
        values = ""
        for column, value in data.items():
            columns += column + ","
            values += "'" + str(value) + "',"

        cols = columns[:-1]  # Remove the last comma
        vals = values[:-1]  # Remove the last comma
        query = f"INSERT INTO {Table} ({cols}) VALUES ({vals})"
        print(query)
        cursor.execute(query)

        # Save changes and close connection
        connection.commit()
        connection.close()
    def selectTable(connection, Table):
        connection = sqlite3.connect(connection)
        cursor = connection.cursor()
        query = f"SELECT * FROM {Table}"
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        connection.close()

        return result















