# Journal Students/Classes/Main.py
import tkinter as tk
from dataclasses import dataclass
from tkinter import *
#from Students.classes.form import Form



from classes.form import Form
from classes.menu import ProgramMenu

from Forms.AddStudent import  FormAddStudent
from Forms.ShowJournal import FormShowJournal
from Forms.AddSubject import FormAddSubject
from Forms.FillAchievement import FillAchivement

@dataclass
class Main():
    title: str
    size: str
    menu:object = None

    window: object = Tk()
    frame: object = None

    def __post_init__(self):
        self.window.title(self.title)
        self.window.geometry(self.size)
        self.frame = self.createFrame()
        self.frame.obj.pack(expand=True)
        self.frame.obj.pack(anchor="nw")

    def windowProperty(self, title, size):
        self.window.title(title)
        self.window.geometry(size)

    def run(self):
        self.window.mainloop()

    def createFrame(self):
        frame = Form(self.window, 10, 10)
        return frame

    def CreateMenu(self):
        self.menu = ProgramMenu(self.window)
        self.menu.CreateMenu()
        self.menu.submenu = {}
        self.menu.submenu["operation"] = ProgramMenu.CreateGraphMenu(
            self.menu.mainmenu,
            0,
            "Операция"
        )
        self.menu.submenu['settings'] = ProgramMenu.CreateGraphMenu(
            self.menu.mainmenu,
            0,
            "Настройки"
        )
        self.menu.submenu["operation"].add_command(
            label = "Добавить студента ",
            command = lambda: FormAddStudent(self.frame)


        )
        self.menu.submenu["operation"].add_command(
            label="Поставить успеваемость студента ",
            command=lambda: FillAchivement(self.frame)

        )

        self.menu.submenu["operation"].add_command(
            label="Список студентов",
            command=lambda: FormShowJournal(self.frame)

        )
        self.menu.submenu["settings"].add_command(
            label="Список студентов",
            command=lambda: FormAddSubject(self.frame)

        )
        #mainmenu = Menu(self.window)
        #self.window.config(menu=mainmenu)
        #return mainmenu

    @staticmethod
    def CreateGraphMenu(mainmenu, tearoff, label):
        grafmenu = Menu(mainmenu, tearoff=tearoff)
        mainmenu.add_cascade(label=label,
                             menu=grafmenu)
        return grafmenu
