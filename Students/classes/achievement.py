from dataclasses import dataclass
from classes.db import DataBase
import classes.db as db
@dataclass
class Achivment:
    student_id: int
    subject_id: int
    score: int

    @staticmethod
    def addAchivment(subject,student_id,score):
       # data = {"subject_name":subject_id, "student_id":student_id, "score":score}
        connection = DataBase.getDbConnection()
       # DataBase.insertTable(connection, "Achivment", data)
        if connection:
            print("Connection established successfully")
            db.DataBase.createAchievementsTable(connection)  # This should now print a message
            data = {"subject_id":subject.id, "student_id":student_id, "score":score}
            DataBase.insertTable(connection, "Achivments", data)
            print("Student addition process completed")
        else:
            print("Failed to establish database connection")
