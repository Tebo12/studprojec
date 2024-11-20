from dataclasses import dataclass
from classes.db import DataBase
from classes.Model import Model
import os


@dataclass
class Subjects(Model):
    name: str
    #score: int

    def __str__(self):
        return self.name


    @staticmethod
    def getSubjects():
#        db = DataBase()
        connection = DataBase.getDbConnection()
        subjects = DataBase.selectTable(connection,"Subjects")
        subjectList=[Subjects(id,name) for id,name in subjects]
        return subjectList

       # subjectsList =