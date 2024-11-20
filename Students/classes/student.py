import tkinter as tk
#from Students.classes import subject
#from Students.classes.subject import Subject
from classes.subject import Subjects
from dataclasses import dataclass
import pandas as pd
import random as rnd
import os
from tkinter import *
from dataclasses import dataclass
from classes.db import DataBase
from classes.Model import Model
subjects = ['Математика','Физика','Химия']
students_names = ['Иванов','Петров','Сидоров']
@dataclass
class Students(Model):
    name: str


    def __str__(self):
        return self.name

    @staticmethod
    def getStudents():
#        db = DataBase()
        connection = DataBase.getDbConnection()
        students = DataBase.selectTable(connection,"Students")
        studentsList = [Students(id, name) for id, name in students]
        return studentsList
    def AverageScore(self):
        return round(sum(subject.score for subject in self.achivment) / len(self.achivment), 2)

    @staticmethod
    def CreateStudent(subjects, students_names):
        achivment = []
        for subject in subjects:
            achivment.append(Subjects(subject, rnd.randint(0, 100)))
        student = Students(students_names[rnd.randint(0, len(students_names) - 1)], achivment)
        return student

    @staticmethod
    def SortJournal(Journal):
        if (isinstance(Journal, list)):
            sortedJournal = sorted(Journal, key=lambda item: item.AverageScore(), reverse=True)
            return sortedJournal

    @staticmethod
    def PrintJournal(Journal):
        Frame = {"Имя": [], "Математика": [], "Физика": [], "Химия": [], "Средний балл": []}
        for student in Journal:
            Frame["Имя"].append(student.name)
            Frame["Математика"].append(student.getSubjectForName("Математика").score)
            Frame["Физика"].append(student.getSubjectForName("Физика").score)
            Frame["Химия"].append(student.getSubjectForName("Химия").score)
            Frame["Средний балл"].append(student.AverageScore())
        df = pd.DataFrame(Frame)
        return df

    def getSubjectForName(self, subjectName):
        for subject in self.achivment:
            if (subject.name == subjectName):
                return subject

    @staticmethod
    def readJournalToCSV(csv):
        Frame = pd.read_csv(csv)
        Journal = []
        subjects = ["Математика", "Химия", "Физика"]

        for ind in Frame.index:
            subjs = []
            for i in range(0, len(subjects)):
                subjs.append(Subjects(subjects[i], Frame[subjects[i]][ind]))
            Journal.append(Subjects(Frame['Имя'][ind], subjs))
        print(Journal)
        return Journal




