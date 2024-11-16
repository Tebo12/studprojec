from classes.form import Form
from classes.subject import Subject
import os
# Абсолютный путь к файлу базы данных


def FormAddSubject(frame):
    frame.clear_frame()

    # Поле для ввода названия предмета
    SubjectName = Form.create_input("Название предмета", frame.obj, 1, 1)

    # Кнопка для добавления предмета
    btn = Form.create_button(
        frame.obj,
        'Добавить',  # Надпись на кнопке
        lambda: Subject.addSubject(SubjectName.get()),  # Добавляем предмет
        2, 1, 3  # Расположение кнопки
    )
