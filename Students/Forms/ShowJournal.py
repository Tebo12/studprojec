#from Students.classes.form import Form
#from Students.classes.student import Student
from classes.student import Student
from tkinter import *
from tkinter import ttk



# Journal Students/Forms/ShowJournal.py
def FormShowJournal(frame):
    frame.clear_frame()
    # определяем столбцы
    columns = ("name", "score1", "score2", "score3", "score4")

    FileJournal = Student.readJournalToCSV('my_data.csv')

    tree = ttk.Treeview(frame.obj, columns=columns, show="headings")
    tree.pack(fill=BOTH, expand=1)

    # определяем заголовки
    tree.heading("name", text="Имя")
    tree.heading("score1", text="Математика")
    tree.heading("score2", text="Физика")
    tree.heading("score3", text="Химия")
    tree.heading("score4", text="Средний балл")

    for student in FileJournal:
        row = [student.name,
               student.getSubjectForName("Математика").score,
               student.getSubjectForName("Физика").score,
               student.getSubjectForName("Химия").score,
               student.AverageScore(),
               ]
        tree.insert("", END, values=row)