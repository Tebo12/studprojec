import tkinter as tk
from tkinter import *
from dataclasses import dataclass

@dataclass
class ProgramMenu():
    window:object
    mainmenu:object = None

    def CreateMenu(self):
        self.mainmenu = Menu(self.window)
        self.window.config(menu = self.mainmenu)

    @staticmethod
    def CreateGraphMenu(mainmenu, tearoff, label):
        grafmenu = Menu(mainmenu, tearoff = tearoff)
        mainmenu.add_cascade(label = label, menu = grafmenu)
        return grafmenu