from dataclasses import dataclass
from classes.db import DataBase
import classes.db as db
from classes.Model import Model

@dataclass
class Achievements(Model):
    student_id: int
    subject_id: int
    score: int

    @staticmethod
    def addAchivment(data):
        print(data)
        Achievements.delete(data)
        Achievements.add(data)

    @staticmethod
    def getAchievement(data):
        connection = DataBase.getDbConnection()
        Achivments = DataBase.selectTableWhere(connection, "Achievements", data)
        AchivmentList = [Achievements(id,student_id, subject_id, score) for id, student_id, subject_id, score in Achivments]

        return AchivmentList
    @staticmethod
    def GetStudentAverageScore(student_id):
        Achivments = Achievements.getAchievement({"student_id":student_id})

        AverageScore = round(sum(item.score for item in Achivments) / len(Achivments),2)
        return AverageScore


