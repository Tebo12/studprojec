import tkinter as tk
from tkinter import ttk
class Combo(ttk.Combobox):
    def __init__(self, *args, values=None, **kwargs):
        super().__init__(*args, values=values, **kwargs)
        if values is None:
            values = []
        self._values = values
    def get(self):
        if self.current() == -1:
            return None
        else:
            return self._values[self.current()]