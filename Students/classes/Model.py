from dataclasses import dataclass
from classes.db import DataBase
@dataclass
class Model:
    id: int

    @staticmethod
    def createTables():
       #
        models = Model.__subclasses__()
        print(models)
        queries = []
        for i in range(0,len(models)):
            DataBase.createTable(models[i])

    @staticmethod
    def getForeignStr(key, ref):
        return " FOREIGN KEY (" + key + ") REFERENCES " + ref + " (id),"

    @classmethod
    def add(cls,data):
        DataBase.insertTable(cls.__name__, data)

    @classmethod
    def get(cls, where = None):
        if(where!=None):
            response = DataBase.selectTableWhere(DataBase.getDbConnection(),cls.__name__, where)
        else:
            response = DataBase.selectTable(DataBase.getDbConnection(),cls.__name__)
        attrs = vars(cls)["__annotations__"].keys()
        if (cls.__name__ != 'Achievements'):
            result = [cls(id, name) for id, name in response]
        else:
            result = [cls(id, student_id, subject_id, score) for id, student_id, subject_id, score in response]
        return result

    @classmethod
    def delete(cls, data):
        DataBase.DeleteData(DataBase.getDbConnection(),cls.__name__, data)


@dataclass
class Subjects(Model):
    name: str

@dataclass
class Students(Model):
    name: str

@dataclass
class Achievement(Model):
    subject_id: int
    student_id: int
    score: int

    @staticmethod
    def foreign():
        return {"subject_id": "Subject", "student_id": "Student"}


