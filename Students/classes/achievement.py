from dataclasses import dataclass
from classes.db import DataBase
import classes.db as db
@dataclass
class Achivment:
    id:int
    student_id: int
    subject_id: int
    score: int

    @staticmethod
    def addAchivment(subject,student_id,score):
        data = {"subject_id":subject.id, "student_id":student_id.id, "score":score}
        connection = DataBase.getDbConnection()
        DataBase.DeleteData(connection,"Achivments", {"subject_id":subject.id, "student_id":student_id.id})
        DataBase.insertTable(connection,"Achivments", data)
       # DataBase.insertTable(connection, "Achivment", data)
        if connection:
            print("Connection established successfully")
            db.DataBase.createAchievementsTable(connection)  # This should now print a message
            data = {"subject_id":subject.id, "student_id":student_id.id, "score":score}
            DataBase.insertTable(connection, "Achivments", data)
            print("Student addition process completed")
        else:
            print("Failed to establish database connection")

    @staticmethod
    def getAchievement(data):
        connection = DataBase.getDbConnection()
        Achivments = DataBase.selectTableWhere(connection, "Achivments", data)
        AchivmentList = [Achivment(id,student_id, subject_id, score) for id, student_id, subject_id, score in Achivments]

        return AchivmentList
    @staticmethod
    def GetStudentAverageScore(student_id):
        Achivments = Achivment.getAchievement({"student_id":student_id})

        AverageScore = round(sum(item.score for item in Achivments) / len(Achivments),2)
        return AverageScore


