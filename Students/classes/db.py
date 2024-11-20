
import sqlite3
from dataclasses import dataclass
import os
#from classes.Model import Model




@dataclass
class DataBase:
    connectionString:str

   #№ @classmethod
    #def initialize(cls, db_path):
    #    cls.connectionString = db_path

    @classmethod
    def getDbConnection(cls):
        return 'db/DataBase.db'

    #@staticmethod
    def createDB(connectionString):
       DataBase.createStudentsTable(connectionString)
       DataBase.createSubjectsTable(connectionString)
       DataBase.createAchievementsTable(connectionString)

    @staticmethod
    def createTable(model):
             types = {int: "INTEGER", str: "TEXT"}
#             DataBase.initialize(db_file)
             connection = sqlite3.connect(DataBase.getDbConnection())
             cursor = connection.cursor()
             query = "CREATE TABLE IF NOT EXISTS "
             print(query)
             modelName = model.__name__
             modelAttrs = vars(model)["__annotations__"]

             query = query + modelName + " (id INTEGER PRIMARY KEY,"
             for attrName, attrType in modelAttrs.items():
                 if(attrName != "id"):
                    query += " " + attrName + " " + types[attrType] + " " + "NOT NULL,"

             if "foreign" in vars(model):
                 for key, ref in model.foreign().items():
                     foreignStr = model.getForeignStr(key, ref)
                     query += foreignStr

             query = query[:-1]  # Удаляет последнюю запятую
             query = query + " )"
             print(query)
             cursor.execute(query)

             # Save changes and close connection
             connection.commit()
             connection.close()

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
    def insertTable(Table, data):
        connection = sqlite3.connect(DataBase.getDbConnection())
        cursor = connection.cursor()
        columns = ', '.join(data.keys())
        placeholders = ', '.join(['?' for _ in data])
        values = tuple(data.values())

        query = f"INSERT INTO {Table} ({columns}) VALUES ({placeholders});"
        print(query)  # For debugging
        cursor.execute(query, values)

        # Save changes and close connection
        connection.commit()
        connection.close()
    def selectTable(connection, Table):
        connection = sqlite3.connect(DataBase.getDbConnection())
        cursor = connection.cursor()
        query = f"SELECT * FROM {Table}"
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        connection.close()

        return result
    def selectTableWhere(connection, Table,data):
        connection = sqlite3.connect(DataBase.getDbConnection())
        cursor = connection.cursor()
        WhereList=""
        for column,value in data.items():
            WhereList = WhereList + column + "=" + str(value) + " AND "

        WhereList = WhereList[:-4]
        query = "SELECT * FROM " + Table + " WHERE " + WhereList

        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        connection.close()

        return result

    def DeleteData(connection, Table, data):
        connection = sqlite3.connect(DataBase.getDbConnection())
        cursor = connection.cursor()
        WhereList = ""
        if data != None:
            WhereList = " WHERE "
            for column, value in data.items():
                WhereList = WhereList + column + '=' + str(value) + ' AND '

            WhereList = WhereList[:-4]

        query = "DELETE FROM " + Table + " " + WhereList
        cursor.execute(query)
        result = cursor.fetchall()
        connection.commit()
        connection.close()










