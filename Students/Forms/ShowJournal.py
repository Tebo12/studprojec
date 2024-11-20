#from Students.classes.form import Form
#from Students.classes.student import Student
from classes.student import Students
from classes.form import Form

from classes.achievement import Achievements
from tkinter import *
from tkinter import ttk
from classes.subject import Subjects


# Journal Students/Forms/ShowJournal.py
def FormShowJournal(frame):
    frame.clear_frame()
    # определяем столбцы
    subjects = Subjects.getSubjects()
    columns=["Фамилия"]
    for subject in subjects:
        columns.append(subject.name)
    columns.append("Средний балл")
    tree = ttk.Treeview(frame.obj, columns= columns, show="headings")
    tree.pack(fill=BOTH,expand=1)
    for item in columns:
        tree.heading(item,text=item)
    students=Students.get()
    rows=[]
    for student in students:
        row = [student.name]
        for subject in subjects:
            achivments = Achievements.get({"student_id":student.id, "subject_id":subject.id})
            if (len(achivments)>0):
                row.append(achivments[0].score)
            else:
                row.append(0)
        row.append(Achievements.GetStudentAverageScore(student.id))
        #tree.insert("", END, values=row)
        rows.append(row)
    SortedRows = sorted(rows,key=lambda item: item[-1], reverse = True)
    for row in SortedRows:
        tree.insert("",END,values=row)

