import tkinter as tk
from dataclasses import dataclass
from tkinter import *


#from Students.classes.student import Student
from classes.student import Student
from classes.comboBox import Combo
@dataclass
class Form():
    window: object
    padx: int
    pady: int
    obj: object = None

    def __post_init__(self):
        self.obj = self.create_obj()

    def create_obj(self):
        frame = Frame(
            self.window,  # Обязательный параметр, который указывает окно для размещения Frame.
            padx=self.padx,  # Задаём отступ по горизонтали.
            pady=self.pady  # Задаём отступ по вертикали.
        )
        return frame

    def clear_frame(self):
        for widgets in self.obj.winfo_children():
            widgets.destroy()

    @staticmethod
    def create_label(label, frame, row, col):
        label = Label(frame, text=label)
        label.grid(row=row, column=col)

    @staticmethod
    def create_input(label, frame, row, col):
        Form.create_label(label, frame, row, col)
        result = Entry(frame)
        result.grid(row=row, column=col + 1)
        return result

    @staticmethod
    def create_button(frame, label, command, row, col, span):
        btn = Button(
            frame,
            text=label,  # Надпись на кнопке.
            command=command
        )
        btn.grid(row=row, column=col, columnspan=span)
    @staticmethod
    def create_combo(values,label, frame, row, col):
        Form.create_label(label, frame, row, col)
        result = Combo(frame,values=values)
        result.grid(row=row,column = col+1)
        return result

# Journal Students/Forms/AddStudent.py
# from classes.form import Form
# from classes.student import Student
def FormAddStudent(frame):
    frame.clear_frame()

    Name = Form.create_input("Имя студента", frame.obj, 1, 1)
    math = Form.create_input("Оценка по Математике", frame.obj, 2, 1)
    phys = Form.create_input("Оценка по Физике", frame.obj, 3, 1)
    chem = Form.create_input("Оценка по Химии", frame.obj, 4, 1)

    btn = Form.create_button(
        frame.obj,
        'Добавить',  # Надпись на кнопке.
        lambda: Student.add_student(
            Name.get(),
            int(math.get()),
            int(phys.get()),
            int(chem.get()),
        ),
        5, 1, 3

    )


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


