from dataclasses import dataclass
from classes.db import DataBase
import os


@dataclass
class Subject:
    id:int
    name: str
    #score: int

    def __str__(self):
        return self.name
    @staticmethod
    def addSubject(name):
        db = DataBase()
        connection = db.getDbConnection()
        if connection:
            print("Connection established successfully")
            db.createSubjectsTable(connection)  # This should now print a message
            data = {'SubjectName': name}
            DataBase.insertTable(connection, "Subjects", data)
            print("Subject addition process completed")
        else:
            print("Failed to establish database connection")

    @staticmethod
    def getSubjects():
        db = DataBase()
        connection = db.getDbConnection()
        subjects = DataBase.selectTable(connection,"Subjects")
        subjectList=[Subject(id,name) for id,name in subjects]
        return subjectList

       # subjectsList =